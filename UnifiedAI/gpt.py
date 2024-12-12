from openai import OpenAI
from openai.types.chat import ChatCompletionMessageParam, ChatCompletionUserMessageParam
from UnifiedAI.api import API

#python version 3.11
# openai==1.35.8 or 1.56.2



class GPT(API):
	def __init__(self, name : str,  api_key: str, model : str):

		self.name = name
		
		self.api_key = api_key

		self.connect = OpenAI(api_key=self.api_key)

		self.model_name = model

		self.system_instructions = "You are a helpful assistant."

		self.max_tokens = 512

		self.history: list[ChatCompletionMessageParam] = [{"role": "system", "content": f"{self.system_instructions}"},]


	def _ask(self) -> str:
		response = self.connect.chat.completions.create(
			model=self.model_name, messages=self.history,max_tokens=self.max_tokens)

		print(f"recieved {self.name}'s response.\n")

		return str(response.choices[0].message.content)


	def _add(self, text: str) -> None:
		self.history.append(ChatCompletionUserMessageParam(
				role="user", content=f"{text}"))

	def set_instructions(self, instructions : str) -> None:
		self.system_instructions = instructions
		self.history[0] = {"role": "system", "content": f"{self.system_instructions}"}


	def history(self) -> list:
		
		history = []

		for item in self.history:
			history.append(f"{item['role']}: {item['content']}")  # type: ignore

		return history








