# AI-Agent-Data-Analyzer

## Description

The AI Agent Data Analyzer is an interactive web application that connects users to a specialized AI agent. This agent is designed to read and analyze a local data file (data.txt) using Azure AI's CodeInterpreterTool. Users can ask questions or give commands in natural language, and the agent will perform data analysis and calculations to provide answers.
Built with a Flask backend, this project demonstrates how to create and manage persistent AI agent conversations, making it an excellent example for developers building custom, stateful AI assistants for data-driven tasks.


---

## Features
- Interactive Chat Interface: A simple web UI to chat with the AI agent.
- Stateful Conversations: Uses Flask sessions to maintain a continuous conversation with the agent.
- Code Interpreter: The agent uses the Azure AI CodeInterpreterTool to analyze a data file and run Python code for calculations.
- File-Based Analysis: The agent is pre-configured to read and understand data from a local data.txt file.
- Easy Setup: Initializes the agent and conversation thread upon starting the web application.




---

##  Tech Stack
- **Python 3.11+**
- **Flask** (for the web interface)
- **Azure AI Agents**
- **Azure Identity**
- 


--- 

##  Project Structure
```
├── app.py                     # Flask web application
├── agent_logic.py             # Core logic for Azure AI Agent
├── templates/
│   └── index.html             # Web interface template
├── static/
│   └── style.css              # (Optional) Web style template
├── data.txt                   # Data file for the agent to analyze
├── requirements.txt           # Python dependencies 
├── .env                       # Environment variables 
├── README.md
└── LICENSE
                  


```

---

## Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/Joshua-Fernando/AI-Agent-Data-Analyzer
cd AI-Agent-Data-Analyzer
```

### 2. Install Dependencies
Using **pip**:
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## Azure AI Language Setup
1. Create an Azure AI Project in the Azure portal.
2. Deploy a model within your project that you want the agent to use (e.g., gpt-4o ).
3. Navigate to your project's settings to get the Project Endpoint.
4. Create a .env file in the root of your project directory and add the following credentials:
   - **Service Endpoint**
   - **API Key**
 
5. Add these to your environment variables:
   ```bash
   
    PROJECT_ENDPOINT="YOUR_AZURE_AI_PROJECT_ENDPOINT"
    MODEL_DEPLOYMENT_NAME="YOUR_MODEL_DEPLOYMENT_NAME"

   ```

---

## Running the Web App
```bash
python app.py
```
Then open your browser and navigate to:
```
http://localhost:5000
```

---

## Deployment
You can deploy this project to:
- **Azure App Service**
- **Replit**
- **Heroku**
- **Any cloud hosting that supports Flask**

---

## License
This project is licensed under the **Apache-2.0 license**.

---

### 👨‍💻 Author
Developed by **Joshua Fernando**  
Feel free to contribute or open issues!

