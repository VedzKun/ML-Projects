from phi.agent import Agent
from phi.model.google import Gemini
import os
from dotenv import load_dotenv

load_dotenv()

finance_agent = Agent(
    name="Finance Agent",
    model=Gemini(id="gemini-2.5-flash", api_key=os.getenv("GEMINI_API_KEY")),
    description="Financial Agent",
    instructions=["Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
)
finance_agent.print_response("Summarize analyst recommendations for NVDA", stream=True)