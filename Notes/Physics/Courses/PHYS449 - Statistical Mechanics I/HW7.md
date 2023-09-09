# PHYS449 - Homework Assignment 7
## Max Stronge (30064749)
***

**1. Shannon Entropy**:

Consider a coin toss for which $P_{h}=\frac{1}{4}$ and $P_{t}= \frac{3}{4}$. Calculate the Shannon entropy. For a different coin, we have $P_{h}= \frac{1}{5}$ and $P_{t}= \frac{4}{5}$. Compare the Shannon entropy of this case to the former. If they are different, explain why the lack of knowledge is higher in one of these cases. 

**Solution:**

The Shannon entropy $S$ for a probability distribution of a random variable is defined as $$S=-\sum\limits_{i=1}^{M} P_{i}\ln P_{i}= -\left<{\ln P}\right> \propto \frac{\log_{2g}}{N} $$
For the first toss, we have $P_{h}= \frac{1}{4}$ and $P_{t}= \frac{3}{4}$. So we will have for the Shannon entropy:

$$\begin{align*}
S&=-\sum\limits_{x \in [h,t]}P(x)\log_{2}P(x)\\
&= -(P_h\log_{2}P_{h}+ P_t\log_{2}P_t)\\
&= -\left(\frac{1}{4}\left(\log_{2}\frac{1}{4}\right)+ \frac{3}{4}(\log_{2} \frac{3}{4}) \right)\\
&= - (-\frac{1}{2}-0.311278)\\
&=0.811278. 

\end{align*}$$
Following an identical process for the second coin:

$$\begin{align*}
S&=-\sum\limits_{x \in [h,t]}P(x)\log_{2}P(x)\\
&= -(P_h\log_{2}P_{h}+ P_t\log_{2}P_t)\\
&= -\left(\frac{1}{5}\left(\log_{2}\frac{1}{5}\right)+ \frac{4}{5}(\log_{2} \frac{4}{5}) \right)\\
&= - (-0.464386-0.257542)\\
&=0.721928. 

\end{align*}$$
The two quantities are indeed different - there is a greater uncertainty/lack of knowledge in the first coin. This seems reasonable - the probability distribution of the second coin is obviously not the same, as it has a higher likelihood of coming up tails than then first coin does. For a coin that never changes state, the information content would be 1, as the probability distribution would be sufficient to determine the state of the system exactly. For a completely  uniform distribution, *i.e.* $P_{h,t}= \frac{1}{2}$, the probability distribution would reveal no information whatsoever, as the result is truly random, giving $I=0$. Both of the coins fall in-between these two cases, and thus it can be seen that the second probability distribution contains more information content than the first, resulting in the second coin having a lower Shannon entropy. 

***


**2. Maximum Entropy Principle:**

A die is loaded such that $6$ occurs twice as often as $1$. Using the maximum entropy principle, calculate the unbiased probabilities for the six faces of the die.

**Solution**:

We are given some information about the probabilities of the die:

$$P_{1}= \frac{P_{6}}{2}$$

We must also have the normalization condition that $\sum\limits_{i}P_i=1$ , so we can introduce constraints on the other probabilities:

$$\frac{3}{2}P_{6}+ P_{5}+ P_{4}+ P_{3}+ P_{2}= 1$$

Since the only information we are given is that the die is loaded s.t. 6 is twice as likely as one, we assume that the probability for the rest of the results is identical:

$$P_2=P_3=P_4=P_5$$
If we call this probability $P_o$ ('o' for 'other' than 6 or 1), we have

$$P_{o}= \frac{1 -  \frac{3}{2}P_6}{4}$$
from normalization, meaning we can reduce the probabilities to a single variable, $P_6$:

$$\begin{align*}
P_{1}&= \frac{1}{2}P_{6}\\
P_{2}&= \frac{1 -  \frac{3}{2}P_6}{4}\\
P_{3}&= \frac{1 -  \frac{3}{2}P_6}{4}\\
P_{4}&= \frac{1 -  \frac{3}{2}P_6}{4}\\
P_{5}&= \frac{1 -  \frac{3}{2}P_6}{4}\\
P_{6}&= P_6
\end{align*}$$
And thus we can write the Shannon entropy as a function of the 1 variable, $P_6$:

$$\begin{align*}
\frac{1}{2} \left(-3 P_6 \log (P_6)+P_6 \log (2)-2 \left(1-\frac{3
   P_6}{2}\right) \log \left(\frac{1}{4} \left(1-\frac{3
   P_6}{2}\right)\right)\right)
\end{align*}$$

This is the function we now want to maximize to find the probability distribution corresponding to maximum entropy. Because we have reduced our function to a single variable, we can optimize in the traditional way by finding the zeros of the derivative of the function. The derivative is

$$\dv{S}{P_6}-\frac{9 P_6}{4 \left(1-\frac{3 P_6}{2}\right)}+\frac{3}{2
   \left(1-\frac{3 P_6}{2}\right)}+\frac{3}{2} \ln \left(\frac{1}{4}
   \left(1-\frac{3 P_6}{2}\right)\right)-\frac{3 \ln
   (P_6)}{2}-\frac{3}{2}+\frac{\ln (2)}{2}$$
Which happily simplifies to $$\dv{S}{P_{6}}= \frac{1}{2} (3 \ln (2-3 P_6)-3 \ln (P_6)-2 \ln (16))$$
The roots of the above were found numerically using Mathematica:

![[Pasted image 20221113155701.png]]

Yielding a value for the probability of rolling a $6$:

$$P_{6}= \frac{2}{2+4(2^{\frac{2}{3})}}= 0.213913$$

From which we can recover all the other probabilities by their relations above:

$$\begin{align*}
P_{1}= \frac{P_{6}}{2}&= 0.106956\\
P_{2,3,4,5}= P_{o}= \frac{1 -  \frac{3}{2}P_6}{4}&=0.169783\\
P_{6}&= 0.213913
\end{align*}$$
Summing these probabilities yields a normalized result of $1$, as expected, confirming our results. 

***

**3. Hamiltonian Dynamics:**

For a simple planar pendulum on Earth in the absence of friction and drag, choose a suitable coordinate system and derive the Hamiltonian and obtain Hamilton's equations of motion. Sketch the corresponding motion in phase space and discuss.

**Solution:**

A simple planar pendulum is pictured in the figure below:

![[Simple_gravity_pendulum.svg.png]]


Let the mass of the pendulum bob be $m$, the length of the rod/string be $L$, and $\theta$ be the noted angle between the rod and its equilibrium position. Working in a Cartesian coordinate system, let the top end of the rod be affixed to the origin, such that the rod may swing in the $xy$-plane without friction or drag. The bob will experience both horizontal and vertical motion, but this motion is subject to the constraint that $\sqrt{x^{2}+ y^{2}}=L$. Because of this constraint equation, only one of the coordinates is independent, as given $x$, $y$ can always be found from the constraint, and vice versa. We could write $y=\sqrt{L^{2}+ x^2}$ and then express everything in terms of $x$, but a simpler approach would be to express both $x$ and $y$ in terms of the single parameter $\theta$. All quantities of interest for motion can be put into terms of $\theta$: for example, since $L$ is constant, the velocity of the bob can be written as

$$v=L\dot{\theta}$$
and thus the kinetic energy of the bob is 

$$T=\frac{1}{2} m L^2\dot{\theta}^{2}$$
The equilibrium position of the pendulum occurs when the rod is parallel to the force of gravity, at $\theta= 0$. The potential energy $U$
of the bob will be equal to $$U=mgh$$
where $h$ is the height of the bob above its equilibrium position. We can write an expression that will give the height of the bob regardless of position via trigonometry:

$$h = L-L\cos \theta = L(1-\cos \theta)$$

which gives the potential energy 

$$U=mgL(1-\cos \theta)$$

We can now write the Lagrangian:

$$\mathcal{L} = T - U = \frac{1}{2} m L^2\dot{\theta}^{2}-mgL(1-\cos \theta)$$

From this, we can note that the generalized momentum associated with the coordinate $\theta$ is $p_{\theta}=\pdv{L}{\dot{\theta}} = mL^2\dot{\theta}$, which allows us to write the Hamiltonian:

$$\mathcal{H}(p_{\theta},\theta) = p_{\theta}\dot{\theta} - \mathcal{L}(\theta, \dot{\theta})$$

$$\begin{align*}
&= mL^2\dot{\theta}^2-\frac{1}{2} m L^2\dot{\theta}^{2}+mgL(1-\cos \theta)\\
&= \frac{1}{2}mL^2\dot{\theta}^{2}+mgL(1-\cos \theta)\\
&= \frac{p_{\theta}^2}{2mL^2}+mgL(1-\cos \theta)
\end{align*}$$

From which we can find Hamilton's equations of motion:

$$\dot{p_{\theta}}= -\pdv{H}{\theta}=mgL\sin \theta$$
$$\dot{\theta} = \pdv{H}{p_{\theta}} = \frac{p_{\theta}}{mL^2}$$


Combining this first equation with the canonical momentum $p_{\theta}$ as defined above, we find that 

$$mL^{2}\ddot{\theta} = -mgL\sin\theta \implies \ddot{\theta} = -\frac{g}{l}\sin\theta$$
....which is encouragingly familiar as the equation of motion for a simple pendulum.
Since the generalized coordinate $\theta$ is not time-dependent, neither is the Hamiltonian, and thus the Hamiltonian is always equal to the total energy of the system $T+U$, which in this example will be constant due to conservation of energy in the absence of friction or drag. 

A phase diagram for the simple pendulum system is pictured below*:

![[Pasted image 20221113193637.png]]

Here, $p$ is the generalized momentum $p_{\theta}$, and $q=\theta$. Each colored trajectory represents a different value for the Hamiltonian - the green trajectory is the lowest energy, and the orange is the highest. On this graph, t on the x-axis is equal to $\pi$, so the green trajectory has enough energy to swing through an angle of about $\pm\frac{\pi}{2}$ radians. As time advances, the pendulum will trace out the trajectory, with one full orbit corresponding to one period of the pendulum. The blue trajectory is at a slightly higher energy, corresponding to higher maximum values for $\theta$ and the momentum. The purple trajectory shows the swing angle $\theta$ approaching its maximum value, $\pm \pi$, and the yellow trajectory is an even higher-energy case in which the trajectory is no longer a closed path - this represents the situation where the pendulum has sufficient energy that it will only ever swing in one direction, and the momentum will never be equal to zero.
***

 *phase space diagram from https://inside.mines.edu/~tohno/teaching/PH505_2011/Matt_Phase%20-%20Space%20Dynamics.pdf