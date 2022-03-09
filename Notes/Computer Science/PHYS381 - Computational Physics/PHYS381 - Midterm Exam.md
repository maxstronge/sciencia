# PHYS381 Midterm Exam
### Max Stronge (30064749)
#### Dr. Claudia Gomes da Rocha

***

### 1.   Finding Minima of a Potential

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


- c) The scientist is unsure of which numerical root-finding method to use between the *Newton-Raphson* method and the *Bisection* method. Which method would you advise? Do you have experience in either method? What did you learn when using these methods? 

> **Answer**:
> I have experience in using both methods for problems of a similar type. There are advantages and disadvantages to both methods. The following is what I learned when working with both methods:
> The Newton-Raphson method is much faster and more efficient, *especially* if one has a good 'initial guess' for $r_0$. If you need very high precision ($\implies$ lots of iterations, very low tolerance value), this method will take far fewer computational resources and will converge quicker than the Bisection method. However, the Newton-Raphson method does not guarantee a solution - if you have an initial guess that is not in the neighborhood of an actual root, it is possible that the function will not ever converge. 
> The Bisection method, on the other hand, does always guarantee a solution, provided the function is continuous and one starts with values of opposite signs on either side of a root. Unfortunately, this method is much more computationally intensive than the Newton-Raphson method is to achieve the same degree of position.
> My recommendation: find two points on the graph of $U(r)$, one positive and one negative, that contain a root between them, and apply the Bisection method ~3 or 4 times to narrow the interval. Then, use the result of that as the  initial guess for the Newton-Raphson method, which will then converge quickly, allowing you to lower your tolerance and increase your iterations without worrying about whether the function will diverge. 
> If you have a decent initial guess somewhere in the neighborhood of a root, then you are safe to start with the Newton-Raphson method. 



### 2.  Solving  Nonlinear Systems of Differential Equations

The second scientist is trying to solve a system of nonlinear differential equations known as the *Lorenz system*, given by:

$$\begin{align} \dv{x}{t} &= \ss (y-x) .\\[2ex] \dv{y}{t} &= x(\rho - z) - y. \\[2ex] \dv{z}{t} &= xy - \bb z.   \end{align}$$

The Lorenz system is a mathematical model for describing atmospheric convection. These equations relate the properties of a two-dimensional fluid layer uniformly warmed from below and cooled from above. They describe the rate of change of three quantities with respect to time: $x$ is proportional to the rate of convection, $y$ to the horizontal temperature variation, and $z$ to the vertical temperature variation. $\ss, \ \rho$, and $\bb$ are constants that the scientist will try to tune to identify *strange attractors* in their solutions. First, they need to find solutions for the Lorenz system.

- a) They have heard that you have experience with both the Trapezoid and Runge-Kutta methods. Which would you suggest be used here?

> **Answer**: 
> We employed a 4th-order Runge-Kutta algorithm in our previous work in a computational physics class. Which method I would suggest depends on your priorities for this experiment - the Runge-Kutta will give a higher-accuracy result, but it requires 4 function evaluations (for 4th-order RK) compared to the 2 function evaluations required for the Trapezoid method. If computational resources would not be strained by applying the Runge-Kutta to high precision, that would be my suggestion. If computational resources are limited, the Trapezoid method will give a good approximation with fewer function evaluations required, but the precision will be inferior to the Runge-Kutta. 

- b) What is the difference between RK2 and RK4? Based on your experience, which RK order do you reccomend implementing, and why?

> **Answer**:
> The difference between different orders of the Runge-Kutta method is the amount of *steps* taken per iteration. An RK2 algorithm takes 2 steps across an interval - it will first 'shoot' to the midpoint, estimate the derivative, then shoot to the end of the interval. For an ordinary differential equation in the form $\dv{y}{t} = f(y(t),t),$ the algorithm is as given below ^[Doctoral Dissertation by Muhammad Fadlisyah, “A Rewriting-Logic-Based Approach for the Formal Modeling and Analysis of Interacting Hybrid Systems”, University of Oslo]:
> $$\begin{align}k_1 &= f(t_n, \ y_n) \\ k_2 &= f(t_n + \frac{1}{2}h, \ y_n + \frac{1}{2}h  k_1) \\ y_{n+1} &= y_n + hk_2 \end{align}$$
> ...where $h$ is the width of the interval. 
> The 4th order Runge-Kutta instead takes 4 steps across the interval: it will go halfway to the midpoint, estimate the derivative, then to the midpoint, estimating the derivative again, then to the three-quarter point, and so on. Thus, the 4th order gives a much more finely-tuned, higher resolution approximation. The algorithm for 4th order Runge-Kutta is as follows:
> $$\begin{align}  	k_1 &= f(t_n, y_n) \\ k_2 &= f(t_n + \frac{1}{2}h, y_n + \frac{1}{2} hk_1) \\ k_3 &= f(t_n + \frac{1}{2}h, y_n + \frac{1}{2}hk_2) \\ k_4 &= f(t_n + h, y_n + hk_3) \\ y_{n+1} &= y_n + \frac{1}{6}h (k_1 + 2k_2 + 2k_3 + k_4).    \end{align}$$
> Again, the recommendation is dependent on the degree of precision required and the available computational resources. For reasons I will outline in the answer to the next question, I would advise the 4th order Runge-Kutta for increased precision.

- c) The scientist has now chosen a method to solve the Lorentz system, and they have initialized their parameters as:

![[Pasted image 20220308123249.png|Initial conditions for numerical method to solve Lorentz system.]]

The scientist ran the code to produce *phase portraits* projected onto the planes depicted below:
![[Pasted image 20220308123357.png|Phase portraits plotted from initial conditions given above. ]]

The scientist then adds a very small random fluctuation (on the order of $10^{-10}$) to the initial conditions and runs the program again, producing the following result:

![[Pasted image 20220308123535.png|Phase portraits with small changes in the initial conditions.]]

Does the scientist have a mistake in their code? Why are the trajectories so different when the initial conditions vary by such a small amount? Is this indicative of a physical phenomenon? 

>**Answer**: 
> No, there is no mistake in the code (or at least, we cannot conclude that there is no mistake in the code because of the difference in the plots). The differences in the phase portraits *are* indicative of a physical phenomenon: chaos. Chaotic systems are dynamical systems that are extremely sensitive to small fluctuations in their initial conditions - even incredibly minute differences, such as the ones produced by the scientist's $\texttt{random.randn}$ function within $\texttt{numpy}$, can lead to radical changes in the evolution of chaotic systems. Weather and climate are generally chaotic systems (which is why our ability to predict the weather dramatically decreases the further out in time one looks). The Lorentz system itself is a famous example of a chaotic system - so no need to worry! There's nothing wrong with your code - in fact, the changes in the trajectories in phase space after such small changes in initial conditions is a good indicator that your program is working correctly.




