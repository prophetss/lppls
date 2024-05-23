import numpy as np
from numba import njit
from lppls.lppls import LPPLS


class LPPLS_R(LPPLS):

    @staticmethod
    @njit
    def lppls(t, tc, m, w, a, b, c1, c2):
        """
        Reversed Log-Periodic Power Law (LPPL) model.

        Parameters:
        t (float or np.ndarray): Time or array of time values.
        tc (float): Critical time at which the market trend changes.
        m (float): Negative exponent to describe the deceleration in price trends.
        a (float): Constant term.
        b (float): Coefficient for the power law term.
        c1 (float): Coefficient for the cosine term.
        c2 (float): Coefficient for the sine term.
        w (float): Frequency of oscillations.

        Returns:
        float or np.ndarray: The reversed LPPL value(s) at time t.
        """
        dt = np.abs(tc - t) + 1e-8
        term1 = np.power(dt, -m)
        term2 = b + ((c1 * np.cos(w * np.log(dt))) + (c2 * np.sin(w * np.log(dt))))
        y_2 = a + term1 * term2
        return y_2
