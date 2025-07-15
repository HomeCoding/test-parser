# Makefile for the Biedronka offer parser

.PHONY: all setup run clean

# Name of the virtual environment directory
VENV_DIR = venv

# Python interpreter from the virtual environment
PYTHON = $(VENV_DIR)/bin/python

all: run

# Create the virtual environment and install dependencies
setup: $(VENV_DIR)/bin/activate

$(VENV_DIR)/bin/activate: requirements.txt
	python3 -m venv $(VENV_DIR)
	$(PYTHON) -m pip install --upgrade pip
	$(PYTHON) -m pip install -r requirements.txt
	touch $(VENV_DIR)/bin/activate

# Run the Python script
run: setup
	$(PYTHON) main.py

# Remove the virtual environment and generated files
clean:
	rm -rf $(VENV_DIR)
	rm -f offers.json
