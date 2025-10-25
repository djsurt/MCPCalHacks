def generate_vibe_summary(prs_summary: list[str]) -> list[str]:
    """
    Generate performance-style bullet points based on PR summaries.
    You can later replace this with a call to OpenAI, Mistral, etc.
    """
    bullets = []
    for pr in prs_summary:
        bullets.append(f"Demonstrated technical ownership by completing: {pr}")
    return bullets
