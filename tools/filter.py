def filter_jobs(jobs, skills):
    filtered = []
    
    for job in jobs:
        desc = job["description"].lower()
        if any(skill in desc for skill in skills):
            filtered.append(job)
    
    return filtered