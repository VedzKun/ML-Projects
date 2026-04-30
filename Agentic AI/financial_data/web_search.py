from phi.agent import Agent
from phi.model.google import Gemini
from phi.tools.duckduckgo import DuckDuckGo
import os
from dotenv import load_dotenv

load_dotenv()

web_agent = Agent(
    name="web-agent",
    model=Gemini(id="gemini-2.5-flash", api_key=os.getenv("GEMINI_API_KEY")),
    tools=[DuckDuckGo()],
    description="Web Search Agent",
    instruction="You are a web search agent. Use DuckDuckGo to search the web and return the results."
)

web_agent.print_response("Im going to invest 100rupees in digital gold, what is the rate of gold right now?", markdown=True)
