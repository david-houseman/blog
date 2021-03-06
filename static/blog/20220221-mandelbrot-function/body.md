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


The mapping into RGB color space was achieved with the following code:

    from PIL import Image

    def interpolate(xs, xpts, ypts):
        assert len(xpts) == len(ypts)
        ys = np.zeros_like(xs)
        
        for k in range(1, len(xpts)):
            xl = xpts[k - 1]
            xr = xpts[k]
            assert(xr > xl)
            
            yl = ypts[k - 1]
            yr = ypts[k]
                
            ys = np.where((xs >= xl) & (xs < xr), yl + (yr - yl) * (xs - xl) / (xr - xl), ys)
        return ys
       
    def map_rgb(zs, color_map):
        red = interpolate(zs, color_map[:, 0], color_map[:, 1])
        green = interpolate(zs, color_map[:, 0], color_map[:, 2])
        blue = interpolate(zs, color_map[:, 0], color_map[:, 3])
        return red, green, blue


    color_map = np.array([
        [0.0, 0.0, 0.0, 0.0],
        [2.5, 0.0, 0.0, 0.0],
        [3.0, 0.4, 0.0, 0.0],
        [3.5, 0.1, 0.1, 0.1],
        [4.0, 0.1, 0.4, 0.5],
        [4.5, 0.2, 0.2, 0.2],
        [5.0, 0.2, 0.6, 0.5],
        [5.5, 0.3, 0.3, 0.3],
        [8.0, 1.0, 0.9, 0.7],
    ])
       
    red, green, blue = map_rgb(np.log1p(mandelbrot), color_map)   
    rgb = np.array(Image.new('RGB', mandelbrot.shape))

    RED = 0
    GREEN = 1
    BLUE = 2

    rgb[:, :, RED] = np.uint8(255 * red)
    rgb[:, :, GREEN] = np.uint8(255 * green)
    rgb[:, :, BLUE] = np.uint8(255 * blue)
        
    img = Image.fromarray(rgb)
    img.save('mandelbrot-III.png')

The color map simply interpolates linearly between the provided set of (value, RGB) pairs.

![Color map](/static/blog/20220221-mandelbrot-function/color-map-III.png)