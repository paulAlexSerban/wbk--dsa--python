setup_venv:
	@echo "Setting up virtual environment..."
	@python3 -m venv .venv

activate_venv:
	@echo "Activating virtual environment..."
	@source .venv/bin/activate

install_deps:
	@echo "Installing dependencies..."
	@pip install -r requirements.txt
	@echo "Dependencies installed."

freeze_deps:
	@echo "Freezing dependencies..."
	@pip freeze > requirements.txt
	@echo "Dependencies frozen."

install_jupiter_n_ipykernel:
	@echo "Installing Jupyter Notebook..."
	@pip install jupyter
	@pip install ipykernel
	@echo "Jupyter Notebook installed."

install_venv_as_kernel:
	@echo "Installing virtual environment as Jupyter kernel..."
	@python -m ipykernel install --user --name=.venv --display-name "Python (.venv)"
	@echo "Virtual environment installed as Jupyter kernel."

start_jupyter:
	@echo "Starting Jupyter Notebook..."
	@jupyter notebook

lint:
	@echo "Linting..."
	@pylint . --rcfile=.pylintrc -r y
	@echo "Linting done."