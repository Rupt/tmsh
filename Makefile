.SUFFIXES:  # disables implicit rules; see https://www.gnu.org/software/make/manual/html_node/Suffix-Rules.html

.venv/.tombstone:
	python3.12 -m venv .venv
	.venv/bin/pip install --upgrade 'pip >=25.0.1'
	.venv/bin/pip install --upgrade --editable .
	.venv/bin/pip install --upgrade --requirement requirements.txt
	touch $@

# TODO: generate coverage on the actual source file
.PHONY: test
test: .venv/.tombstone
	.venv/bin/coverage run -m unittest discover tests
	.venv/bin/coverage xml
	sed -i 's \.venv/lib/python3\.12/site-packages/ src/ g' coverage.xml

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
		'coverage >=7.8.0' \
		'mypy >=1.15.0' \
		'pyright >=1.1.400' \
		'ruff >=0.11.7' \
		'setuptools >=79.0.0' \
		'twine >=6.1.0'
	.venv/bin/pip freeze | grep -v tmsh > requirements.txt

.PHONY: publish
publish: .venv/.tombstone
	.venv/bin/python -m build --no-isolation
	.venv/bin/python -m twine upload --repository pypi dist/*
