import os
import requests
import time

GITHUB_API = "https://api.github.com/graphql"
GITHUB_TOKEN = os.environ["GITHUB_TOKEN"]

def run_query(query):
    headers = {"Authorization": f"Bearer {GITHUB_TOKEN}"}

    for _ in range(5):
        res = requests.post(GITHUB_API, json={"query": query}, headers=headers)

        if res.status_code == 200:
            return res.json()

        if res.status_code == 403:
            print("Rate limited, sleeping...")
            time.sleep(60)

    raise Exception(res.text)
