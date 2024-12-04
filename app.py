import os
import smtplib
import datetime
import pandas as pd
import streamlit as st
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
from langchain_community.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
from imaplib import IMAP4_SSL
from email import policy
from email.parser import BytesParser
from email.utils import parsedate_to_datetime
import re

# Load environment variables
load_dotenv()

# Email configurations
IMAP_SERVER = "imap.gmail.com"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

# Initialize OpenAI LLM
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

# Streamlit Setup
st.set_page_config(page_title="AI Email Assistant", layout="wide")
st.title("AI-Powered Email Assistant")

# Resume for Zeel Prajapati
RESUME = """
Zeel Prajapati 
Data Scientist 
Email: - zeelprajapati78@gmail.com 
Phone number: - 267-626-7574 
GitHub Link: -https://github.com/prajapatizeel240024 
Data Scientist with 3+ years of experience developing AI-driven solutions to solve complex business challenges. Skilled in Python, R, SQL, and 
machine learning techniques such as supervised, unsupervised learning, deep learning, and NLP. Expertise in integrating AI agents and 
advanced technologies like LLM, RAG, and VR for stock market prediction and education platforms. Proficient in big data tools such as Hadoop, 
Spark, and Hive, and cloud platforms like AWS, Azure, and GCP. Adept at statistical analysis, predictive modeling, and data visualization with 
Tableau and Power BI, delivering actionable insights and leading cross-functional teams in AI and data-driven projects. 
TECHNICAL SKILLS  
 Programming Languages: Python (NumPy, Pandas, Matplotlib, SciPy, Scikit-learn, TensorFlow, PyTorch, Hugging Face models, OpenAI 
API), R (ggplot2, dplyr, caret), SQL (MySQL, PostgreSQL, SQL Server), Scala/Java (for big data technologies), JavaScript/TypeScript (for 
front-end frameworks like React) 
 Data Manipulation & Analysis: Data Wrangling & Cleaning, Feature Engineering, Statistical Analysis, Exploratory Data Analysis (EDA), 
Sustainable AI practices, Feature Selection, Dimensionality Reduction 
 Machine Learning & AI: Supervised & Unsupervised Learning, Deep Learning (Neural Networks, CNNs, RNNs, GANs), Natural Language 
Processing (NLP), Time Series Analysis, Transfer Learning, Model Evaluation & Tuning (Cross-validation, Hyperparameter Tuning), 
Retrieval-Augmented Generation (RAG), Large Language Models (LLMs), Langchain Agents, Reinforcement Learning, Model 
Explainability (e.g., SHAP), OpenAI API integration 
 Big Data Technologies: Hadoop, Spark, Hive, HBase, Kafka, Flink, Storm, ElasticSearch 
 Data Visualization: Tableau, Power BI, Seaborn, Plotly, Matplotlib, D3.js (for interactive web visualizations), Dash (for dashboard 
development) 
 Cloud Platforms & AI Services : AWS (S3, Redshift, SageMaker, Lambda, EC2, Athena), Azure (Azure Data Lake, Azure Machine Learning, 
Azure Cognitive Services), Google Cloud Platform (GCP) (BigQuery, AI Platform, AutoML), Hugging Face Transformers, AI-powered APIs 
like Google AI and Microsoft AI 
 DevOps & MLOps: Docker, Kubernetes, Jenkins (CI/CD), Apache Airflow (for scheduling), MLflow (for model management), DVC (Data 
Version Control), FastAPI (for building APIs and services), Langservers (for serving LLMs in real-time environments) 
 Databases & Data Warehousing: SQL (MySQL, PostgreSQL, SQL Server), NoSQL (MongoDB, Cassandra, Neo4j), Data Warehousing 
(Snowflake, Redshift, BigQuery), In-memory Databases (Redis) 
 AI & Deep Learning Frameworks: TensorFlow, PyTorch, Keras, Hugging Face, LangChain (for orchestrating AI agents), ONNX (for model 
interoperability), FastAI, OpenAI Gym (for reinforcement learning) 
 Tools & Frameworks: Jupyter Notebooks, Git/GitHub (version control), Docker/Kubernetes (for deployment), PyCaret, Streamlit (for rapid 
app development), Hugging Face, TensorFlow Serving, Gradio, FastAPI, React (for interactive front-end development) 
 Business & Domain KnowledgeA/B Testing & Experimentation, Business Intelligence (BI) tools, Data-Driven Decision Making, Predictive 
Analytics, Industry-specific knowledge (Finance, Healthcare, E-commerce, Retail), Ethical AI & Sustainable AI 
 Soft Skills: Strong Communication & Presentation Skills, Critical Thinking & Problem Solving, Stakeholder Collaboration, Team Leadership, 
Time Management & Attention to Detail, Mentoring in AI and Data Science Practices. 
PROFESSIONAL EXPERIENCE  
Penn State University 
Research Assistant in the Engineering Division 
Malvern, Pennsylvania 
Oct, 2023 - Present 
 Led Stock Market Prediction Project Using LLMs:- Spearheaded a project that integrated historical stock data with real-time news 
sentiment analysis using Large Language Models (LLMs), improving stock price prediction accuracy by 15%. Deployed the model on 
CauldOps AI for scalable AI operations and used Langchain for efficient workflow management. 
 Enhanced Prediction Model with RAG and Real-Time Insights: - Developed a stock prediction model combining RAG for real-time news, 
LLM-generated insights, and numerical data. Achieved an R² score of 0.85 and reduced the Mean Absolute Percentage Error (MAPE) by 
12%, currently preparing research for publication of this idea. 
 Innovative VR-Based Educational Platform:- Created an educational platform that converts speech-to-text and text-to-image with real- 
time feedback, leveraging VR technology. Integrated APIs with Langserver, FastAPI, and Unity, utilizing Whisper for speech recognition 
and Stability Model for VR image generation. 
 AI-Powered Learning with Real-Time Translation:- Developed an immersive AI-driven platform for real-time language translation and 
AI-generated content, transforming education environments with speech-to-text and visual feedback using VR. Collaborating on 
publishing research that highlights the transformative impact of AI and VR in education. 
 Generative AI Similarity Matrix for Stock Data: - Led the development of a foundational similarity matrix using Generative AI to analyze 
historical stock data and market trends. This project deepened insights into stock market behavior, showcasing technological innovation 
with advanced machine learning frameworks. 
 AI-Driven Financial Sentiment Analysis:- Integrated LLMs and RAG for robust news sentiment analysis, boosting stock prediction accuracy 
by 8%. This advanced AI model showcased improvements in predictive power, with findings being prepared for publication to demonstrate 
AI’s advantages in financial prediction. 
Interactive Manpower Solution Pvt. Ltd (Decimal)  
Data Analyst   
Ahmedabad, Gujarat 
Oct, 2022 – July, 2023 
 Transformed raw data into impactful narratives by seamlessly weaving together R, SQL, and Python, crafting innovative models and 
visualizations that empower stakeholders to make informed, data-driven decisions. 
 Applied advanced statistical analysis techniques to uncover trends and patterns in complex data, transforming raw numbers into 
meaningful insights that guide strategic business decisions and drive measurable outcomes. 
 Leveraged cutting-edge machine learning and AI techniques to develop predictive models and intelligent algorithms, enabling data-driven 
solutions that optimize performance and drive innovation across diverse business domains. 
 Leveraged big data technologies, including Hadoop and Spark, to process and analyze terabytes of data, resulting in a 40% improvement 
in data processing speed and enabling real-time analytics for critical business decisions. 
 Utilized Tableau to create dynamic visualizations and interactive dashboards that transform complex data sets into clear, actionable 
insights, enhancing stakeholder engagement and driving informed decision-making. 
 Expertly utilized AWS services, including S3 for scalable storage, Redshift for data warehousing, SageMaker for building and deploying 
machine learning models, and Lambda for serverless computing, to architect robust data solutions that enhance efficiency and drive 
analytics-driven decision-making. 
 Leveraged strong communication and presentation skills to convey complex data insights to non-technical stakeholders, facilitating 
informed decision-making and fostering cross-functional collaboration. 
 Applied critical thinking and problem-solving skills to identify data anomalies, resulting in a 20% reduction in reporting errors and enabling 
more accurate business intelligence insights. 
Fingertips Data Intelligence Solutions Pvt. Ltd    
Data Science Intern 
Ahmedabad, Gujarat 
June, 2021 – June, 2022 
 Expertly harnessed the power of MySQL and Python to design efficient data pipelines and conduct in-depth analyses, turning complex 
datasets into actionable insights that drive strategic decision-making. 
 Enhanced data integrity by implementing robust data wrangling and cleaning techniques, improving the accuracy of predictive models 
and boosting overall analysis efficiency by 30%. 
 Developed advanced deep learning models for natural language processing, achieving a 25% increase in accuracy for sentiment analysis 
tasks and enabling more effective insights from unstructured text data. 
 Created interactive Power BI dashboards that visualized complex datasets, enhancing stakeholder insights and decision-making efficiency 
by 35% through real-time data analysis and reporting. 
 Implemented Azure Data Lake for scalable data storage and utilized Azure Machine Learning to build predictive models, resulting in a 30% 
increase in forecasting accuracy and streamlined data processing workflows. 
 Designed and implemented efficient data warehousing solutions using Snowflake, Redshift, and BigQuery, optimizing data storage and 
retrieval processes to support real-time analytics and empower data-driven decision-making across the organization. 
EDUCATION  
Pennsylvania State University, PA 
Master of Science in Data Analytics 
GPA: 3.8 
LD College of Engineering, Ahmedabad, Gujarat 
Bachelor of Engineering in Computer Engineering 
GPA: 3.7 
PROJECTS 
(Expected Dec – 2024) 
(June – 2024) 
 Facial Emotion Recognition Using CNNs: Developed a deep learning model using CNN to classify emotions from 34,000 facial images, 
achieving 75% training and 64% testing accuracy. Leveraged Python and NumPy for image processing and ReLU-activated layers to enhance 
detection accuracy, with the entire project documented on GitHub. 
 Google Stock Price Prediction with RNN-LSTM: Built an RNN LSTM model for predicting Google stock prices, achieving an R² score of 0.76. 
Prepared and standardized historical stock data using Numpy and Pandas, with detailed project documentation available on GitHub. 
 Fraud Detection System Using LightGBM & XGBoost: Engineered a fraud detection pipeline using LightGBM and XGBoost, achieving high 
accuracy with strong F1 and AUC scores. Extensive feature engineering and data analysis were conducted on financial transaction data, and 
the full implementation is shared on GitHub. 
EXTRACURRICULAR ACTIVITIES 
 Advanced to the second round of the Humana Competition in September 2023, ranking in the top 50 out of 200 teams, and collaborated 
in a trio for the case study. 
 We developed a multilingual chatbot for farmers, capable of answering questions and providing forecast predictions. The project won the 
local event and advanced to the global finalist stage. Git.
"""

def clean_email_body(body: str) -> str:
    """Clean email body by removing unnecessary links and tracking details."""
    cleaned_body = re.sub(r"https?://\S+", "", body)  # Remove all URLs
    cleaned_body = re.sub(r"\s{2,}", " ", cleaned_body)  # Replace multiple spaces with a single space
    cleaned_body = re.sub(r"\n+", "\n", cleaned_body)  # Remove excessive line breaks
    return cleaned_body.strip()  # Trim leading/trailing whitespace

def fetch_emails_from_past_1_hour():
    """Fetch emails from the past 1 hour using IMAP."""
    try:
        with IMAP4_SSL(IMAP_SERVER) as mail:
            mail.login(EMAIL_USER, EMAIL_PASSWORD)
            mail.select("inbox")
            
            now = datetime.datetime.now()
            past_1_hour = now - datetime.timedelta(hours=1)
            search_criterion = past_1_hour.strftime('%d-%b-%Y')
            
            result, data = mail.search(None, f'(SINCE {search_criterion})')
            email_ids = data[0].split()
            emails = []
            
            for email_id in email_ids:
                result, msg_data = mail.fetch(email_id, "(RFC822)")
                for response_part in msg_data:
                    if isinstance(response_part, tuple):
                        msg = BytesParser(policy=policy.default).parsebytes(response_part[1])
                        subject = msg["subject"] or "No Subject"
                        body = ""
                        if msg.is_multipart():
                            for part in msg.walk():
                                if part.get_content_type() == "text/plain":
                                    body = part.get_payload(decode=True).decode("utf-8", errors="replace")
                                    break
                        else:
                            body = msg.get_payload(decode=True).decode("utf-8", errors="replace")
                        emails.append({
                            "Subject": subject,
                            "Body": clean_email_body(body),
                            "From": msg["from"],
                            "To": msg["to"],
                            "Date": parsedate_to_datetime(msg["date"])
                        })
            return emails
    except Exception as e:
        st.error(f"Error fetching emails: {e}")
        return []

def analyze_email(email_content: str):
    """Analyze an email to determine its category, importance, and whether action is needed."""
    analysis_prompt = f"""
    Analyze the following email content and determine:
    1. The category: [Highly Important, Important, Social, Job Application, Promotion, Irrelevant].
    2. Importance level: [High, Medium, Low].
    3. Action needed: [Yes, No].

    Email Content:
    {email_content}

    Response format:
    {{
        "category": "Category here",
        "importance": "Importance level here",
        "action_needed": "Yes or No"
    }}
    """
    response = llm.invoke([HumanMessage(content=analysis_prompt)])
    return eval(response.content.strip())  # Convert JSON string to dictionary

def draft_cold_email(company_name: str, recruiter_name: str, jd: str = None):
    """Draft a cold email to a recruiter."""
    email_prompt = f"""
    Write a cold email as Zeel Prajapati, a data scientist, to {recruiter_name} at {company_name}. 
    Highlight relevant skills, mention enthusiasm for the company, and request a meeting or interview. 

    Include a subject line. The email should:
    - Be 100-150 words.
    - Have a professional tone.
    - Reference a specific job description (if provided): {jd}.
    """
    response = llm.invoke([HumanMessage(content=email_prompt)])
    return response.content.strip()

def draft_linkedin_message(company_name: str, recruiter_name: str):
    """Draft a LinkedIn message to a recruiter."""
    linkedin_prompt = f"""
    Write a LinkedIn message to {recruiter_name} from Zeel Prajapati, showing interest in connecting and discussing opportunities at {company_name}.
    Keep it concise (50-60 words), professional, and use a warm tone. Add emojis to make it engaging.
    """
    response = llm.invoke([HumanMessage(content=linkedin_prompt)])
    return response.content.strip()

def draft_connection_request(company_name: str, recruiter_name: str):
    """Draft a LinkedIn connection request."""
    connection_prompt = f"""
    Write a LinkedIn connection request message to {recruiter_name} from Zeel Prajapati, showing interest in {company_name}.
    Keep it concise (under 300 characters) and friendly. Add 1-2 emojis for a positive tone.
    """
    response = llm.invoke([HumanMessage(content=connection_prompt)])
    return response.content.strip()

def send_email(recipient, subject, body):
    """Send an email using SMTP."""
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_USER, EMAIL_PASSWORD)
            
            msg = MIMEMultipart()
            msg["From"] = EMAIL_USER
            msg["To"] = recipient
            msg["Subject"] = subject
            msg.attach(MIMEText(body, "plain"))
            
            server.sendmail(EMAIL_USER, recipient, msg.as_string())
            st.success(f"Email sent to {recipient}")
    except Exception as e:
        st.error(f"Error sending email: {e}")

def draft_cover_letter(company_name: str, recruiter_name: str, jd: str = None):
    """
    Draft a personalized cover letter for Zeel Prajapati.
    - Aligns skills and experience with the job description (JD) provided.
    - Uses a formal, professional tone.
    """
    cover_letter_prompt = f"""
    Write a professional cover letter for Zeel Prajapati, applying to a role at {company_name}. 
    Address {recruiter_name}, mention enthusiasm for the company, and align Zeel's skills with the job description (if provided). 
    Use the following details:
    
    Resume: {RESUME}
    
    Job Description (if provided): {jd}
    
    The cover letter should:
    - Begin with a compelling introduction.
    - Highlight relevant skills and achievements.
    - Conclude with a strong call to action.
    """
    response = llm.invoke([HumanMessage(content=cover_letter_prompt)])
    return response.content.strip()

# Sidebar Menu
st.sidebar.title("Menu")
action = st.sidebar.selectbox("Choose an action:", ["Fetch and Analyze Emails", "Generate Outreach Messages", "Send Email"])

if action == "Fetch and Analyze Emails":
    st.header("Emails from the Past 1 Hour with Analysis")
    if st.button("Fetch Emails"):
        emails = fetch_emails_from_past_1_hour()
        if emails:
            email_data = []
            for email in emails:
                analysis = analyze_email(email["Body"])
                email_data.append({
                    "Subject": email["Subject"],
                    "Body": email["Body"],
                    "From": email["From"],
                    "To": email["To"],
                    "Category": analysis["category"],
                    "Importance": analysis["importance"],
                    "Action Needed": analysis["action_needed"]
                })
            st.dataframe(pd.DataFrame(email_data))
        else:
            st.write("No emails found from the past 1 hour.")

elif action == "Generate Outreach Messages":
    st.header("Generate Cold Email, LinkedIn Message, and Cover Letter")
    company_name = st.text_input("Enter Company Name:")
    recruiter_name = st.text_input("Enter Recruiter Name:")
    jd = st.text_area("Paste Job Description (Optional):")
    
    if st.button("Generate Messages"):
        if company_name and recruiter_name:
            cold_email = draft_cold_email(company_name, recruiter_name, jd)
            linkedin_message = draft_linkedin_message(company_name, recruiter_name)
            connection_request = draft_connection_request(company_name, recruiter_name)
            cover_letter = draft_cover_letter(company_name, recruiter_name, jd)
            
            st.subheader("Generated Cold Email:")
            st.text_area("Cold Email", value=cold_email, height=200)

            st.subheader("Generated Cover Letter:")
            st.text_area("Cold Email", value=cover_letter, height=200)

            st.subheader("Generated LinkedIn Message:")
            st.text_area("LinkedIn Message", value=linkedin_message, height=100)

            st.subheader("Generated Connection Request:")
            st.text_area("Connection Request", value=connection_request, height=100)
        else:
            st.error("Please provide both Company Name and Recruiter Name.")

elif action == "Send Email":
    st.header("Send Email")
    recipient = st.text_input("Enter Recipient Email:")
    subject = st.text_input("Enter Email Subject:")
    body = st.text_area("Enter Email Body:")
    
    if st.button("Send Email"):
        if recipient and subject and body:
            send_email(recipient, subject, body)
        else:
            st.error("Please fill in all fields.")