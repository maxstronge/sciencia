# Stealing Momentum from Mars - Optimizing the Gravitational Assist

***

**Goal** - determine the optimal trajectory to obtain the greatest possible magnitude of gravitational assist from the planet Mars. 

This involves breaking the problem down into two regimes: 

- Earth surface -> Mars SOI (heliocentric frame)
- Assist in Mars SOI (Martian frame)

Beginning with the second regime, we aim to determine the initial conditions that will result in the maximum $\Delta v'$ (increase in velocity in the heliocentric frame). As characterized in Berg. et. al, this amounts to a gravitational scattering problem.


## Scattering Regime:

### 1.1 - 90° Scattering

We consider a spacecraft of mass $m$ approaching a planet of mass $M$ located at the origin of the Martian coordinate system. We take $m < < M\to$ the Martian frame is effectively identical to the CM frame of the two-body system. 

![[Pasted image 20231015150207.png]]

(Note that we are assuming the time taken for this process is small enough s.t. we can take the path of the planet $M$ relative to the Sun to be a straight line (very small segment of elliptical orbit))

It may seem strange/challenging to realize a precisely $90$ degree change in velocity, but this is an illustrative special case (and this was achieved for Voyager 1). The scattering angle will, in general, depend on the incoming trajectory of the spacecraft relative to the planet. 

We will denote the pre-scattering velocity of the spacecraft and planet by $\vec{u}_{m}$ and $\vec{u}_{M}$, respectively, and the post-scattering velocities as $\vec{v}_{m}$ and $\vec{v}_{M}$.

In the planet frame:

$$
\begin{align}
\vec{u}_{m} &= \begin{bmatrix}
0 \\
u_{m,y}
\end{bmatrix} \\ \\

\vec{u}_{M} &= 0 \\ \\



\vec{v}_{m} &= \begin{bmatrix}
v_{m,x} \\
0
\end{bmatrix} \\ \\

\vec{v}_{M} &= 0
\end{align}
$$

i.e. speed is conserved and is entirely reoriented at a right angle to the initial velocity (in the planet frame). 

> In other words, the speed of the satellite well before and well after the scattering event is the same since the total energy of the satellite in the planet’s frame of reference is conserved which, at large displacement from the planet where the gravitational field of the planet is vanishingly small, equals its kinetic energy $\frac{1}{2}m(\vec{u}_{mi})^{2}$.

This is logical but is not the case in the heliocentric frame - since the planet is moving w.r.t the Sun (and since we are making the approximation that the planet is only moving a small linear amount in the timescale of this gravity assist) we can model it as a simple Galilean transform, adding a velocity along the positive $x$-axis. Take the velocity

$$
\vec{u}_{p}=\begin{bmatrix}
u_{p} \\
0
\end{bmatrix}
$$
which we will add to the velocities of the spacecraft and the planet. This addition is simulating a spacecraft being scattered in the 'forward' direction (i.e. in the direction of the planet's orbit about the sun). So in the heliocentric frame:

$$
\begin{align}
\vec{u}'_{m}&=\begin{bmatrix}
u_{p} \\
u_{mi}
\end{bmatrix} \\ \\
\vec{u}'_{M}&=\begin{bmatrix}
u_{p} \\
0
\end{bmatrix} \\ \\
\vec{v}'_{m} &= \begin{bmatrix}
u_{mi}+u_{p} \\
0 \\
\end{bmatrix} \\ \\

\vec{v}'_{M} &= \begin{bmatrix}
u_{p} \\
0
\end{bmatrix}


\end{align}
$$

Thus we can see that in the heliocentric frame the spacecraft does change its speed according to 

$$
\Delta u_{m}=|\vec{v}'_{m}|-|\vec{u}'_{m}|=u_{mi}+u_{p}-\sqrt{ u_{p}^{2}+u_{mi}^{2} }
$$

There are three possibilities here, depending on whether the initial velocity of the spacecraft upon entering the SOI is equal to, much greater than, or much less than the velocity of the planet relative to the sun. In all three cases, however, the velocity of the spacecraft increases in the heliocentric frame to a maximum of $u_{p}$, which is logical in the context of conservation of momentum


Note that none of the above at all depends on the nature of the interaction between the two bodies - this is simply a logical conclusion of the Galilean transform.


### 1.2 - Arbitrary Angle Scattering


We now generalize to the case of an arbitrary outgoing angle $\theta$ rather than strictly 90 degree scattering:
![[Pasted image 20231015160850.png]]

In the planet frame we again have conservation of energy for the spacecraft:

$$
\begin{align}
\vec{u}_{m} &= \begin{bmatrix}
0 \\
u_{m,y}
\end{bmatrix} \\ \\

\vec{u}_{M} &= 0 \\ \\



\vec{v}_{m} &= u_{mi}\begin{bmatrix}
\sin \theta \\
\cos \theta
\end{bmatrix} \\ \\

\vec{v}_{M} &= 0
\end{align}
$$

and in the heliocentric frame:

$$
\begin{align}
\vec{u}'_{m}&=\begin{bmatrix}
u_{p} \\
u_{mi}
\end{bmatrix} \\ \\
\vec{u}'_{M}&=\begin{bmatrix}
u_{p} \\
0
\end{bmatrix} \\ \\
\vec{v}'_{m} &= \begin{bmatrix}
u_{mi}\sin\theta +u_{p} \\
u_{mi}\cos \theta \\
\end{bmatrix} \\ \\

\vec{v}'_{M} &= \begin{bmatrix}
u_{p} \\
0
\end{bmatrix}


\end{align}
$$

and so the change in speed of the spacecraft is 

$$
\Delta u_{m}=\left( \sqrt{ 1+\sin \theta } -1\right) \sqrt{ 2 }\,u_{mi}
$$

and the spacecraft gains speed if it is scattered even partially in the forwards direction ($0\leq \theta \leq 180°$) and it loses speed in the heliocentric frame if it is scattered 'backwards' (i.e. it loops around the planet and goes back the way it came). Logical!

### 1.3 - Arbitrary Incoming and Outgoing Angles

Generalizing even further, let us now consider the case that we have the spacecraft approaching the planet at some *incoming angle* $\delta$, again leaving at an outgoing angle $\theta$.

![[Pasted image 20231015162215.png]]

This amount is positive whenever $\sin \theta>\sin\delta$, i.e. when the spacecraft is scattered by the planet in a more-forward-pointing direction (in other words, the $u_{p}$-component of the spacecraft's velocity will increase).

Again this is completely independent of the exact nature of the interaction between the two bodies!



### 1.4 - Explicit Gravitational Scattering

The above is a rough sketch using conservation logic based on a scattering of a particular angle - it does not take into account the actual gravitational interaction between the bodies. We now incorporate this gravitational interaction to derive a relation between the incoming and outgoing angles $\delta$ and $\theta$.


![[Pasted image 20231015171851.png]]

During the maneuver the spacecraft's velocity vector is scattered by an angle $\gamma$ in the positive 'forward' direction. This scattering angle is dependent on one constant and three parameters:

- Gravitational constant $G$
- mass of the planet $M$
- incoming speed of the satellite $u_{mi}$
- impact parameter $d$ (i.e. the magnitude of the displacement between the planet and satellite if no displacement were to take place)

The scattering angle can be determined specifically according to 

$$
\tan \left( \frac{\gamma}{2} \right) =\frac{GM}{d (u_{mi})^{2}}
$$
and thus $0\leq\gamma \leq 180$°. But since we don't know the value of $d$, we will need to use the restrictions on the range of $\gamma$ to generate various possible values of $d$ and optimize for each constant $d$:

$$
d(\gamma)= \frac{GM}{ (u_{mi})^{2}}\cot \left( \frac{\gamma}{2} \right) 
$$

We will find $180$ such values of $d$, one for each degree in the specified range. However, we must note that this distance $d$ logically cannot be smaller than the radius of the planet $R$ or else the spacecraft would crash - this is something we will have to check for, and may further restrict the domain of possible scattering angles. 

Following similar logic as before and employing a couple trigonometric substitutions to simplify our result we obtain 

$$
\Delta u_{m}=  u_{mi}\left[ \sqrt{ 1-2 \frac{\cos(\beta)(1-D^{2})-\sin(\beta)D}{1+D^{2}}\left( \frac{u_{p}}{u_{mi}} \right) ^{2}}  -  \sqrt{ 1-2\cos(\beta) \frac{u_{p}}{u_{mi}}  + \left( \frac{u_{p}}{u_{mi}} \right) ^{2}} \,\right] 
$$

...where $D=\frac{GM}{d(\gamma) (u_{mi})^{2}}$ will take on $180$ different values. This expression for the change in speed of a spacecraft is what we are trying to maximize, and it is a function of five parameters:



$$
\Delta u_{m}= \Delta u_{m}(u_{mi},d,\beta,M, u_{p})
$$

However, in our case, the mass of the planet $M$ and its velocity $u_{p}$ are known, and we will determine the value of $u_{mi}$ from the other regime, so the optimization problem boils down to optimizing the above expression for $\beta$ for the 180 different values of $d$. 


***


