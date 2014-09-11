setuptools:
	wget https://bootstrap.pypa.io/ez_setup.py -O - | python && rm setuptools*.zip
	easy_install pip

requirements: requirements.txt
	pip install -r requirements
