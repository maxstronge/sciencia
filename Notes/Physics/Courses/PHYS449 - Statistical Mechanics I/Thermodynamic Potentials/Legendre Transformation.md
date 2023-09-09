# The Legendre Transformation
***

Let us first restrict ourselves to functions of one variable. The results are readily generalized to multivariate functions. Assume $f(x)$ to be a function of a single variable $x$, with the total differential:

$$df = \pdv{f}{x}dx=p(x)dx$$ ^2a9795

Here, $p(x)=f'(x)$ gives the slope of the curve $f(x)$ for all $x$ (assuming $f$ is differentiable everywhere). The task of the **Legendre** transformation is to find a function $g(p)$ of the new variable $p=f'(x)$ that is *equivalent* to the function $f(x)$ (*i.e.* $g$ and $f$ contain the same information). Thus, one must be able to unambiguously calculate $g(p)$ from $f(x)$, and vice versa. We can find $g$ relatively easily here by examining the figure below:

![[Pasted image 20221208154518.png]]

Consider the point where the *tangent* $T$ to $f$ at the point $(x_{0}, f(x_{0}))$ intersects with the $y$-axis. The tangent has the following equation:

$$T(x)=f(x_{0}) + f'(x_{0})(x-x_{0})$$

The intersection with the $y$-axis $g=T(0)$ is therefore

$$g(x_{0})= f(x_{0})-x_{0}f'(x_{0})$$
....and we see that the intersection (obviously) depends on the point $x_{0}$ under consideration (since different values of $x$ may correspond to different slopes). 

One calls the function $g(x)$ for an arbitrary point $x$ the **Legendre transform** of $f(x)$:
# $$g=f-xp \qq{with} p= \pdv{f}{x}.$$

^6651ef


In other words, $g(x)$ is equal to the corresponding value of the *intersection* to the tangent to $f$ at the point $(x,f(x))$ with the $y$-axis. 


We know want to show that $g$ depends solely on the slope $p=f'(x)$. To this end, we differentiate [[#^6651ef|the above]] equation:

$$\begin{align*}
dg &= d \qty[f - xp]\\
&= df - pdx - xdp\\
&= pdx - pdx - xdp\\\\

dg &= -xdp

\end{align*}$$

^579dfd

...where in the 3rd step we replaced $df$ with the definition found [[#^2a9795|above]]. Thus, $g$ is only dependent on the variable $p$, which we recall is the derivative of $x$. To calculate $g(p)$ explicitly, we have to eliminate $x$ in [[#^6651ef| the definition of g]]:

$$g(x)= f(x) - xf'(x)$$
Luckily, we know

$$p=f'(x)$$ ^760ef6

But this elimination is only possible if the [[#^760ef6|above equation]] can be *uniquely* solved for $x$, *i.e.* if an **inverse** function $f'^{-1}$ exists for $f'$. Then, one can insert

$$x = f'^{-1}(p)$$

into the definition of $g$, and one obtains explicitly the function 

$$g(p)=f(f'^{-1}(p)) - f'^{-1}(p) \ p.$$

Let us consider a specific example.

##  Example: $f(x)=x^{2}$:
>$$f(x)=x^{2}\qq{,}f'(x)=p(x)=2x.$$
> Thus the Legendre transform reads:
> $$g(x) = x^{2}-px$$
> The inverse function $f'^{-1}$ exists, and can be calculated from the above:
> $$f'^{-1}(p)= x = \frac{p}{2}$$
> If one inserts this into the Legendre transformation, it follows that
> $$\begin{align*}
g(x) &= x^{2}-px \\
&= \frac{1}{4} p^{2}-\frac{1}{2} p^{2}\\
&= \frac{-1}{4}p^{2}
\end{align*}$$
> The differential reads
> $$dg = -\frac{1}{2}p \ dp = -x dp$$
> which coincides with the [[#^579dfd|equation above]].


#
***


It is therefore evident that a unique Legendre transform exists *only* if the equation
$$p=f'(x)$$
represents a **bijective mapping**, *i.e.* every value of the variable $x$ is *uniquely* mapped onto a certain value of the slope $p$, and vice versa. Mathematically, the function $f'(x)$ has to be **strictly monotonic** for the above equation to be invertible. Thus, *only if $f'(x)$ is strictly monotonic does the Legendre transform $g(p)$ exist*. If the slope $f'(x)$ is not strictly monotonic, there may be several values of $x$ belonging to a value of the slope $p$, and the transformation is no longer unique. 

We can also *reconstruct* the original function $f(x)$ from the Legendre transform $g(p)$ in a unique way. Because $g(p)=f(p)-xp$, we can write

$$f(p) = g(p) + xp$$ ^44b719

In this equation, we can uniquely replace $p$ by $x$. According to $dg = -xdp$, we find
$$\frac{dg}{dp}= -x \implies x = \frac{-dg}{dp}= - g'(p)$$
Since $f'(x)$ is strictly monotonic, the inverse function is also strictly monotonic, so we can solve the above for $p(x)$ and then recover the original function by substituting that expression in for $p$ in [[#^44b719|this equation.]]


## Example: Reverse Transformation
> Let us once again consider our first example, where we had 
> $$g(p) = - \frac{1}{4} p^{2}$$
> If one calculates $-x = \frac{-1}{2}p = g'(p)$, we can solve this equation for p(x):
> $$p(x)=2x$$
> and so we can substitute that into 
> $$\begin{align*}
f(p) &= g(p)+xp\\
&= - \frac{1}{4}p^{2}+ xp\\
&= - \frac{1}{4}(2x)^{2}+x(2x)\\
&= -x^{2}+2x^{2}\\
&= x^{2}
\end{align*}$$
....the original function is restored.



#

***

The generalization of the Legendre transform to functions of several variables follows easily from what we have done so far. For instance, consider a function $f(x,y)$ of $2$ variables. The total differential is then

$$df=p(x,y)dx + q(x,y) dy$$
where $$p(x,y)=\left (\pdv{f}{x} \right)_{y} \qq{,} q(x,y) = \left (\pdv{f}{y} \right)_{x}$$
If the variable $x$ is to be replaced by $p$, one forms 

$$g(x,y) = f(x,y) - xp$$ ^3ffb5b

and the total differential of this function $g$ is 

$$dg = df -p\ dx-x \ dp$$

and since $df = p dx + q dy$:
$$dg = -x \ dp + q \ dy$$

...where now $g$ is now a function of $p$ and $y$ only, with $x$ and $q$ acting as constants.

To calculate $g(p,y)$ explicitly, we must first verify that the function

$$p(x,y) = \left (\pdv{f}{x} \right)_{y}$$
is invertible $\forall \ y$. Then, one can calculate the function $x(p,y)$ from the known information, and insert it into  [[#^3ffb5b|this equation]], so that the new function $g(p,y)$ is known. 

Analogously, one can replace both variables $x$ and $y$ by $p$ and $q$. To this end, one constructs:

$$h(x,y) = f(x,y) - px - qy$$

$$$$