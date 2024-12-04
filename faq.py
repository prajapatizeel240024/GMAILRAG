import csv
import json
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI

# Load environment variables from .env file (ensure your OpenAI API key is set in this file)
load_dotenv()

# Initialize the OpenAI language model (you can switch to 'gpt-4' if you have access)
llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

def load_csv(file_path):
    """
    Load data from a CSV file into a list of dictionaries.
    Each row in the CSV is converted to a dictionary.
    """
    data_list = []
    with open(file_path, 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            data_list.append(row)
    return data_list

def extract_faq_individual(past_replies):
    """
    Process each email reply individually to extract FAQs.
    Avoids issues with text splitting and reduces the potential for looping.
    """
    faqs = []
    for idx, reply in enumerate(past_replies):
        prompt = f"""
        PAST EMAIL:
        {reply}
        ----

        You are an AI assistant. The above is a past email reply from Zeel (an AI student at Penn State and researcher).
        Your goal is to extract any potential FAQs about Zeel based on this email.
        Identify potential questions and provide Zeel's answers.
        Return the results in JSON format as a list of dictionaries with "Question" and "Answer" fields.
        """
        try:
            # Get the model's response
            response = llm.predict(prompt)
            # Clean up the response to ensure valid JSON
            response = response.strip()
            if response.startswith("```json"):
                response = response[7:]
            if response.endswith("```"):
                response = response[:-3]
            # Parse the JSON response
            faq_list = json.loads(response)
            # Add to the main FAQ list
            faqs.extend(faq_list)
        except json.JSONDecodeError:
            print(f"JSON decode error for email {idx+1}. Response was:\n{response}")
            continue
        except Exception as e:
            print(f"Error processing email {idx+1}: {e}")
            continue

    # Remove duplicate FAQs based on the question text
    unique_faqs = []
    seen_questions = set()
    for faq in faqs:
        question = faq.get('Question', '').strip()
        answer = faq.get('Answer', '').strip()
        if question and question not in seen_questions:
            seen_questions.add(question)
            unique_faqs.append({'Question': question, 'Answer': answer})
    return unique_faqs

def save_json_to_csv(data, file_name):
    """
    Save a list of dictionaries to a CSV file.
    Each dictionary represents a row in the CSV.
    """
    if not data:
        print("No data to save.")
        return
    with open(file_name, mode='w', newline='', encoding='utf-8') as file:
        fieldnames = ['Question', 'Answer']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for entry in data:
            writer.writerow(entry)

def main():
    # Load past emails
    past_emails = load_csv("./Clean_Mails/email_pairs.csv")
    print(f"Number of email pairs loaded: {len(past_emails)}")

    # Extract Zeel's replies and remove duplicates
    zeels_replies = [entry.get("zeels_reply", "") for entry in past_emails]
    zeels_replies = list(set(zeels_replies))  # Remove duplicate replies
    print(f"Number of unique replies: {len(zeels_replies)}")

    # Extract FAQs
    faqs = extract_faq_individual(zeels_replies)
    print(f"Number of FAQs extracted: {len(faqs)}")

    # Save FAQs to CSV
    save_json_to_csv(faqs, "./Clean_Mails/faq.csv")
    print("FAQs have been saved to './Clean_Mails/faq.csv'")

if __name__ == "__main__":
    main()