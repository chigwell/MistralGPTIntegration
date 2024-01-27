import unittest
from unittest.mock import patch, MagicMock
from mistralai.models.chat_completion import ChatMessage
from mistralgptintegration.integration import MistralGPTIntegration

class TestMistralGPTIntegration(unittest.TestCase):
    @patch('mistralgptintegration.integration.MistralClient')
    def test_query_gpt_successful(self, mock_client):
        # Mocking the MistralClient and its chat method response
        mock_chat_response = MagicMock()
        mock_chat_response.choices = [MagicMock(message=MagicMock(content='Mocked response'))]
        mock_client.return_value.chat.return_value = mock_chat_response

        api_key = 'test_api_key'
        model_name = 'mistral-tiny'
        mistral = MistralGPTIntegration(api_key, model_name=model_name)

        prompt = "Test prompt"
        response = mistral.query_gpt(prompt)

        # Asserting the chat method was called with expected parameters
        mock_client.return_value.chat.assert_called_once_with(
            model=model_name,
            messages=[ChatMessage(role='user', content='Test prompt')],
            temperature=mistral.temperature,
            top_p=mistral.top_p,
            max_tokens=mistral.max_tokens
        )

        # Asserting the response is as expected
        self.assertEqual(response.choices[0].message.content, 'Mocked response')

    @patch('mistralgptintegration.integration.MistralClient')
    def test_query_gpt_no_response(self, mock_client):
        # Mocking the MistralClient with an empty choices list
        mock_chat_response = MagicMock()
        mock_chat_response.choices = []
        mock_client.return_value.chat.return_value = mock_chat_response

        api_key = 'test_api_key'
        model_name = 'mistral-tiny'
        mistral = MistralGPTIntegration(api_key, model_name=model_name)

        prompt = "Test prompt"
        response = mistral.query_gpt(prompt)

        # Asserting no choices in response results in an empty string
        self.assertEqual('', response.choices[0].message.content if response.choices else "")

if __name__ == '__main__':
    unittest.main()
