from scipy import sparse as sp

class GMRF(object):
    """
    Description: Gaussian Markov Random Field
    
    Attributes:
    
    Methods: 
    
    """
    def __init__(self, m, Q):
        """
        Constructor
        
        Inputs: 
            
            m: double, (n,1) mean vector
            
            Q: double, (n,n) sparse symmetric positive definite precision matrix
        
            
        Attributes:
            
        
        Methods:
        """
        pass
    
    
    def sample_covariance(self):
        """
        Sample from an unconditional Gaussian random field based on the covariance matrix
        """ 
        pass
    
    
    def sample_precision(self):
        """
        Sample from a GMRF using the precision matrix 
        """
        pass
    
    
    def sample_canonical(self):
        """
        Sample from a GMRF using the canonical parameterization
        """
        pass
    
    
    
    