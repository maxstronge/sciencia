# The Wave Equation for an LC Transmission Line:
***
A ladder network composed of series inductances and parallel capacitances is called an ***LC* transmission line**, or delay line. One such transmission line is pictured below.

```tikz
\usepackage{circuitikz}
\begin{document}

\begin{circuitikz}[cute inductors]
\draw (0,0) to[isource, l=Oscillator (emf)] (0,3) -- (2,3)
to[C=$C$] (2,0) -- (0,0);

\draw (2,3) to[L=$L$] (4,3)
to[C=$C$] (4,0) -- (2,0);

\draw (4,3) to [L=$L$] (6,3)
to[C=$C$] (6,0) -- (4,0);

\draw (6,3) to [L=$L$] (8,3)
to[C=$C$] (8,0) -- (6,0);

\draw (8,3) to [L=$L$] (10,3)
to[C=$C$] (10,0) -- (8,0);

\end{circuitikz}


\end{document}
```

^b458ac

The distance between each leg of the ladder is $\Delta x$, and the circuit continues on to the right towards the load. This model is an excellent analogue to the distributed [[Mass-Spring System|mass-spring system studied earlier.]] It can, in fact, describe electromagnetic waves under many practical situations. 

We select one section of the transmission line located at $x$, and assign currents and voltages as in the following figure:

![[Pasted image 20221121115219.png]]

**Kirchhoff's Voltage Law** requires that the sum of voltage drops around a closed loop is equal to zero. Applying this to the circuit element above, we find:

$$V(x,t)=L \pdv{I(x,t)}{t}+ V(x+ \Delta x, t)$$ ^2f4bad

**Kirchhoff's Current Law** states that the sum of the currents that enter a node is equal to $0$ yields:

$$I(x,t)=C \pdv{V(x,t)}{t} + I(x + \Delta x, t)$$ ^3dd772

but the first term in the RHS really should be written as 

$$C \pdv{V(x+\Delta x,t)}{t}.$$

However, assuming $\Delta x$ is sufficiently small, we may use a Taylor Series expansion for $V(x+\Delta x,t)$ as 

$$V(x+ \Delta x, t) \approxeq V(x,t)+\Delta x \pdv{V(x,t)}{t}$$ ^8a7294

..and $\pdv{t}V(x+ \Delta x,t)$ can be approximated with $\pdv{t} V(x,t).$ 


The current at location $x + \Delta x$ can also be Taylor series expanded as 

$$I(x+ \Delta x,t) \approxeq I(x,t) + \Delta x \pdv{I(x,t)}{t}.$$ ^fda929

After substituting [[#^8a7294|these]] two [[#^fda929|Taylor series approximations]] into the [[The Wave Equation for an LC Transmission Line#^2f4bad|two]] [[#^3dd772|equations]] built from Kirchhoff's laws, we find:

 $$\begin{align*}
- \Delta x \pdv{V(x,t)}{t} &= L \pdv{I(x,t)}{t}.\\
\\
 
- \Delta x \pdv{I(x,t)}{t} &= C \pdv{V(x,t)}{t}.
\end{align*}$$

^717c4c

These are two coupled first-order differential equations for $V(x,t)$ and $I(x,t)$. 

Next, we differentiate [[#^717c4c|the first of these equations]]  with respect to the spatial coordinate $x$ and the [[#^717c4c|next]] with respect to time $t$, to obtain:

$$\begin{align*}
- \Delta x \pdv[2]{V(x,t)}{x} &= L \pdv{I(x,t)}{x}{t}\\
\\
- \Delta x \pdv[2]{I(x,t)}{t}{x} &= C \pdv[2]{V(x,t)}{t}
\end{align*}$$

Since, via equality of mixed partials, $$\pdv[2]{I(x,t)}{x}{t}= \pdv[2]{I(x,t)}{t}{x}$$
...this term can be eliminated, and we can obtain a PDE for the voltage $V(x,t)$:

$$\pdv[2]{V(x,t)}{t}= \frac{(\Delta x)^2}{LC}\pdv[2]{V(x,t)}{x}$$ ^da8385

A similar equation for the current $I(x,t)$ can be obtained by a similar procedure, instead differentiating the [[#^717c4c|first equation]] with respect to time $t$ and the second with respect to space $x$. This yields:

$$\pdv[2]{I(x,t)}{t} = \frac{(\Delta x)^{2}}{LC} \pdv[2]{I(x,t)}{x}$$ ^34656d

The [[#^da8385|previous]] two [[#^34656d|equations]] are of the form of a wave differential equation. The propagation velocity is immediately found to be 

$$c_{w} = \frac{\Delta x}{\sqrt{LC}}$$

or, alternately, 

$$c_{w} = \frac{1}{\sqrt{\frac{L}{\Delta x}\cdot \frac{C}{\Delta x}}}$$

But $\frac{L}{\Delta x}$ and $\frac{C}{\Delta x}$ are, respectively, the inductance and capacitance *per unit length* of the transmission line. It should be noted that both of these parameters are dependent on the materials encased within them. This implies that the numerical value for the velocity of propagation can be significantly different than the velocity of light in a vacuum. 

> The propagation velocity of voltage and current waves on this transmission line is determined by the inductance and capacitance per unit length, having units of $\text{Henry/m}$ and $\text{Farad/m}$ , respectively.

This conclusion is very general, and once we know the *inductance* and *capacitance* per unit length, the wave propagation velocity can easily be found. 

Returning to a previous step in our derivation - we assumed [[#^8a7294|here]] that we could replace a term with its Taylor series expansion if $\Delta x$ was very small. We did not specify how small. When we wrote [[#^3dd772|this equation]], we used $C[\pdv{V(x,t)}{t}]$ instead of $C[\pdv{V(x+\Delta x,t)}{t}]$. This can only be done if 

$$\abs{\Delta x \pdv{V(x,t)}{x}} \llless \abs{V(x,t)}$$
as is clear from the Taylor series expansion for $V(x+\Delta x,t)$. 

For a sinusoidal waveform with voltage $$V(x,t) = V_{0}\sin(kx-\omega t)$$
with $\frac{\omega}{k} = c_w$, we find

$$\pdv{V(x,t)}{x} = kV_{0}\cos(kx-\omega t) = \frac{2 \pi}{\ll}V_{0}\cos(kx-\omega t)$$

Therefore, $$\abs{\Delta x \left(\pdv{V(x,t)}{x}\right)}\llless \abs{V(x,t)} \implies \Delta x \frac{2 \pi}{\ll} \llless 1.$$

Roughly speaking, $\Delta x$ must be smaller than the wavelength $\lambda$. Alternately: $$\Delta x \llless \frac{\lambda}{2\pi}$$

Thus, when we have a discrete LC transmission line as shown in the [[#^b458ac|figure]], the propagation of the voltage and current signals can be described with a *dispersionless*, linear wave equation *only* if the preceding condition is satisfied. 


This limitation may seem severe, but it is not an issue in all in practical transmission lines, which are in most cases *continuous*, and $\Delta x$ can be taken as small as we would like. 

Recall that the propagation velocity was determined by the inductance and capacitance per unit length - these are *intensive quantities* rather than *extensive* ones, and so remain finite quantities no matter how small a $\Delta x$ is chosen. 

The most familiar transmission line is the one composed of just two parallel wires: 

![[Pasted image 20221121190427.png]]

Let us examine this simple system. We assume the wires are conductors of radius $a$ and the distance $d$ separating them is much larger than $a$. 

Assume the linear charge densities on the two wires are $+\rho_L$ and $-\rho_L$, respectively. These charge densities have units of Coulombs per meter. 

In the plane containing the wires, the electric field is given by 

$$\mathbf{E}_{\rho}= \frac{\rho_L}{2\pi\eo}\left(\frac{1}{\rho}+\frac{1}{d-\rho}\right)$$

where $\rho$ is the distance from the positively charged wire. 

The potential difference between the wires is then:

$$V=\int^{d-a}_{a} \mathbf{E}_{\rho}d\rho = \frac{\rho_{L}}{2\pi \eo} \int^{d-a}_{a}\left(\frac{1}{\rho}+\frac{1}{d-\rho}\right)d\rho = \frac{\rho_{L}}{2\pi \eo} \ln\left(\frac{d-a}{a}\right)$$
$$\simeq \frac{\rho_{L}}{\pi\eo}\ln\left(\frac{d}{a}\right).$$

We can find the capacitance with the relation:
$$\frac{C}{l}= \frac{\rho_{l}}{V}=\frac{\pi\eo}{\ln\left(\frac{d}{a}\right)}$$

The inductance per unit length can be found similarly. Let the wires carry currents $+I(A)$ and $-I(A)$, respectively. The magnetic field at a distance $\rho$ from the positive current, as shown in the figure below, is $$\mathbf{B} = \frac{\mu_{0}I}{2 \pi}\left(\frac{1}{\rho}+\frac{1}{d-\rho}\right)$$

![[Pasted image 20221121191649.png]]

Thus the magnetic flux corresponding to a unit length of transmission line is 

$$\frac{\Phi_{B}}{l}= \frac{\mu_{0}I}{2\pi} \int^{d-a}_{a}\left(\frac{1}{\rho}+\frac{1}{d-\rho}\right)d\rho$$


$$\simeq \frac{\mu_{0}I}{2\pi}ln\left(\frac{d}{a}\right)\text{ [W/m]}$$

And thus the inductance per unit length is $$\frac{L}{l}= \frac{\Phi_{B}}{lI}= \frac{1}{\pi}\sqrt{\frac{\mu_0}{\eo}}\ln\left(\frac{d}{a}\right).\text{ [H/m]}$$

***

### Coaxial Cable:

Another important transmission line is the **coaxial cable**, composed of two coaxial cylindrical conductors. Coaxial cables can confine electromagnetic waves between the two conducting cylinders and, under ideal conditions, the electromagnetic waves do not leak out. This is crucial for higher-frequency transmissions, as in the regular LC transmission line, there is leakage of energy.

![[Pasted image 20221122175918.png]]

Suppose we have a coaxial cable like pictured above, connected to a direct current battery at time $t=0$, at one end. The cable cannot be filled with charge instantaneously, since the electromagnetic waves should travel with a very large but finite speed. 

We assume that the space between the inner and outer conductor is filled with vacuum (or air), which has a *permittivity* $\eo$ and a *permeabilitly* $\mu_{0}$. Our purpose here is to find the propagation velocity $c$ of the charge pulse, initially pretending we do not already know the wave equation found previously. 


Let $\rho_L$ be the linear charge density in the region to the left of the pulse front. Since we have cylindrical symmetry, the radial electric field in the space between inner and outer conductors can easily be found from Gauss's Law:

![[Pasted image 20221122181050.png]]

The electric field is 

$$\mathbf{E}_{\rho}= \frac{\rho_{L}}{2\pi\eo}\frac{1}{\rho}$$ ^ae8c80

We can relate the linear charge density to the current $I$ by 

$$I=\rho_{L}c$$
where $c$ is the velocity at which the charge front is moving. Note that this has nothing to do with the velocity of the charge carriers, namely electrons in the conductors. The *perturbation in the charge density* is what propagates at the $c$ given in this equation.

We can find the azimuthal magnetic field from Ampere's Law:

$$\mathbf{B}_{\theta}=\frac{\mu_{0}I}{2 \pi\rho}=\frac{mo \rho_{L}}{2\pi\rho}c$$ ^bd6432

From [[#^bd6432|these]] [[#^ae8c80|two]] equations, we find the ratio of electric to magnetic fields is equal to

$$\frac{\mathbf{E}_\rho}{\mathbf{B}_\theta}=\frac{1}{\eo \mu_{0}c}$$

Thus, if we can find one more relationship between the electric and magnetic fields, we will be able to find the propagation velocity $c$.

With the careful application of Faraday's law, we can indeed find that
$$\mathbf{E}_{\rho}=\mathbf{B}_{\theta}\ c$$

So we find that $c^{2}= \frac{1}{\mu_{0}\eo}$, which is a familar result.  

Let us examine the energy situation here. Since we know the electric and magnetic fields as functions of the radius $\rho$, we can find the electric and magnetic energy density:

$$\text{electric energy density} = \frac{1}{2}\eo \mathbf{E}_{\rho}^{2}=\frac{\rho_{L}^2}{8 \pi^2\eo\rho^2}$$
$$\text{magnetic energy density} = \frac{1}{2 \mu_{0}} \mathbf{B}_{\theta}^{2}=\frac{\mu_{0}\rho_{L}c^2}{8\pi^2\rho^2}$$

But since $c^{2}= \frac{1}{\mu_{0}\eo}$, we find that the electric energy density is equal to the magnetic energy density, analogously to the case of mechanical waves in which the potential and kinetic energies were equal. We conclude that for nondispersive electromagnetic waves, the same amount of energy is stored in the electric and magnetic fields. 

The total energy density is:

$$W=2\times \frac{\rho_{L}^2}{8 \pi^2\eo\rho^2}=\frac{\rho_{L}^2}{4 \pi^2\eo\rho^2}\text{ [J/m$^3$]}$$ ^18a91d

Then the total energy per unit length of the coaxial cable is 

$$\int^{b}_{a}W\cdot 2\pi\rho d\rho = \frac{\rho_{L}^{2}}{2\pi\eo}\ln\left(\frac{b}{a}\right)$$

and the power is 
$$P=c\frac{\rho_{L}^{2}}{2\pi\eo}\ln\left(\frac{b}{a}\right)=\frac{V^{2}}{Z_{c}}=I^{2}Z_{c}\text{ [W]}$$

which is equal to the power supplied by the voltage source $VI$.

***


