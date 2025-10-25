from pydantic import BaseModel
from typing import List, Optional

class PRRequest(BaseModel):
    owner: str
    repo: str
    token: Optional[str] = None

class ReviewBullets(BaseModel):
    bullets: List[str]
