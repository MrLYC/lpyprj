# lpyprj
The project template created by LYC

## Quick  start
### 1. clone project.
From github:
`$ git clone https://github.com/MrLYC/lpyprj.git`
Or from git@osc:
`$ git clone https://git.oschina.net/Mr_LYC/lpyprj.git`

### 2. cd to project and install requirements.
Change directory to project:
`$ cd lpyprj`
Install requirements as sudo:
`$ sudo make requirements`
Install requirements requires pip, if you didn't installed it yet, please use this command as sudo to install setuptools:
`$ sudo make setuptools`

### 3. create your new project.
Use cookiecutter to create your new project:
`$ cookiecutter $path_of_lpyprj`
Replace the var $path_of_lpyprj to the real path of the project lpyprj is.
And then, input the infomations according to the hints to finish this step.

### 4. initalize your project.
First, change the directory to your project.
Then, initalize git:
`$ git init`
Make virtual environment to develop:
`$ make dev-init`

### 5. switch to the virtualenv of this project and start developing
Switch your Python environment and anchor here:
`$ source .dev/toggle`
If your want to switch your environment back, call it again.
