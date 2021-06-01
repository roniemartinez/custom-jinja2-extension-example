.PHONY: test
test:
	poetry run pytest --cov=markdown_extension --cov-report=xml --cov-report=html -vv

.PHONY: requirements.txt
requirements.txt:
	poetry export -f requirements.txt --output requirements.txt --without-hashes
