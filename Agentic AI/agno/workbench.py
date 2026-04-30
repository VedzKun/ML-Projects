import os
from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.google import Gemini
from agno.db.sqlite import SqliteDb
from agno.os import AgentOS
from agno.tools.workspace import Workspace

load_dotenv()

workbench = Agent(
    name="Workbench",
    model=Gemini(
        id="gemini-2.0-flash",
        api_key=os.getenv("GEMINI_API_KEY")
    ),
    tools=[Workspace(".", allowed=["read", "list", "search"], confirm=["write", "edit", "delete", "shell"])],
    enable_agentic_memory=True,
    add_history_to_context=True,
    num_history_runs=3,
)

agent_os = AgentOS(agents=[workbench], tracing=True, db=SqliteDb(db_file="agno.db"))
app = agent_os.get_app()