# PHYS375 - Assignment 4
### Max Stronge (30064749)
***

1. Identify, if any, poles, type of singularities, branch points/cuts of the following functions:
	1. $f(z) = \ln(z^2 + z -2)$
	2. $f(z)=(z^2+4)^{\frac{1}{2}}$
	3. $f(z)=\frac{1+z^3}{z^2+2}$
	4. $f(z)=\csc{(\frac{1}{z^2}})$

**Solutions:**


**a)** Consider the derivative $f'(z)=\frac{1}{z-1}+\frac{1}{z+2}$. From examination, we find singularities at $z=1$ and $z=-2$. We can classify them via definitions:

**Definition:** $z_0$ is a removable singularity of $f$ if $\lim_{z\to z_0}f(z)$ exists.

**Definition**: $z_0$ is a pole singularity if $\lim_{z\to z_0}|f(z)|=\infty$.

**Definition**: $z_0$ is an essential singularity if $\lim_{z\to z_0}|f(z)|\neq\infty$ and the limit does not exist.


By examination we find that for $z_0=1,-2$, the limit of the absolute value of the function converges to infinity, so both $1$ and $-2$ are pole singularities of $f(z)$. 

If we plot $f(z)$, the result is 
![[Pasted image 20221107231845.png]]

Branch points of a log function occur when the argument of the logarithm is equal to zero - hence $z=1,-2$ are branch points as well as poles. A suitable branch cut would be the real axis $-2<x<1$.

**b)** The derivative is $f'(z)=\frac{z}{\sqrt{z^2+4}}$, and finding the roots of the denominator yields singularities at $z=\pm2 i$, and checking the limits as before, they both tend to zero, meaning they represent removable singularities, as well as branch points, for which an appropriate branch cut would be on the imaginary axis from $-2i<y<2i$ . There is an additional singularity at $z=-3i$ which is also removable, tending to the same limit as $\pm i$.

**c)** From the denominator of the function, we see that two singularities must be at $z=\pm \sqrt{2}i$. Examining the behavior of the limits reveals that both singularities are essential (limit does not exist, not removable). No branch points - function is single-valued everywhere.

**d)**  The function is plotted below:
![[Pasted image 20221108174334.png]]
![[Pasted image 20221108174430.png]]

We can note immediately that there must be a singularity at $z=0$ , and since the limit does not exist, we conclude it is an essential singularity. 

***

2. Show that the function $$f(z)=\sqrt{z^2-1}$$ is single-valued if we make a branch cut on the real axis for $-1<x<1$. Draw at least one other possible closed path for which $f(z)$ is single-valued.


**Solution:**

By definition: a branch of a multi-valued function such as $f(z)=\sqrt{z^2-1}$ is a single valued function $g$ that is analytic for each point $z$ at which $g(z)$ is a value of $f$. 

If we plot the function $f(z)$ on the complex plane, we get the following result (created in Mathematica):

![[Pasted image 20221107225922.png]]

The multi-valued nature of the function is evident in the behavior of the color map around the points $x=\pm 1$. The branch cut mentioned is pictured:

![[Pasted image 20221107230323.png]]

and delineates a branch of the function $f(z)$ that is single-valued by restricting the domain of a closed-path integral, such as the one pictured:


![[Pasted image 20221107230539.png]]

An alternate closed path could be

![[Pasted image 20221107230706.png]]






***

3. Show that:
	1. If $f_1(z)=u_1(x,y)+iv(x,y)$ and $f_2(z)=u_2(x,y)$ are analytic in some region of the complex plane, then $f_1(z)f_2(z)$ is also analytic in the same region. 
	2. The function $f_1(z)=\frac{1}{z-z_0}$ is analytic in the complex plane, except at $z=z_0$. We thus conclude that if $f_2(z)$ is also analytic in the same region of space $\mathbb{R}$ which does not include $z=z_0$, then $f(z)=\frac{f_2(z)}{z-z_0}$ is also analytic in $\mathbb{R}$.
**Solution:**

***

4. 

**a)** Determine if the functions $f_1(z)=|z|^2$ and $f_2(z)=\frac{1}{z^2}$ are analytic.


**Solutions:**

Note that $f_1(z)=|z|^2$ can be written as $f_1(z)=z\cdot\bar{z}$. Given $z=x+iy$, this yields that $|z|^2=(x+iy)(x-iy)=x^2+y^2$, a completely real-valued function. Thus $u(x,y)=x^2+y^2$, and $v(x,y)=0$.

We can easily check the Cauchy-Riemann equations:

$$\pdv{u}{x}=\pdv{v}{y}\qq{and}\pdv{v}{x}=-\pdv{u}{y}$$
$$u_x=2x, v_y=0, v_x=0,-u_y=-2y$$
It can be seen that the C.R.E only hold at the origin, $x=y=0$. Since the function $f(z)=|z|^2$ is clearly not differentiable at the origin, we can conclude that $f_1(z)$ is analytic nowhere.


For $f_2(z)=\frac{1}{z^2}=z^{-2}$, we can again put it into the form $f(z)=u+iv$. Expanding $z$ as $x+iy$, we have $$f_2(z)=u(x,y)+iv(x,y) = \left( \frac{x^2-y^2}{(x^2+y^2)^2}\right) + i\left(\frac{-2xy}{(x^2+y^2)^2} \right)$$ Our partial derivatives are $$\pdv{u}{x}=\frac{2x}{(x^2+y^2)^2} - \frac{4x(x^2-y^2)}{(x^2+y^2)^3} = -\frac{2x(x^2-3y^2)}{(x^2+y^2)^3}$$ and $$\pdv{v}{y}=\frac{8 x y^2}{\left(x^2+y^2\right)^3}-\frac{2 x}{\left(x^2+y^2\right)^2} = -\frac{2x(x^2-3y^2)}{(x^2+y^2)^3}$$
So the first of the C.R.E are satisfied. We must also have $\pdv{v}{x}=-\pdv{u}{y}$, so next we check that:

$$\pdv{v}{x}= \frac{8 x^2 y}{\left(x^2+y^2\right)^3}-\frac{2 y}{\left(x^2+y^2\right)^2} = -\frac{2 y \left(y^2-3 x^2\right)}{\left(x^2+y^2\right)^3}$$

$$-\pdv{u}{y} = \frac{2 y}{\left(x^2+y^2\right)^2}+\frac{4 y
   \left(x^2-y^2\right)}{\left(x^2+y^2\right)^3} = -\frac{2 y \left(y^2-3 x^2\right)}{\left(x^2+y^2\right)^3}$$
Thus, the C.R.E are both satisfied and $f_2(z)$ is analytic.



**b)** Evaluate the path integral $$\int_Cf_1(z)dz$$ where the contour $C$ is:

- The straight line segment with initial point $z=-1$ and final point $z=i$.
- The $90\degree$ arc of the unit circle with initial point $z=1$ and final point $z=i$. 
 **Solution:** 
We can parameterize the straight line segment as a function of $t$:

$$(1-t)(-1,0) + t(0,i) \implies z(t)= (t-1)+ti, 0<t<1.$$

***