# orchestrator/engine.py

from orchestrator.state import WorkflowState


class WorkflowEngine:
    """
    Executes a sequence of workflow steps with shared state.
    """

    def __init__(self, steps):
        """
        steps: list of (step_name, callable)
        """
        self.steps = steps

    def run(self, initial_state=None):
        state = WorkflowState(initial_state)

        print("🚀 Starting workflow execution")

        for step_name, step_fn in self.steps:
            print(f"\n➡️  Executing step: {step_name}")

            try:
                state.record_step(step_name)
                state = step_fn(state)
                print(f"✅ Step '{step_name}' completed")

            except Exception as e:
                print(f"❌ Step '{step_name}' failed: {e}")
                raise

        print("\n🎉 Workflow completed successfully")
        return state
