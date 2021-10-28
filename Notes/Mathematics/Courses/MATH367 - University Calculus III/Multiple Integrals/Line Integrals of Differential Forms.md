# Differential Forms:

***

A **differential 1-form** $\omega$ is an expression of the form:


### $$\begin{align} P(x)dx &\qq{($n=1$)} \\ P(x,y)dx + Q(x,y) dy &\qq{$(n = 2)$}\end{align} $$


***
### Integration of Differential Forms:

Take $n=2$: 

### $$\omega = P(x,y)dx + Q(x,y)dy. $$

### $$C = \va{r}(t) = (x(t),y(t)). $$

Define: 

> ### $$\int_C \omega = \int_a^b P(x(t),y(t)) + Q(x(t),y(t)) dt$$


Compactly:

> ### $$\int_C P\,dx + Q\,dy = \int_C(P,Q)\cdot d\,\va{r}.$$
> ### $$=\int_a^b P(x(t),y(t))x'(t)  + Q(x(t),y(t))\,y'(t)\,dt.$$

***

**Eg.**  Evaluate $\int_c x\,dy$, where:


*(a)*: 

$$\begin{align}C:\qquad x &= a \cos t \qq{,}  t\in [0,2\pi].\\ y &= a \sin t\end{align}$$


> ### $$\int_c x\,dy = \int _0^{2\pi}(a\cos t )(a \cos t)\, dt.$$