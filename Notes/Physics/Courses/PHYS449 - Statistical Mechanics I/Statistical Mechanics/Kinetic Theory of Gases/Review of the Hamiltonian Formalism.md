# Review of the Hamiltonian Formalism:
***

**NB:** see [[The Hamiltonian Formalism]] (eventually) for a more complete treatment of Hamiltonian mechanics.

**Theorem**: The system of Lagrange's Equations is equivalent to the following system of $2s$ $1$st order differential equations:

$$\dot{p_{i}} = - \pdv{H}{q_{i}}\qq{,} \dot{q_{i} } = \pdv{H}{p_{i}}\qq{,}1\leq i \leq s.$$ ^ef9f84

$2s$ equations are formed for $s$ generalized coordinates. 

The function $H=H(q_{1},...,q_{s},p_{1},...,p_{s},t) = \sum\limits_{j=1}^{s}\dot{q_{j}}p_{j}-\mathcal{L}$ is the **Hamiltonian**, a **Legendre transform** of the  **Lagrangian** with generalized momenta $p_{j}= \pdv{\mathcal{L}}{\dot{q_{j}}}$ and generalized coordinates $q_{j}$. The [[#^ef9f84|above]] equations are called **Hamilton's equations of motion.** 

It is very cumbersome to calculate the Hamiltonian from the Lagrangian every time, but luckily, in many cases (specifically, for conservative systems with time-independent holonomic constraints), the Hamiltonian equals the total mechanical energy:

$$H = E_\text{mech}=T +U$$

This is the relevant case for us in this course. 

Another important feature of the Hamiltonian is that it is constant $\iff$ it does not depend explicitly on time. We can prove this easily using the equations of motion above:


$$\begin{align*}
\dv{H}{t}&=\sum\limits_{i} \left(\pdv{H}{q_{i}}\dot{q_i}+\pdv{H}{p_i}\dot{p_{i}} \right)    + \pdv{H}{t}\\
\\
		&= \sum\limits_{i}\qty(- \dot{p_{i}}\dot{q_{i}}+\dot{q_{i}}\dot{p_{i}}) + \pdv{H}{t} \\
&= \pdv{H}{t}
\end{align*}$$

where we have proved that the total derivative of the Hamiltonian with respect to time is equal to the partial derivative w.r.t. time. 

This again is the relevant case in this course. 
***

## Examples of the Hamiltonian Formalism:

**1. Single particle in potential $\mathbf{V}=\mathbf{V}(\vec{r})$** 

Because of the potential, we can conclude this is a conservative system, and since there are no constraints whatsoever, we have for the Hamiltonian:

$$H(\vec{r},\vec{p}) = T + U = \frac{\vec{p}^2}{2m}+V(\vec{r})$$

For Hamilton's equations of motion, this gives:

$$\dot{\vec{p}}=-\pdv{H}{\vec{r}} = - \pdv{V}{\vec{r}}= \grad V \qq{,} \vec{\dot{r}} = \pdv{H}{\vec{p}}=\frac{\vec{p}}{m}$$

...which is equivalent to Newton's equations of motion $m\ddot{\vec{r}}=- \grad V$ , as expected. 


**2. One dimensional harmonic oscillator with $V(x)=\frac{1}{2}kx^{2}$** ^321b2c

Here, $k$ is the spring constant of the oscillatory system. Since the motion is one-dimensional, we use a generalized coordinate $x$ with generalized momentum $p_x$. This happens to correspond to actual momentum, but that doesn't mean anything really. 

The Hamiltonian is again the total energy:

$$H = \frac{p_{x}^{2}}{2m} + \frac{1}{2}kx^{2}=E_\text{mech}$$
Hamilton's equations of motion:

$$\dot{p_{x}} = -\pdv{H}{x}=-kx \qq{,} \dot{x}= \pdv{H}{p_{x}}=\frac{\dot{p_{x}}}{m}=-\frac{k}{m}x$$ ^6d52ee

which again coincide with Newton's equations. Since the Hamiltonian does not depend explicitly on time we can easily capture the dynamics of the system in **phase space**.

![[Pasted image 20221125181217.png]]



***

