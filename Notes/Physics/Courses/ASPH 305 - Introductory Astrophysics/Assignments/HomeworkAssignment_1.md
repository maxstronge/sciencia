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

>### $$\begin{align} d\Omega & = \int_{\theta_1}^{\theta_2}\sin\theta\,d\theta \int_{\phi_1}^{\phi_2}\,d\phi \\ & = (-\cos\theta_2 + \cos\theta_1)\, \cdot\, (\phi_2 - \phi_1) \\ & = (-\cos(0.898471)+\cos(0.898974) \,\cdot\,(33.9467\times10^{-4} - 8.77998\times10^{-4}) \\ & = 9.89151\times 10^{-7}\text{ sr}.\end{align}$$

We can now convert to $km^2$ using the relation above:

> ### $$\begin{align} dA &= \rho^2\,d\Omega \\ & = (6465\,km)^2 \,\cdot\,(9.89151\times 10^{-7}\text{ sr}) \\ &=40.0737\,km^2.\end{align} $$

***

### b)

A telescope has a FWHM (Full Width at Half Maximum) resolution that can be approximated by the angle $2\theta$ in the figure to the right. If the FWHM of a telescope is $025''$, **calculate the solid angle of the telescope's resolution (in sr). Calculate the percentage of the full sky that this covers. Using a distance $= 384,000\,km$, calculate the linear size (in m) and the linear area (in $m^2$) of the smallest object that could be clearly seen on the Moon. Calculate the linear size (in AU) of the smallest object that can be clearly seen at a distance of 450*pc* (the distance of Orion). How does this compare to the size of a solar system like our own (*i.e.* to the orbit of Pluto)?**