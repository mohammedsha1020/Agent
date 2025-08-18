from crewai import Agent, Task, Crew
from dotenv import load_dotenv
import os


load_dotenv()

from crewai import LLM


llm = LLM(
    model="gemini/gemini-1.5-flash",
    temperature=0.4,
    api_key=os.environ['GOOGLE_API_KEY']
)

Research_agent=Agent(
    role="Research Agent",
    goal="Conduct research on a given topic and provide a detailed report.",
    backstory="you are a highly skilled researcher in Artificial Intelligence.",
    verbose=True,
    llm=llm
)

original_message = input("Enter the topic you want to research: ")

research_task=Task(
    description=f"""Research the topic: '''{original_message}'''""",
    agent=Research_agent,
    expected_output='give a clear explaination in given topic'
)

crew = Crew(
    agents=[Research_agent],
    tasks=[research_task],
    verbose=True
)

result = crew.kickoff()
print(result)