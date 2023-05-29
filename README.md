# SIN Validator
This intent of this repo is to provide a quick script to validate SIN (Social Insurance Number) numbers. 

## How to use
### Requirements
- [python >= 3.8](https://www.python.org/downloads/)

Optional:
- [pyenv](https://github.com/pyenv/pyenv)


### Instaling requirements
To run the script locally you'll need to:
1. create a virtual environment to isolate the project.  
2. install the dependencies.  

```shell
$ python -m virtualenv venv
$ source .venv/bin/activate
$ make dependencies 
```

### Running the script
To get the help on how to properly use the script you can use `--help`
```shell
$ usage: main.py [-h] sin_number

Validate if a SIN number is valid or not.

positional arguments:
  sin_number  the SIN number to validate or a comma separated list of SIN numbers to validate. i.e. '123456789' or '123456789, 000000000'

options:
  -h, --help  show this help message and exit.
```
example:
```shell
$ python main.py "000 000    000, 046454286, 046 4 542 96"
000000000 is a Invalid SIN number :)
046454296 is a Invalid SIN number :)
046454286 is a Valid SIN number :)
```


### Testing
To execute tests you'll need to install the `dev-dependencies` then you can use the `make test-coverage` when inside the local virtual environment.
```shell
$ source .venv/bin/activate  # if not in the venv already
$ make dev-dependencies 
$ make test-coverage
```

### Commands
To get a general help on how to execute this you can use `make` in the root folder to get the `--help` information from the Makefile.
```shell
$ make
Help documentation for this project

Usage:
  make [command] 

Commands:
ci-dependencies      Install dependencies using pip
clean                Clean bloat files from project
clean-build          Clean build files
clean-eggs           Remove egg files
dependencies         Install dependencies
dev-dependencies     Install dev and main dependencies
format-code          Format code
help                 Display this help
lint                 Check code lint
outdated             Show outdated packages
set-path             Set Python Path
test                 Run tests
test-coverage        Run tests with coverage output
test-coverage-unit   Run unit tests with coverage output
test-debug           Run tests with active pdb
test-unit            Run unit tests
```


## Thoughts and Approach
### - SinValidator Class
To keep things organized and possibly easily reallocated or imported in other parts of a project, I've decided to keep the validation methods inside a stateless class. This way we can easily understand each method purpose and extend it's usage if necessary.


### - SinValidator.validate method
The idea here was:
- easily extendable
- fail fast

I've designed it in a way that if a function fails it will fail fast and not go through other validation functions unecessarily. Also, if by any chance we need more validation methods we can include then in the tuple in the order we want to go throught without needing to change how the function works. i.e. _guarantee_only_digits

### Overall
This is a simple test, we can go on and on trying to make it special but we might be considering time to deliver so I tried to approach it in the simplest way possible but safely with tests that guarantee the edge cases that might happen.