import pandas as pd
import numpy as np
from scipy.stats import ttest_1samp


chat_id = 252623629

def solution(data: pd.Series) -> bool:
alpha = 0.1
sample_mean = data.mean()
n = len(data)
sample_std = data.std(ddof=1)
se = sample_std / np.sqrt(n)
t_stat = (sample_mean - 300) / se
p_value = ttest_1samp(data, 300)[1] / 2
return p_value < alpha and t_stat < 0
