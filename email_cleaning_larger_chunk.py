import os
import json
import csv
from dotenv import find_dotenv, load_dotenv
import openai
from transformers import GPT2TokenizerFast
from email.header import decode_header
from openai.error import OpenAIError
from email.header import decode_header
from bs4 import BeautifulSoup
import sys
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.summarize import load_summarize_chain

# Load OpenAI API key from environment variables
load_dotenv(find_dotenv())
openai.api_key = os.environ.get("OPENAI_API_KEY")

csv.field_size_limit(2147483647)

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

# Initialize GPT-2 tokenizer (compatible with GPT-3.5 and GPT-4)
tokenizer = GPT2TokenizerFast.from_pretrained("gpt2")

def parse_promotional_email(email_content):
    """
    Extracts critical promotional information from an email using OpenAI API.
    """
    system_prompt = """
    You are tasked to analyze and summarize promotional emails. The critical details to extract include:
    
    1. Promotion Title: A concise title summarizing the key offering.
    2. Offer Details: Core information or benefits of the promotion.
    3. Expiration: Deadline for the promotion (if any).
    4. Action Links: Relevant links or steps to claim the offer.
    5. Brand Name: The sender or organization promoting the offer.
    6. Importance: Classify the email as "important" if it relates to internships, job search, new-grads, or related keywords; otherwise, classify it as "not important".
    
    Output Format:
    {
        "promotion_title": "Example promotion title",
        "offer_details": "Details of the promotion or benefits",
        "expiration": "Date or timeline for the offer",
        "action_links": ["https://example.com/claim-offer"],
        "brand_name": "Brand or sender name",
        "importance": "important" or "not important"
    }
    """
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
        print(f"Error parsing promotional email: {e}")
        return {}

def count_tokens(text):
    """
    Counts the number of tokens in the given text using GPT-2 tokenizer.
    """
    return len(tokenizer.encode(text))

def truncate_email(email_content, max_tokens):
    """
    Truncates the email content to fit within the maximum token limit.
    """
    tokens = tokenizer.encode(email_content)
    if len(tokens) > max_tokens:
        truncated_content = tokenizer.decode(tokens[:max_tokens])
        print("Email content truncated to fit within token limit.")
        return truncated_content
    return email_content

def process_promotional_emails_with_importance(input_csv_path, output_csv_path, max_token_limit=3000):
    """
    Processes promotional emails, truncating or skipping emails that exceed the token limit.
    """
    processed_data = []

    # Open and read the input CSV file
    with open(input_csv_path, newline='', encoding='utf-8') as csvfile:
        csv_reader = csv.DictReader(csvfile)

        for idx, row in enumerate(csv_reader, start=1):
            print(f"Processing email {idx}...")
            email_body = row.get('Body', '').strip()
            if not email_body:
                print("Empty email body found. Skipping...")
                continue

            # Check token count and truncate if necessary
            email_token_count = count_tokens(email_body)
            if email_token_count > max_token_limit:
                print(f"Email {idx} exceeds token limit ({email_token_count} tokens). Truncating...")
                email_body = truncate_email(email_body, max_token_limit)

            try:
                parsed_data = parse_promotional_email(email_body)
                if parsed_data:
                    processed_data.append([
                        parsed_data.get("promotion_title", ""),
                        parsed_data.get("offer_details", ""),
                        parsed_data.get("expiration", ""),
                        ", ".join(parsed_data.get("action_links", [])),  # Convert links to a string
                        parsed_data.get("brand_name", ""),
                        parsed_data.get("importance", "not important")  # Default to "not important" if missing
                    ])
            except Exception as e:
                print(f"Error processing email {idx}: {e}. Skipping...")
                continue

    # Write processed data to the output CSV
    with open(output_csv_path, mode='w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        # Write the header row
        csv_writer.writerow(['Promotion Title', 'Offer Details', 'Expiration', 'Action Links', 'Brand Name', 'Importance'])
        # Write data rows
        csv_writer.writerows(processed_data)

    print(f"Processed data has been saved to {output_csv_path}.")

#input_csv_path_5 = './Past_email_mbox/Category Promotions.csv'  
#output_csv_path_5 = './Clean_Mails/action_promotion_pairs.csv'
#process_promotional_emails_with_importance(input_csv_path_5,output_csv_path_5)

#Importtant Mails
def parse_important_email(email_subject, email_body, resume):
    system_prompt = f"""
    You are tasked to analyze professional emails and classify their importance based on their content. Use Zeel's resume for context:
    {resume}

    Rules:
    - Emails related to rejections, interview updates, or application follow-ups are "important."
    - Emails unrelated to Zeel's career progression are "not important."
    - Identify any actions Zeel should take, such as applying for other roles, revisiting a company's career page, or no action required.

    Output Format:
    {{
        "importance": "important" or "not important",
        "action_required": "Action details or 'No action required'"
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
        print(f"Error parsing important email: {e}")
        return {}

def count_tokens(text):
    return len(tokenizer.encode(text))

def truncate_email(email_content, max_tokens):
    tokens = tokenizer.encode(email_content)
    if len(tokens) > max_tokens:
        truncated_content = tokenizer.decode(tokens[:max_tokens])
        print("Email content truncated to fit within token limit.")
        return truncated_content
    return email_content

def process_important_emails(input_csv_path, output_csv_path, max_token_limit=3000):
    processed_data = []

    with open(input_csv_path, newline='', encoding='utf-8') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        
        for idx, row in enumerate(csv_reader, start=1):
            print(f"Processing email {idx}...")
            email_subject = row.get('Subject', '').strip()
            email_body = row.get('Body', '').strip()

            if not email_body:
                print("Empty email body found. Skipping...")
                continue

            email_content = f"Subject: {email_subject}\nBody: {email_body}"
            email_token_count = count_tokens(email_content)
            
            if email_token_count > max_token_limit:
                print(f"Email {idx} exceeds token limit ({email_token_count} tokens). Truncating...")
                email_body = truncate_email(email_body, max_token_limit - count_tokens(f"Subject: {email_subject}\n"))

            try:
                parsed_data = parse_important_email(email_subject, email_body, zeel_resume)
                if parsed_data:
                    processed_data.append([
                        email_subject,
                        row.get("From", ""),
                        row.get("Date", ""),
                        row.get("To", ""),
                        parsed_data.get("importance", "not important"),
                        parsed_data.get("action_required", "No action required")
                    ])
            except Exception as e:
                print(f"Error processing email {idx}: {e}. Skipping...")
                continue

    with open(output_csv_path, mode='w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Subject', 'From', 'Date', 'To', 'Importance', 'Action Required'])
        csv_writer.writerows(processed_data)

    print(f"Processed data has been saved to {output_csv_path}.")

#input_csv_path = './Past_email_mbox/Important.csv'
#output_csv_path = './Clean_Mails/clean_mails_important.csv'
#process_important_emails(input_csv_path, output_csv_path)

#Socails
def parse_social_email(email_subject, email_body, resume):
    system_prompt = f"""
    You are tasked to analyze social and networking emails and classify their importance based on their content. Use Zeel's resume for context:
    {resume}

    Rules:
    - Emails related to networking opportunities, professional connections, or career-related events are "important."
    - Emails from potential employers, mentors, or industry professionals are "important."
    - Emails unrelated to Zeel's professional network or career progression are "not important."
    - Identify any actions Zeel should take, such as responding to a connection request, attending an event, or no action required.

    Output Format:
    {{
        "importance": "important" or "not important",
        "action_required": "Action details or 'No action required'"
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

def count_tokens(text):
    return len(tokenizer.encode(text))

def truncate_email(email_content, max_tokens):
    tokens = tokenizer.encode(email_content)
    if len(tokens) > max_tokens:
        truncated_content = tokenizer.decode(tokens[:max_tokens])
        print("Email content truncated to fit within token limit.")
        return truncated_content
    return email_content

def process_social_emails(input_csv_path, output_csv_path, max_token_limit=3000):
    processed_data = []

    with open(input_csv_path, newline='', encoding='utf-8') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        
        for idx, row in enumerate(csv_reader, start=1):
            print(f"Processing email {idx}...")
            email_subject = row.get('Subject', '').strip()
            email_body = row.get('Body', '').strip()

            if not email_body:
                print("Empty email body found. Skipping...")
                continue

            email_content = f"Subject: {email_subject}\nBody: {email_body}"
            email_token_count = count_tokens(email_content)
            
            if email_token_count > max_token_limit:
                print(f"Email {idx} exceeds token limit ({email_token_count} tokens). Truncating...")
                email_body = truncate_email(email_body, max_token_limit - count_tokens(f"Subject: {email_subject}\n"))

            try:
                parsed_data = parse_social_email(email_subject, email_body, zeel_resume)
                if parsed_data and parsed_data.get("importance") == "important":
                    processed_data.append([
                        email_subject,
                        row.get("From", ""),
                        row.get("Date", ""),
                        row.get("To", ""),
                        parsed_data.get("importance", "not important"),
                        parsed_data.get("action_required", "No action required")
                    ])
            except Exception as e:
                print(f"Error processing email {idx}: {e}. Skipping...")
                continue

    with open(output_csv_path, mode='w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Subject', 'From', 'Date', 'To', 'Importance', 'Action Required'])
        csv_writer.writerows(processed_data)

    print(f"Processed data has been saved to {output_csv_path}.")

# Usage
#input_csv_path = './Past_email_mbox/Category Social.csv'
#output_csv_path = './Clean_Mails/clean_mails_social.csv'
#process_social_emails(input_csv_path, output_csv_path)

#Interview
tokenizer = GPT2TokenizerFast.from_pretrained("gpt2")
def parse_interview_email(email_subject, email_body, resume):
    system_prompt = f"""
    You are tasked with analyzing interview-related emails and categorizing them into:
    - Highly Important: Emails directly related to interview invitations, confirmations, or scheduled interviews.
    - Important: Emails related to interview follow-ups, thank-you notes, or rejections with actionable advice.
    - Non-Important: Emails that do not require action or are irrelevant to the interview process.

    Additionally, extract any actionable steps from the email, if applicable.

    Use the following resume for context:
    {resume}

    Output Format:
    {{
        "category": "Highly Important" or "Important" or "Non-Important",
        "action_required": "Action details or 'No action required'"
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
        print(f"Error parsing interview email: {e}")
        return {}

def count_tokens(text):
    return len(tokenizer.encode(text))

def truncate_email(email_content, max_tokens):
    tokens = tokenizer.encode(email_content)
    if len(tokens) > max_tokens:
        truncated_content = tokenizer.decode(tokens[:max_tokens])
        print("Email content truncated to fit within token limit.")
        return truncated_content
    return email_content

def process_interview_emails(input_csv_path, output_csv_path, max_token_limit=3000):
    processed_data = []

    with open(input_csv_path, newline='', encoding='utf-8') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        
        for idx, row in enumerate(csv_reader, start=1):
            print(f"Processing email {idx}...")
            email_subject = row.get('Subject', '').strip()
            email_body = row.get('Body', '').strip()

            if not email_body:
                print("Empty email body found. Skipping...")
                continue

            email_content = f"Subject: {email_subject}\nBody: {email_body}"
            email_token_count = count_tokens(email_content)
            
            if email_token_count > max_token_limit:
                print(f"Email {idx} exceeds token limit ({email_token_count} tokens). Truncating...")
                email_body = truncate_email(email_body, max_token_limit - count_tokens(f"Subject: {email_subject}\n"))

            try:
                parsed_data = parse_interview_email(email_subject, email_body, zeel_resume)
                if parsed_data:
                    processed_data.append([
                        email_subject,
                        row.get("From", ""),
                        row.get("Date", ""),
                        row.get("To", ""),
                        parsed_data.get("category", "Non-Important"),
                        parsed_data.get("action_required", "No action required")
                    ])
            except Exception as e:
                print(f"Error processing email {idx}: {e}. Skipping...")
                continue

    with open(output_csv_path, mode='w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Subject', 'From', 'Date', 'To', 'Category', 'Action Required'])
        csv_writer.writerows(processed_data)

    print(f"Processed data has been saved to {output_csv_path}.")

# Usage
#input_csv_path = './Past_email_mbox/Interview.csv'
#output_csv_path = './Clean_Mails/interview_emails_processed.csv'
#process_interview_emails(input_csv_path, output_csv_path)

#Update
tokenizer = GPT2TokenizerFast.from_pretrained("gpt2")

def parse_job_application_email(email_subject, email_body, resume):
    system_prompt = f"""
    You are tasked with analyzing job application-related emails and categorizing them into:
    - Application Submitted: Confirmation of job application submission.
    - Interview Invitation: Invitations for interviews or next steps in the application process.
    - Rejection: Clear rejection messages for the application.
    - Follow-up Required: Emails requiring a response or action from the applicant.
    - Status Update: Updates on the application status that don't fit the above categories.
    - Irrelevant: Emails not directly related to job applications.

    Additionally, determine the importance level and extract any actionable steps.

    Use the following resume for context:
    {resume}

    Output Format:
    {{
        "category": "Application Submitted" or "Interview Invitation" or "Rejection" or "Follow-up Required" or "Status Update" or "Irrelevant",
        "importance": "High" or "Medium" or "Low",
        "action_required": "Specific action details or 'No action required'",
        "application_status": "Pending" or "Rejected" or "Progressing" or "N/A"
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
        print(f"Error parsing job application email: {e}")
        return {}

def count_tokens(text):
    return len(tokenizer.encode(text))

def truncate_email(email_content, max_tokens):
    tokens = tokenizer.encode(email_content)
    if len(tokens) > max_tokens:
        truncated_content = tokenizer.decode(tokens[:max_tokens])
        print("Email content truncated to fit within token limit.")
        return truncated_content
    return email_content

def process_job_application_emails(input_csv_path, output_csv_path, max_token_limit=3000):
    processed_data = []

    with open(input_csv_path, newline='', encoding='utf-8') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        
        for idx, row in enumerate(csv_reader, start=1):
            print(f"Processing email {idx}...")
            email_subject = row.get('Subject', '').strip()
            email_body = row.get('Body', '').strip()

            if not email_body:
                print("Empty email body found. Skipping...")
                continue

            email_content = f"Subject: {email_subject}\nBody: {email_body}"
            email_token_count = count_tokens(email_content)
            
            if email_token_count > max_token_limit:
                print(f"Email {idx} exceeds token limit ({email_token_count} tokens). Truncating...")
                email_body = truncate_email(email_body, max_token_limit - count_tokens(f"Subject: {email_subject}\n"))

            try:
                parsed_data = parse_job_application_email(email_subject, email_body, zeel_resume)
                if parsed_data:
                    processed_data.append([
                        email_subject,
                        row.get("From", ""),
                        row.get("Date", ""),
                        row.get("To", ""),
                        parsed_data.get("category", "Irrelevant"),
                        parsed_data.get("importance", "Low"),
                        parsed_data.get("action_required", "No action required"),
                        parsed_data.get("application_status", "N/A")
                    ])
            except Exception as e:
                print(f"Error processing email {idx}: {e}. Skipping...")
                continue

    with open(output_csv_path, mode='w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Subject', 'From', 'Date', 'To', 'Category', 'Importance', 'Action Required', 'Application Status'])
        csv_writer.writerows(processed_data)

    print(f"Processed data has been saved to {output_csv_path}.")

# Usage
input_csv_path = './Past_email_mbox/Category Updates.csv'
output_csv_path = './Clean_Mails/job_application_updates_processed.csv'
process_job_application_emails(input_csv_path, output_csv_path)