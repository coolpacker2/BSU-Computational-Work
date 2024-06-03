import sklearn
from sklearn.cluster import k_means
from sklearn.metrics import silhouette_score
silhouette_score(X, k_means.labels_)