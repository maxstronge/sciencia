# Linear Approximations and Differentiability
***


### The Linear Approximation Principle:

The **Linear Approximation Principle** (LAP): 

> The** tangent plane** to $y=f(\vec{x})$ at $\vec{x} = \vec{a}$ is a *good* linear approximation to $f(\vec{x})$ near $\vec{a}$.


***

Informal definition of differentiability: *f* is differentiable at $\vec{x} = \vec{a}$ if the **Linear Approximation Principle** (LAP) holds for *f* near $\vec{a}$.



Precise definition of the LAP:

if: 

1. $$L(\vec{a}) = f(\vec{a}).$$
2. $$\lim_{\vec{x} \to \vec{a}} \frac{f(\vec{x})-L(\vec{x})}{||\vec{x} - \vec{a} ||} = 0.$$

Then, the LAP holds. 


**Definition**: A function *f* is **differentiable** at $\vec{x} = \vec{a}$ if $f$ has a good linear approximation at $\vec{x} = \vec{a}$.

***
Theorem: if a function is continuous, it is differentiable.

$$\lim_{\vec{x}\to \vec{a}}f(\vec{x}) = \lim_{\vec{x}\to \vec{a}} etc$$


***

**Contrapositive Theorem**: not continuous $\implies$ not differentiable. *NB*: the inverse is not true (for example, $f(x) = |x|$ is continuous at $x=0$, but not differentiable).


Suppose $f(\vec{x})$ is differentiable at $\vec{x} = \vec{a}$. Then: 

1. $\nabla f(\vec{a})$ exists, and...
2. $L(\vec{x}) = f(\vec{a}) + \nabla f(\vec{a}) \cdot (\vec{x} - \vec{a})$ is the *unique* good linear approximation to $f$ at $\vec{a}$. 


In the multivariable case: having partial derivatives and being differentiable are not equivalent statements. This is a departure from single-variable calculus. The following example illustrates this.


***

> ** Example:** A function can have partial derivatives without being differentiable (or even continuous)!
> - $f(x,y) = \begin{cases}1 & \text{ if }x=0 \text{ or } y=0 \\ 0 & \text{ otherwise.} \end{cases}$
> 
> ![[Pasted image 20210917142235.png]]
>  $$\begin{align} f_x(0,0) & = \lim_{h \to 0} \frac{f(0+h) - f(0,0)}{h}\\ & = \lim_{h\to 0} \frac{1-1}{h}\\ &= 0. \end{align}$$
>  - Similar logic follows for $f_y$. The existence of partial derivatives does not imply differentiability or continuity of a function.


***

**Theorem**: If $f(\vec{x})$ has continuous partial derivatives in a *neighborhood* of $\vec{x} = \vec{a}$, then $f(\vec{x})$ is *differentiable* at $\vec{x} = \vec{a}$.

This theorem is how one can conclude that functions given by 'nice' formulas (eg. $f(x,y) = x^2 + 3e^{x^2 + y}$) are differentiable. In this case, 'nice' simply means that the function is expressed in a single formula (*i.e.* not piecewise defined) and that it consists of polynomials / arithmetic / log / exponential functions. 

***

