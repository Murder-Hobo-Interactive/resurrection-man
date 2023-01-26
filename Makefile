run:
	python -m pipenv run python src/main.py

edit:
	python -m pipenv run pyxel edit src/resources.pyxres

types:
	python -m pipenv run mypy --strict --implicit-reexport src

format:
	python -m pipenv run black .

uml:
	python -m pipenv run pyreverse -o png src/*.py src/components/*.py
