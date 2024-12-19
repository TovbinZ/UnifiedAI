from abc import ABC, abstractmethod

class API(ABC):

    class Usage():
        def __init__(self,_input_tokens : int, _output_tokens : int):
            self.input_tokens = _input_tokens

            self.output_tokens = _output_tokens


    # abstract helper method for tracking token usage
    @abstractmethod
    def _trackUsage(self,message) -> None:
        pass

	# abstract helper method for adding text to self.history
    @abstractmethod
    def _add(self, text: str) -> None:
        pass

    # abstract helper method for asking the ai a question.
    @abstractmethod
    def _ask(self) -> str:
        pass

    # abstract method for reseting self.history
    @abstractmethod
    def reset_history(self) -> None:
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
       return self._ask()

    # return a cleaned up self.history.
    @abstractmethod
    def history(self) -> list:
        pass


