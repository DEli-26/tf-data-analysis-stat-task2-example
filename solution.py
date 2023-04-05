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
    #alpha = 1 - p
    #degree_freedom = len(x)
    #x_expon = 0.5 - x
    #a = chi2.ppf(1 - alpha / 2, 2 * degree_freedom)
    #b = chi2.ppf(alpha / 2, 2 * degree_freedom)
    #return 0.5 - b / (2 * degree_freedom * x_expon.mean()), \
    #       0.5 - a / (2 * degree_freedom * x_expon.mean())
    
    # Определение уровня доверия и расчет соответствующих статистик
    alpha = 1 - p
    loc = x.mean()
    scale = np.sqrt(np.var(x)) / np.sqrt(len(x))

    # Вычисление квантилей нормального распределения
    z_upper = norm.ppf(1 - alpha / 2)
    z_lower = norm.ppf(alpha / 2)

    # Вычисление границ интервала
    lower_bound = loc + z_lower * scale
    upper_bound = loc + z_upper * scale
    
    # Возвращение оптимальной интервальной оценки
    return lower_bound, upper_bound
    
