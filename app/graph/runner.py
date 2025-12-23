from typing import Callable, List
from app.core.state import State

Node = Callable[[State], State]

def run_pipeline(topic: str, nodes: List[Node]) -> State:
    state = State(topic=topic)
    for node in nodes:
        state = node(state)
    return state

def state_summary(state: State) -> str:

    lines = []
    lines.append("\n===== NOTES =====")
    lines.extend(f"- {n}" for n in state.notes)

    lines.append("\n===== OUTLINE =====")
    lines.extend(f"- {h}" for h in state.outline)

    lines.append("\n===== DRAFT =====")
    lines.append(state.draft.strip() if state.draft else "(empty)")

    lines.append("\n===== REVIEW FEEDBACK =====")
    lines.extend(f"- {f}" for f in state.feedback)

    return "\n".join(lines)
