# ASPH305: Homework Assignment 3
##### Max Stronge (30064749)

***
### 1.
 The $8.2m$ VLT telescope is located on Cerro Paranal in the Atacama desert in Northern Chile, and is at an an altitude of $2635m$ above sea level. The $1.8m$ ARCT telescope (owned by the University of Calgary) is located near Priddis, AB at a physical altitude of $1300m$ above sea level. Both can operate at wavelengths from $300nm$ to $20\mu m$.

Atmospheric extinction changes as a function of the *atmospheric pressure*, which is itself a function of the physical altitude above sea level. Approximating the atmosphere using a model in which both the atmospheric density and pressure fall off exponentially with physical altitude, atmospheric extinction can be given by the equation:

 $$ k (z) = k_0\,e^{-\frac{z}{H}}$$

...where $k(z)$ is the extinction at a physical altitude of $z$, $z$ is your physical altitude above sea level, $k_0$ is the extinction at sea level, and $H$ is the scale height of the atmosphere (measured to be $\approx \,8km$).

At $\ll = 10\mu m$, and using $\kappa_0 = 0.262\text{ mag }km^{-1}$, calculate the *opacity* $\tau$ AND *transmission of the atmosphere for both telescopes*, for a source at an altitude of $10\degree$ above the horizon. 

**NB**: physical (geographical) altitude $\neq$ astronomical altitude

**NB**: $k$ is not a constant, it varies as the atmosphere varies, so we will need to the opacity equation along the line of sight. 

Which telescope would be better to use for these observations, and why?
***
- Physical altitude of VLT telescope: $2635m$
- Physical altitude of ARCT telescope: $1300m$

![[Pasted image 20211112163421.png|Visualized.]]
- Astronomical altitude of Source 1: $75\degree$ above the horizon
- Astronomical altitude of Source 2: $10\degree$ above the horizon. 
- Wavelength: $\ll = 10\mu m$
- Extinction coefficient at sea level ($z=0$): $k_0 = 0.262\text{ mag km}^{-1}$

Using the plane-parallel atmosphere model, we can determine the distance $ds$ the radiation will travel through the atmosphere in terms of the *zenith angle* $za$ of the radiative source as viewed from the telescope. From trigonometry:

$$ds = H \sec za  \ dz$$

Since the extinction function is not constant, and depends on distance, we will need to integrate the extinction function $\kappa(z)$ over that distance $ds$:

$$\tau = \int \kappa(z) \ ds = \int \ \kappa_0 \ e^{-\frac{z}{H}}H\sec za \ dz$$

The limits of integration for $z$ will be the physical altitude of the telescope for the lower limit, and can be treated as going to infinity:

$$=\kappa_0 \int_{z=z_i}^\infty e^{-\frac{z}{H}}H\sec za \ dz.$$

We can now find the opacity for each source for each telescope. For the VLT telescope, which is at a physical altitude of $2635m$, the first source is at an angle of $75\degree$ above the horizon, which corresponds to a zenith angle of $15\degree$. Then:

$$\begin{align}za = 15\degree &= 0.261799 \text{ rad} \implies \sec za = 1.03528. \\[3ex] \end{align}$$

So the opacity is:

$$\begin{align} \tau &= \kappa_0 \int_{z_i}^\infty e^{-\frac{z}{H}}H\sec za \ dz \\[2ex] &= 0.262\text{ mag km}^{-1} \int_{2.635}^{\infty} e^{-\frac{z}{8}} (8km) (1.03528) \ dz \\[2ex] &= 12.488 \text{ mag}\end{align}$$

And the transmission is given by:
$$I_\nu = e^{-\tau} = 3.7715\times 10^{-6}.$$

For the second source at an angle of $10\degree$ above the horizon, corresponding to a zenith angle of $80\degree$:

$$za = 80\degree = \frac{4\pi}{9}\text{ rad} \implies \sec za = 5.75877.$$

So:

$$\begin{align}\tau &= \kappa_0 \int_{z_i}^\infty e^{-\frac{z}{H}}H\sec za \ dz \\[2ex] &= 0.262 \int_{2.635}^\infty e^{-\frac{z}{8}} (8)(5.75877) \ dz \\[2ex] &= 69.4649\text{ mag} \\[3ex] \text{Transmission} &= I_\nu = e^{-\tau} = 6.78873\times10^{-31}. \end{align} $$

The same process applies for the second telescope, the ARCT,  at a physical altitude of $1.3\text{ km}$. The zenith angles will be the same for the second telescope as the first since the astronomical altitudes of the radiative sources are the same relative to the telescope. For the first source ($za = 15\degree$):



$$\begin{align} \tau &= 0.262 \int_{z=1.3}^\infty e^{-\frac{z}{8}}(8) (1.03528) \ dz \\[2ex] &= 14.7559 \\[2ex] \text{Transmission} &= I_\nu = e^{-\tau} = 3.90469\times10^{-7}.\end{align}$$

And for the second source:

$$\begin{align} \tau &= 0.262 \int_{z=1.3}^\infty e^{-\frac{z}{8}}(8) (5.75877) \ dz \\[2ex] &= 82.0802 \\[2ex] \text{Transmission} &= I_\nu = e^{-\tau} = 2.25446\times10^{-36}.\end{align}$$
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
			<td>12.488</td>
			<td> 3.7715 x 10^(-6) </td>
	</tr>
		<tr>
		
			<td>VLT</td>
			<td>2</td>
			<td> 69.4649</td>
			<td> 6.78873 x 10^(-31) </td>
	</tr>
		<tr>
		
			<td>ARCT</td>
			<td>1</td>
			<td> 14.7559</td>
			<td> 3.90469 x 10^(-7) </td>
	</tr>
	<tr>
		
			<td>ARCT</td>
			<td>2</td>
			<td> 82.0802</td>
			<td> 2.25446 x 10^(-36) </td>
	</tr>
	
</table>

The VLT telescope would yield better results - its higher physical altitude means that light must travel through less airmass to reach the telescope, resulting in less extinction. 

***
### 2.

The table below lists the observed V-band ($\ll = 547.5\,nm$) and B-Band ($\ll =  435.3\,nm$) for some star observed over the course of the night on December 25th, 2021. The time of the observations, altitude, and azimuth of the star are given in the first 5 columns. The star has a parallax of $284.56\text{ mas}$.
![[Pasted image 20211117101741.png|Table of V-band and B-band values.]]

**a.** Plot $m_V$ and $m_B$ versus airmass. From the plot, determine the *atmospheric exctinction coefficients* for both bands, and the *true* V-band and B-band magnitudes for the star (i.e. corrected for extinction).
***

***
	
	
**b.** Spectroscopically, this star is a hot, blue star (known as a B-type star) with known, intrinsic, absolute magnitudes	of $M_{V,0} = -3.7$ and $M_{B,0} = -2.95.$ Calculate the amount of *interstellar extinction* (i.e. $A_V$ and $A_B$) in both bands. 

***

	
***
### 3.

Extreme broadband spectroscopy of a star with a measured parallax of $130.208\text{ mas}$ yields the following spectrum:

![[Pasted image 20211111122414.png|Extreme broadband spectroscopy.]]

