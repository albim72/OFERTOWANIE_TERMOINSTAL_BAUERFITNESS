import math

def grubosc_izolacji(D_mm, Tm, To, lamb, q):
    r1 = (D_mm/1000.0)/2.0
    ln_ratio = (2*math.pi*lamb*(Tm-To))/q
    r2 = r1 * math.exp(ln_ratio)
    g = r2 - r1
    return g*1000.0  # w mm


