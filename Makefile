.SUFFIXES:  # disables implicit rules; see https://www.gnu.org/software/make/manual/html_node/Suffix-Rules.html

.venv/.tombstone:
	python3.13 -m venv .venv
	.venv/bin/pip install --upgrade pip -r dev-requirements.txt
	touch $@

.PHONY: test
test: .venv/.tombstone
	.venv/bin/python -m unittest discover tests

.PHONY: lint
lint: .venv/.tombstone
	-.venv/bin/python -m ruff check
	-.venv/bin/python -m pyright src tests
	-.venv/bin/python -m mypy src tests
