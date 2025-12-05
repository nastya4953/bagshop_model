from dataclasses import dataclass, field
from typing import List, Dict
@dataclass
class ModelParams:
    Q: int                   #замовлень
    avg_check: float         #чек
    p_loc: float             #локальні доставки
    p_int: float             #міжобласні
    return_rate: float       #повернень
    c_loc: float             #вартість локальної доставки
    c_int: float             #вартість міжобласної
    c_ret_loc: float         #вартість повернення локальної доставки
    c_ret_int: float         #вартість повернення міжобласної
    online_share: float      #частка онлайн-оплат
    pay_commission: float    #комісія 
    n_new_customers: int     # кількість нових клієнтів
    cac: float               # CAC, грн
    staff_fixed: float       # фіксовані витрати на персонал
    staff_per_order: float   # витрати на 1 замовлення
def calc_logistics(params: ModelParams) -> float:
  #Логістика
  #доставка виконаних замовлень
    delivery = params.Q * (params.p_loc * params.c_loc +
                           params.p_int * params.c_int)
