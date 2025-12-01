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
================================================================================
CHATBOX IMPLEMENTATION GUIDE - USER TO ADMIN COMMUNICATION
================================================================================

This document provides complete implementation details for the real-time chatbox
system where users can communicate with admins through WebSocket connections.

================================================================================
1. WEBSOCKET CONNECTION SETUP
================================================================================

LIBRARY: Socket.IO (Version 4.8.1)

CONNECTION URL:
- Base URL: Your backend server URL (e.g., https://consulta-server-179772058555.us-central1.run.app)
- Socket.IO connects to the ROOT path, NOT /api/v1
- Full connection: <SERVER_URL> (Socket.IO handles the /socket.io/ path automatically)

CORS CONFIGURATION:
- Origin: Must match CLIENT_URL environment variable from backend
- Credentials: true (cookies/tokens are sent)
- Allowed Headers: ["Content-Type", "Authorization"]

CONNECTION OPTIONS:
- Transports: ["websocket", "polling"] (with automatic upgrade)
- Ping Timeout: 10000ms (10 seconds)
- Ping Interval: 5000ms (5 seconds)
- Connect Timeout: 45000ms (45 seconds)
- Connection State Recovery: Enabled (max disconnection duration: 2 minutes)

================================================================================
2. AUTHENTICATION
================================================================================

AUTHENTICATION METHOD:
- Firebase ID Token
- Token must be sent in socket handshake authentication object
- Path: socket.handshake.auth.token

CONNECTION WITH AUTHENTICATION:
```javascript
import { io } from 'socket.io-client';

const socket = io(SERVER_URL, {
  auth: {
    token: firebaseIdToken // Firebase ID token from your auth system
  },
  transports: ['websocket', 'polling'],
  withCredentials: true
});
```

GUEST CONNECTIONS:
- If no token is provided, connection is treated as a guest session
- Guest sessions can only use AI chat features, not admin conversations
- Guest sessions cannot send messages to admins

AUTHENTICATION FLOW:
1. User authenticates via Firebase Auth
2. Get Firebase ID Token
3. Pass token in socket.handshake.auth.token
4. Backend verifies token and attaches user object to socket.user
5. If verification fails, connection falls back to guest mode

================================================================================
3. EVENT NAMES (ENUMS)
================================================================================

CLIENT-TO-SERVER EVENTS (CTSEvent):
- "aiUserMessage" - AI chat messages (not for admin chat)
- "newMessage" - Send a new message in a conversation
- "updateReadIndex" - Update the read index (mark messages as read)
- "joinConversation" - Join a conversation room to receive real-time updates
- "leaveConversation" - Leave a conversation room

SERVER-TO-CLIENT EVENTS (STCEvent):
- "aiResponse" - AI chat responses (not for admin chat)
- "newMessage" - New message notification in a conversation
- "updateReadIndex" - Read index update notification

================================================================================
4. CONVERSATION ROOM MANAGEMENT
================================================================================

CONVERSATION ROOMS:
- Format: "c:{conversationId}" (e.g., "c:507f1f77bcf86cd799439011")
- Users join rooms to receive real-time messages for specific conversations
- Users automatically join user-specific room: "u:{userId}" for notifications

JOINING A CONVERSATION:
```javascript
socket.emit('joinConversation', {
  conversationId: '507f1f77bcf86cd799439011' // ObjectId string
});
```

LEAVING A CONVERSATION:
```javascript
socket.emit('leaveConversation');
```

AUTHORIZATION:
- Users can only join conversations they are participants of
- Admins can join ANY conversation (bypass participant check)
- Backend validates participation before allowing room join

AUTOMATIC ROOM JOINING:
- On connection, users automatically join their user room: "u:{userId}"
- This room is used for user-specific notifications

================================================================================
5. SENDING MESSAGES
================================================================================

EVENT NAME: "newMessage"

REQUEST PAYLOAD:
```javascript
{
  conversation: "507f1f77bcf86cd799439011", // Conversation ObjectId as string
  content: "Hello, I need help with my application" // Message text content
}
```

EXAMPLE:
```javascript
socket.emit('newMessage', {
  conversation: conversationId,
  content: messageText
});
```

VALIDATION:
- User must be a participant of the conversation
- Conversation must exist
- Content must be a non-empty string

RESPONSE:
- Server emits "newMessage" event to all participants in the conversation room
- Response includes full message object with populated sender and conversation data

RESPONSE STRUCTURE:
```javascript
{
  _id: ObjectId,
  conversation: {
    _id: ObjectId,
    order: ObjectId,
    participants: [
      {
        kind: "user",
        user: {
          _id: ObjectId,
          name: { first: "John", last: "Doe" },
          email: { address: "user@example.com" },
          // ... other user fields (default projection)
        },
        read: {
          index: 5,
          date: Date
        }
      }
    ],
    lastActivity: Date,
    lastMessageIndex: 5
  },
  sender: {
    _id: ObjectId,
    name: { first: "John", last: "Doe" },
    email: { address: "user@example.com" },
    // ... other user fields (default projection)
  },
  content: "Message content",
  index: 5, // Message index in conversation
  createdAt: Date,
  updatedAt: Date
}
```

MESSAGE INDEXING:
- Each message has an incremental index (starting from 0)
- Index is used for read receipts and message ordering
- Last message index is stored in conversation.lastMessageIndex

================================================================================
6. RECEIVING MESSAGES
================================================================================

LISTENING FOR NEW MESSAGES:
```javascript
socket.on('newMessage', (messageData) => {
  // messageData has the same structure as the response above
  // Update your UI with the new message
  console.log('New message received:', messageData);
});
```

MESSAGE ORDERING:
- Messages are ordered by index (ascending)
- Index starts at 0 for the first message
- Always sort by index when displaying messages

================================================================================
7. READ RECEIPTS (UPDATE READ INDEX)
================================================================================

UPDATING READ INDEX:
When a user views messages, update their read index to mark messages as read.

EVENT NAME: "updateReadIndex"

REQUEST PAYLOAD:
```javascript
{
  conversation: "507f1f77bcf86cd799439011", // Conversation ObjectId as string
  index: 5 // Index of the last message read (0-based)
}
```

EXAMPLE:
```javascript
// User read up to message index 5
socket.emit('updateReadIndex', {
  conversation: conversationId,
  index: 5
});
```

VALIDATION:
- User must be a participant of the conversation
- Index must be <= conversation.lastMessageIndex
- Only updates if the new index is higher than current read index

RESPONSE:
- Server emits "updateReadIndex" event to all participants in the conversation room
- Response includes updated conversation with participant read status

RESPONSE STRUCTURE:
```javascript
{
  _id: ObjectId,
  participants: [
    {
      kind: "user",
      user: { /* user object */ },
      read: {
        index: 5, // Last read message index
        date: Date // When it was read
      }
    }
  ],
  lastActivity: Date,
  lastMessageIndex: 5
  // ... other conversation fields
}
```

READ STATUS INDICATORS:
- Check participant.read.index to determine if user has read messages
- If participant.read.index >= message.index, message is read by that participant
- If participant.read.index < message.index, message is unread

================================================================================
8. REST API ENDPOINTS
================================================================================

BASE PATH: /api/v1/conversations

AUTHENTICATION:
- All endpoints require authentication
- Send Firebase ID token in Authorization header: "Bearer <token>"
- Or send token in cookie named "token"

GET ALL CONVERSATIONS:
GET /api/v1/conversations
Query Parameters:
- page: number (default: 1)
- limit: number (default: 100, max: 200)

Response:
```javascript
{
  data: [
    {
      _id: ObjectId,
      participants: [
        {
          user: { /* user object */ },
          read: { index: number, date: Date }
        }
      ],
      lastActivity: Date,
      lastMessage: {
        _id: ObjectId,
        sender: { /* user object */ },
        content: string,
        index: number,
        createdAt: Date
      },
      lastMessageIndex: number,
      createdAt: Date,
      updatedAt: Date
    }
  ],
  totalCount: number,
  page: number,
  limit: number
}
```

GET SINGLE CONVERSATION:
GET /api/v1/conversations/:conversationId

Response:
```javascript
{
  data: {
    _id: ObjectId,
    participants: [
      {
        user: { /* user object */ },
        read: { index: number, date: Date }
      }
    ],
    lastActivity: Date,
    lastMessage: {
      _id: ObjectId,
      sender: { /* user object */ },
      content: string,
      index: number,
      createdAt: Date
    },
    lastMessageIndex: number,
    createdAt: Date,
    updatedAt: Date
  }
}
```

GET CONVERSATION MESSAGES:
GET /api/v1/conversations/:conversationId/messages
Query Parameters:
- before: ObjectId (optional) - Get messages before this message ID (for pagination)
- limit: number (default: 100, max: 500)

Response:
```javascript
{
  data: [
    {
      _id: ObjectId,
      conversation: {
        _id: ObjectId,
        participants: [
          {
            user: { /* user object */ },
            read: { index: number, date: Date }
          }
        ]
      },
      sender: { /* user object */ },
      content: string,
      index: number,
      createdAt: Date,
      updatedAt: Date
    }
  ]
}
```

NOTE: Messages are returned in reverse chronological order (newest first) from the API.
You may need to reverse the array to display oldest first.

================================================================================
9. DATA MODELS
================================================================================

CONVERSATION MODEL:
```javascript
{
  _id: ObjectId,
  order: ObjectId, // Associated order
  participants: [
    {
      kind: "user", // or "guest"
      user: ObjectId, // Required if kind is "user"
      guestId: string, // Required if kind is "guest"
      read: {
        index: number, // Last read message index
        date: Date // When it was read
      }
    }
  ],
  lastMessageIndex: number, // Index of last message (-1 if no messages)
  lastActivity: Date, // Last activity timestamp
  createdAt: Date,
  updatedAt: Date
}
```

CONVERSATION MESSAGE MODEL:
```javascript
{
  _id: ObjectId,
  conversation: ObjectId, // Reference to Conversation
  sender: ObjectId, // Reference to User
  content: string, // Message text content
  index: number, // Message index in conversation (0-based, sequential)
  signatureRequest: ObjectId, // Optional - Reference to FormSignatureRequest
  messageType: "NORMAL" | "WELCOME" | "PAYMENT_REMINDER", // Default: "NORMAL"
  createdAt: Date,
  updatedAt: Date
}
```

USER PROJECTION (Default):
The default user projection includes:
- _id
- name (first, last)
- email (address)
- Other non-sensitive fields

Full user details are NOT exposed in conversations for privacy.

================================================================================
10. NOTIFICATION SYSTEM
================================================================================

ADMIN NOTIFICATIONS (Slack):
- When a user sends a message, admins receive a Slack notification
- Slack channel: "PLATFORM" (production) or "DEV_ASSISTANT" (development)
- Notification includes:
  - User name and email
  - Message content
- Notification only sent if:
  - User role is not Admin
  - Previous message was read by admin (to avoid spam)
  - Message index > 0 (not the first message, unless previous was read)

USER NOTIFICATIONS (Email):
- When an admin sends a message, users receive an email notification
- Email template: "NEW_MESSAGE_CUSTOMER"
- Email includes:
  - User's name
  - Link to chat: https://consultaimm.com/dashboard/order/{orderId}/chat
- Notification only sent if:
  - Sender role is Admin
  - Previous message was read by user (to avoid spam)

NOTIFICATION LOGIC:
- Notifications are sent only if the previous message in the conversation
  was read by the recipient
- This prevents notification spam when users are actively chatting
- First message always triggers notification

================================================================================
11. CONVERSATION FLOW
================================================================================

TYPICAL USER FLOW:

1. User opens chat interface
2. Frontend fetches user's conversations via GET /api/v1/conversations
3. User selects or creates a conversation
4. Frontend joins conversation room: socket.emit('joinConversation', { conversationId })
5. Frontend fetches messages via GET /api/v1/conversations/:id/messages
6. Display messages in UI (sorted by index ascending)
7. Listen for new messages: socket.on('newMessage', ...)
8. User types and sends message: socket.emit('newMessage', { conversation, content })
9. Server broadcasts to all participants in room
10. Frontend receives message and updates UI
11. Frontend updates read index when user views messages:
    socket.emit('updateReadIndex', { conversation, index })
12. Listen for read index updates: socket.on('updateReadIndex', ...)
13. When leaving conversation view: socket.emit('leaveConversation')

ADMIN FLOW:
- Admins can join ANY conversation (no participant validation)
- Admins see all conversations they have access to
- Same real-time flow applies

================================================================================
12. ERROR HANDLING
================================================================================

CONNECTION ERRORS:
- Handle socket.on('connect_error', ...) for connection failures
- Handle socket.on('disconnect', ...) for disconnection events
- Implement reconnection logic (Socket.IO has built-in reconnection)

AUTHENTICATION ERRORS:
- If authentication fails, socket falls back to guest mode
- Check socket.user to verify authenticated state
- Show appropriate UI for authenticated vs guest users

MESSAGE ERRORS:
- If sending message fails, user may not be a participant
- If conversation not found, handle 404 errors
- Display user-friendly error messages

READ INDEX ERRORS:
- If update fails, index may be invalid
- Conversation may have been deleted
- Handle gracefully and retry if appropriate

================================================================================
13. BEST PRACTICES
================================================================================

1. JOIN ROOMS PROACTIVELY:
   - Join conversation rooms as soon as conversation is opened
   - Leave rooms when conversation is closed to save resources

2. UPDATE READ INDEX REGULARLY:
   - Update read index as user scrolls through messages
   - Update when conversation becomes visible
   - Don't spam updates (throttle if needed)

3. HANDLE CONNECTION STATES:
   - Show connection status to users
   - Queue messages when disconnected
   - Sync queued messages when reconnected

4. MESSAGE ORDERING:
   - Always sort by index (ascending) for display
   - Handle new messages that arrive out of order
   - Use index for reliable ordering, not timestamps

5. READ RECEIPTS:
   - Update read index when messages come into view
   - Show read/unread indicators based on participant.read.index
   - Update indicators when receiving updateReadIndex events

6. PERFORMANCE:
   - Use pagination for message history
   - Only load visible messages
   - Implement infinite scroll for message history

7. SECURITY:
   - Always authenticate WebSocket connections
   - Validate conversation access on frontend (backend validates too)
   - Don't expose sensitive user data

================================================================================
14. EXAMPLE IMPLEMENTATION
================================================================================

```javascript
import { io } from 'socket.io-client';

class ChatManager {
  constructor(serverUrl, firebaseToken) {
    this.serverUrl = serverUrl;
    this.socket = io(serverUrl, {
      auth: { token: firebaseToken },
      transports: ['websocket', 'polling'],
      withCredentials: true
    });
    
    this.currentConversationId = null;
    this.setupEventListeners();
  }
  
  setupEventListeners() {
    this.socket.on('connect', () => {
      console.log('Connected to chat server');
    });
    
    this.socket.on('disconnect', () => {
      console.log('Disconnected from chat server');
    });
    
    this.socket.on('connect_error', (error) => {
      console.error('Connection error:', error);
    });
    
    this.socket.on('newMessage', (messageData) => {
      this.handleNewMessage(messageData);
    });
    
    this.socket.on('updateReadIndex', (conversationData) => {
      this.handleReadIndexUpdate(conversationData);
    });
  }
  
  joinConversation(conversationId) {
    if (this.currentConversationId) {
      this.leaveConversation();
    }
    
    this.currentConversationId = conversationId;
    this.socket.emit('joinConversation', { conversationId });
  }
  
  leaveConversation() {
    if (this.currentConversationId) {
      this.socket.emit('leaveConversation');
      this.currentConversationId = null;
    }
  }
  
  sendMessage(conversationId, content) {
    this.socket.emit('newMessage', {
      conversation: conversationId,
      content: content
    });
  }
  
  updateReadIndex(conversationId, lastReadIndex) {
    this.socket.emit('updateReadIndex', {
      conversation: conversationId,
      index: lastReadIndex
    });
  }
  
  handleNewMessage(messageData) {
    // Update UI with new message
    // messageData contains full message object with populated sender and conversation
  }
  
  handleReadIndexUpdate(conversationData) {
    // Update read receipts in UI
    // conversationData contains updated participant read statuses
  }
  
  disconnect() {
    this.leaveConversation();
    this.socket.disconnect();
  }
}

// Usage:
const chatManager = new ChatManager(
  'https://your-server-url.com',
  firebaseIdToken
);

// Join conversation
chatManager.joinConversation('conversation-id-123');

// Send message
chatManager.sendMessage('conversation-id-123', 'Hello, admin!');

// Update read index
chatManager.updateReadIndex('conversation-id-123', 5);

// Leave conversation
chatManager.leaveConversation();
```

================================================================================
15. ENVIRONMENT VARIABLES
================================================================================

Required backend environment variables:
- CLIENT_URL: Frontend URL for CORS
- FIREBASE_SERVICE_ACCOUNT_KEY_FILE_NAME: Firebase admin config
- SLACK_PLATFORM_CHANNEL_URL: Slack webhook for admin notifications
- SLACK_DEV_ASSISTANT_CHANNEL_URL: Slack webhook for dev notifications
- BREVO_API_KEY: For email notifications

================================================================================
16. IMPORTANT NOTES
================================================================================

1. Socket.IO Connection:
   - Connects to ROOT URL, not /api/v1
   - Socket.IO automatically handles /socket.io/ path

2. Message Indexing:
   - Messages are indexed sequentially (0, 1, 2, ...)
   - Index is used for read receipts and ordering
   - Always use index for reliable ordering

3. Participant Validation:
   - Backend validates all conversation access
   - Users can only access conversations they participate in
   - Admins can access all conversations

4. Real-time Updates:
   - All participants in a conversation room receive real-time updates
   - Updates include new messages and read index changes
   - Must join conversation room to receive updates

5. Notification Throttling:
   - Notifications only sent if previous message was read
   - Prevents notification spam during active conversations
   - First message always triggers notification

6. Connection Recovery:
   - Socket.IO has built-in connection state recovery
   - Reconnects automatically within 2 minutes of disconnection
   - Messages sent during disconnection may be lost (handle accordingly)

================================================================================
END OF DOCUMENT
================================================================================

For questions or issues, refer to:
- Backend socket handlers: src/socket/handlers/
- Socket service: src/socket/socketService.ts
- Socket main: src/socket/index.ts
- API controllers: src/api/controllers/conversation/
- Models: src/models/conversation/

