Consider the sawtooth function given by:

$$
f(x) = \begin{cases}
x & \text{if} & 0 \leq x \leq \pi \\
x-2\pi & \text{if} & \pi \leq x \leq 2\pi
\end{cases}
$$

The function is $2\pi$ periodic, so $L = 2\pi$. It satisfies all the Dirichlet conditions. This is an odd function, so we need to find $b_{r}$:

$$
b_{r}=\frac{1}{\pi} \int_{0}^{2\pi} f(t)\sin\left( r t \right) \, dt
$$
We will need to evaluate this integral in two parts due to the piecewise definition:

$$
b_{r} = \left[\frac{1}{\pi} \int_{0}^{\pi} x\sin(rx) \, dx   \right] + \left[ \frac{1}{\pi} \int_{\pi}^{2\pi} (x-2\pi)\sin(rx) \, dx  \right]
$$

$$
= \frac{1}{\pi} \left[ \int_{0}^{\pi} x\sin(rx) \, dx -2\pi \int_{\pi}^{2\pi} \sin(rx) \, dx  \right] 
$$
$$
= 2 \frac{(-1)^{r+1}}{r}.
$$
Putting this into our Fourier series we find:

$$f(x) = \sum_{r=0}^{\infty} 2 \frac{(-1)^{r+1}}{r} \sin(rx)$$
