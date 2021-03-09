from abc import ABC, abstractmethod

class KernelDensityGraph(ABC):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def fit(self, X=None, y=None):
        """
        Fits the transformer.

        Parameters
        ----------
        X : ndarray
            Input data matrix.
        y : ndarray
            Output (i.e. response) data matrix.
        """
        pass
    
    @abstractmethod
    def predict_proba(self, X):
        """
        Calculate posteriors using the kernel density graph.

        Parameters
        ----------
        X : ndarray
            Input data matrix.
        """
        pass

    @abstractmethod
    def predict(self, X):
        """
        Perform inference using the kernel density graph.

        Parameters
        ----------
        X : ndarray
            Input data matrix.
        """
        pass