🧠 How It Works

The system uses multiple AI agents working together in sequence:

User Topic
   ↓
Content Strategist Agent
   ↓
Research Agent
   ↓
Writer Agent
   ↓
Social Media Agent
   ↓
Final Social Post

Each agent has a specialized role in the content creation pipeline.

🏗 Project Structure
autonomous-content-pipeline/
│
├── backend/
│      ├── agents/
│      │   ├── strategist.py
│      │   ├── researcher.py
│      │   ├── writer.py
│      │   ├── seo_optimizer.py
│      │   ├── social_adapter.py
│      │   └── reviewer.py
│      │
│   ├── api/
│      │   └── routes.py
│   │
│   ├── crews/
│      │   └── content_crew.py
│   │
│   ├── config.py
│   └── main.py
│
├── frontend/
│      └── app.py
│
├── .env (hidden)
├── requirements.txt

⚙️ Tech Stack
Backend
Python
FastAPI
Frontend
Streamlit
AI / LLM
Groq API
Llama 3.1 Models
Architecture
Multi-Agent System
Sequential AI Pipeline
🔥 Supported Platforms
LinkedIn
Twitter / X

The generated content adapts automatically based on the selected platform.
