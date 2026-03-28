def match_score(job, skills):
    text = str(job).lower()
    score = 0

    for skill in skills:
        if skill in text:
            score += 1

    return score


def filter_jobs(jobs):
    skills = ["python", "ai", "machine learning", "data"]

    scored_jobs = []

    for job in jobs:
        score = match_score(job, skills)
        if score > 0:
            scored_jobs.append((job, score))

    # sort by score (highest first)
    scored_jobs.sort(key=lambda x: x[1], reverse=True)

    return scored_jobs