from sklearn.cluster import KMeans
from abc import ABC, abstractmethod ##helper class in python, Abstract Base Class
from typing import Union
import numpy as np

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