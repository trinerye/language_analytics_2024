
# Run setup from assignment_3 folder 

## Create virtual environment
python -m venv LA_A3_3_env
## Activate the environment
source ./LA_A3_3_env/bin/activate
## Install requirements
sudo apt-get update
sudo apt-get install python3-dev
sudo apt-get install libopenblas-dev
pip install --upgrade pip
pip install -r requirements.txt
python -m spacy download en_core_web_md
## Deactivate the environment
deactivate 



