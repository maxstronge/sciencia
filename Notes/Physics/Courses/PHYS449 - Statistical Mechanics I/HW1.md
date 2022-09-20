<<<<<<< HEAD
# PHYS449
## Homework Assignment 1
##### Max Stronge (30064749)

9/16/2022
***

**1.1: The Universe as a proton gas**

It is estimated that the universe contains a total mass of $10^{80}$ proton masses ($m_p = 1.67 × 10^{−27}kg$). Its present volume is estimated to be about $10^{80}m^3$. Its temperature is that of the cosmic background radiation, $T = 2.7K$.

1. Assume that the mass is distributed uniformly ignoring aggregation into  stars and galaxies. What is the matter density of the universe? Based on this number, what is a good model for such a proton gas?
2. What is the pressure of the proton gas?


**Solution**:

We can find the matter density of the proton-universe by dividing the total mass by the total volume, since the matter is distributed uniformly. Taking $\rho_p$ as the proton density, $n_p$ as the number of proton masses, and $m_p$ as the mass of each proton, we have:

$$\rho_p = \frac{n_pm_p}{V}$$


$$\rho_p = \frac{10^{80}(1.67 × 10^{−27}kg)}{10^{80}m^3}$$


$$\rho_p = 1.67 \times 10^{-27} \ \text{kg m}^{-3}$$

*i.e.*, the proton-universe has a matter density of one proton mass per cubic meter. 

This universe is a system with an incredibly large number of particles, far in excess of  ~$10^{23}$ , with an extremely low density. With only 1 proton per cubic meter, and the distribution equal everywhere, it is safe to ignore the interactions between them.  The large number of particles and their relative  noninteraction suggest that we can use the *ideal gas* model for this proton gas. 



To describe the pressure of this gas, we can thus use the ideal gas law:

$$
\begin{align}
pV&=Nk_BT \\

p &= \frac{N}{V}k_BT \text{ [N/m}^2] \\ 

&= \left(\frac{10^{80}}{10^{80}m^3}\right) k_BT   \\

&= 1.380649\times10^{−23}J⋅K^{−1}(2.7 \ K) \text{m}^{-3}\\ 

&= 3.72775 \times 10^{-23} Nm^{-2}


\end{align}$$

However, this is slightly suspect as it is unclear whether the universe has a clearly defined boundary - is there any 'wall' for the protons to apply a force to?
	
***

**1.2: Partial Derivatives**

Let $x, \ y, \ z$ be thermodynamic coordinates, obeying the following equation of state $f(x,y,z)=0$ for some state function $f$.

- Show that $$\left( \pdv{x}{y} \right)_z=\frac{1}{\left(\pdv{y}{x}\right)_z}.$$
- Show that 
$$\left( \pdv{x}{y} \right)_z\left(\pdv{y}{z}\right)_x \left( \pdv{z}{x} \right)_y = -1.$$



**Solution:**

For a function $f(x,y,z)$ of three variables, there are three first partial derivatives: 

$$
\begin{align}
f_x = \pdv{f}{x} \\ 

f_y = \pdv{f}{y} \\ 

f_z = \pdv{f}{z}

\end{align}
$$

In situations like this, we can say that (at least very locally) one of the three variables is defined *implicitly* as a function of the other two. 
***

**1.3: Non-ideal gas: Equation of state**

The *isothermal compressibility* is defined as $\kappa_T= - \frac{1}{V}\left(\pdv{V}{p} \right)_T$ , and the *isobaric thermal expansion* is defined as $\bb = \frac{1}{V}\left( \pdv{V}{T} \right)_p$ . For a specific (non-ideal) gas of $N$ particles, an experiment has established that the isobaric thermal expansion and the isothermal compressibility are given by:


$$
\begin{align}

\bb &= \frac{Nk_B}{pV} \\ 

\\

\kk_T &= \frac{1}{p} + \frac{a}{V} + \frac{b}{pV}

\end{align}
$$

respectively, where $a$ and $b$ are some constants. Determine the equation of state $f(T,p,V)=0$ for this gas. Discuss under which circumstances the equation of state is identical to the case of an ideal gas. 

***

