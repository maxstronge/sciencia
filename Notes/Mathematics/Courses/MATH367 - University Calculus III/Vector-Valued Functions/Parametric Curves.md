# Parametric Curves: 
***

We now turn our attention to vector-valued functions of one real variable - primarily, a function that assigns to each real number $t$ (typically in some interval of note) a vector $\va{r}(t)$. For example:

$$\va{r}(t) = \qty(x(t),y(t),z(t))$$

...might be the position of some particle at time $t$. As $t$ varies, $\va{r}(t)$ sweeps out a curve: 

![[Pasted image 20211028124703.png|Vector-valued function of one real variable example]]

While in some applications (mostly in physics) the variable $t$ will indeed be time, there is no requirement for this. Any parameter that is used to label the different points on a curve will do. We then say that $\va{r}(t)$ is a **parameterization** of the curve. 

***

### Parameterization of a circle (centered at origin): $(x^2+y^2=a^2)$

Consider the circle $x^2+y^2=a^2$.

![[Pasted image 20211028125020.png|Parameterization of a circle]]

A natural choice of parameter for the circle above would be to use the angle $\theta$ to label the point $(r\cos\theta,\,r\sin\theta).$ That is:

### $$\va{r}(\theta) = (a\cos\theta,\,a\sin\theta) \qq{} 0 \leq \theta \leq 2\pi$$

...is a parameterization of the circle $x^2+y^2=a^2$. As $\theta$ runs from $0\to2\pi$, $\va{r}$ traces out the entire circle. 

***

### Parameterization of a circle (generalized): $\qty((x-h)^2+(y-k)^2 = a^2)$

We can tweak the above parameterization to parameterize the circle of radius $a$ centered on the point $(h,k)$. 

![[Pasted image 20211028125708.png|Parameterized circle, generalized]]

We can see from the figure that:

### $$\va{r}(\theta) = (h+a\cos\theta,\,k+a\sin\theta)\qq{}0\leq\theta\leq2\pi$$

...is a parameterization.

### Parameterization of an ellipse: $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$

We can build several parameterizations from the equation $\cos^2 t + \sin^2 t = 1$. In the case of an ellipse, if we set $\cos t = \frac{x}{a}$ and $\sin t = \frac{y}{b}$, we find that a parameterization can be written:

### $$\va{r}(t) = (a\cos t, b\sin t)\qq{}0\leq t\leq 2\pi$$

![[Pasted image 20211028130452.png|Parameterized ellipse]]

### Parameterization of an astroid: $x^{2/3}+y^{2/3} = a^{2/3}$

The curve  $x^{2/3}+y^{2/3} = a^{2/3}$ is called an **astroid**. We can again use  $\cos^2 t + \sin^2 t = 1$, this time setting $\cos t =\qty( \frac{x}{a})^{1/3}$ and $\sin t =\qty( \frac{y}{b})^{1/3}$ to get:

### $$\va{r}(t) = \qty(a\cos^3 t,\, a\sin^3 t)\qq{}0\leq t\leq 2\pi$$

...as a parameterizaton for  $x^{2/3}+y^{2/3} = a^{2/3}$, shown below:

![[Pasted image 20211028131147.png|Parameterized astroid]]


### Parameterizations of single-variable functions: $y=f(x)$

A very easy method to parameterize functions is to simply use $x$ or $y$ as the parameter. For example, the function $e^y = 1+x^2$ can be solved for $y$ as a function of $x$, becoming $y =\ln(1+x^2)$. We can then easily use $x$ as the parameter by setting $x=t$:

### $$\va{r}(t) = \qty(t,\,\ln(1+t^2))\qq{}-\infty \leq t \leq \infty$$

### Parameterization of parts of a circle: 

It is quite common to use $x$ or $y$ to parameterize parts, but not all, of a curve. A simple example is again the circle $(x^2+y^2=a^2)$: for each $-a\leq x \leq a$, there are two points on the circle with that value of $x$. The same applies to each $-a\leq y \leq a$. Therefore, $x$ or $y$ cannot be used to parameterize the entire circle - but we can provide parameterizations (with one parameter) of *half* the circle in the following way: 


### $$\begin{align}\va{r}(t) &= \qty(t,\, \sqrt{a^2-t^2})\qq{}-a\leq t  \leq a \\[2ex]\va{r}(t) &=  \qty(t,\,- \sqrt{a^2-t^2})\qq{}-a\leq t  \leq a\end{align}$$

The above two equations parameterize the top half and bottom half of a circle (respectively) using $x$ as a parameter, and:

### $$\begin{align}\va{r}(t) &= \qty(\sqrt{a^2-t^2},\, t)\qq{}-a\leq t  \leq a \\[2ex]\va{r}(t) &=  \qty(-\sqrt{a^2-t^2},\,t)\qq{}-a\leq t  \leq a\end{align}$$

...provide parameterizations of the right and left half, respectively, using $y$ as a parameter. 


### Parameterization of intersection of surfaces:

Curves often arise as the intersection of two surfaces. For example, the intersection of the ellipsoid $x^2+\frac{y^2}{2}+\frac{z^2}{3}=1$ with the paraboloid $z=x^2+2y^2$ is the blue curve in the figure below:

![[Pasted image 20211028132524.png|Intersection of surfaces]]

One way to parameterize such curves is to choose one of the three coordinates $x,\,y,\text{ or }z$ as the parameter, and solve the given equations for the remaining two coordinates *as functions of* that parameter. 

The following examples demonstrate this process.

>The set of all $(x,y,z)$ satisfying the equations:
> $$\begin{align}x^3 - e^{3y} &= 0 \\ x^2 - e^y + z &= 0 \end{align}$$
> is a curve. We can choose to use $y$ as the parameter and think of:
> $$\begin{align}x^3 &= e^{3y} \\ x^2 + z &= e^y \end{align}$$
> ....as a system of equations for the two unknowns $x$ and $z$, with $y$ being treated as a given constant, rather than as an unknown. We can now solve the first equation for $x$:
> $$x^3 = e^{3y} \implies x = e^y $$
> ....and then subsitute that result into the second equation to solve for $z$:
> $$x^2 + z = e^y \implies e^{2y} + z = e^y \implies z = e^y - e^{2y} $$
> which gives us the parameterization:
> ### $$\va{r}(y) = \qty(e^y,\,y,\,e^y - e^{2y}). $$


> The previous example was set up such that we could easily solve for $x$ and $z$ as functions of $y$. In practice, this is rarely so straightforward. A more realistic example is the set of all $(x,y,z)$ obeying:
> $$\begin{align}x^2 + \frac{y^2}{2} + \frac{z^2}{3} &= 1 \\ x^2 + 2y^2 &= z.\end{align}$$
> ...which is the blue curve in the figure above. 