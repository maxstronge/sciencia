# ASPH305: Homework Assignment 3
##### Max Stronge (30064749)

***

1. The $8.2m$ VLT telescope is located on Cerro Paranal in the Atacama desert in Northern Chile, and is at an an altitude of $2635m$ above sea level. The $1.8m$ ARCT telescope (owned by the University of Calgary) is located near Priddis, AB at a physical altitude of $1300m$ above sea level. Both can operate at wavelengths from $300nm$ to $20\mu m$.

	Atmospheric extincition changes as a function of the *atmospheric presure*, which is itself a function of the physical altitude above sea level. Approximating the atmosphere using a model in which both the atmospheric density and pressure fall off exponentially with physical altitude, atmospheric extinction can be given by the equation:

# $$ k (z) = k_0\,e^{-\frac{z}{H}}$$

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

Using the plane-parallel atmosphere model, we can determine the distance $ds$ the radiation will travel through the atmosphere in terms of the *zenith angle* $z$:

$$\cos z = \frac{H}{\DD s}\implies\DD s = H \sec z = H X.$$
...where $\DD s$ is the path length, $H$ is the scale of the horizon (given in this question as $8\,km$), and $z$ is the angle between the observer's zenith and the radiative object (*i.e.* $90\degree - \text{altitude}_{\text{object}}$). $X=\sec z$ is the air mass.

If we use the values of $z$ for the first object

The atmospheric extinction coefficient $k$ changes as a function of the *physical* altitude $z$, as given above. 

We can express the opacity $\tau$ as the integral of the extinction function $k(z)$ over the line of sight (from $0 \to \DD s=HX$) as follows:

### $$\tau = \int_0^{HX}k(z)\,ds =\int_{z_i}^{HX} k_0e^{-\frac{z}{H}}\,ds = k_0 \int_0^{HX} e^{-\frac{z}{H}}$$
***

2. The table below lists the observed V-band ($\ll = 547.5\,nm$) and B-Band ($\ll =  435.3\,nm$) for some star observed over the course of the night on December 25th, 2021. The time of the observations, altitude, and azimuth of the star are given in the first 5 columns. The star has a parallax of $284.56\text{ mas}$.


	**a.** Plot $m_V$ and $m_B$ versus airmass. From the plot, determine the *atmospheric exctinction coefficients* for both bands, and the *true* V-band and B-band magnitudes for the star (i.e. corrected for exctinction).
	
	
	**b.** Spectroscopically, this star is a hot, blue star (known as a B-type star) with known, intrinsic, absolute magnitudes	of $M_{V,0} = -3.7$ and $M_{B,0} = -2.95.$ Calculate the amount of *interstellar extinction* (i.e. $A_V$ and $A_B$) in both bands. 
	
	***
	
	***
3. Extreme broadband spectroscopy of a star with a measured parallax of $130.208\text{ mas}$ yields the following spectrum:

![[Pasted image 20211111122414.png|Extreme broadband spectroscopy.]]

