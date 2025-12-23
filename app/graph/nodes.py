from app.core.state import State

def researcher (state : State) -> State:
    state.notes.extend([
        f"{state.topic}: define the problem and motivation.",
        f"{state.topic}: list 3 key concepts and 2 challenges.",
        f"{state.topic}: include 2 real-world applications."
    ])
    return state

def outliner(state: State) -> State:

    state.outline = [
        f"Introduction: {state.topic}",
        "Background & Key Concepts",
        "Applications",
        "Challenges & Limitations",
        "Conclusion"
    ]
    return state

def writer(state: State) -> State:

    sections = []
    for heading in state.outline:
        sections.append(f"## {heading}")
        sections.append(f"(Draft placeholder) Expand: {heading}\n")
    state.draft = "\n".join(sections)
    return state

def reviewer(state: State) -> State:

    state.feedback.extend([
        "Add concrete examples in 'Applications'.",
        "Define key terms clearly in 'Background & Key Concepts'.",
        "Make the conclusion summarize 3 takeaways."
    ])
    return state

def finalizer (state: State) -> State:
    state.draft += "\nFinal - This is the final state of the report. Ready to display"
    return state
