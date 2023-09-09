# Linear Isotropic Dielectrics:
***

What gives rise to polarization? In general, a material polarizes when placed in an applied electric field, and that polarization is understood as a *response* to the material. 

We now introduce a *constitutive equation* which is not fundamental, but is an excellent model. Note that the $\vec{E}$ that follows is not the applied external field, but rather is a self-consistent empirical relationship between the electric field of the material and the polarization of the material. In what we refer to as **linear isotropic dielectrics**, the relationship between $\vec{E}$ and $\vec{P}$ is linear, and hence **isotropic**, and is given by:


$$\vec{P}= \eo \chi_{e}\vec{E}$$

where $\chi_e$ is a quantity called the **electric susceptibility** of the material. If $\chi_e$ does not depend on position, then we refer to the dielectric as linear, isotropic, and **homogenous**. 

For example - imagine we have a point charge $q$ at the origin, and all of space is filled with an L.I.H. dielectric with electric susceptibility $\chi_e$. What is the electric field? We can't just use Coulomb's law - we do not actually know the charge distribution, since $q$ will generate an electric field that induces some polarization (and thus some bound volume charge) in the dielectric.

The charge $q$, though fixed, is not part of the dielectric and so is still free charge. We can therefore use Gauss's law in the form $\divergence \vec{D}= \rho_f$ , where we have explicitly subscripted the charge density to indicate the *free* charge density. We can take advantage of the obvious spherical symmetry in this case. 

Consequently, since we have L.I.H., each field will be radial, and the electric field, polarization, and displacement will all be parallel.

From Gauss's Law, we have 

$$\Phi_{D}= Q_\text{free enclosed}$$

where $\Phi_D$ is the flux of displacement out of a closed surface, and $Q_\text{free enclosed}$ is the free charge enclosed by that surface. Making use of spherical symmetry, we use a Gaussian surface that is a spherical shell centered on the origin (size doesn't matter), leaving us with 

$$4 \pi r^{2}D_r=q$$

or...

$$\vec{D}= \frac{q\hat{r}}{4 \pi r^{2}}$$
However, since

$$\vec{D}=\eo \vec{E} + \vec{P}$$

and in this dielectric
$$\vec{P}=\eo \chi_{e}\vec{E}$$

we end up with $$\vec{D}=\eo(1+\chi_{e)}\vec{E}$$

and therefore

$$\eo(1+\chi_{e)}\vec{E}=\frac{q\hat{r}}{4 \pi r^{2}}$$


and we can see that the field in this situation is 

$$\vec{E}=\frac{1}{1+\chi_e}\frac{q\hat{r}}{4\pi \eo r^2}$$


And the field is smaller than it would be absent of the dielectric by a factor of $\frac{1}{1+\chi_e}$. 

***

Consider another example of a parallel-plate capacitor with separation $d$ and area $A$. If we know the gap is a vacuum, the capacitance will be given by

$$C=\frac{A\eo}{d}$$

Imagine we have charge $\pm Q$ to the positive and negative plates, respectively. This charge added to the plates is free charge. What if the gap is filled with an L.I.H. dielectric with electric susceptibility $\chi_e$?

Using Gauss's law,