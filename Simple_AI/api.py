from abc import ABC, abstractmethod
from typing import Any


class API(ABC):
	
	# abstract helper method for adding text to self.history
    @abstractmethod
    def _add(self, text: str) -> None:
        pass

    # abstract helper method for asking the ai a question.
    @abstractmethod
    def _ask(self) -> str:
        pass

    # set the system instructions to be used.
    @abstractmethod
    def set_instructions(self,instructions : str) -> None:
    	pass

    # set the max tokens to be used.
    def set_max_tokens(self,tokens: int) -> None:
    	self.max_tokens = tokens

    # add context to self.history without sending an api call.
    def add_context(self, context: str) -> None:
    	self._add(context)

    # get response from the ai with self.history as context along with the question.
    def get_response(self, question: str) -> None:
       self._add(question)
       print(f"recieved {self.name}'s response")
       return self._ask()


    # return a cleaned up self.history.
    @abstractmethod
    def history(self) -> list:
        pass


