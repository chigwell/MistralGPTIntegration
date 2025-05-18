[![PyPI version](https://badge.fury.io/py/MistralGPTIntegration.svg)](https://badge.fury.io/py/MistralGPTIntegration)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Downloads](https://static.pepy.tech/badge/MistralGPTIntegration)](https://pepy.tech/project/MistralGPTIntegration)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-blue)](https://www.linkedin.com/in/eugene-evstafev-716669181/)

# MistralGPTIntegration

`MistralGPTIntegration` is a Python package designed to provide GPT-based functionalities using the Mistral AI API. It enables users to quickly obtain comprehensive, context-aware responses from the model.

## Installation

To install `MistralGPTIntegration`, you can use pip:

```bash
pip install MistralGPTIntegration
```

## Usage

After installation, `MistralGPTIntegration` can be used in your Python scripts.

Example:

```python
from mistralgptintegration import MistralGPTIntegration

api_key = "<your_api_key>"
mistral = MistralGPTIntegration(api_key)
prompt = "Once upon a time"
response = mistral.query_gpt(prompt)
print(response)
```

- `api_key`: Your Mistral API key.
- `model_name`: The name of the Mistral model to use. Defaults to `mistral-tiny`.
- `temperature`: The temperature to use for the model. Defaults to `0.1`.
- `top_p`: The top_p to use for the model. Defaults to `1.0`.
- `max_tokens`: The maximum number of tokens to generate. Defaults to `150`.

## Customizing Your Queries

You can customize the behavior of `MistralGPTIntegration` by adjusting the parameters, such as the temperature, top_p, max_tokens, etc., to fit the specific needs of your queries or to tweak the behavior of the Mistral model.

## Output Example

When you query the model, it processes your prompt and returns a response. Here is an example of the output:

```json
{
  "id": "63213d34c61f4d96b893d7b1afc2b893",
  "object": "chat.completion",
  "created": 1706372087,
  "model": "mistral-small",
  "choices": [
    {
      "message": {
        "role": "assistant",
        "content": "some text"
      },
      "finish_reason": "stop",
      "index": 0
    }
  ],
  "usage": {
    "prompt_tokens": 318,
    "total_tokens": 622,
    "completion_tokens": 304
  }
}
```

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to check [issues page](https://github.com/chigwell/MistralGPTIntegration/issues).

## License

[MIT](https://choosealicense.com/licenses/mit/)
