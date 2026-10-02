import numpy as np
def match_score(a, b):
    a = a.flatten() - a.mean()
    b = b.flatten() - b.mean()
    d = np.sqrt((a**2).sum() * (b**2).sum())
    return 0.0 if d == 0 else float((a*b).sum()/d)
