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
# Review and Sign OCR/Information Retrieval - Frontend API Documentation

## Overview
This document describes all APIs related to the Review and Sign milestone, including OCR-based information retrieval and inconsistency detection.

---

## Table of Contents
1. [Get Unresolved Inconsistencies](#1-get-unresolved-inconsistencies)
2. [Submit Review & Sign Milestone](#2-submit-review--sign-milestone)
3. [Get Milestone (with Application Review URL)](#3-get-milestone-with-application-review-url)
4. [Flow Diagram](#flow-diagram)

---

## 1. Get Unresolved Inconsistencies

**Endpoint:** `GET /api/v1/inconsistencies/:orderId`

**Description:** Retrieves all unresolved inconsistencies (PENDING status) for an order. Use this to check if there are inconsistencies that need to be resolved before submitting for review.

**Authentication:** Required (Bearer token)

**Request:**
```typescript
// URL Parameters
{
  orderId: string; // MongoDB ObjectId
}
```

**Response:**
```typescript
// Status: 200 OK
// Returns array of inconsistencies (empty array if none found)

[
  {
    _id: string;                    // Inconsistency ID
    name: string;                    // Human-readable name (e.g., "First Name")
    for: "Beneficiary" | "Petitioner";
    questionnaireRes: string;        // Value from questionnaire
    documentOptions: [
      {
        _id: string;                 // DocumentOption ID
        documentRes: string;         // Value extracted from document
        documentType: string;        // Document type (e.g., "Birth Certificate")
        url: string;                 // Presigned URL to view document (expires in 30 min)
      }
    ]
  }
]
```

**Example Request:**
```bash
GET /api/v1/inconsistencies/507f1f77bcf86cd799439011
Authorization: Bearer <token>
```

**Example Response:**
```json
[
  {
    "_id": "507f1f77bcf86cd799439012",
    "name": "First Name",
    "for": "Beneficiary",
    "questionnaireRes": "John",
    "documentOptions": [
      {
        "_id": "507f1f77bcf86cd799439013",
        "documentRes": "Jonathan",
        "documentType": "Birth Certificate",
        "url": "https://bucket.s3.amazonaws.com/path?X-Amz-Algorithm=..."
      }
    ]
  },
  {
    "_id": "507f1f77bcf86cd799439014",
    "name": "Date of Birth",
    "for": "Petitioner",
    "questionnaireRes": "1990-01-15",
    "documentOptions": [
      {
        "_id": "507f1f77bcf86cd799439015",
        "documentRes": "1990-01-20",
        "documentType": "Passport",
        "url": "https://bucket.s3.amazonaws.com/path?X-Amz-Algorithm=..."
      }
    ]
  }
]
```

**When to Use:**
- On page load of Review & Sign section
- After user resolves inconsistencies and wants to check if any remain
- Before submitting for review

---

## 2. Submit Review & Sign Milestone

**Endpoint:** `POST /api/v1/milestones/:milestoneId`

**Description:** Submits the Review & Sign milestone for admin review. This triggers OCR/information retrieval on first submission, or updates questionnaire data if resubmitting after resolving inconsistencies.

**Authentication:** Required (Bearer token)

**Request:**
```typescript
// URL Parameters
{
  milestoneId: string; // MongoDB ObjectId
}

// Request Body
{
  status: "AWAITING_ADMIN";
  formResults?: {                    // Required ONLY if resubmitting after inconsistencies
    [inconsistencyId: string]: string | null;  // DocumentOption ID or null
  };
}
```

**Response Scenarios:**

### Scenario A: First Submission (No Inconsistencies Found)
```typescript
// Status: 204 No Content
// Milestone status updated to "AWAITING_ADMIN"
// Proceed to admin review
```

### Scenario B: First Submission (Inconsistencies Found)
```typescript
// Status: 200 OK
// Returns array of inconsistencies (same format as GET /inconsistencies)
// User must resolve these before resubmitting

[
  {
    _id: string;
    name: string;
    for: "Beneficiary" | "Petitioner";
    questionnaireRes: string;
    documentOptions: Array<{
      _id: string;
      documentRes: string;
      documentType: string;
      url: string;
    }>;
  }
]
```

### Scenario C: Resubmission (After Resolving Inconsistencies)
```typescript
// Status: 204 No Content
// formResults must be provided
// Questionnaire data updated based on user selections
// Milestone status updated to "AWAITING_ADMIN"
```

**Example Request (First Submission):**
```bash
POST /api/v1/milestones/507f1f77bcf86cd799439016
Authorization: Bearer <token>
Content-Type: application/json

{
  "status": "AWAITING_ADMIN"
}
```

**Example Request (Resubmission with Resolved Inconsistencies):**
```bash
POST /api/v1/milestones/507f1f77bcf86cd799439016
Authorization: Bearer <token>
Content-Type: application/json

{
  "status": "AWAITING_ADMIN",
  "formResults": {
    "507f1f77bcf86cd799439012": "507f1f77bcf86cd799439013",  // Use document value
    "507f1f77bcf86cd799439014": null                          // Keep questionnaire value
  }
}
```

**formResults Explanation:**
- **Key:** Inconsistency `_id` (from GET /inconsistencies response)
- **Value:** 
  - `string` (DocumentOption `_id`) = Use the document value, update questionnaire
  - `null` = Keep the questionnaire value, don't update

**Error Responses:**
```typescript
// 400 Bad Request - Missing formResults on resubmission
{
  "error": "You must submit the results of your inconsistency form"
}

// 400 Bad Request - Already submitted
{
  "error": "Your application has already been submitted for review"
}

// 400 Bad Request - Previous milestones not completed
{
  "error": "You must complete all previous milestones"
}
```

**Frontend Flow:**
```typescript
// Step 1: Submit for review
const response = await fetch(`/api/v1/milestones/${milestoneId}`, {
  method: 'POST',
  headers: {
    'Authorization': `Bearer ${token}`,
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({ status: 'AWAITING_ADMIN' })
});

// Step 2: Check response
if (response.status === 200) {
  // Inconsistencies found - show them to user
  const inconsistencies = await response.json();
  // Display inconsistency form
} else if (response.status === 204) {
  // Success - no inconsistencies or resubmission successful
  // Redirect or show success message
}
```

---

## 3. Get Milestone (with Application Review URL)

**Endpoint:** `GET /api/v1/milestones/:milestoneId`

**Description:** Retrieves milestone details including the application review PDF URL (presigned) when status is "AWAITING_USER" or "AWAITING_ADMIN".

**Authentication:** Required (Bearer token)

**Request:**
```typescript
// URL Parameters
{
  milestoneId: string; // MongoDB ObjectId
}
```

**Response (Review & Sign Milestone):**
```typescript
// Status: 200 OK
{
  _id: string;
  status: "PENDING" | "AWAITING_USER" | "AWAITING_ADMIN" | "COMPLETED";
  step: {
    type: "REVIEW_AND_SIGN";
    // ... other step fields
  };
  resources: [
    {
      status: "AWAITING_USER" | "AWAITING_ADMIN";
      applicationReview: {
        _id: string;
        url: string;                    // ✅ Presigned URL (expires in 30 min)
        fileName: string;
        mimeType: "application/pdf";
        s3Key: string;
        size: number;
        // ... other asset fields
      };
      additional: Array<{
        _id: string;
        url: string;                    // ✅ Presigned URL
        fileName: string;
        // ... other fields
      }>;
      signatures: Array<{
        form: {
          _id: string;
          url: string;                  // ✅ Presigned URL
          fileName: string;
          // ... other fields
        };
        signedForm?: {
          _id: string;
          url: string;                  // ✅ Presigned URL
          fileName: string;
          // ... other fields
        };
      }>;
      applicationReviewComments: Array<{
        comment: string;
        createdBy: string;
        createdAt: string;
      }>;
    }
  ];
  urlPath: string;                      // Helper path for frontend navigation
}
```

**Example Request:**
```bash
GET /api/v1/milestones/507f1f77bcf86cd799439016
Authorization: Bearer <token>
```

**Example Response:**
```json
{
  "_id": "507f1f77bcf86cd799439016",
  "status": "AWAITING_USER",
  "step": {
    "type": "REVIEW_AND_SIGN",
    "title": "Review and Sign"
  },
  "resources": [
    {
      "status": "AWAITING_USER",
      "applicationReview": {
        "_id": "507f1f77bcf86cd799439017",
        "url": "https://bucket.s3.amazonaws.com/path/to/file.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Expires=1800&...",
        "fileName": "application-review.pdf",
        "mimeType": "application/pdf",
        "s3Key": "userId/milestoneId/application-review.pdf",
        "size": 123456
      },
      "additional": [],
      "signatures": [],
      "applicationReviewComments": []
    }
  ],
  "urlPath": "/dashboard/order/507f1f77bcf86cd799439018/milestone/507f1f77bcf86cd799439016"
}
```

**Using the PDF URL:**
```typescript
// The URL is ready to use - no additional API calls needed!

// Option 1: Display in iframe
<iframe 
  src={milestone.resources[0]?.applicationReview?.url} 
  width="100%" 
  height="800px"
/>

// Option 2: Open in new tab
window.open(milestone.resources[0]?.applicationReview?.url, '_blank');

// Option 3: Download
<a 
  href={milestone.resources[0]?.applicationReview?.url} 
  download="application-review.pdf"
>
  Download PDF
</a>

// Option 4: Use in PDF viewer component
<PDFViewer url={milestone.resources[0]?.applicationReview?.url} />
```

**Note:** The presigned URL expires in 30 minutes. If needed, call the endpoint again to get a fresh URL.

---

## Flow Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                    Review & Sign Flow                        │
└─────────────────────────────────────────────────────────────┘

1. User clicks "Submit for Review"
   ↓
   POST /api/v1/milestones/:milestoneId
   { status: "AWAITING_ADMIN" }
   ↓
   ┌─────────────────────────────────────┐
   │  Backend runs OCR/Info Retrieval    │
   │  - Extracts data from documents     │
   │  - Compares with questionnaire      │
   │  - Finds inconsistencies            │
   └─────────────────────────────────────┘
   ↓
   ┌──────────────┬──────────────────────┐
   │ Inconsistencies │ No Inconsistencies │
   │ Found          │ Found              │
   └──────────────┴──────────────────────┘
   ↓                        ↓
   │                        │
   │ 200 OK                 │ 204 No Content
   │ Returns array          │ Success!
   │                        │ Status: AWAITING_ADMIN
   │                        │
   ↓                        │
   │                        │
   ┌────────────────────────┘
   │
   │ User sees inconsistency form
   │ GET /api/v1/inconsistencies/:orderId
   │ (to refresh if needed)
   │
   │ User selects:
   │ - Use document value (DocumentOption _id)
   │ - Keep questionnaire value (null)
   │
   ↓
   POST /api/v1/milestones/:milestoneId
   {
     status: "AWAITING_ADMIN",
     formResults: {
       "inconsistencyId1": "documentOptionId",  // Use document
       "inconsistencyId2": null                 // Keep questionnaire
     }
   }
   ↓
   204 No Content
   Success! Status: AWAITING_ADMIN
   ↓
   Admin reviews application
   ↓
   Admin uploads applicationReview PDF
   ↓
   Admin changes status to "AWAITING_USER"
   ↓
   GET /api/v1/milestones/:milestoneId
   ↓
   Returns applicationReview.url (presigned)
   ↓
   User can view/download PDF
```

---

## Complete Frontend Implementation Example

```typescript
// ReviewAndSignComponent.tsx

import { useState, useEffect } from 'react';

interface Inconsistency {
  _id: string;
  name: string;
  for: "Beneficiary" | "Petitioner";
  questionnaireRes: string;
  documentOptions: Array<{
    _id: string;
    documentRes: string;
    documentType: string;
    url: string;
  }>;
}

function ReviewAndSignComponent({ milestoneId, orderId, token }: Props) {
  const [inconsistencies, setInconsistencies] = useState<Inconsistency[]>([]);
  const [loading, setLoading] = useState(false);
  const [formResults, setFormResults] = useState<Record<string, string | null>>({});

  // Check for existing inconsistencies on mount
  useEffect(() => {
    fetchInconsistencies();
  }, [orderId]);

  const fetchInconsistencies = async () => {
    try {
      const response = await fetch(`/api/v1/inconsistencies/${orderId}`, {
        headers: { 'Authorization': `Bearer ${token}` }
      });
      const data = await response.json();
      setInconsistencies(data);
      
      // Initialize formResults with null (keep questionnaire values)
      const initialFormResults: Record<string, string | null> = {};
      data.forEach((inc: Inconsistency) => {
        initialFormResults[inc._id] = null;
      });
      setFormResults(initialFormResults);
    } catch (error) {
      console.error('Failed to fetch inconsistencies:', error);
    }
  };

  const handleSubmit = async () => {
    setLoading(true);
    try {
      const body: any = { status: 'AWAITING_ADMIN' };
      
      // Include formResults if there are inconsistencies
      if (inconsistencies.length > 0) {
        body.formResults = formResults;
      }

      const response = await fetch(`/api/v1/milestones/${milestoneId}`, {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${token}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(body)
      });

      if (response.status === 200) {
        // New inconsistencies found - update state
        const newInconsistencies = await response.json();
        setInconsistencies(newInconsistencies);
        alert('Please resolve the inconsistencies before submitting.');
      } else if (response.status === 204) {
        // Success!
        alert('Successfully submitted for review!');
        // Redirect or update UI
      }
    } catch (error) {
      console.error('Failed to submit:', error);
      alert('Failed to submit. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  const handleInconsistencyChange = (inconsistencyId: string, documentOptionId: string | null) => {
    setFormResults(prev => ({
      ...prev,
      [inconsistencyId]: documentOptionId
    }));
  };

  return (
    <div>
      {inconsistencies.length > 0 && (
        <div className="inconsistencies-section">
          <h3>Please resolve the following inconsistencies:</h3>
          {inconsistencies.map(inc => (
            <div key={inc._id} className="inconsistency-item">
              <h4>{inc.name} ({inc.for})</h4>
              <p>Questionnaire: {inc.questionnaireRes}</p>
              <div>
                <label>
                  <input
                    type="radio"
                    checked={formResults[inc._id] === null}
                    onChange={() => handleInconsistencyChange(inc._id, null)}
                  />
                  Keep questionnaire value: {inc.questionnaireRes}
                </label>
                {inc.documentOptions.map(option => (
                  <label key={option._id}>
                    <input
                      type="radio"
                      checked={formResults[inc._id] === option._id}
                      onChange={() => handleInconsistencyChange(inc._id, option._id)}
                    />
                    Use document value: {option.documentRes} 
                    ({option.documentType})
                    <a href={option.url} target="_blank" rel="noopener noreferrer">
                      View Document
                    </a>
                  </label>
                ))}
              </div>
            </div>
          ))}
        </div>
      )}

      <button 
        onClick={handleSubmit} 
        disabled={loading}
      >
        {loading ? 'Submitting...' : 'Submit for Review'}
      </button>
    </div>
  );
}

// Component to display Application Review PDF
function ApplicationReviewViewer({ milestoneId, token }: Props) {
  const [pdfUrl, setPdfUrl] = useState<string | null>(null);

  useEffect(() => {
    fetchMilestone();
  }, [milestoneId]);

  const fetchMilestone = async () => {
    try {
      const response = await fetch(`/api/v1/milestones/${milestoneId}`, {
        headers: { 'Authorization': `Bearer ${token}` }
      });
      const data = await response.json();
      const url = data.data?.resources?.[0]?.applicationReview?.url;
      setPdfUrl(url);
    } catch (error) {
      console.error('Failed to fetch milestone:', error);
    }
  };

  if (!pdfUrl) return <div>Loading PDF...</div>;

  return (
    <iframe 
      src={pdfUrl} 
      width="100%" 
      height="800px"
      title="Application Review PDF"
    />
  );
}
```

---

## Error Handling

```typescript
// Common error responses and how to handle them

// 400 Bad Request
if (response.status === 400) {
  const error = await response.json();
  // error.error contains the message
  // Examples:
  // - "You must submit the results of your inconsistency form"
  // - "Your application has already been submitted for review"
  // - "You must complete all previous milestones"
}

// 401 Unauthorized
if (response.status === 401) {
  // Token expired or invalid - redirect to login
}

// 403 Forbidden
if (response.status === 403) {
  // User doesn't have permission - show error message
}

// 404 Not Found
if (response.status === 404) {
  // Milestone/Order not found - show error message
}
```

---

## Notes

1. **Presigned URLs expire in 30 minutes** - If you need to display a PDF longer, refresh the milestone data to get a new URL.

2. **OCR is async** - The first submission may take a few seconds while OCR processes documents. Show a loading state.

3. **formResults is required on resubmission** - If inconsistencies were found and the user is resubmitting, `formResults` must be included with a value for every inconsistency.

4. **Status flow:**
   - `PENDING` → User hasn't submitted yet
   - `AWAITING_ADMIN` → Submitted, waiting for admin to review
   - `AWAITING_USER` → Admin has uploaded application review, waiting for user
   - `COMPLETED` → Milestone is done

5. **Inconsistency resolution:**
   - `null` = Keep questionnaire value (don't update)
   - `DocumentOption _id` = Use document value (update questionnaire with this value)

---

## Quick Reference

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/api/v1/inconsistencies/:orderId` | GET | Get unresolved inconsistencies |
| `/api/v1/milestones/:milestoneId` | POST | Submit for review (triggers OCR) |
| `/api/v1/milestones/:milestoneId` | GET | Get milestone with PDF URLs |

---

**Questions?** Check the backend code in:
- `src/api/controllers/milestone/editMilestone.ts`
- `src/api/controllers/inconsistency/getUnresolvedInconsistencies.ts`
- `src/api/controllers/milestone/getMilestone.ts`
