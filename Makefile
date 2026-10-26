SHELL := /bin/bash

.PHONE: requirements
requirements: pyproject.toml
	uv sync

.PHONE: run_api
run_api: requirements
	uv run -m src.main
