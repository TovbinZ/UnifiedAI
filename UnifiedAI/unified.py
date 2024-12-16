from UnifiedAI.api import API
from UnifiedAI.claude import Claude
from UnifiedAI.gpt import GPT
from UnifiedAI.gemini import Gemini


def AI(name : str, key : str, model : str) -> API:
	
	if "gpt" in model:
		return GPT(name, key, model)

	elif "claude" in model:
		return Claude(name, key, model)

	elif "gemini" in model:
		return Gemini(name, key, model)

	else:
		raise NameError("No model of that name.")



class Batch():
	def __init__(self, models: list):
		
		self.models = models

		self.usage : dict = {}


	def set_instructions(self,instructions : str) -> None:
		for model in self.models:
			model.set_instructions(instructions)


	def set_max_tokens(self, tokens : int) -> None:
		for model in self.models:
			model.set_max_tokens(tokens)


	def add_context(self, context : str) -> None:
		for model in self.models:
			model.add_context(context)


	def get_response(self, question : str) -> dict:

		responses = {}

		for model in self.models:
			responses[model.name] = model.get_response(question)

			self.usage[model.name] = model.Usage(model.usage.input_tokens,model.usage.output_tokens)

		return responses












