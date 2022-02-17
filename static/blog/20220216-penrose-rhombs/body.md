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
        ub = np.concatenate([vc, vx * (1 - 1 / g) + vz / g])
        uc = np.concatenate([va, vy])
    
        ux = np.concatenate([vx * (1 - 1 / g) + vz / g, vz, vc]) 
        uy = np.concatenate([vx * (1 - 1 / g) + vy / g, vx * (1 - 1 / g) + vz / g, va / g + vb * (1 - 1 / g)])
        uz = np.concatenate([vx, vy, vb])
    
        va, vb, vc, vx, vy, vz = ua, ub, uc, ux, uy, uz

    plt.figure(figsize=(10, 10))
    plt.gca().set_aspect('equal')
    plt.axis('off')
    
    for (x, y, z) in zip(vx, vy, vz):
        plt.plot([x.real, y.real, z.real], [x.imag, y.imag, z.imag], color='black')
        
    for (a, b, c) in zip(va, vb, vc):
        plt.fill([a.real, b.real, c.real], [a.imag, b.imag, c.imag], color='black')
         
