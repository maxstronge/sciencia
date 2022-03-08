# PHYS381 Midterm Exam
### Max Stronge (30064749)
#### Dr. Claudia Gomes da Rocha

***

### 1.  Scientist #1 - Finding Minima of a Potential

Intermolecular interaction between two atoms of krypton (Kr) given by Lennard-Jones potential energy:

$$U(r) = 4\epsilon \left(\left(\frac{\sigma}{r}\right)^{12}-\left(\frac{\sigma}{r}\right)^6\right) \qquad [1]$$

...where $r$ is the separation between atoms, $\epsilon$ is the well-depth (measure of how strongly the two particles attract each other), and $\sigma$ is the distance at which the potential energy of the interaction between the two particles is zero. $\sigma$ is thus the closest two nonbonding particles can get to each other, and it is called the *van der Waals radius*. The values of 	$\epsilon$ and $\sigma$ were determined experimentally:

$$\begin{align}\epsilon &= 18.2 \text{ meV} \\ \sigma &= 3.7 \ang\end{align}$$

Scientist is confused about how to characterize the equilibrium properties of the krypton dimer, and how to use computers to determine those properties.

- a) What conditions should I establish for the interatomic potential energy that give the *most stable* atomic separation in my molecule? Can you quantify the most stable separation between the atoms and the minimum value of the interatomic potential energy as described in Equation [1]?


> **Answer**:
> Note that for a one-dimensional problem such as Equation [1], the force is given by the negative of the gradient of the potential energy, i.e.:
> $$F(r) = -\dv{U(r)}{r}$$
> We are seeking a *stable equilibrium*, which will occur when the force acting on the particles due to their interaction is zero. According to the relation above, the force will be zero when the derivative of the potential energy is zero, i.e. at the stationary points of the function $U(r)$ . The bottom of a potential well (i.e. the minima of $U(r)$) corresponds to a stable equilibrium, while inflection points and maxima of $U(r)$ correspond to unstable equilibria ^[Claudia Gomes de Rocha. Assignment 1 - Finding Minima of Functions - Manual. URL: https://d2l.ucalgary.ca/d2l/le/content/423366/viewContent/5143001/View%7D.]. We can identify the minimum of the potential energy by finding values of $r$ which satisfy the following requirements:
	> 1. The slope of $U(r) =0 \implies \dv{U(r)}{r} = 0.$
	> 2. The second derivative of $U(r)$ is positive. 
> 
>The derivative of the given function $U(r)$ is given by:
> $$\dv{U(r)}{r} = 4\epsilon \left(  \frac{6\sigma^6}{r^7} - \frac{12 \sigma ^{12}}{r^{13}}  \right)\qquad [2]$$
> ...and the second derivative is:
> $$U''(r) = 4\epsilon \left( \frac{156 \sigma^{12}}{r^{14}}- \frac{42\sigma^6}{r^8} \right) \qquad [3]$$
>So, when Equation [2] is zero and Equation [3] is positive for some value of $r$, that $r$ corresponds to the distance at which the two krypton atoms will be in stable equilibrium.


- b) Scientist #1 is seeking advice - should this problem be solved analytically or numerically?

> **Answer**: 
> I would strongly suggest tackling this problem using numerical methods. For one, analytic solutions to problems like this are not always possible (and after researching the conditions under which an analytic solution exists, it seems that it's not trivial to figure out if there is indeed an analytic solution). A numerical method, on the other hand, will not give an exact answer, but it can produce a very good approximation that can be tuned to the desired degree of accuracy. This will likely be much faster and easier than trying to solve analytically (especially if you're trying to do it on paper, without the assistance of calculators / symbolic algebra tools.)
> Another advantage of numerical methods is that you can quickly alter certain values and repeat the experiment - for example, if you wanted to try a similar problem but with argon instead of krypton, all one would need is the experimental values of $\ee$ and $\sigma$. No additional work is required. If one wanted to do this analytically, the marginal time cost of repeating the calculations can get very high very quickly!
> 




