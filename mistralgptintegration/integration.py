from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage

class MistralGPTIntegration:
    def __init__(self, api_key, model_name="mistral-tiny", temperature=0.1, top_p=1.0, max_tokens=150):
        """
        Initializes the Mistral GPT Integration.
        Args:
            api_key (str): Your Mistral API key.
            model_name (str): Identifier for the Mistral model to be used.
            temperature (float): Temperature for the completion.
            top_p (float): Top p for the completion.
            max_tokens (int): Maximum tokens for the completion.
        """
        self.api_key = api_key
        self.model_name = model_name
        self.client = MistralClient(api_key=self.api_key)
        self.temperature = temperature
        self.top_p = top_p
        self.max_tokens = max_tokens

    def query_gpt(self, prompt):
        """
        Queries the GPT model with a prompt and returns the response.
        Args:
            prompt (str): The prompt to send to the model.
        Returns:
            str: The model's response.
        """
        messages = [ChatMessage(role="user", content=prompt)]

        return self.client.chat(
            model=self.model_name,
            messages=messages,
            temperature=self.temperature,
            top_p=self.top_p,
            max_tokens=self.max_tokens
        )
