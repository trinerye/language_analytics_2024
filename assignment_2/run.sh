# Activate the environment (Unix/macOS)
source ./LA_A2_env/bin/activate
# Run the code
python src/logistic_regression.py -i in/fake_or_real_news.csv &
python src/neural_network.py -i in/fake_or_real_news.csv 
# Deactivate the enviroment
deactivate