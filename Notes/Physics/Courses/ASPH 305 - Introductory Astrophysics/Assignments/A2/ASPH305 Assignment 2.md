# ASPH305 - Homework Assignment 2:

Max Stronge (30064749)
*10/26/2021*

***
#####  1: The figure below shows the position of an asteroid as seen from telescope 1 (located in Calgary) and from telescope 2 (located $500km$ away from telescope 1). The observations were taken at the same time. 

![[a2picture1.png|Positions of asteroids measured by telescopes 1 and 2. ]]


##### a.)  Calculate the distance to the asteroid (in $AU$). You may ignore the curvature of the Earth and the exact latitude/longitude of each telescope. 


We can find the distance using the *parallactic angle formula*:

### $$p\,[\text{rads}] = \frac{d}{D}.$$

Rearranging:

### $$D = \frac{d}{p}. $$

The declination $\dd$  of the asteroid is the same as measured from each telescope - therefore, the *parallactic angle $p$* can be found from the difference between the measured values for *right ascension*:

### $$\begin{align} \aa_2 - \aa_1 &= 15^h\,10^m\,0.13^s - 15^h\,10^m\,0.0^s \\ &=0.13^s \\ &= 0.13^s \left(\frac{\pi}{43200}\text{ radians}\right) \\ &= 9.45387\times10^{-6}\text{ rad}.\end{align}$$

However, this is actually *twice* the parallactic angle, leaving us with:

### $$p = \frac{9.45387\times10^{-6}\text{ rad}}{2} = 4.72693\times10^{-6}\text{ rad.}$$

Now that we have the parallactic angle in radians, we need the baseline distance in units of $AU$ (recalling that the baseline is *half* the distance between the telescopes):

### $$250\,km = 1.33692\times10^{-6}\,AU. $$

We can now find the distance to the asteroid:

> ### $$D = \frac{d}{p} = \frac{1.33692\times10^{-6}\,AU}{4.72693\times10^{-6}} = 0.28283\,AU.$$

NASA identifies Potentially Hazardous Objects (PHOs) as near-Earth objects whose orbit brings them within ~0.05 $AU$ of Earth's orbit, so no cause for alarm yet. 

***
##### b.) At the time of the above observation, the asteroid is moving towards us with a velocity of $36.056\,km/s$ at an angle of $30\degree$ with respect to the line of sight (*i.e.* the vector between Earth and the asteroid). Calculate the radial and tangential velocity components (in $km/s$), and the proper motion that would be observed from Earth (in units of BOTH *"/yr* and *"/min*).

 A diagram to illustrate:
 
 ![[propermotiontangrad 1.svg|Proper motion of asteroid]]
 
 	

From the figure we can form a triangle to determine the radial and tangential components of velocity:

![[propermotiontrig_updated.svg|Trigonometric construction for determining velocity components]]

So the radial and tangential velocity components are:

> ### $$\va{v}_r = 31.2254\,km/s.$$
> ### $$\va{v}_t = 18.028\,km/s. $$

We can now find the proper motion with the following relation:

### $$\theta\text{ [rad]} = \frac{D\text{ (km)}}{r\text{ (km)}} $$

...where $\theta$ is the angle in radians through which the body moves in 1 second, $D$ is the distance in kilometers that the body moves in 1 second (tangential to the line of sight), and $r$ is the distance to the body (in km). We can now substitute our values for $D$ and $r$ (remembering to convert $AU$ to km):

 ### $$\begin{align} \theta &\text{ (rads)}= \frac{D}{r} \\[2ex] \theta &= \frac{18.028\text{ km}}{0.28283\,AU \cdot \qty(\frac{1.496 \times 10^8\text{ km}}{AU})} \\[2ex] \theta &= \frac{18.028\text{ km}}{4.23108 \times 10^7 \text{ km}} \\[2ex] \theta &= 4.26085 \times 10^{-7} \text{ rad}.\end{align} $$
 
 We want our answer in units of $"\text{/min}$ and $"\text{/yr}$, so after one final conversion:
 
 > ### $$\begin{align} \theta &= 4.26085 \times10^{-7}\text{ radians/s} \\ &=  4.26085 \times10^{-7} \frac{\text{rad}}{s}\cdot \frac{648,000}{\pi}\frac{"}{\text{rad}} \\ &= 8.78863\times10^{-2}\text{ "/s} \\[3ex] &= 5.27318 \text{ "/min} \\[3ex] &= 2.77158\times10^6 \text{ "/yr.}\end{align}$$
 
 
 
***


##### 2. The molecule CO has a fundamental quantum (rotational) transition that occurs at a rest frequency of $115.27\,GHz\,(1\,GHz = 10^9 Hz)$. Spectra of this transition were obtained at three different positions in a galaxy (see figure below) and shows that this galaxy is simultaneously rotating and moving either towards or away from us. Calculate the velocity and direction with which this galaxy is moving with respect to us (*in km/s*). In the rest frame of the galaxy, calculate its rotational velocity (*in km/s*). Which side is rotating toward us and which is rotating away?

![[Pasted image 20211026113824.png|Spectra]]

We can determine the velocity, direction, and rotation of the galaxy using the Doppler Shift formula:

### $$Z = \frac{\Delta \ll}{\ll_0} $$

...where $\Delta \ll$ is the *change in wavelength* of the shifted light, and $\ll_0$ is the '*rest*' wavelength. By converting the given frequencies into wavelengths, we can find the observed Doppler shift of each of the three observations. The rest wavelength can be obtained from the rest frequency, recalling that $c =\nu \ll$:

### $$\ll_0 = \frac{c}{\nu} = \frac{299,792,458\,m/s}{115.27\times10^9\,Hz} = 2.60078\times10^{-3}m.$$

The spectra show transition frequencies of $\nu_1,\nu_2,\nu_3 =115.04\,GHz, \,114.97\,GHZ,\text{ and } 114.92\,GHz$ (left to right). We can find the corresponding wavelengths in identical fashion:

### $$\begin{align} \ll_1 = \frac{c}{\nu_1} &= 2.60598\times10^{-3}\,m. \\[1ex] \ll_2 = \frac{c}{\nu_2} &= 2.60757\times10^{-3}\,m. \\[2ex] \ll_3 = \frac{c}{\nu_3} &= 2.60871\times10^{-3}\,m.\end{align}$$

We can see already that the wavelengths at all three locations all exceed the rest wavelength - therefore, the light from the galaxy is **redshifted** and we can conclude the galaxy is moving away from us. We can relate the Doppler shift to the velocity of the galaxy with the following (non-relativistic) relation:

### $$Z = \frac{\Delta\ll}{\ll_0} = \frac{v}{c} \implies v = cZ.$$

Since the galaxy is rotating, each side will be moving away from us at a different rate - one will move away faster than the center, and the other will move away slower than the center. If we use the wavelength from light at the *center of the galaxy* ($\ll_2$) in the above relation, it should give us the velocity of the galaxy as a whole with respect to us. The redshift at the center is:

### $$Z = \frac{\Delta \ll}{\ll_0} = \frac{(2.60757\times10^{-3} - 2.60078\times10^{-3})}{2.60078\times10^{-3}} = 0.00260938 $$

Plugging this into the velocity relation above, we find the velocity of the galaxy to be:

> ### $$\begin{align} v &= cZ \\ &=(299792458\text{m/s})\cdot (0.00260938) \\ &= 782,271\,\text{m/s} \\ &= 782.271\,\text{km/s}\qq{away from us.}\end{align}$$

The non-relativistic equation holds in this case since the velocity $v << c$. This is the **recession velocity** of the galaxy, $v_{\text{recession}}$.

Take the *rest frame of the galaxy* to be a coordinate system fixed in the center of the galaxy such that the center of the galaxy is stationary. 

We can find the redshift in this rest frame by subtracting the redshift of the center point ($Z_2$) from the redshifts of all three points, eliminating the redshift caused by the relative motion of the entire galaxy away from us. Doing this, we find the new values for $Z$ to be:

### $$\begin{align} Z_1 = \frac{\Delta \ll_1}{\ll_0}-Z_2  &= -0.000610072. \\[2ex] Z_2 &= 0 .\\[2ex] Z_3 = \frac{\Delta \ll_3}{\ll_0}-Z_2 &= 0.000436221.\end{align}$$

In the rest frame, the center of the galaxy does not experience any Doppler shift (since it is not moving relative to the frame). The left point is **blueshifted**  relative to the center - therefore, it is rotating towards us, while the right point is still redshifted, moving away from us. Therefore, the galaxy is rotating counter-clockwise relative to a vertical axis perpendicular to the disk.

The following formula relates the **rotational velocity **$v_{\text{rotation}}$ to the **recession velocity** $v_{\text{recession}}$:

> ### $$v_{\text{rotation}} = \frac{v_{LOS} - v_{\text{recession}}}{\sin (i)}$$
> where:
>-  $v_{\text{LOS}}$ is the total radial velocity relative to the observer (found via Doppler Shift)
> - $i$ is the **inclination** angle of the galaxy relative to the observer.

From the figure, we assume that the inclination angle $i$ is 90$\degree$ (viewed edge-on, like the side of a plate), so the denominator reduces to 1. We can now pick one of our points on the edge of the galaxy to find the rotational velocity. Taking the rightmost point:

### $$v_{LOS} = cZ_3 = 913047\text{ m/s.}$$

Therefore:

>### $$v_{\text{rotation}} =  v_{LOS} - v_{\text{recession}} =130,776\text{ m/s}.$$


**NB**: the rotational velocity of the galaxy is not constant - the gas on the other side of the galaxy (left), for which we measured a slightly different Doppler shift ($Z_1$),  will have a different $v_{\text{rotation}}$. To find the total angular velocity of the galaxy as a whole, more information is required (eg. distances, mass).
***

##### 3.  This question illustrates how we can use parallax and observations of the general/average properties of stars to "bootstrap" other methods, thereby determining distances to objects that are even further away. Ignore all interstellar extinction in this question. 
***

##### **a.** You observe a star and determine its parallax to be $5.37$ milliarcseconds. From photometery (measuring light intensity), you determine its apparent visual magnitude to be $m_v = +0.50$, and its apparent blue magnitude to be $m_B = +2.35$. From spectroscopy you determine that this is a *red supergiant* star. Calculate the absolute visual and blue magnitudes ($M_v$  and $M_b$) of this star. 


First, we use the measured parallactic angle to find the distance to the star. Assuming the parallax was measured with a baseline of $1\,AU$ (maximum separation in Earth's orbit), we can find the distance via the following relation:


### $$\begin{align}D \text{ (pc)}&= \frac{1}{p\text{ (")}} \\[2ex] &= \frac{1}{5.37 \times 10^{-3}} \\[2ex] &= 186.22\text{ pc}.\end{align}$$

Now that we have the distance in parsecs, we can use the *distance modulus* to relate the apparent magnitudes to the absolute magnitudes using the following relation:

### $$m- M = 5\log[D]-5$$

...where the little $m$ is the apparent magnitude, and the large $M$ is the absolute magnitude. Subsituting the given values of $m_b$ and $m_v$ into the formula, we find the absolute magnitudes to be:

> ### $$\begin{align}M_v &= m_v - 5\log[D] + 5 \\ &= 0.50 - 5\log[186.22]+ 5 \\ &= -5.85013 \\[4ex] M_b &= m_b - 5\log[D]+5 \\ &=2.35 - 5\log[186.22] + 5 \\ &= -4.00013 \end{align}$$
***
##### **b.** Assuming that *every* red supergiant star in the universe has similar properties, and therefore the same $M_v$  and $M_b$ (which happens to be a relatively good assumption), you now find another red supergiant in the Large Magellanic Cloud, a dwarf galaxy orbiting our own. For this star, you measure $m_v$ and $m_b$ to be $12.55$ and $14.40$, respectively. Calculate the distance to the LMC (*in pc*).

We have $M_v,\,M_b=-5.85013,-4.00013$ respectively. We can rearrange the previous equation:


 ### $$m- M = 5\log[D]-5$$
### $$\frac{m-M+5}{5} = \log[D]$$
 ### $$D = 10^{(1/5)(m-M+5)}$$

Substituting our values for $m_b,M_b$ into this equation, we find the distance to be:
> ### $$D_b= 10^{(1/5)(m_ b-M_b+5)} = 10^{(1/5)(14.40+4.00013 + 5)} = 47865.9\,pc.$$

Doing the same for $m_v,M_v$:

> ### $$D_v= 10^{(1/5)(m_ v-M_v+5)} = 10^{(1/5)(12.55+5.85013 + 5)} = 47865.9\,pc.$$

The results agree (as expected), so we can conclude that the distance to the LMC is $47865.9\,pc.$




***
##### **c.** The physical mechanism that produces a supernova results in every supernova having approximately the same *luminosity*. Assume you now see a supernova explosion in the LMC and measure $m_v = -0.77$. Calculate the absolute visual magnitude of this supernova (and therefore, the value of $M_v$ for every supernova in the universe).

Using the same relation as the previous question: 

>### $$\begin{align} M_v &= m_v - 5\log[D]+5 \\[2ex] &= -0.77 - 5\log[47865.9] +5 \\[2ex] &= -19.17013.	\end{align} $$

Hillebrandt, Wolfgang *et al. *found an average value of $-19.3$, so the absolute visual magnitude we found is a reasonable result. ^[Hillebrandt, W., & Niemeyer, J. C. (2000). Type Ia supernova explosion models. _Annual Review of Astronomy and Astrophysics_, _38_(1), 191-230.]
***

##### **d.** Now you observe a supernova explosion (with $m_v = 14.33$) in a distant galaxy. Calculate the distance to this galaxy (*in $Mpc$*). 

With $m_v = 14.33,\,M_v = -19.17013$ (as was found in part **c**), we can find the distance:

> ### $$\begin{align}m- M &= 5\log[D]-5 \\[2ex] \log[D] &= \frac{m_v-M_v+5}{5}  \\[2ex] D &= 10^{\frac{m_v-M_v+5}{5}} \\[2ex] &= 5.01217\times10^7\,pc \\[2ex] &= 50.12\,Mpc.\end{align} $$


***

##### **e.** The Hubble Law is a simple formula relating the redshifted velocity of a galaxy to its distance: $V\text{ (km/s)}=H_0\,D\,(Mpc)$,  originating from the fact that the universe is expanding. $H_0$ is the **Hubble Constant**, and has units of $km/s\cdot Mpc^{-1}$. In the galaxy from part **d.**, you observe a hydrogen spectrum at a wavelength of $664.9916\text{ nm}$. The rest wavelength of hydrogen is $656.000\text{ nm}.$ Calculate the value of the Hubble Constant. 


From **d**, we have distance $D = 50.12\text{ Mpc}$. We can determine the redshifted velocity $v$ with the following relation:

### $$v = cZ,\qq{where} Z=\frac{\Delta\ll}{\ll_0}.$$

The redshift $Z$ can be calculated from the two given wavlengths for the hydrogen spectra:

### $$Z =\frac{\Delta\ll}{\ll_0} = \frac{664.9916\text{ nm} - 656.000\text{ nm}}{656.000\text{ nm}}=0.0137067. $$

Since the observed wavelength is greater than the rest wavelength, the galaxy's light is redshifted, and the galaxy is moving away from us. We can now find the velocity of the galaxy:

### $$\begin{align} v &= cZ \\ &= 299,792,458\,\cdot(0.0137067) \\ &= 4.10917\times10^6\text{ m/s.}\end{align}$$

The Hubble Law takes the velocity of the galaxy in units of $km/s$, however, so converting, we find:

### $$V = 4109.17\text{ (km/s)}.$$

We can now rearrange the Hubble Law to solve for the Hubble Constant:

>### $$V \text{ (km/s)}= H_0 \,D\text{ (Mpc)}$$
>### $$\begin{align}H_0 &= \frac{V}{D}\,\frac{km}{s}\cdot Mpc^{-1} \\[2ex] &=  \frac{4109.17}{50.12}\,\frac{km}{s}\cdot Mpc^{-1} \\[2ex] &=81.9866\,km\,s^{-1}\,Mpc^{-1}. \end{align} $$

***

##### **f.**  Finally, you observe a galaxy that is too far away to see any individual stars and does not have a supernova in it. But you take a spectrum of this galaxy and find that the hydrogen spectrum (which should be at $656.00\text{ nm}$) is actually at a wavelength of $2.00\,\mu m$. Using your results from **e**, calculate the distance to this galaxy (*in $Mpc$*). 

First, we find the redshifted velocity:

### $$Z = \frac{\Delta \ll}{\ll_0} = \frac{2\mu m - 656.00nm}{656.00nm} = \frac{1344nm}{656nm} = 2.04878.$$

### $$v = cZ =2.04878\cdot c. $$

Clearly this is a problem - the velocity of the galaxy cannot exceed c. Instead, we can use the relativistic form of the equation:

### $$\frac{\ll-\ll_0}{\ll_0} =\frac{\Delta\ll}{\ll_0} = Z =\sqrt{\frac{1+\frac{v}{c}}{1-\frac{v}{c}}}-1.$$
 Plugging in our value for $Z$:
 
 ### $$\begin{align}2.04878 &= \sqrt{\frac{1+\frac{v}{c}}{1-\frac{v}{c}}}-1 \\[2ex] 3.04878 &=  \sqrt{\frac{1+\frac{v}{c}}{1-\frac{v}{c}}} \\[2ex] 9.29506 &= \frac{1+\frac{v}{c}}{1-\frac{v}{c}} \\[2ex] 9.29506\qty(1-\frac{v}{c}) &= 1+\frac{v}{c} \\[2ex] 9.29506 -\frac{9.29506 \,v}{c}  - 1 &= \frac{v}{c} \\[2ex] 9.29506  - 1 &= \frac{v}{c}\qty(1 + 9.29506 ) \\[2ex] \frac{8.29506}{\qty(10.29506)}\cdot c &= v  \\[2ex] v &= 2.41552\times10^8\,m/s \\ &= 241,552\text{ km/s}. \end{align}$$

Now that the velocity no longer exceeds $c$, we can proceed to find the distance using the Hubble Law and the calculated value for the Hubble Constant from **e**:

#### $$V \text{ (km/s)}= H_0 \,D\text{ (Mpc)} \implies D = \frac{V}{H_0}$$
> ### $$\begin{align}D &= \frac{V}{H_0} \\[2ex] &= \frac{241,552\text{ km/s}}{81.9866\,km\,s^{-1}\,Mpc^{-1}} \\[2ex] &= 2946.24\text{ Mpc}. \end{align}$$

***

##### 4. Suppose that in ASPH307 (Observational Astrophysics) you observe a cluster of 	stars that has a parallax of $0.50327$ milliarcseconds. In that cluster, there are: 1 O star, 20 B stars, 64 A stars, 192 F stars, 344 G stars, 772 K stars,  and 2052 M stars. The table below provides the observed V-band apparent magnitude for each star in the cluster by spectral type. For reference, you may assume that the Sun's absolute V-band magnitude is $M_{v,\Sun} = +4.83$ and ignore all interstellar extinction.

![[Pasted image 20211026134221.png|Observed V-Band Magnitude for a cluster of stars. ]]

##### **a.** Calculate the V-band luminosities for each type of star (*in units of $L_\Sun$*). How many times more luminous is the single O-star vs. all the other stars combined?

The following relation relates the *absolute* magnitude of two stars and their luminosities:

### $$M_2 - M_1 = 2.5\log\qty(\frac{L_1}{L_2})$$

...or, equivalently...

### $$\frac{L_1}{L_2} = 10^{\frac{M_2-M_1}{2.5}}.$$

Because we want to express the luminosity in terms of the luminosity of our Sun (units of $L_\Sun$), we can set star 2 in the above equation to be our Sun:

### $$\frac{L_1}{L_\Sun} = 10^{\frac{M_\Sun-M_1}{2.5}}.$$

Before we proceed further, we need to determine the absolute magnitudes of each type of star. To do so, we will need to know the *distance* to the star cluster, which can be determined as we did previously via parallax. Assuming again that the parallax was measured with a baseline of $1\,AU$ (maximum separation in Earth's orbit), we can find the distance via the following relation:


### $$\begin{align}D\text{ (pc)} &= \frac{1}{p\text{ (")}} \\[2ex] &= \frac{1}{0.50327\times 10^{-3}\text{ "}} \\[2ex] &= 1987\text{ pc.}\end{align} $$

With the distance determined, we can use the apparent magnitudes given in the table to determine the absolute magnitudes as we did above:
# $$M_v = m_v - 5\log[D]+5$$

In order: 


 $$\text{O Star: }M_{v,O} = 6.991 - 5\log[1987]+5 = -4.49999. $$
 
  $$\text{B Star: }M_{v,B} = 11.091 - 5\log[1987]+5 = -0.39989. $$
  
  $$\text{A Star: }M_{v,A} = 13.491 - 5\log[1987]+5 = 2.00001. $$
   
 $$\text{F Star: }M_{v,F} = 15.191 - 5\log[1987]+5 = 3.70001. $$
  
 $$\text{G Star: }M_{v,G} = 16.691- 5\log[1987]+5 = 5.20001. $$
  
 $$\text{K Star: }M_{v,K} = 18.891- 5\log[1987]+5 = 7.40001. $$
 
$$\text{M Star: }M_{v,M} = 23.791- 5\log[1987]+5 = 12.3. $$ 

Finally, we can use the relation found above to determine the luminosities of each star type (in units of $L_\Sun$). Noting that $M_{v,\Sun}=+4.83$, we find:

>### $$\begin{align} \frac{L_O}{L_\Sun} = 10^{\frac{M_{v,\Sun} - M_{v,O}}{2.5}}	= 10^{\frac{4.83 -+4.49999}{2.5}} &= 5395.06\,L_\Sun.\end{align}$$

Identical calculations yield the rest of the luminosities:

>### $$\begin{align}  \frac{L_B}{L_\Sun} &= 123.582\,L_\Sun. \\[2ex]  \frac{L_A}{L_\Sun} &= 13.5518\,L_\Sun. \\[2ex]  \frac{L_F}{L_\Sun} &= 2.83137\,L_\Sun. \\[2ex]  \frac{L_G}{L_\Sun} &= 0.711207\,L_\Sun. \\[2ex]  \frac{L_K}{L_\Sun} &= 0.093753 L_\Sun. \\[2ex]  \frac{L_M}{L_\Sun} &= 0.00102802\, L_\Sun.\end{align}$$

The sum of the luminosities of all star types except O stars is $140.771\,L_\Sun$ - therefore, the O star is:

> ### $$\frac{L_O}{L_{\text{sum}}} = \frac{5395.06}{140.771} = 38.325\text{ times as luminous.}$$

***

##### **b**: Calculate the absolute and apparent V-band magnitudes of the ENTIRE cluster. 

Since magnitudes cannot be directly added together, we can find the total luminosity of the entire cluster by adding together the luminosities for different types of stars:

### $$\begin{align}L_{\text{total}} &= 1(L_O) + 20(L_B) + 64(L_A) + 192(L_F)+344(L_G)+772(L_K)+2052(L_M). \\[2ex] &= 9596.78\,L_\Sun.\end{align} $$

Recalling our previous expression relating absolute magnitude to luminosity, we find:

### $$M_\Sun - M_v = 2.5\log\qty(\frac{L}{L_\Sun}) \implies M_v = M_\Sun - 2.5 \log\qty(\frac{L}{L_\Sun})$$

>### $$M_v = 4.83 - 2.5\log\qty(9596.78 ) = -5.12531.$$

Finally, we can now relate this back to the apparent magnitude $m_v$ since we already know the distance:


> ### $$\begin{align} m- M = 5\log[D]-5 &\implies m_v = M_v + 5\log[D] - 5 \\[2ex] m_v &= -5.12531 + 5\log[1987] - 5 \\[2ex] &= 6.36568.\end{align}$$
 
 The magnitude of the entire star cluster is only slightly greater than the magnitude of the O star. Indeed, the O star contributes $\approx 97.74$% of the overall luminosity. 
