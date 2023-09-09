# Functions of a Complex Variable:

Any function $f(z)$ consisting of both a real and imaginary part may be written as $$f(z)=u(x,y)+iv(x,y)$$ where $u$ and $v$ denote the real and imaginary parts, respectively, and are in general themselves functions of $x$ and $y$. In this exploration we are typically interested in functions that are *single-valued*, so each value of $z$ corresponds to exactly one value of $f(z)$. 

A function $f(z)$ that is single-valued in some domain $\mathbb{R}$ is *differentiable* at the point $z$ in $\mathbb{R}$ *if* the derivative: $$f'(z)=\lim_{\DD z\to 0}\left[\frac{f(z+\DD z)-f(z)}{\DD z}\right]$$ exists *and* is unique, in that its value does not depend on the direction from which $\DD z$ approaches zero on the **Argand diagram** (the typical 2D representation of the complex plane). 

For example, consider the function $f(z)=x^2-y^2+2ixy$. Is this function differentiable for all values of $z$? We can first note that $$x^2-y^2+2ixy = (x+iy)^2$$ and so $$f(z)=(x+iy)^2=z^2$$ and the derivative is easily taken: $$f'(z)=2z$$ and we can see that the limit does in fact exist for all $z$, and it does not matter which direction the limit approaches from. So $f(z)=z^2$ is differentiable $\forall \ z$.


A function that is single-valued and differentiable at all points of a domain $\mathbb{R}$ is said to be **analytic** (or **regular**) in $\mathbb{R}$. A function may be analytic in a domain *except* at a finite number of points (or an infinite number of distinct points if the domain is infinite) is said to be analytic everywhere except at these points, which are called **singularities** of $f(z)$. 


> Example: Show that the function $f(z)=\frac{1}{1-z}$ is analytic everywhere except $z=1$.
>
>**Solution**: Since $f(z)$ is given explicitly in terms of $z$, evaluating the limit is easy: $$\begin{align}

f'(z)&=\lim_{\DD z \to 0}\left[\frac{f(z+\DD z)-f(z)}{\DD z} \right]\\
&= \lim_{\DD z \to 0}\left[ \frac{1}{\DD z} \left(\frac{1}{1-z-\DD z}-\frac{1}{1-z} \right) \right] \\

&= \lim_{\DD z \to 0}\frac{1}{1-z-\DD z)(1-z)} \\ &= \frac{1}{(1-z)^2}\end{align}$$ ..independently of which direction $z$ is approached - we see that there is a singularity at $z=1$.

***

### The Cauchy-Riemann Relations:

From considering the previous examples, it can be noted that for an function $f(z)$ to be differentiable (and by extension, analytic), there must be some connection between its real and imaginary parts $u$ and $v$.  The relations are quite famous, and are called the Cauchy-Riemann Relations:

$$\pdv{u}{x}=\pdv{v}{y}\qq{and}\pdv{v}{x}=-\pdv{u}{y}.$$

Functions that satisfy the Cauchy-Riemann relations are analytic.

For example, the previous function, $f(z)=x^2+y^2+i2xy$, we have $u(x,y)=x^2-y^2$, and $v(x,y)=2xy$, so
$$\pdv{u}{x}=2x=\pdv{v}{y}\qq{and} \pdv{v}{x}=2y=-\pdv{u}{y}$$

so the function is analytic. 

Since $x$ and $y$ are related to $z$ and its **complex conjugate** $\bar{z}$  by

$$x=\frac{1}{2}(z+\bar{z})\qq{and} y=\frac{1}{2i}(z-\bar{z})$$ we may formally regard any function $f=u+iv$ as a function of both $z$ and $\bar{z}$, rather than of $x$ and $y$. If we do this and examine the derivative $\pdv{f}{\bar{z}}$, it can be seen that this must be zero for any function satisfying the Cauchy-Riemann relations - therefore, if $f$ is analytic, then $f$ cannot be a function of $\bar{z}$, and any expression representing an analytic function of $z$ can contain $x$ and $y$ **only**  in the combination $x+iy$, **not** $x-iy$.

***

