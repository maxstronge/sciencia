# 1.4 - Other Mechanical Oscillation Systems:
***

Whenever there is a **restorative force** to act on a mass, oscillations are likely to occur. As we have seen, there must be two agents for mechanical oscillations to occur: one capable of storing kinetic energy (*i.e.* to move), and one capable of storing potential energy (*i.e.* keeping the system moving), like the mass-spring system.

In rotational devices (like the wheel balance in watches), the  **restoring torque** and **rotational intertia** replace the restorative force and mass, respectively, but the energy considerations are the same.

***

### A Pendulum:
![[Pasted image 20220911134842.png]]

A clock with a pendulum derives its accuracy from the *regularity of its periodic oscillation frequency*.  Interestingly, the period of a pendulum is entirely determined by the length of the support/string $l$, and is completely independent of the mass $M$.

In Fig. 1.8 above, the restorative force acting on the mass is provided by gravity, which will tend to make the mass remain at the equilibrium position $P$ (the lowest position).

The restoring force $F$ is given by:

$$F = Mg\sin\theta\text{ (towards $P$)}$$

And so the equation of motion for the mass becomes:


$$M\dv{v}{t} = -Mg\sin\theta$$

...where the minus sign appears because, in the figure above, the force is initially directed towards the left.

Since the velocity $v$ is given by:

$$v=l\dv{\theta}{t}$$

So the equation of motion itself becomes:

$$\dv[2]{\theta}{t} = -\frac{g}{l}\sin\theta$$

Although this equation looks simple, it is a **nonlinear differential equation** and is not solvable analytically with sine/cosine functions. However! If we use the **small angle approximation** where, in the limit of small $\theta$, we can make the approximation $\sin\theta = \theta$, which results in a *linear* differential equation:

$$\dv[2]{\theta}{t} = -\frac{g}{l}\theta$$

This is now much easier to work with, and we can immediately find the oscillation frequency:

$$\oo = \sqrt{\frac{g}{l}}$$

...which does indeed have units of inverse time, as expected. The above procedure was a **linearization** of the differential equation.

***



