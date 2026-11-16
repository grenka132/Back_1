SHELL := /bin/sh

.PHONY: requirements
requirements: pyproject.toml
	uv sync


.PHONY: run_api
run_api: requirements
	uv run -m src.main

.PHONY: run_for_docker
run_for_docker: requirements
	uv run alembic upgrade head
	uv run -m src.main
