# The Doppler Effect:
***

Up to now, we have assumed that there is no motion in the universe. This is, of course, untrue - everything in the universe is moving. When a moving object emitting radiation (of any kind) is perceived by a stationary observer, the wavelength of the observed radiation is shifted through a phenomenon known as the **Doppler Effect**. 


![[Pasted image 20211015111256.png]]

We are intuitively familiar with the Doppler effect when it comes to sound waves (eg. the engine roar of a speeding car changes pitch as it drives by), but the same effect occurs with light. 

The Doppler Effect, or Doppler shift, can be defined more precisely as *the change in **frequency** of a **wave** in relation to an **observer** who is moving relative to the wave source*. 

Depending on the direction of the relative motion, the wavelength of light can be Doppler-shifted in one of two ways:

- If the object is moving towards the observer, the perceived wavelength is smaller than the 'true' wavelength - it is shifted towards the 'blue'/ultraviolet end of the EM spectrum. We say that the wavlength is **blueshifted**. Conversely, the apparent frequency is higher than the true frequency. 
- If the object is moving away relative to the stationary observer, the wavelength of the radiation is **redshifted**, appearing to be greater than the true wavelength. The apparent frequency, therefore, is less than the true frequency. 


***

We can use the Doppler effect to calculate the velocity of any Doppler-shifted object with the following relation: 

> ### $$\qquad{Redshift} = Z = \frac{\Delta\ll}{\ll_0} $$

...where $Z$ is the observed 	**redshift**, $\Delta\ll$ is the change in wavelength (or the difference between the apparent and true wavelength), and $\ll_0$ is the true/'rest' wavelength. 

We can relate this to the velocity nonrelativistically (for speeds $v<<c$):

> # $$\frac{\Delta\ll}{\ll_0} = \frac{v}{c}.$$

The corresponding relativistic relation is:

> ### $$\frac{\ll-\ll_0}{\ll_0} =\frac{\Delta\ll}{\ll_0} = \sqrt{\frac{1+\frac{v}{c}}{1-\frac{v}{c}}}-1.$$


Obviously, the relativistic equation must be used when the velocity predicted by the classical equation exceeds the speed of light. 


***

### Example: 
Suppose you measure a spectral line in a distance star at a wavelength of $656.5\,nm$. But you *know* that is should be $656.3\,nm$ (from theory and laboratory measurements). What velocity is the star moving at with respect to you, and in which direction?

> Recall the nonrelativistically Doppler shift formula:
> $$\begin{align} \frac{\Delta\ll}{\ll_0} \approx \frac{v}{c} &\implies v = c\qty(\frac{\Delta\ll}{\ll_0}) \\[3ex] v &= 3\times10^8 \frac{0.2\,nm}{656.3\,nm} \\[2ex] v & =91,435\,m/s.\end{align}.$$
> Because the light's apparent wavelength is *longer* than the 'true' wavelength, we can conclude that the wavlength is **redshifted** $\implies$ the star is moving away from the observer.

***
**Example:**

Carbon has a strong and well-known spectral line that is emitted at 158$\mu m$. Suppose you observe it in a galaxy to at a wavelength of 1$mm$. What is the velocity of the galaxy?

**Solution:** Recall that for small velocities ($v<<c$), $Z = \frac{v}{c}$:

> $$Z = \frac{\Delta\ll}{\ll_0} = \frac{1\,mm-0.158\,mm}{0.158\,mm} = 5.329.$$
> $$\implies v = cZ = 5.329\,c$$
> Clearly, this cannot be the case - we need to use the relativistic form of the equation:
> $$\begin{align}Z &= \sqrt{\frac{1+v/c}{1-v/c}}-1 \\[2ex] Z+1 &=\sqrt{\frac{1+v/c}{1-v/c}} \\[2ex] (6.329)^2 &= \frac{1+v/c}{1-v/c} \\[2ex] (1-v/c)\,40.0576 &= 1+v/c \\[2ex] 40.0576 - \frac{40.0576\,v}{c} &= 1 + v/c \\[2ex] 40.0576 - 1 &= \frac{v+40.0576\,v}{c} \\[2ex]39.0576 &= 41.0576\frac{v}{c} \\[2ex] c\qty(\frac{39.0576}{41.0576}) &= v \\[2ex] v &= 0.951288\,c.\end{align}$$
***