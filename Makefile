.PHONY: test lint build

build:
	cargo build

test: test-rust test-python

test-rust:
	cargo test

test-python:
	python -m pytest tests/ -v

lint:
	cargo clippy -- -D warnings

comply:
	pmat comply check
