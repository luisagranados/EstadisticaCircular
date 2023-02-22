import numpy as np
from astropy.stats import circmean
from astropy import units as u
data = np.array([51, 67, 40, 109, 31, 358])*u.deg
circmean(data) 