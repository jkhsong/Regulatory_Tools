from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from abc import ABC, abstractmethod ##helper class in python, Abstract Base Class
from typing import Union
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class cluster(ABC):
    def __init__(self, arraydata: list = None, k: int = None) -> None:
        self.arraydata = arraydata
        self.k = k
    
    @abstractmethod
    def classify(self, arraydata: list = None, k: int = None):
        pass

class kmeans(cluster):
    def __init__(self, arraydata: list = None, k: int = None) -> None:
        super().__init__(arraydata, k)
    
    def classify(self):
        arraydata = np.array(self.arraydata)
        k = self.k
        km = KMeans(n_clusters=k, init='k-means++',
                    n_init=10, max_iter=300, 
                    tol=1e-5, random_state=0)
        
        kmr = km.fit_predict(arraydata)
        kmi = km.inertia_
        return kmr, kmi

def cluster_PCA():
    df = pd.read_excel("X:\Dropbox\GitHub\Skeleton_DB\datafiles\\area_clusters.xlsx")
    # print(df)
    X = df.values
    X = [row[2:] for row in X]
    colname = list(df.columns)[2:]
    # print(X)
    scaler = StandardScaler()
    scaler.fit(X)
    X_scaled = scaler.transform(X)
    # print(X_scaled)


    pca7 = PCA(n_components=None, random_state=13)


    pca7.fit(X_scaled)
    X_pca7 = pca7.transform(X_scaled)
    # print(X_pca7)
    print(pca7.explained_variance_ratio_ * 100)
    print(sum(pca7.explained_variance_ratio_))
    print(np.cumsum(pca7.explained_variance_ratio_ * 100))
    cvalues = [x for x in np.cumsum(pca7.explained_variance_ratio_ * 100)]
    cnums = [x for x in range(1,len(cvalues))]
    ctable = zip(cnums, cvalues)
    cdf = pd.DataFrame(ctable, columns=["# of components", "Explained Variance %"])
    print(cdf.to_markdown(index=False))
    print(pca7.components_)

    _ = sns.heatmap(pca7.components_**2,
                 yticklabels=["PC"+str(x) for x in range(1,pca7.n_components_+1)],
                 xticklabels=list(colname),
                 annot=True,
                 fmt='.2f',
                 square=True,
                 linewidths=0.05,
                 cbar_kws={"orientation": "horizontal"})
    plt.yticks(rotation=0)
    plt.show()


cluster_PCA()
