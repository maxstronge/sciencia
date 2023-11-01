**Fraunhofer Diffraction** is a phenomenon in the field of optics that is a good example of the usage of Fourier transforms. The pattern of transmitted light produced by a partially opaque (or phase-changing) object upon which a coherent beam of radiation falls is called a **diffraction pattern**.

In particular, when the cross-section of the object is small compared with the distance at which light is observed, the pattern is known as a **Fraunhofer** diffraction pattern.


We consider only the case that the light is monochromatic with wavelength $\lambda$. The direction of the incident beam can then be described by the **wave vector** $\mathbf{k}$ - the magnitude of this vector is given by the **wave number** $k=\frac{2\pi}{\lambda}$ of the light. 

The essential quantity in Fraunhofer diffraction patterns is the dependence of the *observed amplitude* (and hence the intensity) on the angle $\theta$ between the **viewing direction** $\mathbf{k}'$ and the direction $\mathbf{k}$ of the incident beam. This is entirely determined by the spatial distribution of the amplitude and phase of the light at the object. The transmitted intensity in a particular direction $\mathbf{k}'$ is determined by the corresponding Fourier component of the spatial distribution.


Using Huygen's principle, we model a spherical antenna 

$$
E_{p} = A e^{i(\vec{k}-\hat{r}-\omega t)} = Ae^{i(kr-\omega t)}
$$

This is a spherical plane wave. 



...


Generalized form:


$$
f(y) = \begin{cases}
E_{0} & -a\leq y\leq a \\
0 & \text{otherwise}
\end{cases}
$$

Let's write as a Fourier transform in a variable $q$ that is *conjugate* to $y$. 


$$\tilde{f}(q)=\frac{1}{\sqrt{ 2\pi }}\int_{-\infty}^{\infty} f(q) e^{-iky\sin\theta}\, dy$$

$$
 = \frac{1}{\sqrt{ 2\pi }}\int_{-\infty}^{\infty} f(y)e^{-iqy} \, dy 
$$
where $f(q)$ is the slit function - may vary.



$$
I(\theta) = |E_{p}|^{2} = \frac{2\pi}{r_{0}^{2}}|\tilde{f}(q)|^{2}
$$

***

Consider a slit from $-a$ to $a$ with constant electric field $E_{0}$. 
$$
\tilde{f}(q=t\sin\theta )=\frac{1}{\sqrt{ 2\pi }}\int_{-\infty}^{\infty} f(y)e^{-iqy} \, dy 
$$

$$
= \frac{1}{\sqrt{ 2\pi }} \int_{-a}^{a} E_{0}e^{-iqy} \, dy 
$$

$$
= \frac{E_{0}}{\sqrt{ 2\pi }}\int_{-a}^{a} e^{-iqy} \, dy =\dots
$$




***
#fourierseries #fouriertransform #optics #wavelength #diffraction 