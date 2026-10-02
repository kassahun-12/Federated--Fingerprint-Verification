import numpy as np
def client_bootstrap_rd(rd, n_boot=5000, alpha=0.05, seed=20261007):
    rng = np.random.default_rng(seed)
    K = len(rd)
    boot = np.array([rng.choice(rd, K, replace=True).mean() for _ in range(n_boot)])
    lo, hi = np.percentile(boot, [100*alpha/2, 100*(1-alpha/2)])
    return boot, lo, hi
