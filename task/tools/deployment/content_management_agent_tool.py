from typing import Any

from task.tools.deployment.base_agent_tool import BaseAgentTool


class ContentManagementAgentTool(BaseAgentTool):

    #TODO:
    # Provide implementations of deployment_name (in core config), name, description and parameters.
    # Don't forget to mark them as @property
    # Parameters:
    #   - prompt: string. Required.
    #   - propagate_history: boolean
    
    @property
    def deployment_name(self) -> str:
        return "content-management-agent"
    
    @property
    def name(self) -> str:
        return "content_management_agent_tool"
    
    @property
    def description(self) -> str:
        return "Manage content with the help of content management agent"
    
    @property
    def parameters(self) -> dict[str, Any]:
        return {
            "type": "object",
            "properties": {
                "prompt": {
                    "type": "string",
                    "description": "The request to content management agent",
                },
                "propagate_history": {
                    "type": "boolean",
                    "description": "Whether to propagate the history of communication with content management agent. If true, the history will be propagated, otherwise only current request will be sent to content management agent",
                    "default": False
                },
            },
            "required": ["prompt"]
        }
