# Microstates, Macrostates, and Phase Space Density
***
Up to now, we have described the macroscopic properties of systems of matter phenomenologically, with the aid of equations of state derived empirically. For thermodynamics, it is irrelevant for this connection how a certain equation of state comes about. This is somewhat unsatisfactory (although it does contribute to the universality of thermodynamics) - many equations of state and quantities of state can be understood very well with the aid of microscopic considerations.

The macroscopic quantities of state result from taking *mean values* of the microscopic properties. For example, the pressure of a gas is due to the collisions of the molecules with a surface, whereas temperature is directly given by the mean kinetic energy of the particles. 

It is now the task of statistical mechanics to define, in an exact way, the process of taking mean values, which leads from the microscopic quantities (generalized coordinates, momenta) to the macroscopic quantities of state, connecting the atomistic, microscopic theory of matter to the macroscopic domain of thermodynamics. The key to this connection is the [[1.6 - Thermodynamic Entropy|thermodynamic entropy]], which connects a macroscopic thermodynamical quantity (entropy) to microscopic statistical physics (the number of possible **microstates**, typically denoted by $\Omega$). 

We now explore the notion of $\OO$, the number of microstates, make it more rigorous, and give a prescription on how to calculate it. It will already be possible at this point to derive equations of state for some concrete physical systems microscopically.

The essential superiority of statistical mechanics, however, will not become apparent until the modern formulation of **ensemble theory**. There, the macroscopic quantities are defined as mean values of microscopic qualities, weighted with probability densities. 


## Phase Space:

First, let us examine in detail what has to be understood for the notion of a **microstate**. For a classical system, it is sufficient to know at a time $t$ all generalized coordinates $q_{i}(t)$ and momenta $p_{i}(t)$ to uniquely fix the state of motion of the system. Thus for a mechanical system, we can interpret the *set* $(q_{i},p_{i}), i=1,...,3N$ as the microstate of this system of $N$ particles, where for simplicity we enumerate coordinates and momenta from $1$ to $3N$, as long as there are no constraints for the coordinates or momenta. 

The set $(q_i,p_i)$ can now be understood as a point in a $6N$-dimensional space, which is called the **classical *phase space***. 

Any point in this phase space uniquely and exactly corresponds to one microscopic state of motion of the *whole system*, the position and momenta of all particles. 

Analogously, one can relate to each particle a $6$-dimensional phase space. Any state of one particle corresponds to a point in this phase space - by extension, $N$ points in this space could uniquely define the state of an $N$ particle system as above. If not explicitly stated differently, however, we will typically want to understand the phase space as the high-dimensional space of the entire system.


Consider the example of the [[Review of the Hamiltonian Formalism#^6d52ee|simple harmonic oscillator]] in one dimension discussed previously. The Hamiltonian is as follows:

$$H(q,p) = \frac{p^{2}}{2m} + \frac{1}{2}kq^{2}$$
The following is a portrait of the $2$-dimensional phase space of the oscillator (one particle $\implies N=1$) , with the generalized momentum $p$ on one axis and the generalized coordinate $q$ on the other:


![[Pasted image 20221125181342.png]]

Since $H$ does not depend explicitly on time, the total energy is a conserved quantity. Because of this, the **energy hypersurface** where $H(q,p)=$ constant takes the form of the equation of an ellipse in one-particle phase space, the dimensions of which are completely determined by the value of $H=E$ (which, in this case, is determined by the mass and the spring constant). During its temporal evolution, the actual phase-space point $\qty(q(t),p(t))$ is constrained to move only along this elliptical trajectory.

We have drawn another ellipse corresponding to a higher value of $H$ for this oscillator. Each point on the ellipses corresponds to a particular concrete state, or snapshot, of the oscillator during its motion. Each point *between* the two ellipses corresponds to a particular copy of the oscillator that has an energy between $E$ and $E+\Delta E$ during some phase of its motion. This means that the *hypersurface*, the shaded region between the two ellipses, also reflects the phase space distribution of *many equal systems* at *one* moment. 

A collection of such phase-space points (systems in various configurations) which are consistent with certain macroscopic properties (in the above example, energies between $E$ and $E + \Delta E$) is called an **ensemble**. In principle, there is, of course, a continuity of phase space points (looking at the above figure, there are infinitely many possible points on each of the infinitely possible ellipses between the two shown), but as an illustration, one often selects a finite number of representative phase-space points.

***

## Higher-Dimensional Phase Space:

In analogy to the usual Cartesian three-dimensional space,  represented by $\RR^{3}$, we can also subdivide a higher-dimensional phase space into volume elements $d^{3N}qd^{3N}p$. For a $2$-dimensional phase space (one coordinate, one momenta), this is illustrated below:

![[Pasted image 20221125212834.png]]

The phase-space element $d^{3N}qd^{3N}p$, which can be of *finite size*, is called a **phase-space cell**. Hence we are able to relate volumes to certain regions of phase space (*i.e.* between the ellipses from earlier).

In general, phase-space volumes shall be abbreviated with the letter $\oo$ (not to be confused with frequencies). Consequently, the shorthand notation of a phase-space cell $d^{3N}qd^{3N}p$ is $d\oo$. For example, for the phase-space volume between the ellipses corresponding to $E$ and $E + \Delta E$, we have

$$\Delta\oo = \int_{E\leq H(q,p)\leq E+ \Delta E}dqdp=\int_{E\leq H(q,p)\leq E+ \Delta E}d\oo$$

In the same way, we can relate an area

$$\ss(E)=\int_{E=H(q,p)}d\ss$$

to the **energy hypersurface**, where $d\ss$ denotes the surface element. 

