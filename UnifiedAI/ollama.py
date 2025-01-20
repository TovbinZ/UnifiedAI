from ollama import chat
from ollama import ChatResponse
from UnifiedAI.api import API
from typing import Any


class Ollama(API):
	def __init__(self,name : str, api_key: Any, model : str):

		self.name = name

		self.type = "ollama"
		
		self.api_key = api_key

		self.model_name = model

		self.system_instructions = "You are a helpful assistant."

		self.usage = self.Usage(0,0,0)

		self.history: list = [{"role": "system", "content": f"{self.system_instructions}"}]


	def _trackUsage(self,message : ChatResponse) -> None:

		self.usage.api_calls += 1

		self.usage.input_tokens += message.prompt_eval_count

		self.usage.output_tokens += message.eval_count


	def _ask(self) -> str:
		
		response : ChatResponse =  chat(model=self.model_name, messages=self.history)

		print(f"recieved {self.name}'s response.\n")

		self._trackUsage(response)

		return response.message.content

	def reset_history(self) -> None:
		self.history : list = []

	def _add(self, text: str) -> None:
		self.history.append(
			{
				'role': 'user',
    			'content': text,

			})


	def set_instructions(self, instructions : str) -> None:
		self.system_instructions = instructions
		self.history[0] = {"role": "system", "content": f"{self.system_instructions}"}

	def set_max_tokens(self,tokens: int) -> None:
		print("WARNING: unable to set max tokens for a local ollama model.")


	def history(self) -> dict:
		return self.history
























