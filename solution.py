import pandas as pd
import numpy as np
import math



chat_id = 5960781343                    # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
   # Рассчитаем среднее значение и дисперсию измерений скорости
   x_1 = np.array(x)
   mean_speed = x_1.mean()
   disper = x_1.var()
       # Рассчитаем точечную оценку коэффициента ускорения
   norm_raspred =  1/(disper*(2*math.pi)**0.5) * math.exp(-((-1-math.exp(1) - mean_speed)**2)/2*disper**2) # Формула из постановки задачи
   a = norm_raspred/10
   return a,disper # Ваш ответ

x = [10, 15 , 17 , 20 ,12 ,14 ]
print(solution(x))
