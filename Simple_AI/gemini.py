from Simple_AI.api import API
import google.generativeai as genai
from google.generativeai.types.generation_types import GenerateContentResponse




class Gemini(API):
	def __init__(self, name : str, api_key : str, model : str):
		
		self.name = name

		self.api_key = api_key

		genai.configure(api_key = self.api_key)

		self.system_instructions =  "You are a helpful assistant."

		self.model_name = model

		self.max_tokens = 512

		self.connect = genai.GenerativeModel(
            model_name=self.model_name,
            generation_config = {"max_output_tokens": self.max_tokens},
            system_instruction = self.system_instructions,
        )

		self.history = []


	def _ask(self):
		response : GenerateContentResponse = self.connect.start_chat(history=self.history).send_message("?")

		return response.text


	def _add(self, text : str) -> None:
		self.history.append(
					{
						"role": "user",
						"parts": [f"{text}"],
					}
				)

	def set_instructions(self, instructions : str) -> None:
		
		self.system_instructions = instructions

		self.connect = genai.GenerativeModel(
            model_name=self.model_name,
            system_instruction=self.system_instructions,
            generation_config = {"max_output_tokens": self.max_tokens}
        )


	def set_max_tokens(self,tokens: int) -> None:
		self.max_tokens = tokens

		self.connect = genai.GenerativeModel(
			model_name=self.model_name,
			system_instruction=self.system_instructions,
			generation_config = {"max_output_tokens": self.max_tokens}
		)

	def history(self) -> list:    
       
		history = []
        
		for item in self.history:
			history.append(f"{item['role']}: {item['parts'][0]}")

		return history





