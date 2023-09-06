# PHYS449: HW 4
### Max Stronge (3006479)
***


### **4.1: Heating and Entropy**

Estimate the change of entropy of the universe due to heat escaping from your home on a winter day.


**Solution:**

For a very rough estimate, consider the difference in natural gas usage for the average Albertan household between the months of July and December:

![[Pasted image 20221007165656.png]]

Let's make the assumption that the difference in energy consumption between July and December comes exclusively from heating during the winter, leaving us with $16.7$ GJ of energy used to heat the house over that month. Averaging over one day yields $\approx 5.39\times10^7$ J of energy used to heat the house in one day. Since heat must constantly be supplied to keep the house warm, clearly all of that heat flows out of the house into the exterior.

Let's say the average outdoor temperature is $-20\degree \ C = 253.15 \ K$, and the average indoor temperature is $20\degree \ C = 293.15 \ K$.

Then, over the course of the day, the entropy gained by the outdoors is 

$$\DD S_\text{outside}=\frac{\DD Q}{T} = \frac{5.39\times10^7}{253.15}\frac{\text{J}}{\text{K}}=2.128\times10^5 \frac{\text{J}}{\text{K}}.$$

The amount lost by the indoors is 
$$\DD S_\text{inside}=\frac{\DD Q}{T} = \frac{-5.39\times10^7}{293.15}\frac{\text{J}}{\text{K}}=-1.837\times10^5 \frac{\text{J}}{\text{K}}.$$


Thus the net change in entropy of the universe due to this interaction is

$$\DD S_\text{net} = \DD S_\text{outside}+\DD S_\text{inside}$$

>$$=2.128\times10^5 - 1.837\times10^5 = 2.90367\times10^4\frac{J}{K}.$$

***


### **4.2: Thermodynamic Entropy**
Two non-ideal gases, $A$ and $B$, whose internal energies only depend on temperature ($U=U(T)$) obey the following equations of state:

$$A: p=\aa_A\frac{NT}{V^2}$$

$$B: p=\left( \bb_B\frac{N}{V}T\right)^{1/2}$$


...where $\aa_A$ and $\bb_B$ are some constants. Determine for both gases whether a well-defined entropy exists. If not, what does that imply?


**Solution:**

For the entropy to be well-defined, the defining differential $dS=\frac{\dd Q}{T}$ must be exact. We have

$$\DD s=\frac{\dd Q}{T}=\frac{dU}{T}+\frac{pdV}{T} = \frac{c_v(T)dT}{T}+\frac{pdV}{T}$$

So for the differential to be exact we require

$$\left( \pdv{V} \right)_T\left( \frac{c_v(T)}{T}	 \right) =\left( \pdv{T}\right)_V \left(\frac{p}{T}\right)$$

and 

$$\left(\pdv{V} \right)_T\left(\frac{c_v(T)}{T} \right)=0.$$

Let us check this for each gas.  For gas $A$:

$$p=\aa_A\frac{NT}{V^2}$$

so 

$$\frac{\dd Q}{T}=\frac{c_v(T)}{T}dT+\aa_A\frac{NT}{V^2}\frac{1}{T}dT$$

and we can see that 

$$\left(\pdv{V} \right)_T\left( \frac{c_v(T)}{T}	 \right)=0=\left( \pdv{T}\right)_V\left( \frac{\aa_A N}{V^2}\right)$$

and the differential is exact $\implies$ gas $A$ has a well-defined entropy.


For gas $B$, we have $p=\left( \bb_B\frac{N}{V}T\right)^{1/2}$, and following a similar procedure:

$$\frac{\dd Q}{T}=\frac{c-V(T)}{T}dT+\frac{	\left( \bb_B\frac{N}{V}T\right)^{1/2}}{T}$$


and it can be seen right away that 

$$\left( \pdv{T}\right)_V\left( \bb_B\frac{N}{V}T\right)^{1/2}\neq 0$$


and so the differential is not exact, meaning that gas $B$ does not have a well defined thermodynamic entropy. This implies that the integral of $\frac{\dd Q}{t}$ is not independent of path, and thus the process is irreversible. 
***

### **4.3:  Entropy of Radiation**

The equation of state of radiation is $pV=U/3$. Stefan's law states that $U / V=\sigma T^4$, where $\sigma$ is the Stefan-Boltzmann constant.

1. Find the entropy of radiation $S=S(V,T)$.
2. During the Big Bang, radiation initially limited to a small region expands adiabatically and cools down. What is the relationship between the temperature $T$ and the radius of the universe? 

**Solution:**

Starting from $$dU =TdS-pdV$$


For an adiabatic expansion, $dS = 0$, so $dU=-pdV$. The radiation pressure $p$ was previously found to be $p=\frac{U}{3V}$, giving:

$$dU=-\frac{U}{3V}dV\implies \frac{dU}{U}=\frac{-dV}{3V}$$

We also have the energy density of the blackbody radiation $u=\frac{U}{V}=\sigma T^4$. So:

$$\begin{align} 
dS &= \frac{1}{T}\left( dU + pdV \right) \\ 

&= \frac{1}{T}\left(Vdu + \frac{4}{3}u dV   \right) \\ 

&= \frac{V}{T}du + \frac{4u}{3T}dV \\ 

&= d\left(\frac{4}{3}\sigma T^4 V  \right)\\

 \\ 

\therefore S &= \frac{4V}{3}\sigma T^4  .




\end{align}$$


Since $\frac{dU}{U}=\frac{-dV}{3V}$ as shown above, we see that $U$ is proportional to $V^{-1/3}$. But since $\frac{U}{V}=\sigma T^4$, we have $U/V \propto T^4$ and thus $$T^4 \propto V^\frac{-4}{3}$$

And since $V \propto r^3$, we have
$$T^4 \propto r^{-4} \implies T \propto r^{-1} \implies Tr = const.$$

***


