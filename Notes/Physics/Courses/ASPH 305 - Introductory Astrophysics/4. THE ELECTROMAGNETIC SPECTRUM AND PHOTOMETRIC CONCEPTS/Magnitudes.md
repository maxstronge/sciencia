# Magnitudes:
***

The concept of brightness **magnitudes** was developed by Hipparchus circa 2nd century *BCE*.

Stellar objects were divided into 6 classes according to their **apparent brightness** - magnitude 1 was the brightest and magnitude 6 was the faintest object detectable with the naked eye. 

![[Pasted image 20211020110159.png]]

Since then, we have developed instruments that  can see objects much fainter than mag 6 and the scale has been modified. Importantly though, the magnitude system reflects that the response of the human eye to the brightness of light is *not* linear - it’s *logarithmic*. Thus, if the flux densities of 3 stars 	are in the proportion 1:10:100, the difference in brightness of the first two stars appears equal to the difference in brightness of the second two stars. 

We can approximate Hipparchus’ system with a mathematical definition of the magnitude:

> ## $$m = -2.5 \log\frac{F}{F_o} $$

…where $m$ is the **apparent magnitude**. The apparent magnitude is related to the apparent brightness / flux. We decide that the magnitude $0$ corresponds to some preselected flux density $F_0$. 

If the magnitudes of two stars are $m$ and $m+1$, and their flux densities $F_m$ and $F_{m+1}$, respectively, we have:

> ## $$\begin{align}m - (m+1) &= -2.5 \log\frac{F_m}{F_o} + 2.5\log\frac{F_{m+1}}{F_o} \\[2ex] &=-2.5\log\frac{F_m}{F_{m+1}}.\end{align} $$

whence…

> # $$\frac{F_m}{F_{m+1}} = \root{5}  \of{100}.  $$


In the same way, we can show that the magnitudes $m_1$ and $m_2$ of two stars and the corresponding flux densities $F_1$ and $F_2$ are related by:

> ## $$m_1 - m_2 = -2.5\log\frac{F_1}{F_2}. $$

**Example:** Star 2 has a flux that is 84x greater than the flux of Star 1. If Star 2 has magnitude $2.7$, what is Star 1’s magnitude?

> #### Solution:
>
> $$\begin{align} m_2 - m_1 &= -2.5\log\frac{F_2}{F_1} \\[2ex] m_1 &= m_2 + 2.5\log\frac{F_2}{F_1} \\[2ex] m_1 &= 2.7  + 2.5\log\frac{84\,F_1}{F_1} \\[2ex] m_1 &= 2.7 + 4.8 = 7.5_{mag}\end{align}$$

Notice that the fainter star has a much larger magnitude!

***

## Apparent Magnitudes:

The magnitude we have been using thus far are **apparent magnitudes** ($m$). Apparent magnitudes correspond to how bright an object appears in the sky. Apparent brightness does not, however, tell us anything about the true luminosity of the star (if we don’t know the distance). 

We can solve this by defining an **absolute magnitude** $(M)$, which is defined as the *apparent magnitude* an object would have if it were a distance of $12\,pc$ from the observer. 

We can relate the absolute magnitude to the apparent magnitude in the following way. Consider a star wit
