from dataclasses import dataclass, field
from typing import List
import time

@dataclass
class Secret:
    id: str
    type: str
    first_seen: float
    last_seen: float
    locations: List[str] = field(default_factory=list)
    occurrences: int = 0
    risk_score: float = 0.0
