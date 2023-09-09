# PHYS449 Assignment 9:
### Max Stronge (30064749)
***

1. **Vibrational Dynamics:**

Consider a system of $N$ distinguishable one-dimensional harmonic oscillators of mass $m$ and frequency $\oo$ with a Hamiltonian given by
$$H(\vec{q}, \vec{p}) = \sum\limits_{i=1}^{N} \qty(\frac{p_{i}^{2}}{2m} + \frac{1}{2}m\oo^{2}q_{i}^{2})$$

- Calculate the partition function $Z(T,V,N)$.
- Calculate the Helmholtz free energy $F(T,V,N)$.
- Calculate the pressure.
- Calculate the chemical potential.
- Calculate the entropy.
- Calculate the internal energy $U$. 


**Solutions:**

Assuming an isolated system, the Hamiltonian given above is equal to the total energy of the system:

$$E_{i}= H(\vec{q_{i}},\vec{p_{i}}) = \sum\limits_{i=1}^{N} \qty(\frac{p_{i}^{2}}{2m} + \frac{1}{2}m\oo^{2}q_{i}^{2})$$
where $p_{i}$ and $q_{i}$ are the generalized momenta and displacement from equilibrium, respectively, of oscillator $i$. 

The phase space is of dimension $2N$.

**a)**

The canonical partition function is defined as 

$$Z=\sum\limits_{i}\exp \qty(\bb E_{i})=\sum\limits_{i}\exp \qty(-\beta \ H(\vec{q_{i}},\vec{p_{i}}))$$

where $\beta= \frac{1}{k_\text{B}T}$. For one classical one-dimensional oscillator, the partition function becomes 

$$Z_{1}= \int_{-\infty}^{\infty}\exp \qty(-\bb \qty(\frac{\vec{p}^{2}}{2m} + \frac{1}{2}m\oo^2\vec{q}^{2}))dxdp$$


The integrations over the Gaussian functions separable (because they're exponential) and will have the form 

$$\int^{\infty}_{- \infty} e^{-ax^{2}}dx = \sqrt{\frac{\pi}{a}}$$


So we are left with 
$$Z_{1}=  \qty(\frac{2 \pi m}{\beta})^{\frac{1}{2}}\qty(\frac{2 \pi}{\beta m \oo^{2}})^{\frac{1}{2}} = \frac{2 \pi k_\text{B} T}{\oo}$$
Since the particles are identifiable and distinguishable:

$$Z=\prod Z_{i}= Z_{1}^{N}$$

and we have
$$Z= \qty(\frac{2 \pi k_\text{B} T}{\oo})^{N}.$$
**b)** With the partition function found, we can easily write the Helmholtz free energy:

$$F=-k_\text{B}T\ln Z = -k_{\text{B}} T \ln \qty[\qty(\frac{2 \pi k_\text{B}T}{\oo})^{N}]$$
$$= -k_\text{B}TN\ln \qty(\frac{2 \pi k_{\text{B}}T}{\oo})= k_{\text{B}}TN \ln \qty(\frac{\oo}{2 \pi k_{\text{B}}T})$$
From which we can calculate the other thermodynamic properties of interest. 

**c)** The pressure can be found from the relation 

$$P(T,V,N)= \left (\pdv{F}{V} \right)_{T,N}$$

and since the Helmholtz free energy is completely independent of volume, the pressure of this system is zero. 

**d)** 

The chemical potential can be found with a similar relation:

$$\mu = \left (\pdv{F}{N} \right)_{T,V}= -k_{\text{B}}T \ln\left(\frac{2 k_\text{B}\pi T}{\oo}\right)$$

**e)** Similarly, for the entropy:

$$S = \left (\pdv{F}{T} \right)_{V,N} = -k_\text{B}N\left(1+\ln \left(\frac{2 \pi k_{\text{B}}T}{\oo}\right)\right)$$


**f)** Finally, we can examine the total internal energy by noting the the definition of the Helmholtz free energy:


$$F = U - TS \implies U = F + TS$$

$$\begin{align*}
U &= F + TS 
\\
&= -k_\text{B}TN\ln \qty(\frac{2 \pi k_{\text{B}}T}{\oo})+ T(-k_\text{B}N\left(1+\ln \left(\frac{2 \pi k_{\text{B}}T}{\oo}\right)\right))\\
\\
&= -k_\text{B} N T \left(2 \log
   \left(\frac{2 \pi  k_\text{B}
   T}{\omega }\right)+1\right).
\end{align*}$$



***

2. **Ideal gas of molecules:**

$N$ diatomic molecules are confined to a volume $V$ at a temperature $T$. Neglecting interactions between molecules, the Hamiltonian for each molecule is 

$$H_{0}(\vec{p_{1}},\vec{p_{2}}; \vec{r_{1}}, \vec{r_{2}}) = \frac{1}{2m} \qty(\vec{p_{1}}^{2}+\vec{p_{2}}^{2})+ \frac{1}{2}\aa |\vec{r_{1}}-\vec{r_{2}}|^{2}$$

...where $m$ is the mass of an atom and $\aa$ is some positive constant. Compute the following quantities:

1. The partition function $Z(T,V,N)=\frac{1}{h^{6N}(2N!)}\int d\Gamma e^{-\beta H_{N}}$ (please note that the specific prefactor in this expression will be discussed in class on Thursday)  
2. The equation of state $f(p,T,V,N)=0$
3. The heat capacity $C_{V}$
4. The average quadratic diameter of a molecule $\langle{\vec{r}^{2}}\rangle= \langle{|\vec{r_{1}}-\vec{r_{2}}|^{2}}\rangle$ 

**Solutions:**

The molecules of a gas are indistinguishable, in contrast to the molecules of a crystal lattice. Recall that the phase space volume for a system of indistinguishable particles takes the form 

$$d \Gamma_{N}= \frac{1}{h^{3N}N!}\prod_{i=1}^{N}d^3\vec{q_{i}}d^3\vec{p_{i}}$$

For a diatomic gas, however, this must be modified, since diatomic molecules have additional degrees of freedom - the three translational ones they share with a monatomic gas, plus an additional two rotational degrees of freedom plus one vibration degree of freedom per molecule. This amounts to $6N$ degrees of freedom for the system instead of $3N$ - hence the alterations in the prefactor of the partition function in the question). 

The partition function is then

$$Z = \frac{1}{h^{6N}(2N!)}\int^{\infty}_{-\infty}\exp \qty(-\beta H)d \vec{p_{1}} d \vec{p_{2}} d \vec{r_{1}}d \vec{r_{2}}$$
$$= \frac{1}{h^{6N}(2N!)}\int^{\infty}_{-\infty}\exp \qty(\frac{-1}{k_\text{B}T} \qty(\frac{1}{2m} \qty(\vec{p_{1}}^{2}+\vec{p_{2}}^{2})+ \frac{1}{2}\aa |\vec{r_{1}}-\vec{r_{2}}|^{2}))d \vec{p_{1}} d \vec{p_{2}} d \vec{r_{1}}d \vec{r_{2}}$$

$$= \frac{1}{h^{6N}(2N!)}\left(\frac{\exp \qty(\frac{-\beta}{2m}(\vec{p_{2}}^{2}+\aa m |\vec{r_{1}}- \vec{r_{2}}|) )\sqrt{2 \pi}}{\sqrt{\frac{\beta}{m}}}\right)\left(\frac{\exp \qty(\frac{-\beta}{2m}(\vec{p_{1}}^{2}+\aa m |\vec{r_{1}}- \vec{r_{2}}|) )\sqrt{2 \pi}}{\sqrt{\frac{\beta}{m}}}\right)\qty(  \frac{-2 \exp \qty(-\frac{\beta}{2m} \qty(\vec{p_{1}}^{2}+\vec{p_{2}}^{2}+\alpha m |\vec{r_{1}}- \vec{r_{2}}|))k_{\text{B}}T}{\alpha}  )\qty(  \frac{2 \exp \qty(-\frac{\beta}{2m} \qty(\vec{p_{1}}^{2}+\vec{p_{2}}^{2}+\alpha m |\vec{r_{1}}- \vec{r_{2}}|))k_{\text{B}}T}{\alpha}  )$$
$$=\frac{1}{h^{6N}(2N!)} \qty(-\frac{8 \pi  k_{\text{B}}^{3} m T^3 \exp \left(-\alpha \beta \qty(| \vec{r_{1}} - \vec{r_{2}}| +  \qty(\vec{r_{1}}-\vec{r_{2}}))   + \frac{3}{2m} \qty( \vec{p_{1}}^{2}+\vec{p_{2}}^{2})
   \right)}{\alpha^{2}})$$
$$= \qty(-\frac{8 \pi  k_{\text{B}}^{3} m T^3 \exp \left(-\alpha \beta \qty(2| \vec{r_{1}} - \vec{r_{2}}| ))   + \frac{3}{2m} \qty( \vec{p_{1}}^{2}+\vec{p_{2}}^{2})
   \right)}{h^{6N}(2N!)\alpha^{2}})$$


**b)** We can then find the Helmholtz free energy as 

$$F=-k_{\text{B}}T \ln Z = -k_{\text{B}}T \left(-\alpha \beta \qty(2| \vec{r_{1}} - \vec{r_{2}}| ))   + \frac{3}{2m} \qty( \vec{p_{1}}^{2}+\vec{p_{2}}^{2})
   \right)\ln\qty(\frac{8 \pi  k_{\text{B}}^{3} m T^3}{h^{6N}(2N!)\alpha^{2}}) $$

