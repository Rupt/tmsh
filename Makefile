.SUFFIXES:  # disables implicit rules; see https://www.gnu.org/software/make/manual/html_node/Suffix-Rules.html

.venv/.tombstone:
	python3.13 -m venv .venv
	.venv/bin/pip install --upgrade pip -r requirements.txt
	touch $@

.PHONY: test
test: .venv/.tombstone
	.venv/bin/python -m unittest discover tests

.PHONY: lint
lint: .venv/.tombstone
	-.venv/bin/ruff check --fix
	-.venv/bin/ruff format
	-.venv/bin/pyright
	-.venv/bin/mypy

# TODO: use the dev group once pip (25.1) releases support
# 	e.g. `.venv/bin/pip install --upgrade --group dev`
.PHONY: upgrade
upgrade: .venv/.tombstone
	.venv/bin/pip install --upgrade . \
		'build >=1.2.2.post1' \
		'mypy >=1.15.0' \
		'pyright >=1.1.399' \
		'ruff >=0.11.6' \
		'setuptools >=79.0.0'
	.venv/bin/pip freeze | grep -v tmsh > requirements.txt
