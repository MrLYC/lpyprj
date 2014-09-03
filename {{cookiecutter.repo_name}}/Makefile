PYTHONREPO = {{ cookiecutter.repo_name }}
PYTHONPATH = .
VENV = .env/
TEMPTOOLS = .temptools/
PYTEST = env PYTHONPATH=$(PYTHONPATH) PYTEST=1 $(VENV)bin/py.test
PYLINT = env PYTHONPATH=$(PYTHONPATH) $(VENV)bin/pylint --disable=I0011 --msg-template="{path}:{line}: [{msg_id}({symbol}), {obj}] {msg}"
PEP8 = env PYTHONPATH=$(PYTHONPATH) $(VENV)bin/pep8 --repeat --ignore=E202,E501
PYTHON = env PYTHONPATH=$(PYTHONPATH) $(VENV)bin/python
PIP = $(VENV)bin/pip install -q -i http://pypi.douban.com/simple/
BOOTSTRAP = $(TEMPTOOLS)bootstrap
ENVTYPE = REAL

run: check-env
	$(PYTHON) {{ cookiecutter.repo_name }}/main.py --env=`$(BOOTSTRAP)`

init-dev:
	$(BOOTSTRAP) init_dev "$(VENV)"
	$(BOOTSTRAP) requirements "$(PIP)"
	git init || true

init:
	$(BOOTSTRAP) requirements pip

clean:
	find . -name "__pycache__" -type d -exec rm -rf {} \; || true
	find . -name "*.pyc" -type f -exec rm -rf {} \; || true

full-clean:
	rm -rf local/ lib/ bin/ include/ build/ dist/ wheelhouse/ webshell.egg-info/ distribute-*.tar.gz
	find . -name "__pycache__" -type d -exec rm -rf {} \; || true
	find . -name "*.pyc" -type f -exec rm -rf {} \; || true

check:
	$(PEP8) "$(PYTHONREPO)"
	$(PYLINT) -E "$(PYTHONREPO)"

test: check
	$(PYTEST) "$(PYTHONREPO)"
