types_cmd = python -m pipenv run mypy --strict --implicit-reexport src
format_cmd = python -m pipenv run black .
uml_cmd = python -m pipenv run pyreverse -o png src/*.py src/components/*.py

run:
	python -m pipenv run python src/main.py

edit:
	python -m pipenv run pyxel edit src/resources.pyxres

types:
	$(types_cmd)

format:
	$(format_cmd)

uml:
	$(uml_cmd)


prebuild_cmd = $(types_cmd) && $(format_cmd) && $(uml_cmd)
version_cmd = $(prebuild_cmd) && python -m pipenv run python src/manage.py

build:
	$(version_cmd)

build-major:
	$(version_cmd) --ver major

build-minor:
	$(version_cmd) --ver minor

build-patch:
	$(version_cmd) --ver patch

scene-default:
	python -m pipenv run python src/manage.py generate-scene src/scenes/default_scene.pickle
