# Extinction and Optical Thickness:
***

We saw when discussing [[Magnitudes#^9b7b43|absolute magnitudes]] that the apparent magnitude increases (and brightness decreases!) with increasing distance between the observer and the radiation source. If the space between these two objects is not completely empty, but instead contains some **interstellar medium**, the equation given above no longer holds exactly, because part of the radiation will be absorbed by that medium (and usually re-emitted at a different wavelength, which may be outside the band defining the magnitude), or scattered away outside the line of sight. All of these forms of radiation loss collectively referred to as **extinction**. 

We would like to be able to determine how the extinction depends on the distance. Assume we have a star radiating a flux $L_0$ into a solid angle $\oo$ in some wavelength range. Since the medium will absorb and scatter radiation, the flux $L$ will now decrease with increasing distance $r$ ($D$ in the equation above, switching now) as the radiation travels through more medium. 

In a short distance interval $\qty[r,\,r+dr]$, the extinction $dL$ is proportional to the flux $L$ and the distance travelled through the medium:

> ### $$dL = -\aa L dr. $$

The factor $\aa$ tells us how effectively the medium can obscure radiation. This quantity is called the **opacity**. From the above equation we can see that the opacity has units $[\aa]=m^{-1}.$ 

The opacity is zero in a perfect vaccum, and approaches infinity when the substance becomes murkier. We can now define a dimensionless quantity called the **optical thickness** $\tau$ by:

$$d\tau = \aa dr. $$ ^b3b71c

Substituting this into the above equation, we find:

> ### $$dL = -L d\tau. $$

Next, we integrate this across the line of sight from the *source* (where $L = L_0$ and $r=0$) to the observer:

> ### $$\int_{L_0}^{L}\frac{dL}{L} = - \int_0^\tau d\tau,$$

...which gives:

> ### $$L = L_0 e^{-\tau}. $$

Here, $\tau$ is the optical thickness of the material between the source and the observer, and $L$ is the observed flux. Empty space is perfectly transparent, *i.e.* its opacity is $\aa = 0$; thus, the optical thickness does not increase in empty space (since $d\tau = \aa dr$), and the flux remains constant. 

Let $F_0$ be the flux density on the surface of a star, and $F(r)$, the flux density at a distance $r$. We can express the fluxes as:

$$L = \oo r^2 F(r),\qq{}L_0 = \oo R^2 F_0 ,$$

..where $R$ is the radius of the star. Substitution into [[#^b3b71c|this equation]] gives:

$$F(r) = F_0 \frac{R^2}{r^2}e^{-\tau}. $$

For the absolute magnitude we need to find the *flux density* at a distance of $10\,pc$, a.k.a $F(10)$, which is still evaluated without extinction:

$$F(10) = F_0 \frac{R^2}{(10\,pc^2)}$$


The distance modulus $m-M$ is now:

$$\begin{align} m-M &= -2.5\log\frac{F(r)}{F(10)} \\[2ex] &= 5\log \frac{r}{10\,pc}-2.5\log e^{-\tau} \\[2ex] &= 5\log \frac{r}{10\,pc}+(2.5\log e) \tau \\[2ex] \end{align}$$

...or...

> ### $$m-M=5\log\frac{r}{10\,pc}+A $$
> ...where $A \geq 0$ is the extinction in the magnitudes due to the entire medium between radiator and observer. 

^21d6a7

If the opacity is constant along the line of sight, we have:

$$\tau = \aa \int_0^r dr = \aa r, $$

and [[#^21d6a7|the distance modulus]] becomes:

> ### $$ m - M = 5\log \frac{r}{10\,pc}+a r, $$
> where the constant $a=2.5\aa \log e$ gives the extinction in magnitudes per unit distance. 


***

### Color Excess:

