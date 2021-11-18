# ASPH305: Homework Assignment 3
##### Max Stronge (30064749)

***
### 1.
 The $8.2m$ VLT telescope is located on Cerro Paranal in the Atacama desert in Northern Chile, and is at an an altitude of $2635m$ above sea level. The $1.8m$ ARCT telescope (owned by the University of Calgary) is located near Priddis, AB at a physical altitude of $1300m$ above sea level. Both can operate at wavelengths from $300nm$ to $20\mu m$.

Atmospheric extinction changes as a function of the *atmospheric pressure*, which is itself a function of the physical altitude above sea level. Approximating the atmosphere using a model in which both the atmospheric density and pressure fall off exponentially with physical altitude, atmospheric extinction can be given by the equation:

 $$ k (z) = k_0\,e^{-\frac{z}{H}}$$

...where $k(z)$ is the extinction at a physical altitude of $z$, $z$ is your physical altitude above sea level, $k_0$ is the extinction at sea level, and $H$ is the scale height of the atmosphere (measured to be $\approx \,8km$).

At $\ll = 10\mu m$, and using $\kappa_0 = 0.262\text{ mag }km^{-1}$, calculate the *opacity* $\tau$ AND *transmission of the atmosphere for both telescopes*, for a source at an altitude of $10\degree$ above the horizon. Which telescope would be better to use for these observations, and why?




***
- Physical altitude of VLT telescope: $2635m$
- Physical altitude of ARCT telescope: $1300m$

![[Pasted image 20211112163421.png|Visualized.]]
- Astronomical altitude of Source 1: $75\degree$ above the horizon
- Astronomical altitude of Source 2: $10\degree$ above the horizon. 
- Wavelength: $\ll = 10\mu m$
- Extinction coefficient at sea level ($z=0$): $k_0 = 0.262\text{ mag km}^{-1}$

Using the plane-parallel atmosphere model, we can determine the distance $ds$ the radiation will travel through the atmosphere in terms of the *zenith angle* $za$ of the radiative source as viewed from the telescope. From trigonometry:

$$ds =  \sec za  \ dz$$

Since the extinction function is not constant, and depends on distance, we will need to integrate the extinction function $\kappa(z)$ over that distance $ds$:

$$\tau = \int \kappa(z) \ ds = \int \ \kappa_0 \ e^{-\frac{z}{H}}\sec za \ dz$$

The limits of integration for $z$ will be the physical altitude of the telescope for the lower limit, and can be treated as going to infinity:

$$=\kappa_0 \int_{z=z_i}^\infty e^{-\frac{z}{H}}\sec za \ dz.$$

We can now find the opacity for each source for each telescope. For the VLT telescope, which is at a physical altitude of $2635m$, the first source is at an angle of $75\degree$ above the horizon, which corresponds to a zenith angle of $15\degree$. Then:

$$\begin	{align}za = 15\degree &= 0.261799 \text{ rad} \implies \sec za = 1.03528. \\[3ex] \end{align}$$

So the opacity is:

$$\begin{align} \tau &= \kappa_0 \int_{z_i}^\infty e^{-\frac{z}{H}}\sec za \ dz \\[2ex] &= 0.262\text{ mag km}^{-1} \int_{2.635}^{\infty} e^{-\frac{z}{8}}  (1.03528) \ dz \\[2ex] &= 1.561 \text{ mag.}\end{align}$$

And the transmission is given by:
$$I_\nu = e^{-\tau} = 0.209927.$$

For the second source at an angle of $10\degree$ above the horizon, corresponding to a zenith angle of $80\degree$:

$$za = 80\degree = \frac{4\pi}{9}\text{ rad} \implies \sec za = 5.75877.$$

So:

$$\begin{align}\tau &= \kappa_0 \int_{z_i}^\infty e^{-\frac{z}{H}}\sec za \ dz \\[2ex] &= 0.262 \int_{2.635}^\infty e^{-\frac{z}{8}} (5.75877) \ dz \\[2ex] &= 8.68311\text{ mag} \\[3ex] \text{Transmission} &= I_\nu = e^{-\tau} = 1.6943\times10^{-4}. \end{align} $$

The same process applies for the second telescope, the ARCT,  at a physical altitude of $1.3\text{ km}$. The zenith angles will be the same for the second telescope as the first since the astronomical altitudes of the radiative sources are the same relative to the telescope. For the first source ($za = 15\degree$):



$$\begin{align} \tau &= 0.262 \int_{z=1.3}^\infty e^{-\frac{z}{8}}(8) (1.03528) \ dz \\[2ex] &= 1.84448\text{ mag}. \\[2ex] \text{Transmission} &= I_\nu = e^{-\tau} = 0.158107 .\end{align}$$

And for the second source:

$$\begin{align} \tau &= 0.262 \int_{z=1.3}^\infty e^{-\frac{z}{8}}(8) (5.75877) \ dz \\[2ex] &= 10.26\text{ mag}. \\[2ex] \text{Transmission} &= I_\nu = e^{-\tau} = 3.5005\times10^{-5}.\end{align}$$
***
<table>
	<tr>
		<th>Telescope</th>
		<th>Source</th>
		<th>Opacity [mag]</th>
		<th>Transmission</th>
	</tr>
	<tr>
		
			<td>VLT</td>
			<td>1</td>
			<td>1.561</td>
			<td> 0.20997 </td>
	</tr>
		<tr>
		
			<td>VLT</td>
			<td>2</td>
			<td> 8.68311</td>
			<td> 1.69423 x 10^(-4) </td>
	</tr>
		<tr>
		
			<td>ARCT</td>
			<td>1</td>
			<td>1.84448</td>
			<td> 0.158107 </td>
	</tr>
	<tr>
		
			<td>ARCT</td>
			<td>2</td>
			<td> 10.26</td>
			<td> 3.5005 x 10^(-5) </td>
	</tr>
	
</table>

The VLT telescope would yield better results - its higher physical altitude means that light must travel through less airmass to reach the telescope, resulting in less extinction. 

***
### 2.

The table below lists the observed V-band ($\ll = 547.5\,nm$) and B-Band ($\ll =  435.3\,nm$) for some star observed over the course of the night on December 25th, 2021. The time of the observations, altitude, and azimuth of the star are given in the first 5 columns. The star has a parallax of $284.56\text{ mas}$.
![[Pasted image 20211117101741.png|Table of V-band and B-band values.]]

**a.** Plot $m_V$ and $m_B$ versus airmass. From the plot, determine the *atmospheric exctinction coefficients* for both bands, and the *true* V-band and B-band magnitudes for the star (i.e. corrected for extinction).
***
![[HW3 1.png|mv and mb vs. X.]]
$$m = m_0 + kX$$

We can put our equations into this form by substituting our values for $m_B$ and $m_V$ in for $m$. The magnitude $m_0$ is the magnitude that would be measured without the effects of atmospheric extinction.

The slope of each line, then, will be the extinction coefficient $k$ for each band:

$$\begin{align} m_B &= m_0 +kX \implies k_B = 0.5187. \\ m_V &= m_0 + kX \implies k_V = 0.2675. \end{align}$$

The true apparent magnitude for each band can also be found from the graph - since the trendline is of the form $y=mx+b$, we see that the true apparent magnitude in each band is the $y$-intercept of each respective line:

$$\begin{align} m_{0,b} &=  1.7714. \\ m_{0,v} &= 0.3266. \end{align}$$


***
	
	
**b.** Spectroscopically, this star is a hot, blue star (known as a B-type star) with known, intrinsic, absolute magnitudes	of $M_{V,0} = -3.7$ and $M_{B,0} = -2.95.$ Calculate the amount of *interstellar extinction* (i.e. $A_V$ and $A_B$) in both bands. 

***
We will need to find the distance to the star using the given parallax. The parallax was given in $\text{mas}$, so the distance will be:

$$D \ [pc] = \frac{1}{p \ ["]} = \frac{1}{284.56 \times 10^{-3}} = 3.5142 \text{ pc}.$$

We now have the distance $r$, as well as the absolute and apparent magnitudes. The total extinction $A$ can be found via the equation:

$$m-M = 5 \log \qty(\frac{r}{10\text{ pc}}) + A \implies A = m - M - 5\log\qty(\frac{r}{10\text{ pc}}).$$

Subsituting our derived and given values for $r, \ m,$ and $M$:

$$\begin{align}A_V &=	m_V - M_V - 5 \log \qty(\frac{3.5142\text{ pc}}{10\text{ pc}}) \\ &= 0.3266 + 3.7 - 5\log(0.35142) \\ & = 6.29747. \\[3ex] A_B &= m_B - M_B - 5 \log \qty(\frac{3.5142\text{ pc}}{10\text{ pc}}) \\ &= 1.7714 + 2.95 - 5 \log(0.35142) \\ &= 6.99227.\end{align}$$
	
***
### 3.

Extreme broadband spectroscopy of a star with a measured parallax of $130.208\text{ mas}$ yields the following spectrum:

![[Pasted image 20211111122414.png|Extreme broadband spectroscopy.]]

Integrating this function (*i.e.* finding the area under the curve) yields a total (*i.e.* bolometric) flux of $2.317185\times10^{-8}\text{ W m}^{-2}$. 

Using this information, calculate the *luminosity* (in $W$ and $L_\Sun$), *temperature* (in $K$ and $T_\Sun$), and *radius* (in $m$ and $R_\Sun$) of this star. 

Use the following constants: 

$$\begin{align}L_\Sun &= 3.828 \times 10^{26} \ W, \\ T_\Sun &= 5772 \ K ,\\ R_\Sun &= 6.963 \times 10^8 \ m. \end{align}$$

***
We have $F_{\text{measured}}=2.31715 \times 10^{-8}\text{ Wm}^{-2}.$

First, using the given parallax, we can find the distance to the star in parsecs:

$$D \ [pc] = \frac{1}{p \ ["]} = \frac{1}{130.208\times 10^{-3}} = 7.68002 \text{ pc}.$$

We can find the bolometric luminosity in $W$ via the following equation:

$$\begin{align} L_{\text{total}} &= 4 \pi D^2 F_{\text{measured}}\\ &= 4\pi (7.68002\text{ pc})^2 \ \cdot 2.31715 \times 10^{-8}\text{ Wm}^{-2} \\ &= 4 \pi (2.36981\times10^{17} \ m)^2 \cdot 2.31715 \times 10^{-8}\text{ Wm}^{-2} \\ &= 1.63527 \times 10^{28} \ W\end{align}$$


***

### 4. 

If you don't have the full spectrum, as in the above question, the stellar temperature can still be obtained by measuring the *ratio* of stellar intensity at two different wavelengths, or, more commonly, in two different *filters*. 

The Johnson Filter system has the approximate wavelength response shown in the image below (*NB:* oversimplification):

![[Pasted image 20211117102513.png|Johnson Filter wavelength response.]]

Using $B$ and $V$ filters, you measure the apparent $V$ magnitude of the star to be $m_V = 0.50$ and $B-V = 1.32$. Extinction and reddening are negligible. 


**a.** Calculate the temperature of the star (to an accuracy of $\pm 5 \ K$). Hint: use the approximation that the ratio of flux in the two bands is equal to the ratio of the 'integrated' Planck function (*i.e.* the ratio of $\ll_{\text{center}}B_{\ll,\text{center}}$). Solve for the temperature numerically. Make sure you account for the relative flux transmission of the two bands. 

***

***

**b.** If the bolometric correction $BC$ of this star (accounting for the flux transmission of the filters) is $7.071$ and the measured parallax $p$ of the star is $5.95 \text{ mas}$, calculate the stellar radius (in $R_\Sun$). You may assume that $T_\Sun = 5772  \ K$ and $M_{\text{bol,}\Sun} = 4.75$.

***
***