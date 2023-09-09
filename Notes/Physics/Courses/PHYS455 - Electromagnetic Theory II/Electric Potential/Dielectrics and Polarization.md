# Dielectrics and Polarization
***
For the most part, matter can be divided into two categories: [[Conductors]], and insulators, or **dielectrics.** A dielectric can be reasonably defined as an insulator, a material through which current cannot flow. 

If an electric field is applied to a dielectric, we do not find a mobile sea of charge, as we do in conductors - instead, there is a shift of charges associated with each atom/molecule comprising the material. The charge is not free to move, like conduction electrons - they are bound to the dielectric, and so we call this **bound charge**.

The application of an electric field induces a **dipole moment** $\vec{p}$ associated with a volume element $d\tau$. We can visualize this as the vector sum of all the atomic-level dipole moments within that volume element:

![[Pasted image 20221116113211.png]]

We want $d\tau$ to be of variable size, so we want to define in terms of *intensive* rather than *extensive* parameters. We define the **Polarization** to be the dipole moment per unit volume:

>$$\vec{P} = \lim_{d\tau\to \infty}\frac{\vec{p}}{d\tau}$$


We reiterate that $\vec{P}$ is the **polarization** which is dipole moment per unit volume: lower case $\vec{p}$ is the dipole moment itself, the vector sum mentioned above. 


In a dielectric, then, the total volume charge density $\rho$ that we would use in Gauss's Law is the sum of the bound and free charges:

> $$\rho = \rho_{f}+ \rho_{b}$$

^6ba499

How does bound charge arise? Consider first a polarized dielectric with *uniform polarization*. 

![[images 1.png]]

If each atomic dipole is identical to the others, they are all similarly aligned and the density of atomic dipoles is uniform (i.e. $\vec{P}$ is uniform in that region). If we examine all the charges in a small volume, the positive and negative charge will be exactly balanced - so in a region where the polarization is uniform, **the volume bound charge density will be zero.** In order for there to be nonzero bound volume charge, there must be some variation in the polarization. 

Note that a dipole moment can be expressed as the sum of three linearly independent components:

>$$\vec{p}=p_{x}\hat{x}+p_{y}\hat{y} + p_{z}\hat{z}$$

If this is the dipole moment of a volume element $\Delta V$ of a polarized dielectric, then each of these components can be expressed as follows:

>$$p_{x}= P_{x}\Delta V,\qq{} p_{y} = P_{y}\Delta V,\qq{} p_z=P_{z}\Delta V $$

We've seen that if $P_{x}$ is varying in the $x$-direction, then there is a bound charge density that results from that variation. If there is a variation of $p_{x}$ in the $y$ or $z$ direction, however, that does *not* result in bound charge. We can understand the bound charge by ONLY examining the quantity $\pdv{P_{x}}{x}$ , the polarization aligned with a variation in dipole moment. 

Let's examine the bound volume charge density that results from this situation. Consider each elementary electric dipole to consist of a positive and negative charge $\pm q$ separated in $x$ by a distance $d$. In this case, the dipole moment is $p_{\text{atomic}} = qd$, so $q=\frac{p_\text{atomic}}{d}$ and $-q=\frac{-p_{\text{atomic}}}{d}$. 

More importantly, if we are looking at a small volume of polarized material $\delta V$, then the positive charge $Q$ associated with all the atomic dipoles that are in the volume element is given by 

$$Q = \frac{p}{d} =  \frac{\sum p_\text{atomic}}{d}=P_x \frac{\delta V}{d}$$
From some more manipulation, we can find that the total bound charge in a volume is given by 

$$Q_{b}= -\Delta V \left(\pdv{P_x}{x}+\pdv{P_y}{y}+\pdv{P_z}{z}\right)$$

...and thus the bound volume charge density $\rho_{b} = \frac{Q_{b}}{\Delta V}$ is given by 

$$\rho_{b}= -\grad\cdot\vec{P}$$

....the bound charge density in a polarized dielectric is the **negative divergence of the polarization**. 

