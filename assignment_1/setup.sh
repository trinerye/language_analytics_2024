
# Run setup from assignment 2 folder 

## create virtual env
python -m venv A1_env
## activate env
source ./A1_env/bin/activate
## install requirements
pip install --upgrade pip
pip install -r requirements.txt
python -m spacy download en_core_web_md
## deactivate env
deactivate 



