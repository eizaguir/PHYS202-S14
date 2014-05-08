
import numpy as np

def fourPtCenteredDiff(x,y):
    """ Enter in an x array and a y array, send back
    the derivative using the 4pt-Centered Difference 
    method"""
    dydx = np.zeros(y.shape,float)
    h = x[1]-x[0]
    dydx[2:-2] = (y[:-4] - 8*y[1:-3] + 8*y[3:-1] - y[4:])/(12*h)
    dydx[0] = (y[1]-y[0])/(x[1]-x[0])
    dydx[1] = (y[2]-y[1])/(x[2]-x[1])
    dydx[-1] = (y[-1] - y[-2])/(x[-1] - x[-2])
    dydx[-2] = (y[-2] - y[-3])/(x[-2] - x[-3])
    
    return dydx

def twoPtForwardDiff(x,y):
    """Takes in an array of x values and an array of y values, and returns
    the 2pt-forward derivatives of those values."""
    
    dydx = np.zeros(y.shape,float)
    dydx[0:-1] = np.diff(y)/np.diff(x)
    dydx[-1] = (y[-1] - y[-2])/(x[-1] - x[-2])
    
    return dydx
        
def twoPtCenteredDiff(x,y):
    """Takes in an array of x values and an array of y values, and returns
    the 2pt-center derivatives of those values."""
    
    dydx = np.zeros(y.shape,float)
    dydx[1:-1] = (y[2:] - y[:-2])/(x[2:] - x[:-2])
    dydx[0] = (y[1]-y[0])/(x[1]-x[0])
    dydx[-1] = (y[-1] - y[-2])/(x[-1] - x[-2])
    
    return dydx