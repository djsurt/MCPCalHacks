from fastapi import FastAPI
from app.github_client import GitHubClient
from app.models import PRRequest, ReviewBullets
from app.creao_adapter import generate_vibe_summary

app = FastAPI(title="PerfPilot API", version="1.0.0")

@app.get("/")
def root():
    return {"message": "PerfPilot API is running 🚀"}

@app.post("/generate_review", response_model=ReviewBullets)
def generate_review(data: PRRequest):
    gh = GitHubClient(data.token)
    prs = gh.get_pull_requests(data.owner, data.repo)

    # Only use title and description/body from the PR list response.
    # The list-pulls endpoint does NOT include additions/deletions — those
    # are available from the single-PR endpoint. Keep this simple: title + body.
    summarized_prs = [
        f"{p.get('title', '').strip()} - {p.get('body') or ''}".strip()
        for p in prs
    ]

    bullets = generate_vibe_summary(summarized_prs)
    return {"bullets": bullets}
