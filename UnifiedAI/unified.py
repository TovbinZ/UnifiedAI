from UnifiedAI.api import API
from UnifiedAI.claude import Claude
from UnifiedAI.gpt import GPT
from UnifiedAI.gemini import Gemini
from UnifiedAI.ollama import Ollama



def AI(instance_name : str, api_provider : str, key : str, model : str) -> API:
	
	if api_provider == "openai":
		print("open")
		return GPT(instance_name, key, model, False)

	elif api_provider == "anthropic":
		print("anth")
		return Claude(instance_name, key, model)

	elif api_provider == "google":
		print("goo")
		return Gemini(instance_name, key, model)

	elif api_provider == "ollama":
		print("oll")
		return Ollama(instance_name, key, model)
	else:
		print("Error: no AI API provider by that name.")


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

			self.usage[model.name] = model.Usage(model.usage.api_calls,model.usage.input_tokens,model.usage.output_tokens)

		return responses












