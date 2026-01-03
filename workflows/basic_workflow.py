# workflows/basic_workflow.py

from orchestrator.engine import WorkflowEngine
from orchestrator.steps import fetch_text, transform_text, save_output


def run():
    steps = [
        ("fetch_text", fetch_text),
        ("transform_text", transform_text),
        ("save_output", save_output),
    ]

    engine = WorkflowEngine(steps)
    final_state = engine.run()

    print("\n🧠 Final Workflow State:")
    print(final_state.snapshot())


if __name__ == "__main__":
    run()
