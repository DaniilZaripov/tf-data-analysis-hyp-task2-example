import pandas as pd
import numpy as np
from scipy.stats import anderson_ksamp

chat_id = 931254925 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    p_value = anderson_ksamp([x, y]).pvalue 
    alpha = 0.07
    return p_value < alpha 
