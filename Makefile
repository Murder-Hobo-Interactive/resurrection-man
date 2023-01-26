run:
	pipenv run python src/main.py

edit:
	pipenv run pyxel edit src/resources.pyxres

types:
	pipenv run mypy --strict --implicit-reexport src

format:
	pipenv run black .

uml:
	pipenv run pyreverse -o png src/*.py src/components/*.py
