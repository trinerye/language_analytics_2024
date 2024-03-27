import os
import gensim
import gensim.downloader as api
import matplotlib.pyplot as plt
from sklearn.decomposition import TruncatedSVD
from sklearn.decomposition import PCA

model = api.load("glove-wiki-gigaword-50")