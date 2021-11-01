# Blackbody Radiation:
***

![[Pasted image 20211101111324.png|Max Planck]]


### Radiation of Atoms and Molecules:

Electromagnetic is emitted or absorbed when an atom or molecule moves from one *energy level* to another. If the energy of an atom decreases by an amount $\Delta E$, then the atom emits/radiates a *quantum* of electromagnetic radiation called a *photon*, whose frequency $\nu$ is given by the equation:

> ### $$\Delta E = h \nu.$$

[See earlier work on [[3.2 - The Photoelectric Effect]] for further exploration.]

Similarly, if an atom receives or absorbs a photon of a frequency $\nu$, its energy *increases* by $\Delta E = h \nu.$

***

### Blackbody Radiation:

A **blackbody** is defined as an object that does *not* reflect or scatter any radiation incident upon it, but absorbs and re-emits the radiation completely. 

Blackbodies are idealized radiators and as such cannot physically exist, but they serve as an excellent approximation for many sufficiently dense bodies. 

The radiation of a blackbody depends entirely on its temperature $T$, being perfectly independent of the body's shape or material composition. 

The *wavelength distribution* of blackbody radiation follows **Planck's Law** (which is a function of temperature only). The intensity at a frequency $\nu$ of a blackbody at temperature $T$ is given by:

>  $$B_v(T) = B(v;T) = \frac{2 h \nu^3}{c^2} \frac{1}{e^{h \nu / k T}-1}$$
>  ...where:
>  - $h = \text{ the Planck constant }= 6.63 \times 10^{-34}J\,s.$
>  - $c = \text{ the speed of light } = 299,792,458\,m/s.$
>  - $k = \text{ the Boltzmann constant } = 1.38\times10^{-23}J/K.$

^e0fd83


By definition of the intensity, the dimension of $B_v$ is $\frac{W}{m^2\,Hz\,sterad}$.
***

Blackbody radiation can be produced in a closed cavity whose walls absorb all radiation incident upon them (as well as the radiation coming from inside the cavity). The walls and the cavity are in *equilibrium*; both are at the same temperature, and the walls emit all radiation they receive $(T_{in} = T_{out})$. Since the radiation is being transformed into thermal energy (and back into radiation), it is called *thermal radiation*. 

The spectrum of a blackbody, as given by [[#^e0fd83|Planck's law]] is *continuous*. This is true if the size of the radiator is very large compared with the *dominant wavelengths*. In the case of the radiating cavity, the radiation can be considered as *standing waves* trapped in the cavity. The larger the number of different wavelengths, the shorter the wavelengths are relative to the size of the cavity. We already mentioned that the spectra of solid bodies are continuous - this is one of the reasons that blackbodies can provide good approximations for sufficiently dense objects. 

***

We can also write Planck's law as a function of *wavelength*, rather than temperature. Because frequency and wavelength are inversely related, we require that $B_\nu\,d\nu  = - B_\ll \,d\ll$. Since $\nu = \frac{c}{\ll}$, we have:

>  $$\dv{\nu}{\ll} = -\frac{c}{\ll^2},$$
>  ...therefore, 
>  $$B_\ll = -B_\nu \dv{\nu}{\ll} = B_\nu\frac{c}{\ll^2},$$
>  ...or:
>  $$B_\ll(T) = \frac{2hc^2}{\ll^5}\frac{1}{e^{hc/(\ll kT)}-1}.$$


$B_\ll$ has units $\frac{W}{m^2 \, \ll\,sterad}$.

***

### Intensity: 

The functions $B_\nu$ and $B_\ll$ are defined in such a way that the *total intensity* can be obtained the same way using either one. :


> #### $$B(T) = \int_0^\infty B_\nu\,d\nu = \int_0^\infty B_\ll\,d\ll.$$

Let us now try to find the total intensity using the first of these two integrals:

$$B(T) = \int $$