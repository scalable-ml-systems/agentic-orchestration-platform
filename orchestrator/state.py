# orchestrator/state.py

from typing import Dict, Any
import time


class WorkflowState:
    """
    Central state object shared across all workflow steps.
    """

    def __init__(self, initial_data: Dict[str, Any] = None):
        self.data = initial_data or {}
        self.metadata = {
            "created_at": time.time(),
            "steps_executed": []
        }

    def update(self, key: str, value: Any):
        self.data[key] = value

    def get(self, key: str, default=None):
        return self.data.get(key, default)

    def record_step(self, step_name: str):
        self.metadata["steps_executed"].append({
            "step": step_name,
            "timestamp": time.time()
        })

    def snapshot(self) -> Dict[str, Any]:
        """
        Returns a full snapshot of workflow state.
        Useful for debugging and logging.
        """
        return {
            "data": self.data,
            "metadata": self.metadata
        }
