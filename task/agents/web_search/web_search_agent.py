from task.agents.base_agent import BaseAgent
from task.agents.web_search._prompts import SYSTEM_PROMPT
from task.tools.base_tool import BaseTool

#TODO:
# Just simply extend the BaseAgent and provide the constructor

class WebSearchAgent(BaseAgent):
    def __init__(self, tools: list[BaseTool], endpoint: str):
        super().__init__(
            system_prompt=SYSTEM_PROMPT,
            tools=tools,
            endpoint=endpoint
        )
