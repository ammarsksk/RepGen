from dataclasses import dataclass, field
from typing import Any, Dict, List

@dataclass

class State:
    topic :str
    notes: List[str] = field(default_factory=list)
    outline: List[str] = field(default_factory=list)
    draft: str = ""
    feedback: List[str] = field(default_factory=list)
    meta: Dict[str, Any] = field(default_factory=dict)
