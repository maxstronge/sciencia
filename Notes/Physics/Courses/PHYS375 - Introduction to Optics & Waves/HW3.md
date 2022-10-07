# PHYS375 Homework Assignment 3
## Max Stronge (30064749)
***

### **Written Response**:

1. Consider a function $f(x)$:

![[Pasted image 20220927205228.png]]

Say we want to generate another function $g$ that is an approximation for the function $f$ at a particular point, $x=0$. We could start by just taking the literal value of the function of that point, $g=f(0)$:

![[Pasted image 20220927205537.png]]

This is of course exactly equal to $f$ at $x=0$, but becomes a pretty poor approximation to $f$ once you start to move in either direction from $x=0$. It would be better if our function didn't just have the same value of $f(x)$ at $x=0$, but it also had the same slope as $f$ at that point, such that

$$g(x) = f(x) + f'(x)x$$

![[Pasted image 20220927210239.png]]

The approximation $g(x)$ is still equal to $f(x)$ at the point in question, but it now approximates $f$ much better at points surrounding $x=0$. If we then ensure the function $g$ has the same second derivative as $f$, we will not only take on the slope of $f$ at that point, but also some of the curvature of $f$:

![[Pasted image 20220927211545.png]]

...and the approximation becomes better still. The Taylor expansion simply takes this process even further, adding more derivatives to improve the approximation further and further:
![[Pasted image 20220927211818.png]]

All of this was done with the idea of approximating $f$ at a particular point $x$, and with each term added, the function $g$ became a better approximation of $f$ *in the neighborhood* of $x=0$. 

***

2. Say we have an object moving along the $x$-axis, such that the position $x$ of the object is a function of $t$, $x=x(t)$. We can write a Taylor expansion of the function $x(t)$ in the following way:


Say we want to predict the position of the object at some time $t_f$ after the initial time $t_i = 0$. We will say

$$x(t_f) \approx x(t_i)$$

to start, but this is obviously not correct -  this would not be a very good approximation for a moving object. It would imply that the object has no velocity - so to improve the approximation, let's ensure the velocity of our approximation function is the same as the velocity of $x(t)$ at the given time. Adding the next term of the Taylor expansion:

$$x(t_f) \approx x(t_i) + x'(t_i)t$$

....since the point in question here is $t_i = 0$. This will result in an object with constant velocity, but will not approximate any acceleration in the object's motion very well. Adding another term, we find:

$$x(t_f) \approx x(t_i) + x'(t_i)t + \frac{x''(t_i)}{2!}t^2$$

Noting that $x(t_f)=x_f$ and $x(t_i)=x_i$, we have

$$x_f = x_1 + \dv{x}{t}t+\frac{1}{2}\dv[2]{x}{t} t^2$$

....which, in the neighborhood of a small timestep $\DD t$ away from $t=0$$, we find:

$$x_f = x_1 + \dv{x}{t}\DD t+\frac{1}{2}\dv[2]{x}{t} \DD t^2$$

which is identical to the form of the first kinematic equation learned in introductory mechanics. There are further terms including the higher derivatives of $x$, but they are negligible in terms of the object's motion. 

***

3.  Starting from $$x_f = x_1 + \dv{x}{t}\DD t+\frac{1}{2}\dv[2]{x}{t} \DD t^2$$


we can add more terms following the Taylor series expansion:

$$x_f = x_1 + \dv{x}{t}\DD t+\frac{1}{2}\dv[2]{x}{t} \DD t^2 + \frac{1}{6}\dv[3]{x}{t} \DD t^3 + \frac{1}{24}\dv[4]{x}{t}\DD t^4 + \frac{1}{120}\dv[5]{x}{t}\DD t^5  + \frac{1}{720}\dv[6]{x}{t}\DD t^6$$

I am going to guess here that all of the coefficients added after $\frac{1}{2}\dv[2]{x}{t} \DD t^2$ are either zero or so close to zero they will be negligible in practice, since the product of small differentials $\DD t$ become vanishingly small as the coefficients continue. In fact, this kinematic equation itself is an approximation learned in high school for cases of constant acceleration (*i.e.* the jerk and all higher derivatives are zero), so I will rephrase my guess to say that every derivative higher than the second is zero and hence all coefficients after the second will be zero. 

***

### **Calculation Questions**:

2. Find the first three terms of the Taylor series expansion of $f(x)=\tan(x^2)$ about $x=1$.

**Solution**:

$$\begin{align}
f(x)&=\tan(x^2)\\ &\approx \tan(1)+2\sec^2(1)(x-1) +\frac{2\sec^2(1)+8\sec^2(1)\tan(1)}{2}(x-1)^2.

\end{align}
$$

***

3.

a) Find 2 different complex numbers $z$ that are square roots of $i$ (*i.e.* $z^2=i$).
b) Find 1 value for $z$ such that $z^4=i.$

**Solution**:

a) 

Take a complex number $z=a+ib=\sqrt{i}$. 

We then have $(a+bi)^2 = a^2 + 2abi+b^2i^2 = (a^2-b^2)+2abi = 0.$ Thus, we have the following two relations:

$$a^2-b^2=0 \implies a^2 = b^2$$

...which means that $a$ and $b$ are either equal or opposite, and 

$$2abi = 0 -\implies 2ab=1 \implies ab = \frac{1}{2}$$

....and since the product of $a$ and $b$ is positive, we know $a=b$. Rewriting the second equation, we have:

$$ab=a^2=\frac{1}{2} \implies a = \frac{\pm1}{\sqrt{2}} = \frac{\pm\sqrt{2}}{2}$$

and since $a=b$, we now know the two square roots of $i$:
$$\sqrt{i}=\left(\frac{\sqrt{2}}{2} + \frac{\sqrt{2}}{2}i\right)$$
and
$$\sqrt{i}=\left(-\frac{\sqrt{2}}{2} - \frac{\sqrt{2}}{2}i\right).$$


b) 

To start, we can make use of the identity that

$$i=e^{\frac{i\pi}{2}}.$$

Taking that to the power of $1/4$, we get

$$i^{\frac{1}{4}} = \left( e^{\frac{i \pi}{2}} \right)^{\frac{1}{4}} = e^{\frac{i \pi}{8}}.$$

We can then use Euler's identity to show that

$$e^{\frac{i \pi}{8}}=\cos(\pi/8) + i \sin(\pi/8)$$

which evaluates to the complex number 

$$z=\frac{\sqrt{2+\sqrt{2}}}{2} + \frac{\sqrt{2+\sqrt{2}}}{2}i$$


....which is one of the possible complex numbers equal to $i^{\frac{1}{4}}$.

***

Chapter 2, Q12:

**Solution**:

Phase velocity $c_p = \frac{\oo}{k} = \sqrt{\frac{g}{m}+\frac{T_s}{\rho_m}k} \implies \oo = k\sqrt{\frac{g}{m}+\frac{T_s}{\rho_m}k}$.

We can find the group velocity as $\dv{\oo}{k}$:

$$\dv{\oo}{k} = \dv{k}\left[ k\sqrt{\frac{g}{m}+\frac{T_s}{\rho_m}k}\right] = \frac{g \rho_m+3k^2 T_s}{2 k \rho_m\sqrt{\frac{g}{m}+\frac{T_s}{\rho_m}k}} = c_g.$$

The shortest moving wavelength component will be the one with the longest wavelength.
***
Chapter 3, Q3:

Show that $\cos x = \frac{e^{ix}+e^{-ix}}{2}$ and that $\sin x = \frac{e^{ix}-e^{-ix}}{2i}$.

**Solution**:

First, we can note that $\cos x$ is an *even* function, $\cos(-x)=
cos(x)$, and $\sin{x}$ is an *odd* function, $\sin (-x) =-\sin(x)$. This will come in handy in a second. 

We can write $e^{ix}$ as $\cos x + i \sin x$. We can also write $e^{i(-x)}$ as $\cos (-x) +\sin (-x) = \cos x - \sin x$, due to the even/odd nature of the functions described above. Thus:

$$e^{ix}+e^{-ix} = (\cos x + i \sin x) + (\cos x - i \sin x) = 2\cos x$$

Dividing both sides by $2$ we find

$$\cos x = \frac{e^{ix}+e^{-ix}}{2}$$

...QED part 1. Following very similar logic, we can examine the second equality:

$$e^{ix}-e^{-ix} = (\cos x + i \sin x) - (\cos x - i \sin x) = 2i\sin x$$

$$\sin x = \frac{e^{ix}-e^{-ix}}{2i}$$

...QED part 2. 

***

4. Electromagnetic waves in the ionosphere are described by the following differential equation:


$$\pdv[2]{E}{t} + \oo_p^2 E = c^2 \dv[2]{E}{x}$$

...where $\oo_p$ is the *plasma frequency*, which is a constant. Show that the dispersion relation for this wave is given by $$\oo^2 = \oo_p^2 + c^2k^2.$$

**Solution**:

Assume the electric field is a function of time and space like a typical wave $E=E(x,t) = Ae^{i(kx-\oo t)}$. We are by this point very familiar with the two second derivatives of this function, with respect to $t$ and $x$:

$$
\begin{align}

\pdv[2]{E}{t} &= -A\oo^2e^{i(kx-\oo t)} \\ 

\\

\pdv[2]{E}{x} &= -Ak^2e^{i(kx-\oo t)}


\end{align}
$$

Inserting these into our equation, we find:

$$-A\oo^2e^{i(kx-\oo t)} + \oo_p^2 E = (c^2)(-Ak^2e^{i(kx-\oo t)})$$

And noting that $E=E(x,t) = Ae^{i(kx-\oo t)}$, we have

$$
\begin{align}

-A\oo^2e^{i(kx-\oo t)} + \oo_p^2 Ae^{i(kx-\oo t)} &= -Ak^2c^2e^{i(kx-\oo t)} \\ 
\\

\oo^2 + \oo_p^2  &= c^2k^2


\end{align}
$$

***

Chapter 3, Q7:

Show that the differential equation to yield the dispersion relation of a water wave $\oo^2=gk$ can be given by either 
$$\pdv[2]{\xi}{t}=i g \pdv{\xi}{x}$$

or 

$$\pdv[4]{\xi}{t} + g^2\pdv[2]{\xi}{x}=0.$$

**Solution**:

Assume $\xi(x,t)=Ae^{i(kx-\oo t)}.$ Thus:

$$\pdv[2]{\xi}{t}=-A\oo^2e^{i(kx-\oo t)}$$

$$\pdv{\xi}{x}=Aike^{i(kx-\oo t)}$$

Thus $$-A\oo^2e^{i(kx-\oo t)} = i g (Aike^{i(kx-\oo t)})$$

$$-A\oo^2e^{i(kx-\oo t)} =  -gk Ae^{i(kx-\oo t)})$$

$$\oo^2 = gk.$$

Alternately, we can note that 

$$\pdv[4]{\xi}{t} = \oo^4 Ae^{i(kx-\oo t)} $$

And $$\pdv[2]{\xi}{x} = -Ak^2e^{i(kx-\oo t)}$$

Therefore

$$\oo^4 Ae^{i(kx-\oo t)} = -g^2(-Ak^2e^{i(kx-\oo t)})$$

and $$\oo^4 = g^2k^2 \implies \oo^2 = gk. $$

***

