install:
	pip install poetry && \
	poetry install

start:
	poetry run python bot_seo/main.py