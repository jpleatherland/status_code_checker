ARGS ?= --help
run:
	uv run python3 -m statuscodechecker $(ARGS)
test:
	uv run pytest -v
lint:
	uv run ruff check .

