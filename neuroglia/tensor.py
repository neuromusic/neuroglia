import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin

class ResponseExtractor(BaseEstimator,TransformerMixin):
    """docstring for Annotator."""
    def __init__(self, method='mean', dim='time'):
        super(ResponseExtractor, self).__init__()

        if method == 'mean':
            self.method = np.mean
        elif method == 'max':
            self.method = np.max
        else:
            self.method = method
        self.dim = dim

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        return X.mean(dim=self.dim).data
