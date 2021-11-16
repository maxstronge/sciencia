# Vector-Valued Functions:

***

To this point, we have exclusively considered real (scalar) valued functions of a vector variable. Now, we expand our focus to **vector-valued** functions of a vector variable, which take this form:

### $$\vec{f}: \Rn \to \Rm$$
In other words, the function $f$ will now result in a vector (we assume $m>1$). We are now examining functions that assign to each $t\in\RR$ a vector $\vec{f}(t)$

There are three main cases to consider:

- $m > n$
- $m = n$
- $m < n$

***

Let us begin by examining a common case: 

$$\vec{f}: \RR \to \Rii .$$

This function takes a real number as input and returns a point in $\Rii$. For example:

> $$\vec{f}(t) = (\cos t, \sin t). $$

![[Pasted image 20210927141317.png]]

We can say that $\vec{f}$ returns a vector with the **component functions** of $\vec{f}$ as the elements of the vector, as below:

### $$\vec{f}(t) = \left( \vec{f_1}(t),\vec{f_2}(t), \,\dots\, \vec{f_m}(t) \right)$$

It is by no means required that a vector-valued function maps to or from $\RR$ - we could have a function $\vec{f}:\RRii \to \RRiii$. Such functions plot a **parametric surface**, rather than a **parametric curve**. 


***

What about functions $\vec{f}: \RR^n \to \RR^n$?

These typically come up in the context of *vector fields* (of which the gradient is an example) and *changes of variable*. 


***

### Changes of Variable: 

Consider a function $\vec{f}: \RRii \to \RRii.$


One popular example of such a function is the function:

### $$\vec{f}(r,\theta) = \left(r\cos\theta,\,r\sin\theta\right). $$

You may recognize this function - it is the function that converts polar coordinates in $r$ and $\theta$ to a vector $(x,y)$, since the conversion is $x = r\cos\theta$, etc. 

This is a transformation $\RRii \to \RRii$ that we've seen before, but now we can explicitly write it as a vector-valued function. 

***

### The Chain Rule for Vector-Valued Functions of a Vector Variable:

Consider the function $f(x,y)$ where $x = x(r,\theta)$ and $y = y(r,\theta)$. Clearly $f$ is also a function of $r\text{ and }\theta$ through the dependencies of $x$ and $y$.

If we use the familiar $x = r\cos\theta,\, y = r\sin\theta$, we can define a new function $F$ that is a composition of the component functions:

$$F(r,\theta) = f(x(r,\theta),\,y(r,\theta)). $$

When $r$ or $\theta$ vary in the function above, both the x-arguments and the y-arguments of $f$ vary as well. Consequently, the chain rule for $f\,(x(r,\theta),\,y(r,\theta))$ is the sum of two terms: one resulting from the variation of the x-argument, and the other from the variation of the y-argument. 

***

### **Theorem:** 

Assume that all first order partial derivatives of $f(x,y)$, $x(r,\theta)$, and $y(r,\theta)$ exist and are continuous. Then the same is true for $F(r,\theta) = f(x(r,\theta),\,y(r,\theta))$, and:


>  $$\begin{align} \pdv{F}{r} (r,\theta) &= \pdv{f}{x} (x(r,\theta),\,y(r, \theta))\pdv{x}{r} (r,\theta) + \pdv{f}{y} (x(r,\theta),\,y(r, \theta))\pdv{y}{r} (r,\theta). \\ \pdv{F}{\theta}(r,\theta) & = \pdv{f}{x} (x(r,\theta),\,y(r, \theta))\pdv{x}{\theta} (r,\theta) + \pdv{f}{y} (x(r,\theta),\,y(r, \theta))\pdv{y}{\theta} (r,\theta).\end{align}  $$

![[Pasted image 20211028204231.png]]