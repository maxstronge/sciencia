# Magnification, Sensitivity, and Resolution:

***
### Magnification:
![[Pasted image 20210922110903.png]]

The **magnification**, $\omega$, of a telescope is given by:

$$\omega = \frac{u'}{u} \approx \frac{f'}{f}...$$


...where we have used the equation for the **scale** of an image, $s = fu$. Here, $f$ is the focal length of the *objective* and $f'$ that of the *eyepiece*. For example, if $f=100$ *cm* and we use an eyepiece with $f' = 2$ *cm*, the magnification is 50-fold. The magnification is not an essential feature of the telescope, however, since it can be changed by simply changing the eyepiece. 

The **maximum magnification**, $\omega_{max}$, is the largest magnification that is worth using in telescopic observations. Beyond this magnification, the image becomes too blurry to be of much use to observers. Its value is obtained from the ratio of the *resolving capability of the human eye*, $e \approx 2' = 5.8 \times 10^{-4}\, rad$ , to the resolving power of the telescope, $\theta$:

$$\begin{align} \omega_{max} = \frac{e}{\theta} \approx e \frac{D}{\lambda} & = \frac{5.8 \times 10^{-4}D}{5.5 \times 10^{-7} m} \\ & \approx D /1 \,mm. \end{align} $$


If we use, for example, an objective lens with a diameter of 100 *mm*, the maximum magnification is about 100x. The human eye cannot make effective use of higher magnifications.


The **minimum magnification**, $\omega_{min}$, is the smallest magnification that is useful in visual observations. Its value is obtained from the condition that the diameter of the **exit pupil** $L$ of the telescope must be smaller than or equal to the diameter of the pupil of the human eye.

The exit pupil is the *image of the objective lens*, through which the light from the objective goes behind/through the eyepiece, as in the figure below:

![[Pasted image 20210922114241.png]]

From this figure we can obtain: 

$$L = \frac{f'}{f}D = \frac{D}{\omega}.$$

Therefore the condition $L \leq d$ requires that:

$$\omega \geq \frac{D}{d} $$

At night, the darkness shrinks the diameter of the human pupil to about $6\,mm$, and thus the minimum magnification of a $100\,mm$ telescope is about 17x. 
***
### Resolution:

A more important feature of telescopes is the **resolving power**, which depends on the aperture. The resolving power of a telescope determines, for example, the *minimum* angular separation of the components of a binary star system that can be seen as two distinct stars. 

The theoretical limit for the resolution is set by the *diffraction of light*: a telescope does not render a point image of a star, but rather a small disc, since light "bends around a corner" for all radiation. 

The theoretical resolution of a telescope is often given in the form introduced by Rayleigh:


$$\sin\theta \approx \theta = 1.22 \frac{\lambda}{D}, \, [\theta] \text{ in radians.}$$

The above relation is known as the **Rayleigh Criterion**, where $D$ is the diameter of the telescope, and $\lambda$ is the wavelength of light. Therefore the diffraction of light at high wavelengths is greater than at lower wavelengths. 

As a practical rule, we can say that two objects are observed as separate entities if the angular distance between them is:
 
$$\theta \gtrapprox \frac{\lambda}{D}, \, [\theta] \text{ in radians.}$$

This formula can be applied to optical *as well as* radio telescopes. For example, if one makes observations at a typical wavelength of visible light ($\lambda = 550$ *nm*, yellow), the resolving power of a reflector with an aperture of $1$m is about $0.2''$. 

![[Pasted image 20210922112655.png]]
