ARGS ?= --help
run:
	uv run python3 -m status_code_checker $(ARGS)
test:
	uv run pytest -vs
lint:
	uv run ruff check .

