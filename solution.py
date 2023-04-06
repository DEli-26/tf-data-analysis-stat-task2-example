import pandas as pd
import numpy as np

from scipy.stats import norm
from scipy.stats import chi2
from scipy.stats import expon


chat_id = 723988166 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    
    t = 89
    alpha = 1 - p
    minimum = (-x).min()
    z_2 = -np.log(1 - p) / len(x)    
    
    return 2 * (-minimum - 1 / 2) / t ** 2, \
           2 * (z_2 - minimum - 1 / 2) / t ** 2
