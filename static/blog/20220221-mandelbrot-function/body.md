![Mandelbrot time-to-escape function](/static/blog/20220221-mandelbrot-function/mandelbrot-III.png)

The following code computes the Mandelbrot time-to-escape function:

    import cmath
    import numpy as np

    x, y = -0.535, -0.615
    halfwidth = 0.03

    xmin, xmax = x - halfwidth, x + halfwidth
    ymin, ymax = y - halfwidth, y + halfwidth
    resolution = 720

    max_iter = 2048

    xs = np.linspace(xmin, xmax, resolution, endpoint=False)
    ys = np.linspace(ymin, ymax, resolution, endpoint=False)

    ordinates = np.add.outer(ys * 1j, xs)
    states = np.zeros_like(ordinates, dtype=complex)
    mandelbrot = np.zeros_like(ordinates, dtype=int)

    for k in range(max_iter):
        states = np.where(mandelbrot == 0, states * states + ordinates, 0.0)
        mandelbrot = np.where(abs(states) > 2.0, k + 1, mandelbrot)
        print('Completed: {}/{}'.format(k, max_iter), end='\r')

