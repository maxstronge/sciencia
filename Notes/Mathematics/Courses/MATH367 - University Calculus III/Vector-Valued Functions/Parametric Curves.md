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

The curve  $x^{2/3}+y^{2/3} = a^{2/3}$ is called an **astroid**. We can again use  $\cos^2 t + \sin^2 t = 1$, this time setting $\cos t =\qty( \frac{x}{a})^{1/3}$ and $\sin t =\qty( \frac{y}{b})^{1/3}$