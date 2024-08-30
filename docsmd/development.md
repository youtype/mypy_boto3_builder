# Development

- Install Python 3.12+, ideally with [pyenv](https://github.com/pyenv/pyenv)
- Install [uv](https://docs.astral.sh/uv/): `curl -LsSf https://astral.sh/uv/install.sh | sh`
- Install dependencies: `uv sync --all-extras --dev`
- Use scripts for repo to check if everything works: `./scripts/build.sh`
- Run manual pre-commit: `./scripts/before_commit.sh`
