# Oproof
Validate prompt-response pairs using Ollama and Python

## Overview
Oproof is a tool designed to validate prompt-response pairs in domains such as basic math, grammar, or spelling. It uses the Ollama model to ensure that responses are coherent and relevant to their corresponding prompts. Invalid pairs are identified and can be removed from the dataset to maintain high-quality data.

## Features
- Validate prompt-response pairs in basic math, grammar, or spelling
- Detect and include the domain and context in the validation report
- Generate JSON reports indicating the validity of each pair
- Filter out invalid pairs from the dataset

## Installation
To install Oproof, clone the repository and install the required dependencies:

```bash
git clone https://github.com/p3nGu1nZz/oproof.git
cd oproof
pip install -e .
```

## Usage
Oproof is set up and run as a Python command-line interface (CLI) package. To validate a prompt-response pair, use the following command:

```bash
oproof "What is 2 + 2?" "4"
```

This will output a JSON report indicating whether the pair is valid or not, along with the detected domain and context.

## Example
Here's an example of how to use Oproof in a script:

```python
import json
from oproof import oproof

prompt = "What is 2 + 2?"
response = "4"
model = YourModel()  # Replace with your model initialization
proof_result = oproof(prompt, response, model)

print(json.dumps(proof_result, indent=4))
```

### Example JSON Output
Here's what the JSON output might look like for a valid pair:

```json
{
    "prompt": "What is 2 + 2?",
    "response": "4",
    "is_valid": true,
    "domain": "basic math",
    "context": "arithmetic",
    "reason": null
}
```

And for an invalid pair:

```json
{
    "prompt": "What is 2 + 2?",
    "response": "5",
    "is_valid": false,
    "domain": "basic math",
    "context": "arithmetic",
    "reason": "Incorrect response."
}
```

## Development
To set up a development environment, follow these steps:

1. **Create a virtual environment**:
    ```bash
    python -m venv .venv/oproof
    ```

2. **Activate the virtual environment**:
    - On Windows:
        ```bash
        .venv\oproof\Scripts\activate
        ```
    - On macOS and Linux:
        ```bash
        source .venv/oproof/bin/activate
        ```

3. **Install the package in editable mode**:
    ```bash
    pip install -e .
    ```

4. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Contributing
We welcome contributions! Please read our [contributing guidelines](CONTRIBUTING.md) for more details.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
