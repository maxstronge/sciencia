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

$$B(T) = \int_0^\infty B_\nu (T) \,d\nu = \int_0^\infty \frac{\nu^3\,d\nu}{e^{h\nu/(kT)}-1} .$$

We can evaluate this with a change of variable $x = h\nu/(k\,T)$, whence $d\nu = (k\,T/h)dx:$

$$B(T) = \frac{2h}{c^2} \frac{k^4}{h^4}T^4 \int_0^\infty \frac{x^3\,dx}{e^x-1}$$

The definite integral term in the above equation evaluates simply to a real number:

$$\int_0^\infty \frac{x^3\,dx}{e^x-1} = \frac{\pi^4}{15}$$

...leaving us with: 

> $$B(T) = A T^4 $$
> ...where the constant $A$ has the value:
> $$A = \frac{2k^4}{c^2h^3}\frac{\pi^4}{15}.$$

***

Note that for small frequency or wavelength ranges it is possible to use the approximation: 

$$\int B_\nu \,d\nu \approx B_\nu \nu_0 \text{ W m$^{-2}$ sterad$^{-1}$}$$

$$\int B_\ll \,d\ll \approx B_\ll \ll_0 \text{ W m$^{-2}$ sterad$^{-1}$}$$

...instead of integrating the Planck function. 

***

**Example**: 

What is the ratio of red emission ($\ll = 6000\, \ang$) to blue emission ($\ll = 4000\,\ang$) for a $3000K$ star? For a $10,000K$ star? 

**Solution**: 

$$\begin{align} \frac{B_\ll (\text{red})}{B_\ll (\text{blue})} &= \frac{\qty(\frac{2hc^2}{\ll(r)^5})\cdot\,\frac{1}{e^{hc/\ll(r)kT}-1}}{\qty(\frac{2hc^2}{\ll(b)^5})\cdot\frac{1}{e^{hc/\ll(b)kT}-1}} \\[4ex] \frac{B_\ll (\text{red})}{B_\ll (\text{blue})} &= \frac{\ll(b)^5}{\ll(r)^5}\,\cdot\frac{e^{hc/\ll(b)kT}-1}{e^{hc/\ll(r)kT}-1} \\[4ex]\end{align}$$

Substituting our values for $\ll_r$ and $\ll_b$:

$$= \frac{\qty(4000\times 10 ^{-10})^5}{\qty(6000\times 10 ^{-10})^5}\,\frac{e^{(6.626\times 10^{-34})(c)/(4000\times10^{-10}(1.38\times10^{-23})T}-1}{e^{(6.626\times 10^{-34})(c)/(6000\times10^{-10}(1.38\times10^{-23})T}-1}$$

### $$\frac{B_\ll(\text{red})}{B_\ll(\text{blue})} = 0.1369\frac{e^{3.598\times10^4/T }-1}{e^{2.399\times10^4/T }-1}$$

Now, if we put in values of $T$ in Kelvin, we find that at $3000K$, the ratio was 3:1, whereas at $10,000K$ the ratio was 1:2 (red to blue light, respectively).

***
