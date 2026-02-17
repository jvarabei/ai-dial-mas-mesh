from typing import Any

from task.tools.deployment.base_agent_tool import BaseAgentTool


class CalculationsAgentTool(BaseAgentTool):

    #TODO:
    # Provide implementations of deployment_name (in core config), name, description and parameters.
    # Don't forget to mark them as @property
    # Parameters:
    #   - prompt: string. Required.
    #   - propagate_history: boolean
    
    @property
    def deployment_name(self) -> str:
        return "calculations-agent"
    
    @property
    def name(self) -> str:
        return "calculations_agent_tool"
    
    @property
    def description(self) -> str:
        return "Perform calculations with the help of calculations agent, can run code in python"
    
    @property
    def parameters(self) -> dict[str, Any]:
        return {
            "type": "object",
            "properties": {
                "prompt": {
                    "type": "string",
                    "description": "The request to calculations agent",
                },
                "propagate_history": {
                    "type": "boolean",
                    "description": "Whether to propagate the history of communication with calculations agent. If true, the history will be propagated, otherwise only current request will be sent to calculations agent",
                    "default": False
                },
            },
            "required": ["prompt"]
        }

