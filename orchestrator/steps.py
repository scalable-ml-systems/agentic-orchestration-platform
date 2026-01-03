# orchestrator/steps.py

def fetch_text(state):
    """
    Simulates fetching input text.
    """
    text = "Agentic systems treat AI workflows as distributed systems."
    state.update("raw_text", text)
    return state


def transform_text(state):
    """
    Simulates a transformation step.
    """
    raw_text = state.get("raw_text")
    transformed = raw_text.upper()
    state.update("transformed_text", transformed)
    return state


def save_output(state):
    """
    Simulates saving output.
    """
    output = state.get("transformed_text")
    state.update("saved_output", output)
    return state
