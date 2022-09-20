

# Homework Assignment 1
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

However, this feels slightly dubious as it is unclear whether the universe has a clearly defined boundary - is there any solid area for the protons to apply a force to? Can a gas apply pressure to itself if it's the only thing that exists?
	
***

**1.2: Partial Derivatives**

Let $x, \ y, \ z$ be thermodynamic coordinates, obeying the following equation of state $f(x,y,z)=0$ for some state function $f$.

- Show that $$\left( \pdv{x}{y} \right)_z=\frac{1}{\left(\pdv{y}{x}\right)_z}.$$
- Show that 
$$\left( \pdv{x}{y} \right)_z\left(\pdv{y}{z}\right)_x \left( \pdv{z}{x} \right)_y = -1.$$



**Solution:**

The  partial derivative on the LHS of the first equation is the partial derivative of $x$ with respect to $y$, holding $z$ constant. For some function $f = f(x,y,z)$, we can make use of the implicit function theorem. 

Consider the total differential of $f$:

$$df = f_xdx+f_ydy+f_zdz = 0 $$
...where $f_x$, $f_y$, and $f_z$ are the derivatives of $f$ with respect to $x$, $y$, and $z$, respectively. Since $dz$ is zero in this case as we're holding it constant, we have:

$$\begin{align}
f_xdx+f_ydy &= 0 \\ 

f_xdx &= -f_ydy \\ 

\pdv{x}{y} &= -\frac{f_y}{f_x}\\

\end{align}$$






The inverse also applies:

$$\pdv{y}{x} = -\frac{f_x}{f_y}$$

Since $-\frac{f_x}{f_y} = \left( \frac{f_y}{f_x} \right)^{-1}$, we have: 

$$
\begin{align}
\left( \pdv{x}{y} \right)_z &= -\frac{f_y}{f_x} \\ 

&= \frac{1}{\left(\pdv{y}{x}\right)_z}



\end{align}
$$
...after the negative signs cancel.


For the second equation, we start with 

$$f(x,y,z)=0$$

As in the previous part, we can take any one of these variables to be a function of the other two, *i.e*:

$$
f=f(x(y,z),y,z) = f(x,y(x,z),z) = f(x,y,z(x,y)).

$$

Taking the third expression, we can write the total differential $dz$ as:

$$dz = \left( \pdv{z}{x}\right)dx + \left( \pdv{z}{y}\right)dy$$

via the chain rule. For the first term, $z$ is held constant, meaning $dz=0$. Thus, we can write $y$ in terms of $x$, and by the chain rule, we have

$$
\begin{align}
dy &= \pdv{y}{x}dx
\end{align}
$$

...which, subbing this into the earlier equation, yields

$$dz = 0 = \left( \pdv{z}{x}\right)dx+\left(\pdv{z}{y} \right)\left(\pdv{y}{x}\right)dx$$

....which, rearranging, becomes:

$$
\begin{align}

-\left( \pdv{z}{x}\right)dx &= \left(\pdv{z}{y} \right)\left(\pdv{y}{x}\right)dx \\ 

\\

-\left( \pdv{z}{x}\right) &= \left(\pdv{z}{y} \right)\left(\pdv{y}{x}\right)


\end{align}
$$

The result from the first part of the question will now be quite useful, as we can replace $\left(\pdv{z}{y} \right)$ and $\left(\pdv{y}{x}\right)$ with the inverse of their reciprocals:

$$
\begin{align}
-\left( \pdv{z}{x}\right) &= \frac{1}{\left(\pdv{y}{z}\right)}\frac{1}{\left(\pdv{x}{y}\right)}

\end{align}
$$

Multiplying both sides by the two differentials in the denominator, we have:

$$-\left( \pdv{z}{x}\right)\left(\pdv{y}{z}\right)\left(\pdv{x}{y}\right) = 1$$

or:

$$\left( \pdv{z}{x}\right)\left(\pdv{y}{z}\right)\left(\pdv{x}{y}\right) = -1$$

QED.
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


**Solution:**

Recall from part two that for a function $f$ of three variables, the following identity holds:

$$\left( \pdv{z}{x}\right)\left(\pdv{y}{z}\right)\left(\pdv{x}{y}\right) = -1$$

Our state function $f$ is a function of three variables, so the same relation will hold with our thermodynamic coordinates:

$$\left( \pdv{p}{V}\right)_T\left(\pdv{T}{p}\right)_V\left(\pdv{V}{T}\right)_p = -1$$

From here, we can make some substitutions using the other identity proven in 1.2. Given that $\bb = \frac{1}{V}\left( \pdv{V}{T} \right)_p$, we can see that

$$\bb V = \left( \pdv{V}{T} \right)_p$$

so we can make the substitution 

$$\left( \pdv{p}{V}\right)_T\left(\pdv{T}{p}\right)_V(\bb V) = -1.$$
We can also make the substitution 

$$\left( \pdv{V}{p} \right)_T =-\kk_TV $$

which, after using the first identity , we can insert into the equation:


$$
\begin{align}

\left(\pdv{T}{p}\right)_V(\bb V) &= - \frac{1}{\left( 
\pdv{V}{p} \right)} \\ 

\left(\pdv{T}{p}\right)_V(\bb V) &= -  \left( \pdv{V}{p} \right)_T \\ 

\left(\pdv{T}{p}\right)_V(\bb V) &= \kk_TV


\end{align}
$$

Rearranging this equation, we can isolate that last differential:

$$\frac{\bb}{\kk_T} = \left(\pdv{p}{T}\right)_V$$

And after integrating with respect to $T$, we find


$$\frac{\bb}{\kk_T}T = p$$



or 

$$\frac{N k_B}{\kk_T p V}T - p = 0 = f(T,p,V)$$
which is the equation of state for the non-ideal gas. 

We can see in which circumstances the equation would reduce to an ideal gas by putting the equation into the form of the ideal gas law. Adding $p$ to both sides and multiplying both sides by $V$, we find


$$\frac{N k_B T}{p \kk_T} = p V$$

Therefore, the equation will reduce to the ideal gas law if and only if the denominator $p\kk_T=1$, which will occur when:


$$\frac{1}{p}=\left( 
\frac{1}{p} + \frac{a}{V} 
 + \frac{b}{pV}\right)$$


....which obviously will occur only in the case that $a=b=0.$


***

