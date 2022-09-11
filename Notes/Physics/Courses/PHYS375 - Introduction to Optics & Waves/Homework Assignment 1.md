# PHYS375 Homework Assignment 1
### Max Stronge (30064749)
***

**Written Response**:
1. An equation of motion is a model that seeks to describe how an object's position changes with time.  Motion is very often explained in terms of dynamics, i.e. the effect of forces acting on an object. The central dynamical equation is Newton's second law, relating the force acting on a body to the resulting acceleration caused by the force:

$$\va{F} = m\va{a}$$

The reason that equations of motion are so often differential equations is because the acceleration $\va{a}$ in the equation above is the second derivative of the *position*, which is the property of interest when describing motion. Motion is simply a change in position over time, so an equation of motion should yield a position for each point in time. Hence, to find the motion from the force, the equation must involve some derivative of the position. Taking $\va{a} = \ddot{\vec{r}}$:

$$\ddot{\vec{r}} = \frac{\va{F}}{m}$$

***
2.  Simple harmonic motion describes a particular kind of periodic behavior, oscillating back and forth between some endpoints in a regular, repeated way. It seems logical that, mathematically, periodic behavior should be described by periodic *functions*, and the sine and cosine functions are simple periodic functions well-suited to modelling simple harmonic motion. They also oscillate smoothly between endpoints, and can be easily scaled or shifted to match a particular model.

Mathematically, this intuition can be justified by examining the form of the equation of motion in simple harmonic cases. Using Hooke's Law, for example, Newton's second law would be:

$$\begin{align} \va{F} &= m\va{a} \\ -ks &= m \dv[2]{\va{r}}{t}\\ \dv[2]{\va{r}}{t} &= \frac{-k}{m}s\end{align}$$

....where $k$ is the spring constant term, $s$ is the displacement from equilibrium, and $r$ is position. 

I will follow the instructor's example and avoid a full derivation, but it has been quite reputably shown that the solution to the above differential equation has the form:

$$\va{r}(t) = A \cos{\oo t} + B \sin{\oo t}$$

....where $\oo = \sqrt{\frac{k}{m}}$ is the angular frequency.

***

**Textbook Questions**:

4. Show that the functions:
	a. $x=A\sin{\oo t}$
	b. $x=A\sin{\oo t} + B \cos{\oo t}$
	c. $x = A\cos{\oo t + \phi}$

all satisfy Eq. 1.7, provided $\oo = \sqrt{\frac{k_s}{M}}$, $A$, $B$, and $\phi$ are all constants. 

Eq. 1.7: 
$$M\dv[2]{x}{t}=-k_sx$$

*Solution:*

Begin with a: 

$$x(t) = A \sin{\oo t}$$

We need the second derivative, so we'll differentiate two times:

$$\begin{align} \dv{x}{t} &= A\oo \cos{\oo t} \\ 

\dv[2]{x}{t} &= -A\oo^2\sin{\oo t}

\end{align}$$

Noting that $\oo^2 = \left(\sqrt{\frac{k_s}{M}}\right)^2 = \frac{k_s}{M}$, we can rearrange the equation to have the mass and acceleration on the left hand side:

$$M\dv[2]{x}{t} = -Ak_s\sin{\oo t}$$

...and, recalling that $A\sin{\oo t} = x(t)$ as given, we can replace that term on the right side, yielding:

$$M\dv[2]{x}{t}=-k_s x(t)$$

Similar reasoning for b:

Beginning by differentiating the given expression twice, we have:

$$\begin{align}\dv{x}{t} &= A\oo \cos{\oo t} - B\oo \sin{\oo t} \\

\dv[2]{x}{t} &= -A\oo^2\sin{\oo t} - B\oo^2 \cos{\oo t}

 \end{align}$$

In the second derivative, we can factor the term of $\oo^2$ out of the right-hand side and replace it as before with $\frac{k_s}{M}$:

$$\dv[2]{x}{t} = \frac{-k_s}{M} \left( A\sin{\oo t} + B\cos{\oo t}\right)$$

Which, rearranging the mass and replacing the given expression for $x(t)$, results in:

$$M\dv[2]{x}{t}=-k_s x(t)$$