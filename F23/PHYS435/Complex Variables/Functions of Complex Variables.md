### Functions of Complex Variables
#### K.F. Riley 24.1

***

The quantity $f(z)$ is said to be a function of the complex variable $z=x+iy$ if to every value of $z$ in some region $R$ of the complex plane (i.e. the **Argand Diagram**) there corresponds one or more values of $f(z)$. Thus the output of a complex function, given a complex number as input, is one or more complex numbers. 

In this framing, $f(z)$ can be any function consisting of a real and imaginary part, each of which is (in general) itself a function of $x$ and $y$. If we denote the real and imaginary parts of $f(z)$ by $u$ and $v$, respectively, then

$$
f(z) = u(x,y) + i\,v(x,y)
$$
We will be primarily concerned for our purposes with functions that are single-valued, so that to each value of $z$ there corresponds just one value of $f(z)$. We also restrict our attention to functions that are *differentiable* in a particular sense, which we will now discuss further. 

### Differentiability of Functions of Complex Variables

A function $f(z)$ that is **single-valued** in some domain $R$ is **differentiable** at the point $z$ in $R$ if the derivative 

$$
f'(z) = \lim_{ \Delta z \to 0 } \left[ \frac{f(z+\Delta z)-f(z)}{\Delta z} \right] 
$$

exists and is unique, i.e. its value does not depend on the direction from which $\Delta z$ tends to zero in the Argand diagram.

***
