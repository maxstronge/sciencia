# Directional Derivatives:

***

Let $\vec{u} \neq 0$. The derivative of $f$ at $\vec{a}$ *along (or, in the direction of)* is defined as the following limit:

#### $$D_{\vec{u}}f(\vec{a})  = \lim_{h\to0} \frac{f(\vec{a} + h\vec{u})-f(\vec{a})}{h}. $$

This **directional derivative** gives the rate of change along the axis of some specified vector, rather than the traditional basis vectors of the space. 

If $\vec{u}$ is the standard basis vector (eg. $\hat i, \hat j, \hat k$), this is equivalent to the normal partial derivative. 


**Theorem**: If $f$ is differentiable at $\vec{x} = \vec{a}$, then $D_{\vec{u}}f(\vec{a})$ exists, and:

### $$D_{\vec{u}}f(\vec{a}) = \nabla f(\vec{a}) \cdot \vec{u}. $$



**Proof**: Consider the limit:

#### $$\lim_{h \to 0} \frac {f(\vec{a}+h\vec{u}) - f(\vec{a})}{h}.$$

Recall that $L(\vec{a}) =$