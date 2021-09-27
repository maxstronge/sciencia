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