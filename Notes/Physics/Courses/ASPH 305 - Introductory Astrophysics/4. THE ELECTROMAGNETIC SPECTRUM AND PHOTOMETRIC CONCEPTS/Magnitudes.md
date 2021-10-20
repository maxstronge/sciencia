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

We can relate the absolute magnitude to the apparent magnitude in the following way. Consider a star with apparent magnitude $m$ at a distance of $D\,pc$, as yet unknown. Define $M$ as the *absolute* magnitude of the *same* star if it were at a distance of $10\,pc$: 


> ## $$m_2 - m_1 = -2.5\log\frac{F_2}{F_1} $$
> ## $$m-M = -2.5\log\frac{F(D)}{F(10\,pc)}, $$ 
>where $F(D)$ is the flux it has at some unknown distance $D$, and the flux in the denominator is the flux it would have at $10\,pc$. 
>
> Recall that $F(D) = \frac{L}{4\pi D^2}$ and $F(10\,pc) = \frac{L}{4\pi \,(10\,pc)^2}$.

***

### Magnitude Systems:

The *apparent magnitude $m$*, which we have just defined, depends on the instrument used to measure it. The sensitivity of a detector will be different at different wavelengths/different instruments detect different wavelength *ranges*. Thus the flux measured by an instrument is	*not* equal to the total flux, but only the fraction of it which that instrument can detect. Depending on the method of the observation, we can define various different magnitude systems, each with different zero points (*i.e.* different flux densities $F_o$ corresponding to zero magnitude). 


In daylight, the *human eye* is most sensitive to radiation with a wavelength of about $550\,nm$, and the sensitivity decreases towards red (longer wavelengths) and violet (shorter wavelengths). The magnitude corresponding to the sensitivity of the human eye is called the **visual magnitude**, $m_v$ . 

*Photographic plates* are typically most sensitive at *blue* and *violet* wavelengths, but they are also able to register radiation not detectable by the human eye. Thus the **photographic magnitude** $m_{pg}$ usually differs from the visual magnitude. 

The sensitivity of the human eye can be *simulated* with a photographic plate by using a yellow filter in combination with plates sensitized to yellow light. Magnitudes observed this way are called **photovisual magnitudes**.



If, in an ideal case, 
