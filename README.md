# **Email Management and FAQ Knowledge Base System**

This repository provides a streamlined system to convert `.mbox` email files into actionable data, categorize emails, generate FAQs, and build a semantic knowledge base for intelligent query processing.

---

## **Directory Structure**
```plaintext
├── requirements.txt         # Python dependencies
├── mbox_to_csv.py           # Converts .mbox files to .csv
├── email_cleaning.py        # Cleans and categorizes emails
├── faq.py                   # Generates FAQs from cleaned email data
├── create_knowledge_base.py # Builds a vectorized knowledge base
├── app.py                   # Interactive interface (e.g., for email queries)
├── Clean_Mails/             # Folder for processed email data
├── Past_email_mbox/         # Folder for raw .csv email data after conversion
├── Mbox_Files/              # Folder to store raw .mbox files from Gmail
├── vector_store/            # Folder for persistent vector database
```

---

## **Features**
1. **Convert `.mbox` Files to `.csv`:**
   - Reads `.mbox` files from the `Mbox_Files/` folder.
   - Converts them into structured `.csv` files saved in the `Past_email_mbox/` folder.

2. **Email Cleaning and Categorization:**
   - Cleans and categorizes emails into types such as:
     - **Action Needed**
     - **Promotions**
     - **Important Emails**
     - **Social Emails**
     - **Archived Emails**
   - Outputs cleaned emails into the `Clean_Mails/` folder.

3. **FAQ Generation:**
   - Extracts key questions and answers from sent emails.
   - Saves the FAQs in a structured `.csv` file in the `Clean_Mails/` folder.

4. **Knowledge Base Creation:**
   - Combines FAQs, emails, and promotions into a unified **semantic vector database**.
   - Stores the database in the `vector_store/` folder for persistent use.

5. **Interactive Interface:**
   - Use `app.py` for querying emails or the knowledge base.

---

## **Requirements**
### **Install Dependencies**
Create a Python virtual environment and install the required dependencies:
```bash
pip install -r requirements.txt
```

### **Contents of `requirements.txt`:**
```
openai
langchain
python-dotenv
pandas
numpy
chroma
transformers
beautifulsoup4
```

---

## **Setup Instructions**
1. **Download `.mbox` Files from Gmail:**
   - Export your Gmail data as `.mbox` files and place them in the `Mbox_Files/` directory.

2. **Set Up Environment Variables:**
   - Create a `.env` file in the root directory with the following content:
     ```plaintext
     OPENAI_API_KEY=your_openai_api_key
     ```
   - Replace `your_openai_api_key` with your actual OpenAI API key.

3. **Convert `.mbox` Files to `.csv`:**
   - Run the `mbox_to_csv.py` script to process all `.mbox` files:
     ```bash
     python mbox_to_csv.py
     ```

4. **Clean and Categorize Emails:**
   - Run the `email_cleaning.py` script to clean and categorize emails:
     ```bash
     python email_cleaning.py
     ```
   - Cleaned emails will be saved in the `Clean_Mails/` folder.

5. **Generate FAQs:**
   - Run the `faq.py` script to create FAQs from sent emails:
     ```bash
     python faq.py
     ```
   - FAQs will be saved in `Clean_Mails/faq.csv`.

6. **Create the Knowledge Base:**
   - Run `create_knowledge_base.py` to build the vectorized knowledge base:
     ```bash
     python create_knowledge_base.py
     ```
   - The knowledge base will be stored in the `vector_store/` folder.

7. **Run the Interactive App:**
   - Launch the interactive app to query emails or the knowledge base:
     ```bash
     streamlit run app.py
     ```

---

## **Workflow**
1. Place raw `.mbox` files in the `Mbox_Files/` folder.
2. Convert `.mbox` files into `.csv` files using `mbox_to_csv.py`.
3. Clean and categorize emails using `email_cleaning.py`.
4. Generate FAQs from sent emails using `faq.py`.
5. Build a semantic knowledge base using `create_knowledge_base.py`.
6. Query emails or the knowledge base using `app.py`.

---

## **File Descriptions**
### **Scripts**
1. **`mbox_to_csv.py`:**
   - Converts `.mbox` files to `.csv` format for easier processing.
   - Input: `.mbox` files in `Mbox_Files/`
   - Output: `.csv` files in `Past_email_mbox/`

2. **`email_cleaning.py`:**
   - Cleans email content, removes unnecessary details, and categorizes emails.
   - Input: `.csv` files in `Past_email_mbox/`
   - Output: Cleaned email data in `Clean_Mails/`

3. **`faq.py`:**
   - Extracts FAQs from sent email replies.
   - Input: Cleaned email data in `Clean_Mails/`
   - Output: FAQs in `Clean_Mails/faq.csv`

4. **`create_knowledge_base.py`:**
   - Builds a semantic knowledge base using embeddings and cleaned data.
   - Input: FAQs, email pairs, and promotion emails from `Clean_Mails/`
   - Output: Vectorized knowledge base in `vector_store/`

5. **`app.py`:**
   - Launches an interactive interface to query the knowledge base or emails.

---

## **Folder Descriptions**
1. **`Mbox_Files/`:**
   - Raw `.mbox` files exported from Gmail.
   - Input directory for `mbox_to_csv.py`.

2. **`Past_email_mbox/`:**
   - Stores `.csv` files generated from `.mbox` files.
   - Input directory for `email_cleaning.py`.

3. **`Clean_Mails/`:**
   - Contains cleaned and categorized email data.
   - Used as input for `faq.py` and `create_knowledge_base.py`.

4. **`vector_store/`:**
   - Persistent vector database for the semantic knowledge base.

---

## **Example Usage**
1. Convert `.mbox` files to `.csv`:
   ```bash
   python mbox_to_csv.py
   ```

2. Clean and categorize emails:
   ```bash
   python email_cleaning.py
   ```

3. Generate FAQs:
   ```bash
   python faq.py
   ```

4. Build the knowledge base:
   ```bash
   python create_knowledge_base.py
   ```

5. Launch the app:
   ```bash
   streamlit run app.py
   ```

---

## **Key Benefits**
- Automates email categorization and cleaning.
- Extracts actionable insights and generates FAQs.
- Builds a reusable, persistent knowledge base.
- Provides an interactive query interface.

---

Feel free to clone, customize, and improve the system! If you have any questions or issues, please open an issue on GitHub. 🎉
