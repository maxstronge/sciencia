# Line Integrals of Vector Fields:

***

For the next several sections, we will focus our attention more specifically on the origin of the functions we seek to integrate. 

Recall: 

$$\va{r}: [a,b] \to \Rn,\,H = \va{r}([a,b]).$$

Consider a function $f: \Rn \to \RR.$ Such a function can be integrated in the following way:


### $$\int_{H}f(\va{x})ds = \int_a^b f(\va{r}(t))\,\|\va{r}(t)\|dt.$$

Our focus here is on the function $f(\va{x})$, and the set of such functions that produce interesting results. 



***

### Nonconstant $\va{F}$:

Recall [[Vector Fields]]. 

Consider a function $\va{F}(\va{x})$ that represents something like a force acting on a particle with position $\va{x}$. 

The work done by $\va{F}$ in moving a particle from position $\va{r}(t)$ to $\va{r}(t+dt)$ is:


### $$\begin{align} dW &= \va{F}\cdot(\va{r}(t+dt)-\va{r}(t)) \\ W = \int dW& = \int_a^b \va{F}(\va{r}(t))\cdot\va{r}'(t)dt. \end{align}$$

We can extract the component of work in the direction of motion similarly to how we did [[Directional Derivatives|earlier]]:


### $$\int_a^b\va{F}(\va{r}(t)) \cdot  $$

***

#### Notation for Vector Fields:

The function $\va{F}$ defines a **vector field** on $\Rn$, which can be written as a transformation:


### $$\va{r}:[a,b] \to \Rn .$$

We can define:


### $$\int_C \va{F}\cdot d\va{r} = \int_a^b \va{F}(\va{r}(t))\cdot\va{r}'(t)dt$$

as a generalized **line integral**.


***

### Examples:

Consider the following line segments:


![[lineintegral_examples.svg]]
 

**a.** Compute $\int_a^b \va{F}\cdot d\va{r}$ where $\va{F} = (y^2,\,2xy)$ and $C$ is the line segment from $(0,0)$ to $(1,1)$:



### $$\begin{align} \int_C \va{F}\cdot d\,\va{r} &=  \int_0^1\va{F}(t,t) \cdot (1,1)\,dt \\ &= \,\dots  \end{align}$$


**b.** Using the same function $\va{F}$, where $C$ is the arc of $y=x^2$ between $(0,0)$ and $(1,1)$. Instead of moving in a straight line ($C$ colinear with the line), we're now moving in a parabolic arc:

### $$\begin{align}\va{r}: [0,1] \to C \qq{} \va{r}(t) &= (t,t^2)\\ \va{r}'(t) &= (1,2t)\end{align}$$


### $$\int_C\va{F}\cdot d\,\va{r} = \dots$$

you will notice, when you finish this, that they are the same



**c.** Again using the same $\va{F}$, integrate over $C$ as specified above.


***

### The Fundamental Theorem of Calculus for Line Integrals:


## $$\int_C \nabla f \cdot d\va{r} = f(\va{r}(b)) - f(\va{r}(a)). $$


***

**E.g.** To show $\va{F}$ is **not** a gradient by showing its integrals are **not** independent of path (conservative). 

***

**E.g.**  Show that $\va{F} = (-y,x)$ is not a gradient by showing that:

> ###  $$\int_{C_1} \va{F} \cdot d\,\va{r} \neq  \int_{C_2} \va{F} \cdot d\,\va{r} .$$