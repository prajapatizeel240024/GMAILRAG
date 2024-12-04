# create_knowledge_base.py

import os
import csv
from dotenv import load_dotenv

# Update imports according to deprecation warnings
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma

def load_csv(file_path):
    """Load data from a CSV file into a list of dictionaries."""
    data_list = []
    with open(file_path, 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            data_list.append(row)
    return data_list

def process_faqs(faqs):
    """Process FAQs into texts and metadatas."""
    texts = [f"Question: {faq['Question']}\nAnswer: {faq['Answer']}" for faq in faqs]
    metadatas = [{"source": f"FAQ {i+1}", "type": "faq"} for i in range(len(faqs))]
    return texts, metadatas

def process_email_pairs(email_pairs):
    """Process email pairs into texts and metadatas."""
    texts = []
    metadatas = []
    for i, pair in enumerate(email_pairs):
        original_message = pair.get('original_message', '')
        zeels_reply = pair.get('zeels_reply', '')
        text = f"Original Message: {original_message}\nZeel's Reply: {zeels_reply}"
        texts.append(text)
        metadatas.append({"source": f"Email Pair {i+1}", "type": "email_pair"})
    return texts, metadatas

def process_action_archived_pairs(pairs):
    """Process action archived pairs into texts and metadatas."""
    texts = []
    metadatas = []
    for i, pair in enumerate(pairs):
        original_message = pair.get('original_message', '')
        follow_up_message = pair.get('follow_up_message', '')
        text = f"Original Message: {original_message}\nFollow-up Message: {follow_up_message}"
        texts.append(text)
        metadatas.append({"source": f"Action Archived Pair {i+1}", "type": "action_archived_pair"})
    return texts, metadatas

def process_action_assessment_pairs(pairs):
    """Process action assessment pairs into texts and metadatas."""
    texts = []
    metadatas = []
    for i, pair in enumerate(pairs):
        action_required = pair.get('action_required', '')
        deadline = pair.get('deadline', '')
        important_links = pair.get('important_links', '')
        important_instructions = pair.get('important_instructions', '')
        text = (
            f"Action Required: {action_required}\n"
            f"Deadline: {deadline}\n"
            f"Important Links: {important_links}\n"
            f"Instructions: {important_instructions}"
        )
        metadatas.append({"source": f"Action Assessment Pair {i+1}", "type": "action_assessment_pair"})
        texts.append(text)
    return texts, metadatas

def process_action_needed_pairs(pairs):
    """Process action needed pairs into texts and metadatas."""
    texts = []
    metadatas = []
    for i, pair in enumerate(pairs):
        original_message = pair.get('original_message', '')
        zeels_reply = pair.get('zeels_reply', '')
        text = f"Original Message: {original_message}\nZeel's Reply: {zeels_reply}"
        texts.append(text)
        metadatas.append({"source": f"Action Needed Pair {i+1}", "type": "action_needed_pair"})
    return texts, metadatas

def process_promotion_emails(promotion_emails):
    """Process promotion emails into texts and metadatas."""
    texts = []
    metadatas = []
    for i, promo in enumerate(promotion_emails):
        title = promo.get('Promotion Title', '')
        details = promo.get('Offer Details', '')
        expiration = promo.get('Expiration', '')
        action_links = promo.get('Action Links', '')
        brand_name = promo.get('Brand Name', '')
        importance = promo.get('Importance', '')
        text = (
            f"Promotion Title: {title}\n"
            f"Offer Details: {details}\n"
            f"Expiration: {expiration}\n"
            f"Action Links: {action_links}\n"
            f"Brand Name: {brand_name}\n"
            f"Importance: {importance}"
        )
        texts.append(text)
        metadatas.append({"source": f"Promotion {i+1}", "type": "promotion"})
    return texts, metadatas

def process_clean_mails_important(emails):
    """Process important emails into texts and metadatas."""
    texts = []
    metadatas = []
    for i, email in enumerate(emails):
        subject = email.get('Subject', '')
        sender = email.get('From', '')
        date = email.get('Date', '')
        recipient = email.get('To', '')
        importance = email.get('Importance', '')
        action_required = email.get('Action Required', '')
        text = (
            f"Subject: {subject}\n"
            f"From: {sender}\n"
            f"Date: {date}\n"
            f"To: {recipient}\n"
            f"Importance: {importance}\n"
            f"Action Required: {action_required}"
        )
        texts.append(text)
        metadatas.append({"source": f"Important Email {i+1}", "type": "important_email"})
    return texts, metadatas

def process_clean_mails_social(emails):
    """Process social emails into texts and metadatas."""
    texts = []
    metadatas = []
    for i, email in enumerate(emails):
        subject = email.get('Subject', '')
        sender = email.get('From', '')
        date = email.get('Date', '')
        recipient = email.get('To', '')
        importance = email.get('Importance', '')
        action_required = email.get('Action Required', '')
        text = (
            f"Subject: {subject}\n"
            f"From: {sender}\n"
            f"Date: {date}\n"
            f"To: {recipient}\n"
            f"Importance: {importance}\n"
            f"Action Required: {action_required}"
        )
        texts.append(text)
        metadatas.append({"source": f"Social Email {i+1}", "type": "social_email"})
    return texts, metadatas

def process_interview_emails(interview_emails):
    """Process interview emails into texts and metadatas."""
    texts = []
    metadatas = []
    for i, email in enumerate(interview_emails):
        subject = email.get('Subject', '')
        sender = email.get('From', '')
        date = email.get('Date', '')
        recipient = email.get('To', '')
        category = email.get('Category', '')
        action_required = email.get('Action Required', '')
        text = (
            f"Subject: {subject}\n"
            f"From: {sender}\n"
            f"Date: {date}\n"
            f"To: {recipient}\n"
            f"Category: {category}\n"
            f"Action Required: {action_required}"
        )
        texts.append(text)
        metadatas.append({"source": f"Interview Email {i+1}", "type": "interview_email"})
    return texts, metadatas

def process_job_application_emails(job_application_emails):
    """Process job application emails into texts and metadatas."""
    texts = []
    metadatas = []
    for i, email in enumerate(job_application_emails):
        subject = email.get('Subject', '')
        sender = email.get('From', '')
        date = email.get('Date', '')
        recipient = email.get('To', '')
        category = email.get('Category', '')
        importance = email.get('Importance', '')
        action_required = email.get('Action Required', '')
        text = (
            f"Subject: {subject}\n"
            f"From: {sender}\n"
            f"Date: {date}\n"
            f"To: {recipient}\n"
            f"Category: {category}\n"
            f"Importance: {importance}\n"
            f"Action Required: {action_required}"
        )
        texts.append(text)
        metadatas.append({"source": f"Job Application Email {i+1}", "type": "job_application_email"})
    return texts, metadatas

def create_knowledge_base():
    # Load environment variables
    load_dotenv()

    # Initialize OpenAI embeddings
    embeddings = OpenAIEmbeddings()

    # Prepare lists to collect texts and metadatas
    all_texts = []
    all_metadatas = []

    # Define file paths to your CSV files (Ensure these paths are correct)
    archived_pairs_emails_path = './Clean_Mails/action_archived_pairs.csv'
    assessment_pairs_emails_path = './Clean_Mails/action_assessment_pairs.csv'
    action_needed_pairs_emails_path = './Clean_Mails/action_needed_pairs.csv'
    action_promotion_pairs_emails_path = './Clean_Mails/action_promotion_pairs.csv'
    importance_emails_path = './Clean_Mails/clean_mails_important.csv'
    social_emails_path = './Clean_Mails/clean_mails_social.csv'
    interview_emails_path = './Clean_Mails/interview_emails_processed.csv'
    job_application_emails_path = './Clean_Mails/job_application_updates_processed.csv'
    sent_emails_path = './Clean_Mails/email_pairs.csv'
    faq_csv_file = './Clean_Mails/faq.csv'  # Adjust if necessary

    # Load and process FAQs
    faqs = load_csv(faq_csv_file)
    faq_texts, faq_metadatas = process_faqs(faqs)
    all_texts.extend(faq_texts)
    all_metadatas.extend(faq_metadatas)
    print(f"Loaded {len(faqs)} FAQs.")

    # Load and process email pairs (sent emails)
    email_pairs = load_csv(sent_emails_path)
    email_pair_texts, email_pair_metadatas = process_email_pairs(email_pairs)
    all_texts.extend(email_pair_texts)
    all_metadatas.extend(email_pair_metadatas)
    print(f"Loaded {len(email_pairs)} Email Pairs.")

    # Load and process action archived pairs
    action_archived_pairs = load_csv(archived_pairs_emails_path)
    archived_texts, archived_metadatas = process_action_archived_pairs(action_archived_pairs)
    all_texts.extend(archived_texts)
    all_metadatas.extend(archived_metadatas)
    print(f"Loaded {len(action_archived_pairs)} Action Archived Pairs.")

    # Load and process action assessment pairs
    action_assessment_pairs = load_csv(assessment_pairs_emails_path)
    assessment_texts, assessment_metadatas = process_action_assessment_pairs(action_assessment_pairs)
    all_texts.extend(assessment_texts)
    all_metadatas.extend(assessment_metadatas)
    print(f"Loaded {len(action_assessment_pairs)} Action Assessment Pairs.")

    # Load and process action needed pairs
    action_needed_pairs = load_csv(action_needed_pairs_emails_path)
    action_needed_texts, action_needed_metadatas = process_action_needed_pairs(action_needed_pairs)
    all_texts.extend(action_needed_texts)
    all_metadatas.extend(action_needed_metadatas)
    print(f"Loaded {len(action_needed_pairs)} Action Needed Pairs.")

    # Load and process promotion emails
    promotion_emails = load_csv(action_promotion_pairs_emails_path)
    promotion_texts, promotion_metadatas = process_promotion_emails(promotion_emails)
    all_texts.extend(promotion_texts)
    all_metadatas.extend(promotion_metadatas)
    print(f"Loaded {len(promotion_emails)} Promotion Emails.")

    # Load and process important emails
    important_emails = load_csv(importance_emails_path)
    important_texts, important_metadatas = process_clean_mails_important(important_emails)
    all_texts.extend(important_texts)
    all_metadatas.extend(important_metadatas)
    print(f"Loaded {len(important_emails)} Important Emails.")

    # Load and process social emails
    social_emails = load_csv(social_emails_path)
    social_texts, social_metadatas = process_clean_mails_social(social_emails)
    all_texts.extend(social_texts)
    all_metadatas.extend(social_metadatas)
    print(f"Loaded {len(social_emails)} Social Emails.")

    # Load and process interview emails
    interview_emails = load_csv(interview_emails_path)
    interview_texts, interview_metadatas = process_interview_emails(interview_emails)
    all_texts.extend(interview_texts)
    all_metadatas.extend(interview_metadatas)
    print(f"Loaded {len(interview_emails)} Interview Emails.")

    # Load and process job application emails
    job_application_emails = load_csv(job_application_emails_path)
    job_app_texts, job_app_metadatas = process_job_application_emails(job_application_emails)
    all_texts.extend(job_app_texts)
    all_metadatas.extend(job_app_metadatas)
    print(f"Loaded {len(job_application_emails)} Job Application Emails.")

    # Directory to save the vector store
    persist_directory = "./vector_store"

    # Create vector store with persist_directory specified
    vector_store = Chroma.from_texts(
        texts=all_texts,
        embedding=embeddings,
        metadatas=all_metadatas,
        persist_directory=persist_directory
    )
    print("Knowledge base created.")

    # Save the vector store
    vector_store.persist()
    print(f"Vector store saved to {persist_directory}")

def main():
    create_knowledge_base()

if __name__ == "__main__":
    main()