import os
import json
import csv
from dotenv import find_dotenv, load_dotenv
import openai

# Load OpenAI API key from environment variables
load_dotenv(find_dotenv())
openai.api_key = os.environ.get("OPENAI_API_KEY")

# Define the resume for context
zeel_resume = """
Zeel Prajapati 
Data Scientist 
Email: - zeelprajapati78@gmail.com 
Phone number: - 267-626-7574 
GitHub Link: - https://github.com/prajapatizeel240024 
Data Scientist with 3+ years of experience developing AI-driven solutions to solve complex business challenges. Skilled in Python, R, SQL, and 
machine learning techniques such as supervised, unsupervised learning, deep learning, and NLP. Expertise in integrating AI agents and 
advanced technologies like LLM, RAG, and VR for stock market prediction and education platforms. Proficient in big data tools such as Hadoop, 
Spark, and Hive, and cloud platforms like AWS, Azure, and GCP. Adept at statistical analysis, predictive modeling, and data visualization with 
Tableau and Power BI, delivering actionable insights and leading cross-functional teams in AI and data-driven projects.
"""

# Function to parse general email threads into original message / reply pairs
def parse_email(email_thread):
    system_prompt = """
    You are an expert at converting raw email threads into original message / reply pairs. 
    You are given a raw email thread that Zeel's reply to others, and your goal is to convert it into original message / reply pairs. 
    - original_message: the last message sent to Zeel; if it is a long email thread, only take the last message
    - Zeel_reply: Zeel's reply to the original message

    If there is only one message in the thread, that should be Zeel_reply.

    The exported format should look something like 
    {
        "original_message": "xxxx",
        "Zeel_reply": "xxxx"
    }
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  
            messages=[{
                "role": "system", 
                "content": system_prompt
            },
            {
                "role": "user", 
                "content": email_thread
            }]
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        print(f"Error in API call: {e}")
        return "{}"  # Return empty JSON to handle errors gracefully

# Function to parse actionable emails (e.g., job interviews or other tasks)
def parse_action_needed_email(email_thread):
    system_prompt = """
    You are an expert at processing email threads and identifying "actionable" emails.
    You are given a raw email thread where Zeel is asked to take an action, typically related to job interviews or other important tasks. Your goal is to identify the last actionable request and Zeel's response or suggested reply.

    - original_message: The last message in the thread where an actionable request is made, for example, "Please schedule an interview" or "Confirm your availability for a call."
    - zeel_reply: Zeel's reply to that request, confirming actions or providing the necessary information, for example, "I am available for an interview on Wednesday at 3 PM."

    If there is only one message in the thread, that message will be Zeel's reply to the request, or Zeel may provide an appropriate response in this case.

    The format should be:
    {
        "original_message": "xxxx",
        "zeel_reply": "xxxx"
    }
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  
            messages=[{
                "role": "system", 
                "content": system_prompt
            },
            {
                "role": "user", 
                "content": email_thread
            }]
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        print(f"Error in API call: {e}")
        return "{}"  # Return empty JSON to handle errors gracefully

# Function to parse archived emails (emails that are important but require no immediate response)
def parse_archived_email(email_thread):
    system_prompt = """
    You are an expert at processing archived email threads. These emails might contain important information, such as job updates, event notifications, or newsletters, but they do not require an immediate reply. Your task is to summarize the key points of the email.

    - original_message: The core content of the email that provides the main purpose or information. For example, a job update, event details, or a product offer.
    - follow_up_message: If the email contains any subsequent offers, reminders, or links, summarize those as well. This could be links to apply for a job, RSVP to an event, or promotional offers.

    The format should be:
    {
        "original_message": "xxxx",
        "follow_up_message": "xxxx"
    }
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  
            messages=[{
                "role": "system", 
                "content": system_prompt
            },
            {
                "role": "user", 
                "content": email_thread
            }]
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        print(f"Error in API call: {e}")
        return "{}"  # Return empty JSON to handle errors gracefully


    """
    Extracts importance of emails from the social category using OpenAI API.

    Args:
        email_subject (str): The subject of the email.
        email_body (str): The body of the email content.

    Returns:
        dict: Summary of importance classification for the email.
    """
    system_prompt = f"""
    You are tasked to analyze emails from the "Social" category and classify their importance based on the following rules:

    - Emails related to job applications, interviews, internships, or any correspondence with hiring managers are classified as "important."
    - Emails that are general newsletters, promotional content, or irrelevant to career progression are classified as "not important."
    - Consider the following resume for context when assessing importance:

    {zeel_resume}

    Output Format:
    {{
        "importance": "important" or "not important"
    }}
    """
    email_content = f"Subject: {email_subject}\nBody: {email_body}"
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": email_content}
            ]
        )
        return json.loads(response["choices"][0]["message"]["content"])
    except Exception as e:
        print(f"Error parsing social email: {e}")
        return {}
    """
    Categorizes and extracts action steps for interview-related emails using OpenAI API.

    Args:
        email_subject (str): The subject of the email.
        email_body (str): The body of the email content.

    Returns:
        dict: Summary of email categorization and action steps.
    """
    system_prompt = """
    You are tasked with analyzing interview-related emails and categorizing them into:
    - Highly Important: Emails directly related to interview invitations, confirmations, or scheduled interviews.
    - Important: Emails related to interview follow-ups, thank-you notes, or rejections with actionable advice.
    - Non-Important: Emails that do not require action or are irrelevant to the interview process.

    Additionally, extract any actionable steps from the email, if applicable.

    Output Format:
    {
        "category": "Highly Important" or "Important" or "Non-Important",
        "action_required": "Action details or 'No action required'"
    }
    """
    email_content = f"Subject: {email_subject}\nBody: {email_body}"
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": email_content}
            ]
        )
        return json.loads(response["choices"][0]["message"]["content"])
    except Exception as e:
        print(f"Error parsing interview email: {e}")
        return {}

# Function to process general email CSV (parse standard emails)
def process_csv(input_csv_path, output_csv_path):
    with open(input_csv_path, newline='', encoding='utf-8') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        processed_data = []
        
        for row in csv_reader:
            text = row['Body']  # Get the text from the 'Body' column
            
            if not text.strip():
                print("Empty email body found. Skipping...")
                continue

            json_string = parse_email(text)
            print(f"API Response: {json_string}")

            try:
                json_data = json.loads(json_string)  # Convert JSON string to dictionary
                original_message = json_data.get('original_message', '')
                zeel_reply = json_data.get('Zeel_reply', '')
                # Append original message and reply to processed data
                processed_data.append([original_message, zeel_reply])
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON: {e}. Response: {json_string}")
                continue

    # Write processed data to a new CSV file
    with open(output_csv_path, mode='w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        # Write header
        csv_writer.writerow(['original_message', 'zeels_reply'])
        # Write data rows
        csv_writer.writerows(processed_data)

# Function to process actionable email CSV (e.g., job interviews, tasks)
def process_action_needed_csv(input_csv_path, output_csv_path):
    with open(input_csv_path, newline='', encoding='utf-8') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        processed_data = []
        
        for row in csv_reader:
            text = row['Body']  # Get the text from the 'Body' column
            
            if not text.strip():
                print("Empty email body found. Skipping...")
                continue

            json_string = parse_action_needed_email(text)
            print(f"API Response: {json_string}")

            try:
                json_data = json.loads(json_string)  # Convert JSON string to dictionary
                original_message = json_data.get('original_message', '')
                zeel_reply = json_data.get('zeel_reply', '')
                # Append original message and reply to processed data
                processed_data.append([original_message, zeel_reply])
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON: {e}. Response: {json_string}")
                continue

    # Write processed data to a new CSV file
    with open(output_csv_path, mode='w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        # Write header
        csv_writer.writerow(['original_message', 'zeels_reply'])
        # Write data rows
        csv_writer.writerows(processed_data)

# Function to process archived email CSV
def process_archived_email_csv(input_csv_path, output_csv_path):
    with open(input_csv_path, newline='', encoding='utf-8') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        processed_data = []
        
        for row in csv_reader:
            text = row['Body']  # Get the text from the 'Body' column
            
            if not text.strip():
                print("Empty email body found. Skipping...")
                continue

            # Parse archived email using the updated function
            json_string = parse_archived_email(text)
            print(f"API Response: {json_string}")

            try:
                json_data = json.loads(json_string)  # Convert JSON string to dictionary
                original_message = json_data.get('original_message', '')
                follow_up_message = json_data.get('follow_up_message', '')
                # Append original message and follow-up message to processed data
                processed_data.append([original_message, follow_up_message])
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON: {e}. Response: {json_string}")
                continue

    # Write processed data to a new CSV file
    with open(output_csv_path, mode='w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        # Write header
        csv_writer.writerow(['original_message', 'follow_up_message'])
        # Write data rows
        csv_writer.writerows(processed_data)

# Function to process actionable email CSV (e.g., job interviews, assessments)
def process_assesment_csv(input_csv_path, output_csv_path):
    with open(input_csv_path, newline='', encoding='utf-8') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        processed_data = []
        
        for row in csv_reader:
            text = row['Body']  # Get the text from the 'Body' column
            
            if not text.strip():
                print("Empty email body found. Skipping...")
                continue

            # Parse actionable email using the custom function
            json_string = parse_assessment_email(text)
            print(f"API Response: {json_string}")

            try:
                json_data = json.loads(json_string)  # Convert JSON string to dictionary
                action_required = json_data.get('action_required', '')
                deadline = json_data.get('deadline', '')
                important_links = json_data.get('important_links', [])
                important_instructions = json_data.get('important_instructions', '')
                
                # Append the processed data to the list
                processed_data.append([action_required, deadline, important_links, important_instructions])
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON: {e}. Response: {json_string}")
                continue

    # Write processed data to a new CSV file
    with open(output_csv_path, mode='w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        # Write header
        csv_writer.writerow(['action_required', 'deadline', 'important_links', 'important_instructions'])
        # Write data rows
        csv_writer.writerows(processed_data)


    """
    Processes update category emails, extracts details, and classifies relevance.

    Args:
        input_csv_path (str): Path to the input CSV file containing emails.
        output_csv_path (str): Path to the output CSV file to save extracted data.
    """
    processed_data = []

    # Open and read the input CSV file
    with open(input_csv_path, newline='', encoding='utf-8') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        
        for row in csv_reader:
            email_subject = row.get('Subject', '').strip()
            email_body = row.get('Body', '').strip()

            if not email_body:
                print("Empty email body found. Skipping...")
                continue

            try:
                # Parse the update email content
                parsed_data = parse_update_email(email_subject, email_body)
                if parsed_data:
                    processed_data.append([
                        row.get("Subject", ""),
                        row.get("From", ""),
                        row.get("Date", ""),
                        row.get("To", ""),
                        parsed_data.get("importance", "not relevant"),  # Default to "not relevant" if missing
                        parsed_data.get("action_required", "No action required")
                    ])
            except Exception as e:
                print(f"Error processing email: {e}. Skipping...")
                continue

    # Write processed data to the output CSV
    with open(output_csv_path, mode='w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        # Write the header row
        csv_writer.writerow(['Subject', 'From', 'Date', 'To', 'Importance', 'Action Required'])
        # Write data rows
        csv_writer.writerows(processed_data)

    print(f"Processed data has been saved to {output_csv_path}.")
    """
    Processes important emails, extracts details, and identifies relevance and actions.

    Args:
        input_csv_path (str): Path to the input CSV file containing emails.
        output_csv_path (str): Path to the output CSV file to save extracted data.
    """
    processed_data = []

    # Open and read the input CSV file
    with open(input_csv_path, newline='', encoding='utf-8') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        
        for row in csv_reader:
            email_subject = row.get('Subject', '').strip()
            email_body = row.get('Body', '').strip()

            if not email_body:
                print("Empty email body found. Skipping...")
                continue

            try:
                # Parse the important email content
                parsed_data = parse_important_email(email_subject, email_body)
                if parsed_data:
                    processed_data.append([
                        row.get("Subject", ""),
                        row.get("From", ""),
                        row.get("Date", ""),
                        row.get("To", ""),
                        parsed_data.get("importance", "not important"),  # Default to "not important" if missing
                        parsed_data.get("action_required", "No action required")
                    ])
            except Exception as e:
                print(f"Error processing email: {e}. Skipping...")
                continue

    # Write processed data to the output CSV
    with open(output_csv_path, mode='w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        # Write the header row
        csv_writer.writerow(['Subject', 'From', 'Date', 'To', 'Importance', 'Action Required'])
        # Write data rows
        csv_writer.writerows(processed_data)

    print(f"Processed data has been saved to {output_csv_path}.")

    """
    Processes all emails in an inbox, categorizes them, and highlights their importance.

    Args:
        input_csv_path (str): Path to the input CSV file containing emails.
        output_csv_path (str): Path to the output CSV file to save categorized data.
    """
    processed_data = []

    # Open and read the input CSV file
    with open(input_csv_path, newline='', encoding='utf-8') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        
        for row in csv_reader:
            email_subject = row.get('Subject', '').strip()
            email_body = row.get('Body', '').strip()

            if not email_body:
                print("Empty email body found. Skipping...")
                continue

            try:
                # Parse the inbox email content
                parsed_data = parse_inbox_email(email_subject, email_body)
                if parsed_data:
                    processed_data.append([
                        row.get("Subject", ""),
                        row.get("From", ""),
                        row.get("Date", ""),
                        row.get("To", ""),
                        parsed_data.get("category", "Non-Important"),  # Default to "Non-Important" if missing
                        parsed_data.get("action_required", "No action required")
                    ])
            except Exception as e:
                print(f"Error processing email: {e}. Skipping...")
                continue

    # Write processed data to the output CSV
    with open(output_csv_path, mode='w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        # Write the header row
        csv_writer.writerow(['Subject', 'From', 'Date', 'To', 'Category', 'Action Required'])
        # Write data rows
        csv_writer.writerows(processed_data)

    print(f"Processed data has been saved to {output_csv_path}.")

    """
    Processes interview-related emails, categorizes them, and extracts actionable steps.

    Args:
        input_csv_path (str): Path to the input CSV file containing interview emails.
        output_csv_path (str): Path to the output CSV file to save processed data.
    """
    processed_data = []

    # Open and read the input CSV file
    with open(input_csv_path, newline='', encoding='utf-8') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        
        for row in csv_reader:
            email_subject = row.get('Subject', '').strip()
            email_body = row.get('Body', '').strip()

            if not email_body:
                print("Empty email body found. Skipping...")
                continue

            try:
                # Parse the interview email content
                parsed_data = parse_interview_email(email_subject, email_body)
                if parsed_data:
                    processed_data.append([
                        row.get("Subject", ""),
                        row.get("From", ""),
                        row.get("Date", ""),
                        row.get("To", ""),
                        parsed_data.get("category", "Non-Important"),  # Default to "Non-Important" if missing
                        parsed_data.get("action_required", "No action required")
                    ])
            except Exception as e:
                print(f"Error processing email: {e}. Skipping...")
                continue

    # Write processed data to the output CSV
    with open(output_csv_path, mode='w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        # Write the header row
        csv_writer.writerow(['Subject', 'From', 'Date', 'To', 'Category', 'Action Required'])
        # Write data rows
        csv_writer.writerows(processed_data)

    print(f"Processed data has been saved to {output_csv_path}.")

# Usage
input_csv_path_1 = './Past_email_mbox/Sent.csv'  
output_csv_path_1 = './Clean_Mails/email_pairs.csv'  

input_csv_path_2 = './Past_email_mbox/Action Needed.csv'  
output_csv_path_2 = './Clean_Mails/action_needed_pairs.csv'  

input_csv_path_3 = './Past_email_mbox/Archived.csv'  
output_csv_path_3 = './Clean_Mails/action_archived_pairs.csv'

input_csv_path_4 = './Past_email_mbox/Assessment.csv'  
output_csv_path_4 = './Clean_Mails/action_assessment_pairs.csv'

# Call the functions to process the CSV files
process_csv(input_csv_path_1, output_csv_path_1)
process_action_needed_csv(input_csv_path_2, output_csv_path_2)
process_archived_email_csv(input_csv_path_3, output_csv_path_3)
process_assesment_csv(input_csv_path_4,output_csv_path_4)