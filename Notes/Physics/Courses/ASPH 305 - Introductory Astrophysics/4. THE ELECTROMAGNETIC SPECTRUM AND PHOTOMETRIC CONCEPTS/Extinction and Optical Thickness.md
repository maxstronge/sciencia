# Extinction and Optical Thickness:
***

We saw when discussing [[Magnitudes#^9b7b43|absolute magnitudes]] that the apparent magnitude increases (and brightness decreases!) with increasing distance between the observer and the radiation source. If the space between these two objects is not completely empty, but instead contains some **interstellar medium**, the equation given above no longer holds exactly, because part of the radiation will be absorbed by that medium (and usually re-emitted at a different wavelength, which may be outside the band defining the magnitude), or scattered away outside the line of sight. All of these forms of radiation loss collectively referred to as **extinction**. 

![[Pasted image 20211112163016.png|Extinction model.]]

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

Another effect caused by the interstellar medium is the **reddening** of light: blue light is scattered/absorbed more than red. Therefore, the color index $B - V$ *increases*. The visual magnitude of a star, as given above, is:

$$V = M_V + 5\log frac{r}{10\,pc} + A_V $$

...where $M_V$ is the absolute visual magnitude and $A_V$ is the extinction in the visual band. Similarly, we get for the blue magnitudes: 

$$B = M_B + 5 \log frac{r}{10\,pc}+A_B $$


So the observed color index is now:

$$B - V = M_B - M_V +A_B -A_V $$

or 

> ### $$ B - V = (B - V)_0 + E_{B-V} $$
> ...where $(B-V)_0=M_B -M_V$ is the **intrinsic color** of the star and $E_{B-V}=(B-V)-(B-V)_0$ is the **color excess**.

Studies of the interstellar medium show that the ratio of the visual extinction $A_V$ to the color excess $E_{B-V}$ is almost constant *for all stars*:

> #### $$R = \frac{A_V}{E_{B-V}}\approx 3.0. $$

That makes it possible to find the visual extinction if the color excess is known:

$$A_V \approx 3.0 E_{B-V}.$$

When $A_V$ is obtained, the distance can be solved directly from the distance modulus when $V$ and $M_V$ are known. 

We will continue our study of the interstellar medium in a future course. 

***
### Atmospheric Extinction:

The Earth's atmosphere also causes extinction. The observed magnitude $m$ of a body depends on the location of the observer and the *zenith distance of the object*, since these factors determine the distance light has to travel through the atmosphere. To compare different observations, we must *reduce* them, *i.e.* remove the atmospheric factors somehow. The magnitude $m_0$ obtained from such a reduction can then be compared with other observations. 

If the **zenith distance** $z$ is not too large, we can approximate the atmosphere by a *plane layer* of constant thickness, as in the figure below:

![[Pasted image 20211112161959.png|Atmospheric extinction plane model.]]

If the thickness of the atmosphere is used as a unit, the light must travel a distance:

$$X = \frac{1}{\cos z} = \sec z. $$

The quantity $X$ is the **air mass**. According to our earlier work, the magnitude increases linearly with the distance $X$:

> ### $$m = m_0 + k X $$


 ...where $k$ is the **extinction coefficient**.
 
 The extinction coefficient can be determined by observing the same source several times during a single night with as *wide a zenith distance as possible*. The observed magnitudes are plotted in a diagram as a function of the air mass $X$. The points lie on a straight line, the slope of which gives the extinction coefficient $k$. 	 
 
 When this line is extrapolated to $X = 0$, we get the magnitude $m_0$, which is the apparent magnitude immediately outside the atmosphere. 
 
 In practice, observations with zenith distances higher than $70\degree$ (or altitudes less than $20\degree$) are *not* used to determine $k$ and $m_0$, since at low altitudes the curvature of the atmosphere begins to complicate matters, and the plane layer is no longer a sufficient approximation. 
 
 The value of the extinction coefficient $k$ also depends on the observation site and the time of the observation, as well as the wavelength (since extinction increases strongly towards short wavelengths). 
 
 


***
#physics #astrophysics #extinction #magnitude #optics #brightness #wavelength #flux 

