
import asyncio
from agno.agent import Agent
from agno.tools.mcp import MCPTools
from dotenv import load_dotenv
from agno.models.groq import Groq
import warnings
warnings.filterwarnings("ignore", category=ResourceWarning)
import nest_asyncio

load_dotenv()


# Allow nested event loops
nest_asyncio.apply()


async def run_agent(query: str):
    
    
    async with MCPTools("npx -y firecrawl-mcp") as mcp_tools2:
  
    
        try:
            agent = Agent(model=Groq(id="meta-llama/llama-4-scout-17b-16e-instruct"), tools=[mcp_tools2], markdown=True, show_tool_calls=True, debug_mode=True)
            await agent.aprint_response("Please use the provided tools and answer the query and also show the exact Tools used: " + query, stream=True)
            
            
        except Exception as ex:
            print(ex)
            


if __name__ == "__main__":      
    query = input("Query: ")
    asyncio.run(run_agent(query))

      
