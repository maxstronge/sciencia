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

> #### $$f_x(x,y)= \frac{1}{1+(\frac{y}{x})^2}(\frac{-y}{x^2}) =  - \frac{y}{x^2(1+\frac{y^2}{x^2})}.$$

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

$$f_{x_1} =  $$