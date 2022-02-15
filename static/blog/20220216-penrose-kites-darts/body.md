![Penrose P2 tiling](static/blog/20220216-penrose-kites-darts/penrose-II.png)

The following code is used to generate the Penrose P2 tiling by repeated subdivision.

    import math
    import cmath
    import numpy as np
    import matplotlib.pyplot as plt

    g = (1 + math.sqrt(5)) / 2

    va = np.array([complex(0, 0) for k in range(10)])
    vb = np.exp(np.array([(k + 1) // 2 * 2 for k in range(10)]) * 1j * math.pi / 5)
    vc = np.exp(np.array([1 + (k // 2 * 2) for k in range(10)]) * 1j * math.pi / 5)
    
    vx = np.array([])
    vy = np.array([])
    vz = np.array([])
        
    for k in range(4):
        ua = np.concatenate([vb, vb, vz]) 
        ub = np.concatenate([vc, va / g + vb * (1 - 1 / g), vy / g + vz * (1 - 1 / g)])
        uc = np.concatenate([va * (1 - 1 / g) + vc / g, va * (1 - 1 / g) + vc / g, vx])
    
        ux = np.concatenate([vy / g + vz * (1 - 1 / g), va / g + vb * (1 - 1 / g)])
        uy = np.concatenate([vx, va * (1 - 1 / g) + vc / g])
        uz = np.concatenate([vy, va])
    
        va, vb, vc, vx, vy, vz = ua, ub, uc, ux, uy, uz


    plt.figure(figsize=(10, 10))
    plt.gca().set_aspect('equal')
    plt.axis('off')
    
    for (x, y, z) in zip(vx, vy, vz):
        plt.fill([x.real, y.real, z.real], [x.imag, y.imag, z.imag], color='black')
        
    for (a, b, c) in zip(va, vb, vc):
        plt.plot([a.real, b.real, c.real], [a.imag, b.imag, c.imag], color='black')
         