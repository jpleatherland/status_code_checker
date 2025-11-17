ARGS ?= --help
UVFLAGS ?=

install:
	uv $(UVFLAGS) sync
	uv build
	uv tool install --force --no-cache .

install-dev:
	uv $(UVFLAGS) sync
	uv tool install --editable .

run:
	uv run python3 -m status_code_checker $(ARGS)

test:
	uv run pytest -vs

lint:
	uv run ruff check .
