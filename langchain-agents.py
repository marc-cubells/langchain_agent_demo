from langchain.agents import load_tools # load_tools is a function that loads the specified tools
from langchain.agents import initialize_agent # initialize_agent is a function that initializes an agent with the given tools and language model
from langchain.llms import OpenAI # OpenAI is the LLM class for interfacing with OpenAI's LLM
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

#Load the LLM Model
open_ai_llm = OpenAI(temperature=0)

#Load the Tools the agent can use
tools = load_tools(["serpapi", "llm-math"], llm=open_ai_llm)

#Instantiate the agent
agent = initialize_agent(
    tools   = tools, 
    llm     = open_ai_llm, 
    agent   = "zero-shot-react-description", 
    verbose = True
    )

#Execute the agent by passing a prompt
agent.run("Who is the current president of Switzerland? What is the largest prime number that is smaller that their age? Just give me the number.")