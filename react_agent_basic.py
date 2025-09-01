from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_community.tools import TavilySearchResults
from langchain.agents import initialize_agent , tool
import datetime

# Load environment variables
load_dotenv()

# Initialize LLM 
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

# Define tools
search_tool = TavilySearchResults(search_depth="basic")

@tool
def get_system_time(format : str = "%y-%m-%d %H:%M:%S"):
    """ Return the current date and time in the specified format  """

    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime(format)
    return formatted_time

tools = [search_tool , get_system_time]

# Initialize agent
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent="zero-shot-react-description",
    verbose=True
) 
# Invoke the agent
agent.invoke("when was spacxx last launch and how man days age this happend ")          