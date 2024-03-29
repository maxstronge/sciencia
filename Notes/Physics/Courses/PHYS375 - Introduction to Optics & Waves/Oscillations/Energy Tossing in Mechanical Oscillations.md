# 1.3 - Energy Tossing in Mechanical Oscillations:
***

We again consider the [[Mass-Spring System|mass-spring system]] oscillating according to:

$$x(t) = x_0\cos{\oo t}$$

As we have seen, this equation describes the case in which the mass is pulled a distance $x_0$ and then released at time $t=0$.

In this process, the spring was *elongated* a distance $x_0$, and, before releasing the mass, the spring had a stored **potential energy** given by:

$$U = \frac{1}{2} k_s x_0^2 \text{ [J]}$$ ^4beab4

Recall that the energy required to elongate the spring gradually by a length $x_0$ is $\int_0^{x_0}k_sxdx = \frac{1}{2}k_sx_0^2$. This potential energy must be supplied by an external source, in this case, the hands pulling the mass to $x_0$, and this is what provides the energy source for the oscillations.

After being released, the mass starts moving toward the negative $x$-direction and acquires a **kinetic energy**. At the same time, the spring begins losing potential energy as it returns to its equilibrium position (since $x$ is now $<x_0$). 

We expect, however, that the sum of the potential energy and kinetic energy should remain equal to the potential energy given in [[#^4beab4|this earlier equation]], since our model is an isolated system and hence total energy must be conserved (neglecting friction).

In order to see this, we calculate each form of energy at an arbitrary instant of time. The potential energy is:

$$U = \frac{1}{2}k_sx^2 = \frac{1}{2}k_sx_0^2\cos^2(\oo t)$$

The kinetic energy is:

$$T = \frac{1}{2}Mv^2$$

....where the instantaneous velocity $v$ can be found by differentiating the position:

$$v = \dv{x}{t} = -\oo x_0\sin{\oo t}$$

Therefore the kinetic energy is:

$$T = \frac{1}{2}M\oo^2x_0^2\sin^2(\oo t)$$

And thus the total energy is

$$E_\text{total} = T + U = \frac{1}{2}M\oo^2x_0^2\sin^2(\oo t) + \frac{1}{2}k_sx_0^2\cos^2(\oo t)$$

However, the frequency of oscillation $\oo$ is

$$\oo = \sqrt{\frac{k_s}{M}}$$

which, after some algebra, allows us to write the energy:


$$
\begin{align}
E_\text{total} = T + U &= \frac{1}{2}M\oo^2x_0^2\sin^2(\oo t) + \frac{1}{2}k_sx_0^2\cos^2(\oo t)\\

E_\text{total} &= \frac{1}{2}M \frac{k_s}{M} x_0^2\sin^2(\oo t) + \frac{1}{2}k_sx_0^2\cos^2(\oo t) \\

E_\text{total} &= \frac{1}{2}k_sx_0^2 \left( \cos^2 \oo t + \sin^2 \oo t \right) \\ 

E_\text{total} &= \frac{1}{2}k_s x_0^2


\end{align}
$$

This holds true at any instant, and our guess is justified. 

The energy in the mass-spring system is itself oscillating, transferring between the spring and the mass periodically.
***

