DEVPATH ?= $(PWD)
VIRTUALENV ?= $(DEVPATH)/.env
VENVPATH := $(VIRTUALENV)/bin

# virtual env
ifeq ($(VIRTUAL_ENV),)
PYTHON := $(PYENV) $(VENVPATH)/python
PEP8 := $(PYENV) $(VENVPATH)/pep8 --repeat --ignore=E202,E501
PYLINT := $(PYENV) $(VENVPATH)/pylint --disable=I0011 --msg-template="{path}:{line}: [{msg_id}({symbol}), {obj}] {msg}"
PYTEST := $(PYENV) $(VENVPATH)/py.test
PIPINSTALL := $(PYENV) $(VENVPATH)/pip install -i http://pypi.douban.com/simple/
VIRTUAL_ENV := $(VIRTUALENV)
endif

.PHONY: dev-mk dev-venv

dev-venv: dev-mk
	[ -e "$(VIRTUAL_ENV)" ] || virtualenv "$(VIRTUALENV)"
	ln -s "$(VENVPATH)/activate" "$(DEVPATH)/activate"

dev-requirements: dev-venv
	$(PIPINSTALL) -r "$(DEVPATH)/requirements.txt"
