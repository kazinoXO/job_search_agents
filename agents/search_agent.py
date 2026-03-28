from crewai import Agent
from tools.job_api import fetch_jobs

def get_jobs_tool():
    return fetch_jobs()

search_agent = Agent(
    role="Job Searcher",
    goal="Fetch latest jobs",
    backstory="Expert in finding jobs",
    tools=[get_jobs_tool]
)   