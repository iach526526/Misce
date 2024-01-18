import random as rad
def P2():
    rad.seed(48763)
    top=141592653
    table=[rad.randint(1,top)for _ in range(300000)]
    return table
# T=P2()
# print(T[214269])