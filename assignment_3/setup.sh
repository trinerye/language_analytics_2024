
# Run setup from assignment 3 folder 

## create virtual env
python -m venv A3_env
## activate env
source ./A3_env/bin/activate
## install requirements
pip install --upgrade pip
pip install -r requirements.txt
python -m spacy download en_core_web_md
## deactivate env
deactivate 



