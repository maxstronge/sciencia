# 1.2 - Mass-Spring System:
***

Consider a mass $M$ (kg) on a frictionless plane that is connected to a spring with *spring constant* $k_s$ (N/m), with an initial (natural) length $l$:

![[Pasted image 20220910184603.png]]

WIthout any disturbance, the mass would remain at its *equilibrium position,* $x=0$. If the mass was pulled a certain distance away and released, the mass would begin to oscillate with a given frequency. The same would occur if the mass was pushed such that the spring compressed, the mass would also begin to oscillate with the same frequency. 

One of the major objectives in studying oscillations is to find *oscillation frequencies* that are determined by physical properties. In the preceding example, they are the mass $M$ and the spring constant $k_s$. 	

The pulling force in this case is given (in one dimension) by **Hooke's Law**:

$$F = \begin{cases} k_s x & \text{(directed to the left)} \\ -k_sx & \text{(directed to the right)}\end{cases}$$

...where $x$ is the deviation of the spring length from the natural length $l$. The minus sign occurs when the displacement is negative.

The force provided by the spring is the key agent in the oscillatory motion, acting as a *restorative force*, which is present in any mechanical oscillating system (or torque). If the spring constant $k_s$ is greater (*i.e.* a stronger spring), it can push or pull the mass more quickly, and we expect the oscillation frequency to be larger. On the other hand if the mass is larger, the mass should accelerate more slowly, and we expect the oscillation frequency will be smaller. 

Indeed, the **oscillation frequency** $\nu$ is given by:

$$\nu = \frac{1}{2\pi}\sqrt{\frac{k_s}{m}}$$

Let us now determine what kind of mathematical expression can describe the oscillatory motion of the mass-spring system. We assume the mass is gradually pulled a distance $x_0$ away from the equilibrium position $x=x_0$, then released at a time $t=0$. The instantaneous velocity of the mass is given by:

$$v=\dv{x}{t} \ [m/s]$$

...and the acceleration is 

$$a = \dv{v}{t} = \dv[2]{x}{t}$$

But the force acting on the mass is $-k_s x$, so we have the differential equation:

$$M\dv[2]{x}{t}=-k_sx$$

This is the equation of motion for the mass. Remember that the mass was at position $x(0)=x_0$.

The solution to a differential equation of this type will take the form 

$$x(t) = A\cos{\oo t}$$

...where $\oo$ and $A$ are constants to be determined. Since $\cos{0}=1$, we find that:

$$x(0) = A$$

....therefore, we must have $A = x_0$. This quantity is called the **amplitude** of the oscillation. 

To find $\oo$, we can calculate the second derivative of $x(t) = x_0 \cos{\oo t}$:

$$\begin{align}

\dv{x}{t} &= x_0 \dv{t}\cos{\oo t} = -x_0\oo \sin{\oo t} \\

\dv[2]{x}{t} &= x_0 \dv[2]{t}\cos{\oo t} = -x_0 \oo \dv{t}\sin{\oo t} = -x_0 \oo^2 \cos{\oo t}

\end{align}$$

After substituting this into the earlier equation of motion, we find:

$$-M\oo^2 \cos{\oo t} = -k_s x_0 \cos{\oo t}$$

...which yields:

$$\oo = \sqrt{\frac{k_s}{M}}.$$

This quantitiy $\oo$ is called the **angular frequency**, and has the dimensions of inverse time (radians/second). 

Since the function $\cos{\oo t}$ has a period of $2\pi$ radians, the **temporal period** $T$ is given by:

$$T = \frac{2\pi}{\oo} \text{ [s]}$$

In 1 second, the oscillation repeats itself $\frac{1}{T}$ times:

![[Pasted image 20220911124802.png]]


This number is defined as the **natural frequency** $\nu$:

$$\nu = \frac{1}{T} = \frac{\oo}{2\pi} \text{ [Hz]}$$




***

