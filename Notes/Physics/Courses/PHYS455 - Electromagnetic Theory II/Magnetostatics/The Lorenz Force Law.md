# The Lorenz Force Law:
***

## Magnetic Fields:

Recall the basic problem of classical electrodynamics: given a collection of charges $q_{1},q_{2},q_{3}$ , the *source* charges, and we want to calculate the resulting force exerted on some other charge $Q$, a *probe* charge. This led us to the discovery of the electric field, which formulated much of our later work. Until now, we have confined our attention almost exclusively to electrostatics (and any variation was in the context of *quasi-static* processes). The time has come to consider the forces between charges in motion.

Consider the following two setups of parallel conducting wires:

```tikz

```
[![magnetic_field_wire_force-001.png](https://tikz.net/files/magnetic_field_wire_force-001.png)](https://tikz.net/files/magnetic_field_wire_force-001.png)

[![magnetic_field_wire_force-002.png](https://tikz.net/files/magnetic_field_wire_force-002.png)](https://tikz.net/files/magnetic_field_wire_force-002.png)

It is found that if parallel wires carrying parallel currents experience an attractive force, while parallel wires with antiparallel currents experience a repulsive force. Nothing we have explored in electrostatics thus far can explain this phenomenon. It is not electrostatic in nature: this is a magnetic force.

While stationary charges produce an electric field $\mathbf{E}$ in space, a *moving* charge generates, in addition, a **magnetic field,** $\mathbf{B}$. This is what a compass measures - the direction of the local magnetic field (which, absent other influences, points towards the geographic north pole). If one uses a compass to examine a current carrying wire, however, the result is very peculiar:

![[Pasted image 20221128182534.png]]

We can relate the **magnetic force** experienced by a charge $Q$ to its velocity $\mathbf{v}$ and the **magnetic field** $\mathbf{B}$ via the **Lorenz Force law**:

$$\mathbf{F_\text{mag}} = Q(\mathbf{v}\cross \mathbf{B}).$$

In the presence of both electric *and* magnetic fields, the overall **Lorenz force** on $Q$ would be given by

$$\mathbf{F} = Q(\mathbf{E + [\mathbf{v}\cross \mathbf{B}}])$$

Our main task from now on will be to calculate the magnetic field $\mathbf{B}$, as well as continuing to find the electric field $\mathbf{E}$, which is more complicated when the charges are in motion. Before we proceed, let us consider a few examples of the Lorentz force law to become acquainted with it. 

> Example: Cyclotron motion

The archetypical motion of a charged particle in a magnetic field is circular, with the magnetic force $F_B$ providing the centripetal acceleration. Consider the figure below:

![[magnetic_field-005 2.png]]


The purple symbols represent a uniform magnetic field $\mathbf{B}$ going into the page. If the charge $Q$ in red moves counterclockwise around the circle of radius $r$ with velocity $v_0$, the magnetic force is centripetal, pointing inwards always, with constant magnitude $Qv \mathbf{B}$, just enough to sustain uniform circular motion:

$$qv \mathbf{B} = m\frac{v^{2}}{r},\qq{or} p=Q \mathbf{B} r$$ ^8fb5ea

where $m$ is the particle's mass and $p=mv$ is its momentum.

This [[#^8fb5ea|equation]] is known as the **cyclotron formula**, because it describes the motion of a particle in a cyclotron, the first of the modern particle accelerators.

