# Vector-Valued Functions:

***

To this point, we have exclusively considered real (scalar) valued functions of a vector variable. Now, we expand our focus to **vector-valued** functions of a vector variable, which take this form:

### $$\vec{f}: \RR^n \to \RR^m.$$
The function $f$ will now result in a vector (we assume $m>1$).

There are three main cases to consider:

- $m > n$
- $m = n$
- $m < n$

***

Let us begin by examining a common case: 

$$\vec{f}: \RR \to \RRii .$$

This function takes a real number as input and returns a point in $\RRii$. For example:

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