![Pentagon inscribed in unit circle.](static/blog/20220215-pentagon-constructibility/pentagon.png)

A regular pentagon is inscribed in the unit circle with vertices at
the roots of the polynomial $z^5 - 1 = 0$. This may be factorised as
$$
(z - 1)(z^4 + z^3 + z^2 + z + 1) = 0
$$
We write $z = \exp(2 \pi i / 5) = a + ib$ with $a, b > 0$ and
$a^2 + b^2 = 1$. Then
$$
z^2 = a^2 - b^2 + 2iab .
$$
By symmetry,
$$
\begin{aligned}
z^3 &= (z^2)^* = a^2 - b^2 - 2iab \\
z^4 &= z^* = a - ib
\end{aligned}
$$
Therefore
$$
\begin{aligned}
0 &= z^4 + z^3 + z^2 + z + 1 \\
&= 2a^2 - 2b^2 + 2a + 1 \\
&= 4a^2 + 2a - 1
\end{aligned}
$$
By the quadratic formula we have
$$
a = \frac{-1 + \sqrt{5}}{4}.
$$
Therefore
$$
\cos \frac{2 \pi}{5} = \frac{-1 + \sqrt{5}}{4},
$$
which is constructible since $\sqrt{5}$ is the hypotenuse of a right
triangle with sides of length 1 and 2. Thus the first vertex of the
regular pentagon may be constructed.

We remark that this result is related to the _golden ratio_
$$
\phi = (1 + \sqrt{5}) / 2 = 1.618033 \ldots,
$$
the positive root of the quadratic equation $z^2 - z - 1 = 0$. We can write
$$
\cos \frac{2 \pi}{5} = \frac{1}{2 \phi}.
$$

The second vertex, $z^2$, may be constructed similarly as 
$$
\begin{aligned}
\cos \frac{\pi}{5} &= -\Re(z^2) \\
&= -(a^2 - b^2) \\
&= 1 - 2a^2 \\
&= \frac{1 + \sqrt{5}}{4} \\
&= \frac{1}{2} + \frac{1}{2 \phi}.
\end{aligned}
$$
The third and fourth vertices are, as noted previously, reflections of the first and 
second vertices. This completes the construction of the regular pentagon.

The relationship to the golden ratio is central to the construction of the Penrose tilings.


