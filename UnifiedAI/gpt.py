from openai import OpenAI
from openai.types.chat import ChatCompletionMessageParam, ChatCompletionUserMessageParam
from UnifiedAI.api import API

class GPT(API):
	def __init__(self, name : str,  api_key: str, model : str):

		self.name = name

		self.type = "gpt"
		
		self.api_key = api_key

		self.connect = OpenAI(api_key=self.api_key)

		self.model_name = model

		self.system_instructions = "You are a helpful assistant."

		self.max_tokens = 512

		self.usage = self.Usage(0,0)

		self.history: list[ChatCompletionMessageParam] = [{"role": "system", "content": f"{self.system_instructions}"},]



	def _trackUsage(self,message) -> None:

		self.usage.input_tokens += message.usage.prompt_tokens

		self.usage.output_tokens += message.usage.completion_tokens


	def _ask(self) -> str:
		response = self.connect.chat.completions.create(
			model=self.model_name, messages=self.history,max_tokens=self.max_tokens)

		print(f"recieved {self.name}'s response.\n")

		self._trackUsage(response)

		return str(response.choices[0].message.content)

	def reset_history(self) -> None:
		self.history : list[ChatCompletionMessageParam] = [{"role": "system", "content": f"{self.system_instructions}"},]

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








