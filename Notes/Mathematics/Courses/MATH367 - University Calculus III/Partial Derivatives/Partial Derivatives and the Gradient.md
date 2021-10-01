# Partial Derivatives and the Gradient:

***


Take some function *f* such that:

$$f:\bf{U} \to \RR$$

...where $\bf{U}$ is the domain, some subset of $\RR$ ($\bf{U}\subseteq \RR$).
***

**Definition**: The *i*-th partial derivative of some function *f* of *n* variables:

> $f_{x_i}(\vec{x}) = \lim_{h \to 0} \frac{f(\vec{x}+h\vec{e_i}  - f(\vec{x})}{h}$, where $\vec{e_i} = (0,\dots,\underset{i}{1},\dots,0)$.

*** 
This is the formal definition, but we don't want to use that all the time - to compute partial derivatives, we hold all but *the distinguished variable* fixed (treat them as constants), and then differentiate the resulting single-variable function. 

Eg. $f(x,y) = \tan^{-1}\frac{y}{x}$.


To compute $f_x$, take *y* as fixed:

> #### $$\begin{align} f_x(x,y) &= \frac{1}{1 + \left(\frac{y}{x}\right)^2} \,\cdot\,\frac{-y}{x^2} \\ &=\frac{-y}{x^2 + y^2}\end{align}$$

This approach scales to any number of dimensions:


Eg. $f(\vec{x}) = -\sum_{j=1}^{n}x_j\ell_nx_j.$

$$f_{x_i}(\vec{x}) =  \dotsb $$ 

***


Recall that we can package the *n* partial derivatives of an *n*-variable function to form an *n*-dimensional vector called the **gradient**. 

The gradient is denoted with the **nabla**, an inverted triangle: $\nabla$. 

> ### $$\nabla f =(f_{x_1}(\vec{x}),f_{x_2}(\vec{x}),\dots,f_{x_n}(\vec{x})). $$

The gradient is also called the **total derivative** of *f*. 

***

Suppose you have a vector function $f(\vec{x}) = \vec{a} \ \cdot \vec{x}.$ What is the gradient $\nabla f$ of this function?

We can rewrite $f(\vec{x})$ as $f = x_1a_1 + x_2 a_2 + \dots + x_n a_n.$

We can then take the partial derivative of this function with respect to each successive $x_i$:

$$f_{x_1} = a_1 + 0 + \dots + 0 $$

$$f_{x_2} =  0 + a_2 + \dots + 0 $$

...and so on. 

***
#### **Special Case**:

Take a matrix $\bf{A}=\left[\begin{array}{cc}
  a&b\\
  c&d\\ 
\end{array}
\right]$ and a vector $\vec{x} =\begin{bmatrix}x \\ y \end{bmatrix}$. 

Let $f(x,y) = \vec{x}^T \bf{A}\, \vec{x}$. This can be rewritten as:

$$\begin{pmatrix}x&y \end{pmatrix} \begin{pmatrix} a&b \\ c&d\end{pmatrix} \begin{pmatrix}x \\ y \end{pmatrix}$$
$$= \begin{pmatrix} x&y \end{pmatrix} \begin{pmatrix} ax+by \\ cx + dy\end{pmatrix}$$

$$= ax^2 + bxy + cyx + dy^2. $$

We can therefore express our function $f(x,y)$ as: $f(x,y) = ax^2 + (b+c)\,xy + dy^2.$

From this, we can take the two partial derivatives of $f$ with respect to $x$ and $y$:


> $$f_x = 2ax + (b+c)\, y.$$
> $$f_y = (b+c)\,x + 2dy.$$

The gradient of the function can then be expressed:

> #### $$\nabla f = \begin{bmatrix}f_x \\ f_y \end{bmatrix} = \begin{bmatrix} 2ax + (b+c)\, y \\ (b+c)\,x + 2dy \end{bmatrix} = \begin{bmatrix} 2a & b+c \\ b+c & 2d \end{bmatrix} \begin{bmatrix}x \\ y \end{bmatrix}.$$

This can be even further rearranged to yield:

> $$\left( \begin{bmatrix} a & b \\ c & d  \end{bmatrix} + \begin{bmatrix} a & b \\ c & d  \end{bmatrix}\right) \begin{bmatrix} x \\ y \end{bmatrix} = (\bf{A} + \bf{A}^T)\,\vec{x}.$$

$$\nabla f = (\bf{A}+\bf{A}^T) \, \vec{x}. $$

***

### Remark: 

If $\bf{A}$ happens to be a symmetric matrix, such that $\bf{A}^T = \bf{A}$, then the gradient of the function:

$$\nabla \vec{x}^T\bf{A}\vec{x} = 2\bf{A}\vec{x}. $$

Note that we have something in a similar form to the power rule for derivatives: $ax^2 \to 2ax$.

***

#### DIfferentiation Rules:

> 1. $\nabla (af) = a \nabla f$ (constant rule)
> 2. $\nabla (f \pm g) =\nabla f \pm \nabla g.$ (sum rule)
> 3. $\nabla(fg) = g\nabla f + f \nabla g$. (product rule - note that the two terms on the right are both the results of *scalar multiplication*)
> 4. $\nabla \frac{f}{g} = \frac{g \nabla f - f \nabla g}{g^2}$ (division rule)
> 5. If *g* is a function of a *single* variable:
> ##### $$\nabla g(f(\vec{x}))= g'(f(\vec{x})) \nabla f (\vec{x}). $$
> This ends up being **scalar multiplication** and is analogous to the chain rule. 

***

#### Example:

![[Pasted image 20210912151456.png]]

***


#### Implicit DIfferentiation:

Sometimes $f(x,y) = 0$ may define *y* implicitly as a function of *x*. To differentiate, just differentiate both sides with respect to *x*, noting that *y* is itself a function of *x*. 


$$\begin{align} y^3 - 3y + 2x & = 0\\ 
3y^2y' - 3y' + 2 &= 0 \text{ (through the chain rule)} \\ 
y' &= \frac{-2}{3y^2 - 3}.
\end{align}$$

**Observation**: can be expressed in terms of partial derivatives: $f_x = 2$, $f_y = 3y^2 - 3$. Therefore:

> ## $$y' = -\frac{f_x}{f_y}.$$ 


***

### **Example**:
Let $f(x,y,z) = z^3 + (y^2+1)z + e^{2x} = 0.$

We will claim that $f(x,y,z) = 0$ defines $z$ implicitly as a function of *x* and *y*. To see if this is true, let's compute $z_x$ and $z_y$.

Partially differentiate both sides of $f=0$ with respect to *x*:

> #### $3z^2 z_x + (y^2+1)\,z_x + 2e^{2x} = 0$
> ## $z_x = \frac{-2e^{2x}}{3z^2 + y^2 + 1}$
> ## $= \frac{-f_x}{f_z}$.

**	Theorem**: when *z* is defined implicitly as a function of *x* and *y*, the following is true:


### $z_x = \frac{-f_x}{f_y}$
### $z_y = \frac{-f_y}{f_x}$

***


### Higher Derivatives:

Consider the function $f(x,y) = x e^{x \sin(y^2)}$. The two partial derivatives are:

- $f_x = e^{x \\sin(y^2)}+xe^{x\sin(y^2)}\sin(y^2)$
- $f_y = xe^{x\sin(y^2)}x\cos(y^2)2y$

These partial derivatives can themselves be differentiated - for example...

> $$(f_x)_x = f_{xx} = e^{x\sin(y^2)}\sin(y^2) + \sin(y^2) \left( e^{x\sin(y^2)} + xe^{x\sin(y^2)}\sin(y^2)\right).$$

The same logic applies to $f_{yy}$. The two successive derivatives taken need not be with respect to the same variable: for example, $f_{xy}$ denotes the partial derivative of $f$ with respect to *x*, differentiated again with respect to *y*. These four derivatives ($f_{xx},\,f_{yy},\,f_{xy},\,f_{yx}$) are the four **second partial derivatives**.



**Theorem**: if the second partial derivatives of $f(x_1,\dots,x_n)$ are continuous, then: 

> #### $$f_{x_ix_j} = f_{x_jx_i}\,\,[\text{equality of mixed partial derivatives}]$$

There are only very specific situations where this does not hold.

***
### The Multivariable Chain Rule:

***

