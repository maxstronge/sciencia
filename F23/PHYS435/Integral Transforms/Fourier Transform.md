

Important results:

## Fourier's Inversion Theorem:

$$

f(t)=\frac{1}{2\pi} \int_{-\infty}^{\infty} d\omega \, e^{i\omega t} \int_{-\infty}^{\infty}  \, du \,f(u) e^{-i\omega u} 
$$

From the above we may define the **Fourier Transform** of $f(t)$:
$$
\tilde{f}(\omega)=\frac{1}{\sqrt{ 2\pi }}\int_{-\infty}^{\infty} f(t)e^{-i\omega t} \, dt
$$

and its inverse by

$$

f(t)=\frac{1}{\sqrt{ 2\pi }}\int_{-\infty}^{\infty} \tilde{f}(\omega)e^{i\omega t} \, d\omega
$$

***
## Example: Exponential decay function

Find the Fourier transform of the exponential decay function $f(t)=0\text{ for }t<0$ and $f(t)=Ae^{-\lambda t}$ for $t\geq0$.


Using the definition:


