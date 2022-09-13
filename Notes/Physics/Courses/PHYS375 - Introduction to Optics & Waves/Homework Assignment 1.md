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

**NB:** all figures created

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

For c, we will need to employ the chain rule, but the process is the same:

$$\dv{x}{t} = -A\oo \sin(\oo t + \phi)$$

$$\dv[2]{x}{t} = -A\oo^2\cos(\oo t + \phi)$$

$$M\dv[2]{x}{t} = -Ak_s\cos(\oo t + \phi)$$

$$M\dv[2]{x}{t}=-k_s x(t)$$

QED.

***

5. In the mass-spring system setup below:

![[Pasted image 20220910184603.png]]

The mass (1.5 kg) is displaced 10cm to the left and then released. Twenty oscillations are observed in one minute. Find:

- a) the spring constant $k_s$
- b) the equation describing the oscillation
- c) the energy associated with the oscillation

*Solution*:

**a)**
The observed natural frequency $\nu = \frac{20}{60 \text{ s}} = \frac{1}{3\text{ s}}$.

The frequency $\nu$ can be related to the spring constant and the mass by the following relation:

$$\nu = \frac{1}{2\pi}\sqrt{\frac{k_s}{M}}$$


which, with some algebra, we can use to find the spring constant:

$$\begin{align}2\pi \nu &= \sqrt{\frac{k_s}{M}} \\ 

4\pi^2\nu^2 &= \frac{k_s}{M} \\ 

4\pi^2(\frac{1}{3})^2 (1.5) &= k_s \\ 

k_s &= 6.57974 \text{ N/m}

\end{align}$$

**b)**

The equation describing the oscillation is the equation of motion. The spring force on the mass is given by:

$$F = -k_s s = -k_s x_0$$

...where $s=x_0$ is the displacement from equilibrium, in this case $10$cm to the left. The force on the mass will act to the right, in the positive $\hat{x}$ direction.

The solution to the differential equation that comes from Newton's second law is:

$$x(t) = A \cos{\oo t}$$

We have enough information to know that the angular frequency $\oo = \sqrt{\frac{k_s}{M}} = \sqrt{\frac{6.57974}{1.5}}$. Since $\cos{\oo t} = 1$, and $x(0) = x_0$, we know that the constant $A$ must be equal to $x_0$, resulting in the equation of motion:

$$
\begin{align}

x(t) &= x_0\cos{\oo t} \\

\end{align}
$$

....where $x_0 = 0.1m$ and $\oo = \sqrt{\frac{6.57974}{1.5}}$ with units of inverse time, leaving the final expression with units of distance as expected.

**c)**

At the instant the mass is released, it has no velocity and therefore no kinetic energy - the total energy of the system is stored in the string as potential energy, given by:



$$\int_0^{x_0}k_sxdx = \frac{1}{2}k_sx_0^2$$

Assuming an isolated system with no external disturbances and no loss of energy via heat from the spring, we can show that this total energy will remain constant throughout the motion, oscillating between kinetic energy of the mass and potential energy in the spring. The kinetic energy is:

$$T = \frac{1}{2}Mv^2$$

....where the instantaneous velocity $v$ can be found by differentiating the position:

$$v = \dv{x}{t} = -\oo x_0\sin{\oo t}$$

Therefore the kinetic energy is:

$$T = \frac{1}{2}M\oo^2x_0^2\sin^2(\oo t)$$

And thus the total energy is

$$E_\text{total} = T + U = \frac{1}{2}M\oo^2x_0^2\sin^2(\oo t) + \frac{1}{2}k_sx_0^2\cos^2(\oo t)$$

However, the frequency of oscillation $\oo$ is

$$\oo = \sqrt{\frac{k_s}{M}}$$

which, after some algebra, allows us to write the energy:


$$
\begin{align}
E_\text{total} = T + U &= \frac{1}{2}M\oo^2x_0^2\sin^2(\oo t) + \frac{1}{2}k_sx_0^2\cos^2(\oo t)\\

E_\text{total} &= \frac{1}{2}M \frac{k_s}{M} x_0^2\sin^2(\oo t) + \frac{1}{2}k_sx_0^2\cos^2(\oo t) \\

E_\text{total} &= \frac{1}{2}k_sx_0^2 \left( \cos^2 \oo t + \sin^2 \oo t \right) \\ 

E_\text{total} &= \frac{1}{2}k_s x_0^2


\end{align}
$$

It is indeed conserved, and thus the total energy at any instant will be equal to :

$$
\begin{align}
E_\text{total} &= \frac{1}{2}k_s x_0^2 \\

E_\text{total} &= \frac{1}{2} (6.57974 \text{ N/m})(0.1\text{ m})^2 \\ 


E_\text{total} &= 3.28987 \times 10^{-2} \text{ [J]}

\end{align}
$$

***

7. A thin circular hoop of radius $a$ is hung over a sharp horizontal knife edge. Show that the hoop oscillates with an oscillation frequency $\oo = \sqrt{\frac{g}{2a}}$.

*Solution* :



The situation is pictured below:

![[Pasted image 20220911143716.png|Ring balanced on edge of knife]]


At equilibrium, the restorative torque by the solid hoop will seek to keep the hoop at the position in the figure. Say the hoop is initially rotated a small amount $d\theta$ and released. The angle $\theta$ between the center of the ring and a downwards vector (the direction of gravity, which is involved in the torque) will begin to oscillate with a certain frequency $\oo$, which we aim to find. 

Newton's second law in rotational form is

$$\tau = I\dv[2]{\theta}{t}$$

where $I$ is the moment of inertia and $\tau$ is the net torque. 

Many commonly-used geometric solids have well-known moments of inertia - the moment of inertia for a loop through its center is:

$$I = ma^2$$

....where $a$ is the radius of the loop in this case. However, this is not the moment of inertia needed for the problem - since the actual axis of rotation is through the perimeter of the loop, not through the center, we need to employ the *parallel axis theorem*, which states that

$$I = I_c + md^2$$

...where $I_c$ is the moment of inertia through the center of the body, $m$ is the mass of the body, and $d$ is the perpendicular distance from the central axis. We know that $I_c=ma^2$ - since the axis of rotation is exactly one radius away from the center, we find the moment of inertia:

$$
\begin{align}

I &= I_c + ma^2 \\ 

I &= ma^2 + ma^2 \\

I &= 2ma^2

\end{align}
$$

The torque on the ring is due to gravity, given by 

$$\tau = -mga\sin\theta$$

And so we have Newton's second law:

$$
\begin{align}
I\dv[2]{\theta}{t} &= \tau \\

 
\dv[2]{\theta}{t} &= \frac{\tau}{I} \\

\ddot{\theta} &= -\frac{mga}{2ma^2}\sin\theta \\

\ddot{\theta} &= -\frac{g}{2a}\sin\theta 

\end{align}
$$
...or, with the small-angle approximation:

$$\dv[2]{\theta}{t}=-\frac{g}{2a}\theta$$

From here, we have seen several times from previous work that the $\frac{g}{2a}$term plays the role of $\oo^2$, showing that after solving the differential equation we will have 

$$\oo = \sqrt{\frac{g}{2a}}.$$

***

8. A marble thrown into a bowl executes oscillatory motion. Assuming that the inner surface of the bowl is parabolic (y = ax2) and the marble has a mass m, find the oscillation frequency. Neglect friction and assume a small oscillation amplitude.


*Solution*:

The geometry of the situation is pictured below:

![[Pasted image 20220912225811.png]]

The driving restorative force behind the marble's oscillations is gravity, which we know to be a conservative force (since we neglect friction, mechanical energy will be conserved). There must therefore be a corresponding gravitational potential energy, dependent on the distance of the object from the zero point. Taking the origin to be zero, the gravitational potential energy of the marble can be written as a function of its horizontal position $x$:

$$U(x)=mgy = mgax^2$$

From this, we can find the force by recalling that force is the negative of the gradient of the potential energy:

$$F(x) = - \nabla U(x) = -2mgax$$

By Newton's 2nd Law, the equation of motion for the marble will  then be:

$$-2mgax=m\dv[2]{x}{t}$$

...which, after rearranging, becomes:

$$\dv[2]{x}{t} = 2gax$$

And, following the same logic, the $2ga$ term is playing the role of $\oo^2$ this time, and hence:

$$\oo = \sqrt{2ga}$$

***

15. Consider two cascaded mass-spring systems:

![[Pasted image 20220913123229.png]]

 a) Write the equation of motion for *each* mass, assigning displacements $x_1(t)$ and $x_2(t)$ for masses $m_1$ and $m_2$, respectively. The springs are identical.
 
 b) Then, eliminate $x_2(t)$ between the two equations to show that the differential equation for $x_1(t)$ is given by 
 
 $$m_1m_2\dv[4]{x_1}{t}+k(m_1+m_2)\dv[2]{x_1}{t} + k_s^2x_1=0$$
 
 c) Show that the oscillation frequency $\oo$ is given as solutions to 
 
 $$m_1m_2\oo^4-k(m_1+2m_2)\oo^2+k_s^2=0$$
 
 ..which allows two possible solutions for $\oo$. 
 
 *Solution*:
 
 
Only one force acts on $m_2$, provided by the spring between the two masses. This spring's compression or elongation is dependent on the positions of *both* masses - the length of the spring at a time $t$ is given by

$$l(t) = x_2(t)-x_1(t)$$


Thus, the force on $m_2$ is given by 

$$F_2 =-k_s(x_2-x_1)$$

Which allows us to write the equation of motion for $m_2$:

$$m_2 \dv[2]{x_2}{t} = -k_s(x_2-x_1)$$

The first mass ($m_1$) is slightly more complicated, as it has two springs attached to it - the force associated with the first spring, attaching $m_1$ to the wall, we'll call $F_1$:

$$F_1 = -k_s x_1(t)$$

But that is not the net force on $m_1$, since there is another spring connecting it and $m_2$. The force by spring 2 acting on $m_1$ is equal and opposite by Newton's 3rd law to the force by spring 2 acting on $m_2$. Thus the total force on $m_1$ is

$$
\begin{align}

\sum F_\text{on $m_1$} &= F_1 + (-F_2) \\ 

&= -k_s x_1(t)+ k_s(x_2(t) - x_1(t)) \\ 

&= k_s\left(x_2(t)-2x_1 \right)

\end{align}
$$
Which allows us to write the equation of motion for $m_1$:

$$

m_1 \dv[2]{x_1}{t} = k_s\left(x_2(t)-2x_1(t) \right)


$$


***
for c:


$x_1(t) = A\sin\oo t$ where $\oo$ is a big messy function