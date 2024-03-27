
# activate env
source ./A2_env/bin/activate
# run the code
python src/logistic_regression.py -i in/fake_or_real_news.csv &
python src/neural_network.py -i in/fake_or_real_news.csv 
# close the enviroments
deactivate