# 	ASPH305: Homework Assignment #1
***

## 1. 
Astronomers on Earth have measured the distance to a hypothetical approaching asteroid to be $0.713\,AU$. 

***

### *a)*

If the observed angular diameter of the asteroid at the time of observation is $0.01''$, **calculate the physical diameter (in *m*) and the solid angle (in *sr*)**. For the physical diameter, use both the *small angle approximation* **AND** the *full trigonometric approach* to confirm whether or not the small angle approximation is valid. **Explain your reasoning**. 


> Assuming the asteroid can be approximated as a sphere. 
> - distance $d = 0.713\,AU = 1.06663 \times 10^{8}\,km$
> - angular diameter $\alpha = 0.01'' = 4.84814 \times 10^{-8}\,rad$

With small-angle approximation: physical diameter $D = d \alpha:$

$$\begin{align} D & = d \alpha \\ & = (1.06663 \times 10^{8})\,(4.84814 \times 10^{-8}) \\ &=5.17118 \,km.\end{align} $$

Full trigonometric approach: 

$$R = r \tan\theta \implies D = 2R = 2r\tan\theta.$$

$$\theta = \frac{\alpha}{2} = \frac{4.84814 \times 10^{-8} rad}{2}$$

$$r = 1.06663 \times 10^{8} \,km$$

$$D = 2(1.06663\times10^{8})\cdot\tan\left(\frac{4.84814 \times 10^{-8} rad}{2}\right) = 5.17117\,km.$$

The small angle approximation is accurate to within a millimetre of the full trigonometric approach, so it is a valid approximation for this calculation.

***

### *b)*

After a few months, the asteroid has entered Earth's atmosphere and is only 10km from the surface. Given the physical diameter in *a)*, **calculate the asteroids angular diameter (in rads and degrees) and solid angle (in sr).** For both calculations, use **both the small angle approximation AND the full trigonometric approach** to confirm whether or not the small angle approximation is valid. Explain your reasoning. 

***

>With the small angle approximation:  $d = 10\,km \implies D = d \alpha \implies \alpha = \frac{D}{d}$.

Using our calculated value for the physical diameter, we find the new angular diameter to be:

>$$\alpha = \frac{5.17117}{10} = 0.517117\,rad = 29.6286\degree.$$

For the solid angle (still using the small angle approximation): $d\Omega \approx \pi \theta^2.$

> $$\theta = \frac{\alpha}{2} = 0.258559\,rad. $$
>$$\pi \theta^2 = \pi (0.0668525) = 0.210023\,sr. $$


Without the small angle approximation, the angular size of the asteroid is given by rearranging the equation:

>$$D = 2r\tan\theta \implies \tan\theta= \frac{D}{2r} = \frac{5.17117\,km}{20\,km}$$
>$$\theta = \arctan\left(\frac{5.17117}{20}\right) = 0.253017\, rad = 14.4968\degree. $$
>$$\alpha = 2\theta = 0.506035\,rad = 28.9937 \degree.$$

Now that the asteroid is much closer (which means the angle is not as small), the approximation is not nearly as close as it was in the previous question, as it is now off by almost a full degree. Some might say that the approximation would still suffice, but when dealing with imminent asteroid impacts, every degree counts. 

To find the solid angle without using the small angle approximation: 

> $$d\,\Omega = 2\pi\left(1-\cos\theta\right). $$
> $$\theta = \frac{\alpha}{2} = \frac{0.517117\,rad}{2} = 0.258559\,rad.$$
> $$2\pi\left(1-\cos\left(0.258559\right)\right) = 0.208857\,sr. $$

Again, the discrepancy between the approximation and the full trigonometric approach is much greater than before (though it is still relatively small). When the survival of the human race is concerned, this approximation loses too much precision to be useful. 

***

## 2.

### a)


Assuming the Earth is perfectly spherical with a radius of $6365\,km$ and using the formulae from the notes, **calculate the solid angle (in sr) and geographical area (in $km^2$)** of a portion of the Earth's surface enclosed by the points with coordinates:

- $\theta_1 = +51\degree\, 30'\,26.6''$ (N)
- $\theta_2 = +51\degree\, 28'\,43.0''$ (N)
- $\phi_1 = -0\degree\,3'\,1.1''$ (W)
- $\phi_1 = -0\degree\,11'\,40.2''$ (W)

To illustrate:

![[q2diagram.svg]]

We can relate the geographical area $dA$ to the solid angle $d\Omega$ with the following formula:

## $$dA = \rho^2 d\Omega $$

And since $dA = \rho^2 \sin\theta\, d\theta \,d\phi$, we can find the solid angle to be:

## $$d\Omega = \sin\theta\,d\theta\,d\phi. $$

We can integrate this equation over the specified coordinates to find the actual solid angle - but first, we need to convert the latitude/longitude coordinates to angles we can use as the limits for $\theta$ and $\phi.$


> - $\theta_1 = +51\degree\, 30'\,26.6'' = 51\degree + \frac{30}{60}\degree + \frac{26.6}{3600}\degree = 51.5073888\degree = 0.898974\,rad$
> - $\theta_2 = +51\degree\, 28'\,43.0'' = 51\degree + \frac{28}{60}\degree + \frac{43.0}{3600}\degree = 51.47861111\degree = 0.898471\,rad$
> - $\phi_1 = -0\degree\,3'\,1.1'' = 0\degree + \frac{3}{60}\degree + \frac{1.1}{3600}\degree = 0.4669722222\degree = 8.77998\times10^{-4}\,rad$
> - $\phi_2 = -0\degree\,11'\,40.2'' = 0\degree + \frac{11}{60}\degree + \frac{40.2}{3600}\degree = 0.1945\degree = 33.9467\times10^{-4}\,rad$.

 

Now we can integrate our expression for the solid angle from above and fill our values for $\theta$ and $\phi$:

> $$\begin{align} d\Omega & = \int_{\theta_1}^{\theta_2}\sin\theta\,d\theta \int_{\phi_1}^{\phi_2}\,d\phi \\ & = (-\cos\theta_2 + \cos\theta_1)\, \cdot\, (\phi_2 - \phi_1) \\ & = (-\cos(0.898471)+\cos(0.898974) \,\cdot\,(33.9467\times10^{-4} - 8.77998\times10^{-4}) \\ & = 9.89151\times 10^{-7}\text{ sr}.\end{align}$$

We can now convert to $km^2$ using the relation above:

> ### $$\begin{align} dA &= \rho^2\,d\Omega \\ & = (6465\,km)^2 \,\cdot\,(9.89151\times 10^{-7}\text{ sr}) \\ &=40.0737\,km^2.\end{align} $$

***

### b)

A telescope has a FWHM (Full Width at Half Maximum) resolution that can be approximated by the angle $2\theta$ in the figure below. If the FWHM of a telescope is $25''$, **calculate the solid angle of the telescope's resolution (in sr). Calculate the percentage of the full sky that this covers. Using a distance $= 384,000\,km$, calculate the linear size (in m) and the linear area (in $m^2$) of the smallest object that could be clearly seen on the Moon. Calculate the linear size (in AU) of the smallest object that can be clearly seen at a distance of 450*pc* (the distance of Orion). How does this compare to the size of a solar system like our own (*i.e.* to the orbit of Pluto)?**

![[asph_FWHM_diagram.svg]]

> **FWHM** = $2\theta$ = $25'' \implies \theta = \frac{25}{2}'' = (\frac{25''}{2}\,\cdot\,\frac{1\degree}{3600''}) = \frac{1}{288}\degree = 6.0601 \times 10^{-5}\text{ rad}.$ 	

We can find the solid angle in two ways: we can use the full formula for the solid angle of a circular region...

>## $$d\Omega = 2\pi (1-\cos\theta) $$

...or, given that this angle is incredibly small, we can use the small-angle approximation....


> ## $$\begin{align} d\Omega &\approx \pi \theta^2 \\ &= \pi (6.0601 \times 10^{-5})^2 \\ &= 1.15377 \times 10^{-8}\text{ sr}.\end{align}$$

Since the entire sky (when modeled as a sphere) has a surface area of $4\pi\text{ sr}$, we can find the percentage of the visible sky with a ratio:

> $$\text{percentage of sky }=\frac{1.15377 \times 10^{-8}}{4\pi}\,\cdot\,100\% = 9.18142\times10^{-8}\,\%. $$

Since only half the sky (at most) is visible at one time, however, the percentage of the visible sky taken up by the telescope's resolution is twice as high. 

The *FWHM* of a telescope is the smallest possible angular separation it can detect. So at a distance of $r = 384,000\,km$, we can again use the small-angle approximation to find the linear diameter $D$ of the smallest detectable object:

> ### $$\begin{align}D &\approx 2r\theta \\ & = 2 \,(384,000)\,\cdot\,(6.0601 \times 10^{-5}) \\ &= 46.5421\text{ km}.  \end{align} $$

We can find the linear area (in $m^2$) of this smallest detectable object on the surface of the moon by using the same formula as we did previously:

> ### $$\begin{align} dA &= \rho^2\,d\Omega \\ &= (384,000)^2\,\cdot\,(1.15377 \times 10^{-8}) \\ & = 1701.3\,\text{km}^2.\end{align} $$

Following a similar process at a distance of $450\text{ pc}$, we can find the linear size (in **AU**) of the smallest object that can be clearly seen. First, since we need the size in astronomical units, let's convert our distance $r$:

> $$450 \text{ pc} \,\cdot\,\frac{648,000}{\pi} = \frac{291,600,000}{\pi}\text{ AU} = 9.28192\times10^7 \text{ AU}. $$

We can now follow exactly the same steps as before with this new distance (in *AU* instead of *km*) to find the new linear diameter:


> ### $$\begin{align}D &\approx 2r\theta \\ & = 2 \,(9.28192\times10^7)\,\cdot\,(6.0601 \times 10^{-5}) \\ &= 11250.0\text{ AU}.  \end{align} $$

The orbit of Pluto around the Sun is 49.305 *AU* at aphelion, giving our solar system a diameter of approximately 98.61 *AU*. To compare sizes....


> $\frac{11250}{98.61} = 114.086 \implies$ the smallest detectable object is over 100x the size of our solar system at that distance. 


***

## 3.

The image below shows an "optical" image of the Orion Constellation ($\lambda = 550\,nm$) with an $8''$ ($20\,cm$) telescope. The inset at the top right shows a small region of the optical image observed with the $15\,m$ JCMT telescope at $\lambda = 850\,\mu m$ and shows a region containing a newly forming star. The inset at the bottom right shows a small region of the JCMT image observed with the ALMA array (composed of fifty $12m$ telescopes and another twelve $7m$ telescopes that make up something called the *compact array*) at $\lambda = 1.3\,mm$ and shows that what we thought was one forming star in the JCMT image is actually **two** new stars forming ("blobs" **B1** and **B2** in the ALMA image). 

![[Pasted image 20210928124342.png]]
***

### a)

**Calculate the resolutions of the optical image and the JCMT image (in '').**


To approximate the resolution of a telescope using a Gaussian whose FWHM angular resolution ~ the Rayleigh Criterion:

> ### $$\text{angular resolution: }\theta('') = 2.516\times 10^5 \frac{\lambda}{D}. $$

Plugging in the given values of $\lambda$ and $D$ for the optical telescope gives a resolution of:

> ### $$\begin{align} \theta_{optical} &= 2.516\times10^5 \left(\frac{5.50\times10^{-7}\,m}{0.2\,m} \right) \\ &= 2.516\times10^5 (2.75\times10^{-6}) \\ &= 0.6919''.\end{align}$$ 

We use a similar calculation for the JCMT image, using the appropriate values of $\lambda$ and $D$:

> ### $$\begin{align} \theta_{JCMT} &= 2.516\times10^5 \left(\frac{8.50\times10^{-4}\,m}{15\,m} \right) \\ &= 2.516\times10^5 (0.01275) \\ &= 14.2573''.\end{align} $$

***

### b)

If the distance to the Orion Molecular Cloud (in which blobs **B1** and **B2** are located) is $412\,pc$ and, at this distance, ALMA has a linear resolution of $500\,AU$, **calculate the maximum baseline of the ALMA array used to obtain this image (in m)**. 

Aperture synthesis arrays can achieve high resolutions - we can find the baseline using a similar relation as we did for the above telescopes:

> ### $$\text{Resolution: } \theta = 2.516\times 10^5 \frac{\lambda}{B},\text{ where B is the baseline.}$$

We don't yet know the angular resolution $\theta$ - to find it, we need to convert the *linear* resolution, $500\,AU$, to angular using the relation from before (since this distance is so large, we will again use the small-angle approximation):

> $$D \approx 2r\theta \implies \theta \approx \frac{D}{2r}$$

Filling in our given values for the distance and linear resolution:

> ### $$\begin{align} \theta = \frac{500\,AU}{2(412\,pc)} &= \frac{7.479893\times10^{13}\,m}{2.50557\times10^{19}\,m} \\ &= 5.884\times10^{-6}\text{ rad} \\ \theta &= 1.21407''. \end{align} $$

Now that we have $\theta$ in arcseconds, we can rearrange the above formula:

> ### $$\begin{align} \theta = 2.516\times10^5 \frac{\lambda}{B} &\implies B = 2.516\times 10^5 \frac{\lambda}{\theta} \\ &=2.516\times10^5 \frac{0.0013\,m}{1.21407''} \\ B &=269.408\,m.  \end{align} $$

***

### c)

If it took ALMA 1 hour of observing to make this image, **calculate how long it would take the JCMT to observe the source to the same flux limit** (assuming they are both observing at the same frequency).

The **flux limit** $F_{min}$ is proportional to the area and integration time according to the following relation:

> ### $$F_{min} \propto \frac{1}{A \sqrt{t_{int}}} .$$



If we set the two flux limits $F_{min}^{ALMA}$ and $F_{min}^{JCMT}$ to be equal, we find:


> ### $$\frac{1}{A_{ALMA}\sqrt{t_{ALMA}}} = \frac{1}{A_{JCMT}\sqrt{t_{JCMT}}}. $$


The light-gathering area $A$ of each telescope is given by:

> ### $$A = \pi \frac{D^2}{4} $$

Plugging in our values for the diameter $D$ of each telescope, we can find the area of the JCMT telescope to be:


> ### $$A_{JMCT} = \pi \frac{15^2}{4} = 176.715\,m^2.$$

For an interferometer like ALMA, the process of finding the light-gathering area is slightly more involved. It is the sum of the areas of all the telescopes within the baseline. Since there are 50 $12\,m$ telescopes and  12 $7\,m$ telescopes, the total area is:


> ### $$A_{ALMA} = 50\left(\pi \frac{12^2}{4} \right) + 12\left(\pi \frac{7^2}{4} \right) = 6116.68\,m^2.$$


We now have enough information to determine how long the JCMT would take to to observe the source to the same flux limit. If the ALMA telescope had an integration time $t_{int}$ of $3600\,s$:


> ### $$\frac{1}{A_{ALMA}\sqrt{t_{ALMA}}} = \frac{1}{A_{JCMT}\sqrt{t_{JCMT}}}. $$
> ### $$\frac{1}{6116.68\,m^2\sqrt{3600\,s}} = \frac{1}{176.715\,m^2\sqrt{t_{JCMT}}}. $$


Rearranging:

> ### $$\begin{align} \sqrt{t_{JCMT}} &= \frac{6116.68\,m^2\sqrt{3600\,s}}{176.715\,m^2} \\ &= 2076.79 \\ t_{JCMT} &= 4.31308 \times 10^6\,s \\ &= 1198.06 \,h.\end{align}$$

The JCMT would take almost 1200x as long to observe the source to the same flux limit due to its significantly smaller light-gathering area. This highlights the advantages of interferometers. 

***

## 4.

The image below is direct detection (using an $8m$ telescope at $\lambda = 1.3 \mu m$) of an exoplanet orbiting around a star that is $110\,pc$ from Earth. The star is located at the "+" symbol and its light is blocked out by the instrument used to take this image (a coronagraph). The planet is the point marked "b". It has a mass of ~9 Jupiter masses and a radius of 1.5 Jupiter radii. 

![[Pasted image 20210928142308.png]]
***
### a)

**Estimate the orbital distance of the planet from the star (in '') and, from that, calulate the orbital distance of the planet in AU.**


We can use the given scale of 1 arcsecond to set up a scale conversion factor from pixels to arcseconds: 

![[Pasted image 20210928143457.png]]

![[Pasted image 20210928143523.png]]

The 1 arcsec line is 219.32 pixels in length. Therefore:

> ## $$\text{Scale factor }= \frac{219.32\,p}{''}.$$

We can now measure the length of the line connecting the center of the exoplanet **b** and the star **+** in pixels:

![[Pasted image 20210928143856.png]]

![[Pasted image 20210928143908.png]]

That distance is $181.38\,p.$ We then use our scale factor to find the angular distance in **''**:

> ## $$181.38\,p\,\cdot\, \frac{''}{219.32\,p} = 0.827011''.  $$

We can again utilize the small-angle approximation to calculate the linear orbital distance of the planet from the star:


> ## $$\begin{align} D &= 2r\theta \\ &=2\, (110\,pc)\,(0.827011'') \\ &= (220\,pc)\,(0.827011'') \\ &= (6.78849\times10^{18}\,m)(0.827011'') \\ &= 5.61415\times10^{18}\,m \\ &= 3.75273\times10^7\,AU.\end{align}$$

***
## b)

At the same wavelength, **calculate the size of the hypothetical telescope needed to be able to clearly resolve an exoplanet orbiting this star at a distance of 1AU (in m)** (*i.e.* clearly see that the star and an exoplanet in an Earth-like orbit are separate objects). 


The **Rayleigh Criterion**, as mentioned above, defines the minimal angular separation of two point sources that can still be identified as distinct sources. It is given by: 

> ## $$\theta \text{ [rads]} = 1.22 \frac{\lambda}{D}.$$


Here, we are interested in the diameter $D$ of the telescope making the hypothetical observation. We know that the wavelength $\lambda = 1.3\mu m$, but we do not yet know the angular separation of the new orbit. If the linear orbital distance is now $1\,AU$, we can use the same relation as above to find the new angular separation:


> ### $$\begin{align} D = 2r  \theta \implies  \theta &= \frac{D}{2r} \\ &= \frac{1AU}{2(110\,pc)} \\ &= \frac{1AU}{220\,pc} \\ & = \frac{1.496 \times 10^{11}\,m}{6.78849\times10^{18}\,m} \\ \theta &=2.20373\times10^{-8}\text{ rads.}\end{align}$$

We can now substitute this value of $\theta$ into the Rayleigh Criterion above and solve for the diameter:

> ### $$\begin{align} \theta = 1.22 \frac{\lambda}{D} \implies D &= 1.22 \frac{\lambda}{\theta}\\ &=1.22 \left( \frac{1.3\times10^{-6}\,m}{2.20373\times10^{-8}\text{ rads}} \right) \\ &= 71.9689\,m.\end{align}$$

***

## c)

If you wanted to observe the planetary system shown in the figure using the Thirty Meter Telescope (TMT - currently under construction on Mauna Kea in Hawaii) at the same wavelength, **calculate the maximum distance this system could be from Earth and still be resolved (in pc).**

Since we're interested in finding the maximum distance where the two points can be seen as distinct, let's use the Rayleigh Criterion:


> ## $$\theta \text{ [rads]} = 1.22 \frac{\lambda}{D}. $$

This relation does not involve distance. We can, however, put $\theta$ in the above equation in terms of the distance $r$ and linear separation $D$ between the star and the exoplanet from the small-angle approximation:

> ## $$D = 2r\theta\implies \theta = \frac{D_{\text{linear separation}}}{2r} = 1.22 \frac{\lambda}{D_{TMT}}. $$

The diameter of the TMT is $30\,m$. [^1] We earlier calculated that the linear distance of the star's orbit is approximately $3.75273\times10^7\,AU =5.614\times10^{18}\,m.$ We can solve the above equation for the distance $r$ to find:


> ### $$\frac{D_{\text{linear separation}}}{2r} = 1.22 \frac{\lambda}{D_{TMT}} \implies r = \frac{D_{\text{linear separation}}\,\cdot\,D_{TMT}}{2(1.22\,\lambda)}$$
>  ### $$ r = \frac{5.614\times10^{18}\,m\,\cdot\,30\,m}{2(1.22\,(1.3\times10^{-6}\,m)}$$
>  ### $$ r = \frac{1.6842\times10^{20}\,m^2}{3.172\times10^{-6}\,m}$$
>  ## $$ r = 5.30958\times10^{25}\,m = 1.72085\times10^9 \,pc.(!!)$$

The distance from which the system can be resolved using the TMT is incredibly large. 


[^1]: https://www.tmt.org/page/optics