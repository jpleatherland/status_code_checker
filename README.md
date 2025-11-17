# Status Code Checker

A simple and lightweight CLI tool to quickly look up HTTP status code meanings and descriptions.

<img width="1177" height="562" alt="image" src="https://github.com/user-attachments/assets/de95717b-2b6b-448a-a3f7-a5f5c894ed72" />

## Features

- 🚀 **Fast lookups**: Instantly get explanations for HTTP status codes
- 📚 **Comprehensive database**: Covers all standard HTTP status codes
- 🔢 **Batch processing**: Check multiple status codes at once
- 🛡️ **Error handling**: Gracefully handles invalid inputs
- 🐍 **Pure Python**: No external dependencies required

## Installation

### Quick Install (using Make)

```bash
git clone https://github.com/jpleatherland/status_code_explainer.git
cd status_code_explainer
make install
```

### From Source

```bash
git clone https://github.com/jpleatherland/status_code_explainer.git
cd status_code_explainer
pip install -e .
```

### Using uv (recommended)

```bash
git clone https://github.com/jpleatherland/status_code_explainer.git
cd status_code_explainer
uv sync
```

## Usage

### Command Line Interface

Check a single status code:
```bash
statuscodechecker 404
```

Check multiple status codes:
```bash
statuscodechecker 200 404 500
```

### As a Python Module

```bash
python -m status_code_checker 404
```

### Example Output

```bash
$ statuscodechecker 200 404 500

Status Code Explanations:
200 - OK: The request was successful.
404 - Not Found: The server can not find the requested resource.
500 - Internal Server Error: The server has encountered a situation it doesn't know how to handle.
```

### Handling Unknown Codes

```bash
$ statuscodechecker 999

Status Code Explanation:
999 - Unknown: Status code may be a custom error defined on the server.
```

### Invalid Input Handling

```bash
$ statuscodechecker 200 abc 404

Discarded non-integer values: abc (integers are required)

Status Code Explanations:
200 - OK: The request was successful.
404 - Not Found: The server can not find the requested resource.
```

## Supported Status Codes

This tool includes explanations for all standard HTTP status codes including:

- **1xx Informational**: Continue, Switching Protocols, etc.
- **2xx Success**: OK, Created, Accepted, No Content, etc.
- **3xx Redirection**: Moved Permanently, Found, Not Modified, etc.
- **4xx Client Error**: Bad Request, Unauthorized, Forbidden, Not Found, etc.
- **5xx Server Error**: Internal Server Error, Bad Gateway, Service Unavailable, etc.

## Development

### Prerequisites

- Python 3.12 or higher
- uv (recommended) or pip

### Setting Up Development Environment

```bash
# Clone the repository
git clone https://github.com/jpleatherland/status_code_explainer.git
cd status_code_explainer

# Install development dependencies
uv sync

# Install pre-commit hooks
uv run pre-commit install
```

### Running Tests

```bash
# Run all tests using Make
make test

# Or run directly with uv
uv run pytest

# Run tests with coverage
uv run pytest --cov=status_code_checker

# Run specific test file
uv run pytest tests/test_main.py
```

### Code Quality

This project uses several tools to maintain code quality:

- **Black**: Code formatting
- **Ruff**: Fast linting and formatting
- **MyPy**: Static type checking
- **Pyright**: Additional type checking
- **Pre-commit**: Git hooks for quality checks

```bash
# Lint code using Make
make lint

# Or run directly with uv
uv run ruff check src tests

# Format code
uv run black src tests

# Type checking
uv run mypy src
uv run pyright src
```

### Make Commands

The project includes a Makefile with convenient commands:

```bash
make install    # Install the package using uv
make run        # Run the tool (use ARGS="200 404" to pass arguments)
make test       # Run all tests
make lint       # Run linting checks
```

Example with arguments:
```bash
make run ARGS="200 404 500"
```

### Project Structure

```
├── src/
│   └── status_code_checker/
│       ├── __init__.py
│       ├── __main__.py          # CLI entry point
│       ├── status_code_checker.py # Core logic
│       └── status_codes.py      # Status code database
├── tests/
│   ├── test_main.py            # CLI tests
│   └── test_status_explainer.py # Core logic tests
├── pyproject.toml              # Project configuration
└── README.md
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run tests and quality checks
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## Author

**Jack Leatherland**

## Acknowledgments

- HTTP status codes follow the official [RFC 7231](https://tools.ietf.org/html/rfc7231) specification
- Inspired by the need for quick status code lookups during web development
