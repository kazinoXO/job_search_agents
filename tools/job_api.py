import requests

def fetch_jobs():
    url = "https://remotive.com/api/remote-jobs"

    try:
        response = requests.get(url)
        print("Status:", response.status_code)

        data = response.json()
        return data.get("jobs", [])[:10]

    except Exception as e:
        print("Error:", e)
        return []