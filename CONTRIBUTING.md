# Contributing to PROV-ES

Thank you for your interest in contributing to PROV-ES! We welcome contributions from the community.

## Prerequisites

- Python 3.12 or higher
- Git
- pip (Python package manager)

## Development Setup

1. Fork the repository on GitHub
2. Clone your fork locally:
   ```bash
   git clone https://github.com/your-username/prov_es.git
   cd prov_es
   ```
3. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
4. Install development dependencies:
   ```bash
   pip install -e .[dev]
   ```

## Code Style

We use the following tools to maintain code quality:

- **Black** for code formatting
- **isort** for import sorting
- **flake8** for linting

Before submitting a pull request, please run:

```bash
black .
isort .
flake8
pytest
```

## Pull Request Process

1. Create a feature branch from the `main` branch
2. Make your changes
3. Add tests for your changes
4. Update documentation if needed
5. Run tests and ensure they pass
6. Submit a pull request with a clear description of your changes

## Reporting Issues

When reporting issues, please include:

- A clear description of the issue
- Steps to reproduce the issue
- Expected behavior
- Actual behavior
- Python version and operating system

## License

By contributing to this project, you agree that your contributions will be licensed under the project's [LICENSE](LICENSE) file.
