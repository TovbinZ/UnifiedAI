from anthropic import Anthropic
from UnifiedAI.api import API

class Claude(API):
	def __init__(self, name : str, api_key: str, model : str):
		
		self.name = name

		self.type = "claude"

		self.api_key = api_key

		self.connect = Anthropic(api_key=self.api_key)

		self.model_name = model

		self.system_instructions = "You are a helpful assistant."

		self.max_tokens = 512

		self.usage = self.Usage(0,0,0)

		self.history = []


	def _trackUsage(self,message) -> None:

		self.usage.api_calls += 1

		self.usage.input_tokens += message.usage.input_tokens

		self.usage.output_tokens += message.usage.output_tokens

	def _ask(self) -> str:
		response = self.connect.messages.create(
			model=self.model_name,
			max_tokens=self.max_tokens,
			system=self.system_instructions,
			messages=self.history
		)

		self._trackUsage(response)

		print(f"recieved {self.name}'s response.\n")

		return  response.content[0].text


	def _add(self, text : str) -> None:
		self.history.append({"role": "user", "content": [{"type": "text", "text": f"{text}"}]})


	def reset_history(self) -> None:
		self.history = []

	def set_instructions(self, instructions) -> None:
		self.system_instructions = instructions


	def history(self) -> list:

		history = []

		for item in self.history:
			history.append(f"{item['role']}: {item['content'][0]['text']} ")

		return history
	









		