types_cmd = python -m pipenv run mypy --strict --implicit-reexport src
format_cmd = python -m pipenv run black .
uml_cmd = python -m pipenv run pyreverse -o png src/*.py src/components/*.py

run:
	python -m pipenv run python src/main.py

run-make-scene:
	python -m pipenv run python src/main.py --build

edit:
	python -m pipenv run pyxel edit src/resources.pyxres

types:
	$(types_cmd)

format:
	$(format_cmd)

uml:
	$(uml_cmd)


prebuild_cmd = $(types_cmd) && $(format_cmd) && $(uml_cmd)
version_cmd = $(prebuild_cmd) && python -m pipenv run python src/manage.py build

build:
	$(version_cmd)

build-major:
	$(version_cmd) --ver major

build-minor:
	$(version_cmd) --ver minor

build-patch:
	$(version_cmd) --ver patch

scene-defaults:
	python -m pipenv run python src/manage.py generate-scene src/scenes/default_scene.pickle
	python -m pipenv run python src/manage.py generate-scene-builder src/scenes/create_scene.pickle

scene-builder:
	python -m pipenv run python src/main.py --build
