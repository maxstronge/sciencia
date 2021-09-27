# Radio Telescopes and Interferometers:
***
![[Pasted image 20210927112247.png]]

***
### Radio Telescopes:

Radio telescopes tend to be very large (significantly larger than any optical telescopes) because:

- Signals going into radio telescopes are very weak
- Wavelengths are very large

Because the wavelength $\lambda$ is very large, $\implies$ energy $hv$ is small, which is why they need to be so large to detect signals - they need a large *aperture* (diameter of the reflecting mirror $D$). Unlike an optical reflecting telescope, radio telescopes do not require actual mirrors - for radio waves, the opaque surface of a radio dish acts as a near-perfect mirror. The resolution can be given by:

$$\text{Resolution}\,\theta = 2.516\times10^5 \frac{\lambda}{D}$$

Therefore, to achieve a given resolution if $\lambda$ increases, $D$ must also increase. 

Because we're working with long wavelengths, we can make these telescopes quite large because the **surface accuracy** needed is quite low compared to optical light. 

***

### Limits to Telescope Aperture Size:


$$\theta('') = 2.516\times10^5 \frac{\lambda}{D}$$

- For a given $\lambda$, the resolution $\theta$ will improve (smaller $\theta$) as $D$ increases, as mentioned above. 
- So, as $\lambda$ increases, telescopes must become bigger and bigger to achieve good resolution - to get the same resolution as a good optical telescope ($\theta = 0.1''$), the diameter of a radio telescope would need to be 25*km* - not feasible.

How can we resolve this? 

***

### Interferometers:

Interferometers consist of a collection of distinct radio telescopes that all observe the same area of the sky. The incoming radiation produces an **interference pattern** (hence the name). These interferometers can achieve much higher resolution with several cheaper telescopes than that of one massive telescope. 

The defining characteristic of an interferometer is the **Baseline**, $B$, which is the distance between the two furthest telescopes in the interferometer. The larger the baseline, the greater the resolution - this comes with a trade-off, however, of less light-collecting area. 

This can be ameliorated by adding more telescopes within the baseline - this dramatically increases the light-collecting area, creating a *"synthetic aperture"*. A single monolithic telescope with a diameter equal to the baseline would still have greater sensitivity - but the *resolution* of an interferometer of baseline $B=B\,\text{ meters}$ is the **same** as a monolithic telescope with a diameter of $B\,\text{meters}$, and is much more manageable to construct and maintain. 
