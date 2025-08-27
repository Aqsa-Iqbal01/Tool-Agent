from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, set_tracing_disabled
from dotenv import load_dotenv
from my_tool.tools import add , subtract
import os


set_tracing_disabled(True)
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
base_url = os.getenv("GEMINI_BASE_URL")
model_name = os.getenv("GEMINI_MODEL_NAME")


client = AsyncOpenAI(api_key=api_key, base_url=base_url)

model = OpenAIChatCompletionsModel(
    openai_client=client,
    model=model_name
)


agent = Agent(
    name="Math Agent",
    instructions="You are a helpful Math Agent",
    model=model,
    tools= [add , subtract]
)

questions = [
    "what is 5 + 7?",
    "subtract 4 and 6",
    "what is 9 + 3?"
]

for q in questions:
    result = Runner.run_sync(starting_agent=agent, input=q)
    print(f"Q: {q}\nA: {result.final_output}\n")