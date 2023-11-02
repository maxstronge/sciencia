# PHYS397 Pre-Lab
### Max Stronge (30064749)


1.

![[Pasted image 20230927193822.png]]
2.

*NB: I initially just wrote the equation of motion here but I wasn't sure if we needed to derive it - in case we do I have copied another homework assignment in which we derive the equation of motion using the Hamiltonian formalism. Apologies if this was unnecessary.* 



Let the mass of the pendulum bob be $m$, the length of the rod/string be $L$, and $\theta$ be the noted angle between the rod and its equilibrium position. Working in a Cartesian coordinate system, let the top end of the rod be affixed to the origin, such that the rod may swing in the $xy$-plane without friction or drag. The bob will experience both horizontal and vertical motion, but this motion is subject to the constraint that $\sqrt{x^{2}+ y^{2}}=L$. Because of this constraint equation, only one of the coordinates is independent, as given $x$, $y$ can always be found from the constraint, and vice versa. We could write $y=\sqrt{L^{2}+ x^2}$ and then express everything in terms of $x$, but a simpler approach would be to express both $x$ and $y$ in terms of the single parameter $\theta$. All quantities of interest for motion can be put into terms of $\theta$: for example, since $L$ is constant, the velocity of the bob can be written as

$$v=L\dot{\theta}$$
and thus the kinetic energy of the bob is 

$$T=\frac{1}{2} m L^2\dot{\theta}^{2}$$
The equilibrium position of the pendulum occurs when the rod is parallel to the force of gravity, at $\theta= 0$. The potential energy $U$ of the bob will be equal to $$U=mgh$$
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

Using the small angle approximation this becomes
$$
\frac{d^{2}\theta}{dt^{2}} = -\frac{g}{L}\theta
$$
$$
 
$$

3.

The following video is a well-done animation of this particular question:
https://www.youtube.com/watch?v=1TR856BWAX0

If one rearranges the equation of motion in terms of the period, one finds for the small angle approximation

$$
T = 2\pi \sqrt{ \frac{l}{g} }
$$

whereas without the small angle approximation we are not so lucky:

$$
T=2\sqrt{ 2 } \sqrt{ \frac{L}{g} }\int_{0}^{\theta_{\text{max}}} \frac{1}{\sqrt{ \cos \theta-\cos \theta_{\text{max}} }}  \, d\theta 
$$

so one comment we can immediately make is that abandoning the approximation produces an incredibly ugly integral for us to solve, which indeed is a potential difficulty. 



4.

In a more physically relevant sense, though, the period calculated with the help of the small angle approximation will be an *underestimate* of the true period, and the error increases as the angle $\theta$ increases. 

This can be mathematically justified using the periods for the pendulum as written above, but it is even more evident if one watches the video posted earlier - several pendulums of different starting angles are animated, one with the small angle approximation, and the other without. It can be intuitively seen that the error introduced by the small angle approximation increases as the angle becomes less small, which seems sensible. 

