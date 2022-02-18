![Penrose P2 tiling](/static/blog/20220216-penrose-kites-and-darts/penrose-II.png)

The following code is used to generate the Penrose P2 tiling by repeated subdivision.

    import math
    import cmath
    import numpy as np
    import matplotlib.pyplot as plt

    g = (1 + math.sqrt(5)) / 2

    pa = np.array([complex(0, 0) for k in range(10)])
    pb = np.exp(np.array([(k + 1) // 2 * 2 for k in range(10)]) * 1j * math.pi / 5)
    pc = np.exp(np.array([1 + (k // 2 * 2) for k in range(10)]) * 1j * math.pi / 5)
    
    px = np.array([])
    py = np.array([])
    pz = np.array([])
        
    for k in range(4):
    	pd = pa / g + pb * (1 - 1 / g)
        pe = pc / g + pa * (1 - 1 / g)
        pu = py / g + pz * (1 - 1 / g)

        ta = np.concatenate([pb, pb, pz]) 
        tb = np.concatenate([pc, pd, pu])
        tc = np.concatenate([pe, pe, px])
    
        tx = np.concatenate([pu, pd])
        ty = np.concatenate([px, pe])
        tz = np.concatenate([py, pa])
    
        pa, pb, pc, px, py, pz = ta, tb, tc, tx, ty, tz


    plt.figure(figsize=(10, 10))
    plt.gca().set_aspect('equal')
    plt.axis('off')
    
    for (x, y, z) in zip(px, py, pz):
        plt.fill([x.real, y.real, z.real], [x.imag, y.imag, z.imag], color='black')
        
    for (a, b, c) in zip(pa, pb, pc):
        plt.plot([a.real, b.real, c.real], [a.imag, b.imag, c.imag], color='black')
         
