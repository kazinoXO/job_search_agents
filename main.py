from tools.job_api import fetch_jobs
from agents.filter_agent import filter_jobs

jobs = fetch_jobs()

matched_jobs = filter_jobs(jobs)

print("\nTop Matched Jobs:\n")

for job, score in matched_jobs:
    print(f"Title: {job['title']}")
    print(f"Company: {job['company_name']}")
    print(f"Match Score: {score}")
    print("-" * 40)