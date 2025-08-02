import os
from dotenv import load_dotenv
from pathlib import Path
from azure.identity import DefaultAzureCredential
from azure.ai.agents import AgentsClient
from azure.ai.agents.models import FilePurpose, CodeInterpreterTool, MessageRole

def initialize_agent():
    """
    Initializes the agent, uploads the data file, and creates a conversation thread.
    Returns the agent_id and thread_id.
    """
    try:
        load_dotenv()
        project_endpoint = os.getenv("PROJECT_ENDPOINT")
        model_deployment = os.getenv("MODEL_DEPLOYMENT_NAME")

        agent_client = AgentsClient(
            endpoint=project_endpoint,
            credential=DefaultAzureCredential(
                exclude_environment_credential=True,
                exclude_managed_identity_credential=True
            )
        )
        
        # Upload the data file and create a CodeInterpreterTool
        script_dir = Path(__file__).parent
        file_path = script_dir / 'data.txt'
        file = agent_client.files.upload_and_poll(file_path=file_path, purpose=FilePurpose.AGENTS)
        # print(f"Uploaded {file.filename} with ID: {file.id}")
        code_interpreter = CodeInterpreterTool(file_ids=[file.id])

        # Define an agent that uses the CodeInterpreterTool
        agent = agent_client.create_agent(
            model=model_deployment,
            name="data-agent-web",
            instructions="You are an AI agent that analyzes data in the uploaded file. Use Python for calculations.",
            tools=code_interpreter.definitions,
            tool_resources=code_interpreter.resources,
        )
        # print(f"Created agent: {agent.name} with ID: {agent.id}")

        # Create a thread for the conversation
        thread = agent_client.threads.create()
        # print(f"Created thread with ID: {thread.id}")
        
        return agent_client, agent.id, thread.id

    except Exception as ex:
        print(f"Error during initialization: {ex}")
        return None, None, None

def get_agent_response(agent_client, thread_id, agent_id, user_prompt):
    """
    Sends a user's prompt to the agent and gets the response.
    """
    try:
        # Send a prompt to the agent
        agent_client.messages.create(
            thread_id=thread_id,
            role=MessageRole.USER,
            content=user_prompt,
        )

        run = agent_client.runs.create_and_process(thread_id=thread_id, agent_id=agent_id)

        # Check the run status for failures
        if run.status == "failed":
            print(f"Run failed: {run.last_error}")
            return f"Run failed: {run.last_error}"

        # Get the latest response from the agent
        last_msg = agent_client.messages.get_last_message_text_by_role(
            thread_id=thread_id,
            role=MessageRole.AGENT,
        )
        
        return last_msg.text.value if last_msg else "Sorry, I couldn't get a response."

    except Exception as ex:
        print(f"Error during agent response: {ex}")
        return f"An error occurred: {ex}"