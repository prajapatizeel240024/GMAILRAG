import mailbox
import csv
import os
from email import policy
from email.parser import BytesParser

def get_body(message):
    if message.is_multipart():
        for part in message.walk():
            if part.is_multipart():
                for subpart in part.walk():
                    if subpart.get_content_type() == 'text/plain':
                        return subpart.get_payload(decode=True)
            elif part.get_content_type() == 'text/plain':
                return part.get_payload(decode=True)
    else:
        return message.get_payload(decode=True)

def mbox_to_csv(mbox_file_path, csv_file_path):
    mbox = mailbox.mbox(mbox_file_path)

    with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Subject', 'From', 'Date', 'To', 'Message-ID', 'Body'])

        for message in mbox:
            body = get_body(message)  # Get the message body using the new get_body function
            if body:
                body = body.decode('utf-8', errors='replace').replace('\n', ' ').replace('\r', '')
            else:
                body = ''
            writer.writerow([
                message['subject'],
                message['from'],
                message['date'],
                message['to'],
                message['message-id'],
                body
            ])

def convert_mboxes_to_csv(input_dir, output_dir):
    # Get all .mbox files from the input directory
    for filename in os.listdir(input_dir):
        if filename.endswith('.mbox'):
            mbox_file_path = os.path.join(input_dir, filename)
            csv_filename = filename.replace('.mbox', '.csv')  # Change the extension from .mbox to .csv
            csv_file_path = os.path.join(output_dir, csv_filename)

            # Call mbox_to_csv for each .mbox file
            mbox_to_csv(mbox_file_path, csv_file_path)
            print(f'Converted {mbox_file_path} to {csv_file_path}')

# Usage
input_dir = './Mbox_Files'  # Directory containing .mbox files
output_dir = './Past_email_mbox'  # Directory where .csv files will be saved
convert_mboxes_to_csv(input_dir, output_dir)
