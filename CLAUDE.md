# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is `mypy-boto3-builder`, a code generator that creates type annotations for AWS SDK libraries (boto3, aioboto3, aiobotocore). It introspects AWS service definitions from botocore and generates Python type stubs, enabling static type checking for AWS SDK usage.

## Common Development Commands

### Setup and Dependencies
```bash
# Install uv (if not already installed)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install dependencies
uv sync --all-extras --dev
```

### Building and Testing
```bash
# Build the main package
./scripts/build.sh

# Run pre-commit checks (formatting, linting, type checking)
./scripts/before_commit.sh

# Run integration tests
python scripts/integration.py

# Run unit tests
pytest

# Type checking with mypy
mypy mypy_boto3_builder

# Type checking with pyright
pyright mypy_boto3_builder

# Linting and formatting with ruff
ruff check mypy_boto3_builder
ruff format mypy_boto3_builder
```

### Project Commands
```bash
# Generate type stubs interactively
uvx mypy_boto3_builder

# Generate specific services
python -m mypy_boto3_builder output_dir --services s3 ec2 --product types-boto3

# Run CI workflows
python scripts/ci.py integration
python scripts/ci.py sanity
```

## Architecture Overview

The codebase follows a three-stage pipeline:

1. **Parsers** (`mypy_boto3_builder/parsers/`) - Extract AWS service definitions from botocore
2. **Structures** (`mypy_boto3_builder/structures/`) - Internal data model representing services
3. **Generators** (`mypy_boto3_builder/generators/`) - Convert structures to target library formats using Jinja2 templates

### Key Components

- **`/parsers/`** - Extract service definitions (ShapeParser, ClientParser, ResourceParser)
- **`/structures/`** - Data model (ServicePackage, Client, Method, TypeAnnotation)  
- **`/generators/`** - Target-specific generators (TypesBoto3Generator, Boto3Generator, etc.)
- **`/templates/`** - Jinja2 templates organized by target library
- **`/type_annotations/`** - Abstract type system for Python type hints
- **`/type_maps/`** - Configuration for shape-to-type mappings

### Supported Products

The generator supports multiple target libraries:
- `types-boto3` - Type stubs for boto3
- `boto3-stubs` - Legacy boto3 stubs (deprecated)
- `types-aioboto3` - Type stubs for aioboto3
- `types-aiobotocore` - Type stubs for aiobotocore

## Configuration Files

- **`pyproject.toml`** - Project configuration, dependencies, tool settings
- **`/scripts/`** - Development and CI scripts
- **`/integration/`** - Integration test examples and snapshots
- **`vulture_whitelist.txt`** - Dead code detection whitelist

## Testing Strategy

- **Unit tests** in `/tests/` - Test individual components
- **Integration tests** via `scripts/integration.py` - End-to-end generation and type checking
- **Type checking validation** - Generated stubs are validated with mypy and pyright