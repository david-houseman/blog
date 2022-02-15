![Penrose P3 tiling](static/blog/20220216-penrose-rhombs/penrose-I.png)

The following code is used to generate the Penrose P3 tiling by repeated subdivision.

    import math
    import cmath
    import numpy as np
    import matplotlib.pyplot as plt

    ## Golden ratio
    g = (1 + math.sqrt(5)) / 2

    va = np.exp(np.array([(k + 1) // 2 * 2 for k in range(10)]) * 1j * math.pi / 5)
    vb = np.array([complex(0, 0) for k in range(10)])
    vc = np.exp(np.array([1 + (k // 2 * 2) for k in range(10)]) * 1j * math.pi / 5)
    
    vx = np.array([])
    vy = np.array([])
    vz = np.array([])
        
    for k in range(5):
        ua = np.concatenate([va / g + vb * (1 - 1 / g), vx * (1 - 1 / g) + vy / g]) 
        ub = np.concatenate([vc, vx / (1 + g) + vz * g / (1 + g)])
        uc = np.concatenate([va, vy])
    
        ux = np.concatenate([vx / (1 + g) + vz * g / (1 + g), vz, vc]) 
        uy = np.concatenate([vx * (1 - 1 / g) + vy / g, vx / (1 + g) + vz * g / (1 + g), va / g + vb * (1 - 1 / g)])
        uz = np.concatenate([vx, vy, vb])
    
        va, vb, vc, vx, vy, vz = ua, ub, uc, ux, uy, uz

