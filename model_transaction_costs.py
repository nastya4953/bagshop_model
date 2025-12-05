from dataclasses import dataclass, field
from typing import List, Dict
#Вихідні дані та функції
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
    n_new_customers: int     #кількість нових клієнтів
    cac: float               #CAC, грн
    staff_fixed: float       #фіксовані витрати на персонал
    staff_per_order: float   #витрати на 1 замовлення

def calc_logistics(params: ModelParams) -> float:
  #Логістика
  #доставка виконаних замовлень
    delivery = params.Q * (params.p_loc * params.c_loc +
                           params.p_int * params.c_int)
    #повернення
    avg_ret_cost = params.p_loc * params.c_ret_loc + params.p_int * params.c_ret_int
    returns = params.Q * params.return_rate * avg_ret_cost
    return delivery + returns
    
def calc_payments(params: ModelParams) -> float:
    #комісія
    q_online = params.Q * params.online_share
    return q_online * params.avg_check * params.pay_commission

def calc_marketing(params: ModelParams) -> float:
    #маркетинг
    return params.n_new_customers * params.cac

def calc_staff(params: ModelParams) -> float:
    #витрати персоналу
    return params.staff_fixed + params.staff_per_order * params.Q

def calc_total(params: ModelParams) -> Dict[str, float]:
    #підрахунок
    logistics = calc_logistics(params)
    payments = calc_payments(params)
    marketing = calc_marketing(params)
    staff = calc_staff(params)
    total = logistics + payments + marketing + staff

    return {
        "logistics": logistics,
        "payments": payments,
        "marketing": marketing,
        "staff": staff,
        "extra_cost": extra["extra_cost"],
        "extra_revenue": extra["extra_revenue"],
        "extra_net": extra["extra_net"],
        "total": total,
    }
    

  
