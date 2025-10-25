import os
import requests
from typing import List
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

class GitHubClient:
    def __init__(self, token: str = None):
        self.token = token or GITHUB_TOKEN
        if not self.token:
            raise ValueError("GitHub token not provided. Set GITHUB_TOKEN in .env or pass it explicitly.")

        self.base_url = "https://api.github.com"
        self.headers = {"Authorization": f"Bearer {self.token}"}

    def get_pull_requests(self, owner: str, repo: str) -> List[dict]:
        """Fetch the latest closed pull requests."""
        url = f"{self.base_url}/repos/{owner}/{repo}/pulls?state=closed&per_page=20"
        print(f"Fetching PRs from {url}")
        res = requests.get(url, headers=self.headers)
        print(res.json())
        res.raise_for_status()
        return res.json()

    def get_pr_details(self, owner: str, repo: str, pr_number: int) -> dict:
        """Fetch details for a specific pull request."""
        url = f"{self.base_url}/repos/{owner}/{repo}/pulls/{pr_number}"
        res = requests.get(url, headers=self.headers)
        res.raise_for_status()
        return res.json()
