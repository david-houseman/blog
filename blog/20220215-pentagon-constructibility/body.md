title: Constructibility of the pentagon
author: David Houseman
date: 2022-02-15

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
\cos \frac{2 \pi}{5} = a = \frac{-1 + \sqrt{5}}{4}
$$
which is constructible since $\sqrt{5}$ is the hypotenuse of a right
triangle with sides of length 1 and 2. Thus the first vertex of the
regular pentagon may be constructed, and the remaining vertices
follow trivially.

We remark that this result is related to the _golden ratio_
$$
\phi = (1 + \sqrt{5}) / 2 = 1.618033 \ldots,
$$
the positive root of the quadratic equation $z^2 - z - 1 = 0$.
We can write
$$
\cos \frac{2 \pi}{5} = \frac{1}{2 \phi}
$$
and, by the half-angle formula,
$$
\cos \frac{\pi}{5} = \frac{1}{2} + \frac{1}{2 \phi}.
$$
These two results are central to the construction of the Penrose tilings.


