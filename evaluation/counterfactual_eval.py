import numpy as np

def ips(rewards, pi, b):
    w = pi / np.clip(b, 1e-6, None)
    return np.mean(w * rewards)

def snips(rewards, pi, b):
    w = pi / np.clip(b, 1e-6, None)
    return np.sum(w * rewards) / np.sum(w)

def dr(rewards, pi, b, q):
    # q: reward model predictions
    w = pi / np.clip(b, 1e-6, None)
    return np.mean(q + w * (rewards - q))

if __name__ == "__main__":
    rng = np.random.default_rng(0)
    n = 1000
    rewards = rng.integers(0, 2, size=n)  # clicks
    b = rng.uniform(0.1, 1.0, size=n)     # behavior policy
    pi = rng.uniform(0.1, 1.0, size=n)    # target policy
    q = rng.uniform(0.0, 1.0, size=n)     # reward model preds
    print("IPS:", ips(rewards, pi, b))
    print("SNIPS:", snips(rewards, pi, b))
    print("DR:", dr(rewards, pi, b, q))
