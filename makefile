setuptools:
	wget https://bootstrap.pypa.io/ez_setup.py -O - | python && rm setuptools*.zip
	easy_install pip

requirements: requirements.txt
	pip install -r requirements

author-config:
	git config user.email imyikong@gmail.com --local
	git config user.name MrLYC --local
