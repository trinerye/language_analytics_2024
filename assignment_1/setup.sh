
# Run setup from assignment_1 folder 

## Create virtual environment
python -m venv LA_A1_env
## Activate the environment
source ./LA_A1_env/bin/activate
## Install requirements
pip install --upgrade pip
pip install -r requirements.txt
python -m spacy download en_core_web_md
## Deactivate the environment
deactivate 


