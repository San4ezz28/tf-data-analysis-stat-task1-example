import pandas as pd
import numpy as np
import math
from scipy.stats import norm


chat_id = 5960781343                    # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    mu, sigma = norm.fit(x)
    a = 2/(np.exp(2)-1)
    a_cf = a*mu/10
    return a_cf
