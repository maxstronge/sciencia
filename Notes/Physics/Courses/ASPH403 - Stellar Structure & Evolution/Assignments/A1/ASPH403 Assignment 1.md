# Homework Assignment #1
### ASPH403
### Jan 31, 2022
***

#### 1. 
Extremely broadband spectroscopy of a star with a measured parallax of 130.208 mas (milli-arcseconds) yields the Black Body spectrum pictured below. Integrating this function (i.e. finding the area under the curve) yields a total (i.e. bolometric) flux of $2.317185\times10^{-8} \ W \ m^{-2}$. Using this information, calculate the *Luminosity* (in $W$ and $L_\Sun$), *Temperature* (in $K$ and $T_\Sun$) , and *Radius* (in $m$ and $R_\Sun$) of this star.

Use the following constants:
- $L_\Sun =  3.828 \times 10^{26} \ W$
- $T_\Sun = 5772 \ K$
- $R_\Sun = 6.963 \times 10^8 \ m$

![[Pasted image 20220128154935.png]]

**Solution**: 

First, we can use the given parallax to find the distance to the star:

$$D \ [pc] = \frac{1}{p \ ["]} = \frac{1}{130.208\times 10^{-3}} = 7.68002 \text{ pc}.$$

We can find the surface temperature from the peak wavelength on the above figure using Wien's law. The peak intensity occurs at $\ll_{\text{peak}}=300\text{ nm}$, so:


$$\ll_{\text{peak}} = \frac{2.898\times10^{-3}\text{ K $\cdot$ m}}{T} \implies T = \frac{2.898\times10^{-3}\text{ K $\cdot$ m}}{300\times 10^{-9}\text{ m}}  ...$$

>$$=9660\text{ K}.$$

In units of $T_\Sun$:

> $$\frac{T}{T_\Sun}=\frac{9660}{5772} = 1.6736 \ T_\Sun.$$

With the distance given from the parallax and the bolometric flux, we can find the luminosity:

$$\begin{align} F_{\text{bol}} = \frac{L}{4 \pi D^2}&\implies L = F_{\text{bol}}   \qty(4 \pi D^2)\\ &= 2.317185\times10^{-8}\text{ W m}^{-2} \cdot \qty(4\pi(7.68002\text{ pc})^2) \\ &= 2.31715\times10^{-8} \qty(4\pi)\qty(5.6198\times10^{34}\text{ m}^2) \end{align} $$

> $$ = 1.6353 \times 10^{28}\text{ W}. $$

In units of $L_\Sun$:

>$$\frac{L}{L_\Sun} = \frac{1.6353 \times 10^{28}}{3.828 \times 10^{26}} = 42.7193 \ L_\Sun.$$

We can find the surface flux using the temperature found earlier via the following relation:

$$F_{\text{surface}}=\sigma \ T^4 = 5.67037\times10^{-8} (9660)^4 = 4.93765 \times 10^8 \text{ Wm}^{-2}.$$

And finally, we can find the radius of the star using the surface flux and the luminosity:

$$F_{\text{ surface}} = \frac{L}{4\pi R^2} \implies R = \sqrt{\frac{L}{4 \pi F_{\text{ surface}}}}.$$

$$= \sqrt{\frac{1.6353 \times 10^{28} }{4\pi \qty(4.93765 \times 10^8 )}}$$

>$$= 1.62343\times10^9\text{ m.}$$

In units of $R_\Sun$:


$$\frac{R}{R_\Sun}=\frac{2.53956\times10^9}{6.963 \times 10^8} $$

> $$= 2.33151 \ R_\Sun.$$

***

#### 2.

The density of a star is bounded by 2 constraints: the density at the center $(r=0)$ is a *constant* denoted by $\rho(0)=\rho_c$, and the density at the surface $(r=R)$ is $\rho(R)=0$. The equation connecting the two limits is: 

$$\rho(R) = \rho_c \left[ 1- \left(\frac{r}{R}\right)^2 \right]$$

**a)** Derive an equation for the central density of a star as a function of the total mass $M$ and radius $R$, and calculate the central density of the sun. By way of comparison, the atmospheric density at sea level on Earth is $\approx 1.2 \ kg/m^3$. Also, prove that the average density of a star is given by $\overline{\rho}=0.4\rho_c$.

**b)** Derive an equation for the central pressure of a star in terms of its total mass $M$ and radius $R$, and calculate the central pressure of the sun. By way of comparison, the atmospheric pressure at sea level on Earth is $\approx 10^5 \ N/m^2$.

***

#### 3. 
**a)** Using the same density profile as in Q2, prove that the potential energy of a star is given by 