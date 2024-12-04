# **Email Management and FAQ Knowledge Base System**

![image](https://github.com/user-attachments/assets/2d62b782-5e80-46d1-99d4-bc4c26a9dec5)


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

### **How Agents Work in This System**

Agents are specialized tools or mechanisms that use AI models to analyze, process, and respond to specific tasks or queries. In this system, agents are built using **LangChain**, **OpenAI embeddings**, and other AI-powered tools to automate email management and FAQ generation.

---

### **What Are Agents?**

Agents are decision-making components powered by AI. They can:

1. **Understand Natural Language Queries:**
   - Accept queries in plain English, like *"Show me all emails requiring action."*
   
2. **Perform Specific Actions:**
   - Categorize emails into meaningful groups.
   - Summarize email content.
   - Generate FAQs from conversations.
   - Respond to user queries using the knowledge base.

3. **Interact Dynamically:**
   - Use a knowledge base (vector database) to provide accurate and context-aware responses.

---

### **Agent Roles in This System**

#### **1. Categorization Agent**
- **Purpose:** Classify emails into categories like:
  - *Action Needed*, *Promotions*, *Archived*, etc.
- **How It Works:**
  - Uses the **OpenAI GPT API** to read email content.
  - Based on the content and rules, assigns categories and importance levels.
- **Example:**
  - Query: *"Classify this email."*
  - Response: *"This email belongs to 'Promotions' and is 'Low Importance'."*

---

#### **2. FAQ Generation Agent**
- **Purpose:** Extract FAQs from past email conversations (sent emails).
- **How It Works:**
  - Scans cleaned email threads for patterns like:
    - Questions asked.
    - Responses provided.
  - Uses GPT to format FAQs into:
    - *Question: What is X?*
    - *Answer: X is...*
- **Example:**
  - Input: *Sent email containing a reply about pricing.*
  - Output: *"Question: What are the pricing options?"*

---

#### **3. Knowledge Base Agent**
- **Purpose:** Use the cleaned data (emails, FAQs, etc.) to answer user queries intelligently.
- **How It Works:**
  - Combines all cleaned data into a **vectorized knowledge base** using **Chroma**.
  - Uses semantic search to retrieve relevant answers.
  - When you ask a question (e.g., *"What tasks are due this week?"*), the agent searches the database for similar topics and provides responses.
- **Example:**
  - Query: *"Show me all emails related to interview scheduling."*
  - Response: *Returns a summary of emails matching this category.*

---

### **How Agents Interact With the System**

1. **Input:** A user query or raw email thread.
2. **Processing:** 
   - The agent uses AI models (e.g., GPT) and logic to analyze the input.
   - It queries the **vectorized knowledge base** or processes raw email data.
3. **Output:** Provides a meaningful response or action.

---

### **Key Technologies Enabling Agents**

1. **LangChain Framework:**
   - Used to chain together tasks like categorization, semantic search, and query handling.
   - Enables seamless interactions between different agents.

2. **OpenAI GPT Models:**
   - Core AI engine behind all agents.
   - Provides language understanding, summarization, and natural language processing.

3. **Vector Databases (Chroma):**
   - Stores all cleaned and categorized data as embeddings.
   - Enables fast and accurate retrieval of relevant information.

4. **Text Splitters:**
   - Handles large email threads by breaking them into manageable chunks for analysis.

---

### **How It All Comes Together**

1. **Data Preparation:**
   - `.mbox` files are converted to `.csv`.
   - Emails are cleaned and categorized into types (action-needed, archived, etc.).

2. **FAQ Generation:**
   - Sent emails are analyzed to extract common questions and answers.

3. **Knowledge Base Creation:**
   - FAQs, email pairs, and promotional content are embedded into a **vectorized knowledge base**.

4. **Interactive Querying:**
   - The app (`app.py`) allows users to interact with agents.
   - Queries are processed by:
     - **Categorization Agent:** Returns classified emails.
     - **FAQ Agent:** Retrieves FAQs for specific topics.
     - **Knowledge Base Agent:** Searches the knowledge base for answers.

---

### **Example Use Cases**

1. **Query Emails by Category:**
   - *"Show me all emails marked as 'Action Needed'."*
   - The agent fetches relevant emails using the vectorized knowledge base.

2. **Generate Summaries:**
   - *"Summarize all archived emails from last week."*
   - The agent reads the archived email data and generates concise summaries.

3. **Generate FAQs:**
   - *"What are the most common questions asked about project deadlines?"*
   - The FAQ agent pulls related questions and answers.

---

### **Why Agents Are Powerful**

1. **Automation:**
   - Saves time by categorizing and cleaning emails automatically.
   - Handles repetitive tasks like FAQ generation without human intervention.

2. **Context-Aware Responses:**
   - Agents use Zeel's resume and knowledge base to provide accurate, personalized answers.

3. **Scalability:**
   - With embeddings, the system can handle thousands of emails efficiently.

4. **Interactivity:**
   - Users can directly query the system for specific needs without manual searching.

---

Let me know if you'd like a deeper dive into a specific part of the agent system!
