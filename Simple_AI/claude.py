from anthropic import Anthropic
from Simple_AI.api import API
import os

# Anthropic 0.30.1

class Claude(API):
	def __init__(self, name : str, api_key: str, model : str):
		
		self.name = name

		self.api_key = api_key

		self.connect = Anthropic(api_key=self.api_key)

		self.model_name = model

		self.system_instructions = "You are a helpful assistant."

		self.max_tokens = 512

		self.history = []


	def _ask(self) -> str:
		response = self.connect.messages.create(
			model=self.model_name,
			max_tokens=self.max_tokens,
			system=self.system_instructions,
			messages=self.history
		)

		return  response.content[0].text  # type: ignore


	def _add(self, text : str) -> None:
		self.history.append({"role": "user", "content": [{"type": "text", "text": f"{text}"}]})


	def set_instructions(self, instructions) -> None:
		self.system_instructions = instructions


	def history(self) -> list:

		history = []

		for item in self.history:
			history.append(f"{item['role']}: {item['content'][0]['text']} ")

		return history
	









		