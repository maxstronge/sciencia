# Assignment 3
## Max Stronge (30064749)



***

### 1. Systematic Approach for Calculating Convolution Integrals

#### a) 

Show that 
$$
\mathcal{L}\left[ H(t-a)f(t-a) \right] = e^{-as} \bar{f}(s) 
$$

From the definition of the Laplace transform:

$$
\mathcal{L}\left[ H(t-a)f(t-a) \right] = \int_{0}^{\infty} e^{-st}H(t-a)f(t-a) \, dt 
$$

Because the Heaviside function is equal to zero in the range $(0,a)$, presuming $a$ is positive, we can change the bounds of the integral and eliminate $H(t-a)$ from the integrand:

$$
= \int_{a}^{\infty} e^{-st} f(t-a) \, dt
$$

If we then let $u=t-a \implies t = u+a$ and $dt=du$, we have

$$
\int_{a}^{\infty} e^{-s(u+a)}f(u) \, du = e^{-sa}\int_{a}^{\infty} e^{-su}f(u) \, du 
$$

and the integrand is now just the Laplace transform of $f(u)$, leaving us with 

$$
=e^{-sa}\bar{f}(s).
$$

#### b)


To find the convolution integral, then, we can instead find the product of the Laplace transforms of $f_{1}$ and $f_{2}$ and then take the inverse Laplace transform of the result. 

For the two functions 
$$
\begin{align}
f_{1}(t) &= \begin{cases}
2  , & 0\leq t\leq 2 \\
0  , & \text{otherwise}
\end{cases} \\  \\

f_{2}(t) &= \begin{cases}
-t+2, & 0\leq t\leq 2 \\
0  , & \text{otherwise}
\end{cases} \\

\end{align}
$$

which represent a rectangular and triangular pulse, respectively, we can find the convolution integral using the above result and the convolution theorem for Laplace transforms:

$$
\mathcal{L}\left[ \int_{0}^{t} f(u)g(t-u) \, du  \right] = \bar{f}(s)\bar{g}(s)
$$

where $\int_{0}^{t} f(u)g(t-u) \, du = (f \ast g) (t)$.

To start, we find the Laplace transform of $f_{1}$ and $f_{2}$. 

$$
\mathcal{L}\left\{ f_{1}(t) \right\} =\int_{0}^{\infty} e^{-st}f_{1}(t) \, dt = 2 \int_{0}^{2} e^{-st} \, dt 
$$
$$
= \frac{2}{s}\left( 1-e^{-2s} \right) 
$$
and 

$$
\mathcal{L}\left\{ f_{2}(t) \right\} =\int_{0}^{\infty} e^{-st}f_{2}(t) \, dt = \int_{0}^{2} e^{-st}(-t+2) \, dt = -\int_{0}^{2} te^{-st} \, dt + 2\int_{0}^{2} e^{-st} \, dt   
$$
$$
= \frac{2}{s}\left( 1-e^{-2s} \right)  - \int_{0}^{2} te^{-st} \, dt 
$$

...where the second integral can be evaluated using integration by parts, setting $u=t$ and $dv = e^{-st}dt$, leading to $du = dt$ and $v = -\frac{1}{s}e^{-st}$:

$$
\int_{0}^{2} te^{-st} \, dt  = \left[ (t)\frac{-1}{s}e^{-st} \right] _{0}^{2}- \frac{1}{s}\int_{0}^{2} e^{-st} \, dx 
$$

and so
$$
\mathcal{L}\left\{ f_{2}(t) \right\} = \frac{2}{s} \left( 1+\frac{e^{-2s}}{s^{2}} \right) 
$$

and the product is then

$$
\mathcal{L}\left\{ f_{1}(t) \right\} \cdot \mathcal{L}\left\{ f_{2}(t) \right\} =\left(  \frac{2}{s}\left( 1-e^{-2s} \right)   \right) \cdot \left( \frac{2}{s} \left( 1+\frac{e^{-2s}}{s^{2}} \right)  \right) 
$$

and, expanding this out, we are left with 

$$
\bar{f_{1}}(s)\cdot \bar{f_{2}}(s)= \frac{4e^{-2s}}{s^{3}}-\frac{2}{s^{3}}-\frac{2e^{-4s}}{s^{3}}+\frac{4}{s^{2}} - \frac{4e^{-2s}}{s^{2}}$$
We now need to find the inverse Laplace transform of this expression to find the value of the convolution integral we were after. Recalling that the inverse Laplace is linear and unique, i.e. 

$$
\mathcal{L}^{-1}\left[ a \bar{f}(s) + b \bar{g}(s) \right] = af(t) + bg(t)
$$

we can look at the above term by term:

$$
\begin{align}
\mathcal{L}^{-1}\left[ 4 \frac{e^{-2s}}{s^{3}} \right] &= 2(t-2)^{2}H(t-2) = 2t^{2}H(t-2)-8tH(t-2)+8H(t-2) \\

\\
\mathcal{L}^{-1}\left[  \frac{2}{s^{3}}   \right] &= t^{2} \\
\\
\mathcal{L}^{-1}\left[  \frac{2e^{-4s}}{s^{3}}   \right] &= (t-4)^{2}H(t-4) = t^{2}H(t-4)-8tH(t-4)+16H(t-4) \\
\\
\mathcal{L}^{-1}\left[  \frac{4}{s^{2}}   \right] &= 4t \\
\\
\mathcal{L}^{-1}\left[  \frac{4e^{-2s}}{s^{2}}   \right] &= 4(t-2)H(t-2) = 4tH(t-2)-8H(t-2)

\end{align}
$$

thus 

$$
\mathcal{L}^{-1}\left[ \bar{f_{1}}(s) \bar{f_{2}}(s) \right] = 2t^{2}H(t-2)-8tH(t-2)+8H(t-2) - t^{2} - t^{2}H(t-4) + \dots
$$
$$
= - t^2 + 4 t+ -t^2H(t - 4) + 2 t^2 H(t - 2) + 8 t H(t - 4) - 12 t H(t - 2) - 16 H(t - 4) + 16 H(t - 2) 
$$




#### c) 

When $t<0$, both functions are zero and thus the convolution will also be zero. 

#### d)

In the interval $0\leq t\leq 2$, all the terms involving the Heaviside functions shifted by $2$ and $4$ are zero, and so the above expression reduces to 
$$
\mathcal{L}^{-1}\left[ \bar{f_{1}}(s) \bar{f_{2}}(s) \right] = 4t-t^{2}
$$

#### e)

Over the interval $2\leq t\leq 4$, all the Heaviside functions shifted by $2$ 'switch on', and all the $H(t-4)$ terms are still zero, leaving us with 

$$
= 2t^{2}-8t+8 - t^{2} + 4t - 4t+8
$$
$$
= (t-4)^{2}
$$

#### f)

For $t>4$, the two functions are no longer overlapping each other, as each is only nonzero in the interval $(0,2)$. Thus the convolution will be zero after $t=4$. 

#### g)

![[Figure_1g.png]]


***


### 2. Laplace Transforms for Solving Integrals

#### a)

Show that 
$$
\int_{s}^{\infty} \bar{f}(u) \, du = \mathcal{L}\left\{ \frac{f(t)}{t} \right\} 
$$
If we rewrite $\bar{f}(u)$ in terms of $f(t)$:

$$
\bar{f}(u) = \int_{0}^{\infty} e^{-ut}f(t) \, dt 
$$

and if we replace that in the original expression we find

$$
\int_{s}^{\infty} \left( \int_{0}^{\infty} e^{-ut}f(t) \, dt  \right)  \, du
$$

and since $f(t)$ has no dependence on $u$, we can rearrange the integrand as follows:

$$
\int_{0}^{\infty}  \left( \int_{s}^{\infty} e^{-ut} \, du  \right)f(t) \, dt 
$$

and the central integral evaluated from $s$ to $\infty$ is $$\frac{e^{-st}}{t}$$

Thus we have

$$
\int_{0}^{\infty} \frac{e^{-st}}{t}f(t) \, dt = \int_{0}^{\infty}e^{-st} \frac{f(t)}{t}\, dt 
$$
which is, by definition, 

$$
= \mathcal{L}\left\{ \frac{f(t)}{t} \right\} .
$$

#### b)

Following an identical procedure as before, we arrive at the rearranged expression 

$$
\int_{0}^{\infty}  \left( \int_{0}^{\infty} e^{-ut} \, du  \right)f(t) \, dt $$
...where the only difference is that both integrals have $0$ for the lower bound. This time, however, the central integral evaluates simply to $\frac{1}{t}$ because of the zero on the lower bound, leaving us with


$$
 \int_{0}^{\infty} \frac{f(t)}{t}\, dt 
$$

which is also equal to the definition of the Laplace transform for $\frac{f(t)}{t}$ when $s=0$, i.e. $e^{-st}=1$.

#### c)

Using the above results, we can show that 

$$
\int_{0}^{\infty} \frac{\sin(t)}{t} \, dt = \frac{\pi}{2} 
$$

in the following way. Recalling that 
$$
\int_{s}^{\infty} \bar{f}(u) \, du = \mathcal{L}\left\{ \frac{f(t)}{t} \right\} 
$$
it will be easier to integrate the Laplace transform of $\sin(t)$, which is known to be 

$$
\mathcal{L}\left\{ \sin(t) \right\} = \frac{1}{s^{2}+1}
$$
We can also recognize that the integral of that expression is $\arctan(s)$, and evaluating that at $\infty$ and $0$ results in 

$$
\arctan(s)|_{0}^{\infty}= \arctan(\infty)-\arctan(0) = \frac{\pi}{2}.
$$

***

### 3. Conjugate Physical Quantities in Quantum Mechanics

Note that $x$ and $p$ are Fourier conjugate variables, and as such can be written in terms of each other as Fourier transforms:

$$
\psi(x) = \frac{1}{\sqrt{ 2\pi }}\int_{-\infty}^{\infty} \phi(p)e^{\frac{-ipx}{\hbar} } \, dp 
$$
If we take the partial derivative of this expression with respect to $x$, we find

$$
\frac{ \partial  }{ \partial x } \psi(x) = \int_{-\infty}^{\infty} \psi(p) \frac{ \partial  }{ \partial x } \left( e^{\frac{-ipx}{\hbar}} \right)  \, dp =\frac{i}{\sqrt{ 2\pi } \hbar} \int_{-\infty}^{\infty} p\, \psi(p)e^{\frac{-ipx}{\hbar}} \, dp 
$$

If we rearrange this, we find it also has the form of a Fourier transform:

$$
-i \hbar \frac{ \partial  }{ \partial x } \psi(x)=\frac{1}{\sqrt{ 2\pi }}\int_{-\infty}^{\infty} p\, \psi(p) e^{\frac{-ipx}{\hbar}}\, dp 
$$

And the inverse of this transform would be 

$$
p\, \psi(p) = \frac{1}{\sqrt{ 2\pi }}\int_{-\infty}^{\infty} -i \hbar \psi(x) e^{\frac{-ipx}{\hbar}}\, dx 
$$

And we have an expression for $p \cdot \psi(p)$ in terms of $x$ - now we just need to find the complex conjugate of $\psi(p)$, $\psi^*(p)$, and we will be able to form the expectation value $\langle p \rangle$ according to the given formula. 

We can do this by simply conjugating the expression for $\psi(p)$ in terms of $x$:

$$
\begin{align}
\psi(p) &= \frac{1}{\sqrt{ 2\pi }}\int_{-\infty}^{\infty} \psi(x)e^{\frac{-ipx}{\hbar}} \, dx  \\

\\ \\
\psi^*(p) & =\frac{1}{\sqrt{ 2\pi }}\int_{-\infty}^{\infty} \psi^*(x')e^{\frac{ipx'}{\hbar}} \, dx' 
\end{align}
$$

...where the prime has been added to keep it distinct from the other $x$. 

We can then use these results to rewrite the expression for the expectation value for momentum:


$$
\begin{align}
\langle p \rangle &= \int_{-\infty}^{\infty} \psi^{*}(p) (p) \psi(p) \, dp \\

\\
&=\int_{-\infty }^{\infty} \left[ \frac{1}{\sqrt{ 2\pi }}\int_{-\infty}^{\infty} \psi^*(x')e^{\frac{ipx'}{\hbar}} \, dx'  \right]  \left[ \frac{1}{\sqrt{ 2\pi }}\int_{-\infty}^{\infty} -i \hbar \psi(x) e^{\frac{-ipx}{\hbar}}\, dx  \right] \, dp
\end{align}
$$

Rearranging, we have

$$
= \int_{-\infty}^{\infty}\int_{-\infty}^{\infty}  \psi^{*}(x) (-i\hbar)\frac{ \partial  }{ \partial x' } \left( \psi(x') \right)  \left[ \frac{1}{2\pi}\int_{-\infty}^{\infty} e^{\frac{ip}{\hbar}(x-x')} \, dp \right]  \, dxdx'
$$

and we can rewrite the integral in square brackets as a delta function $\delta(x-x')$, allowing us to integrate out the primed variable and leaving us with 

$$
\langle p \rangle = \int_{-\infty}^{\infty} \psi^{*}(x) \left[ -i\hbar \frac{ \partial  }{ \partial x } \right]\psi(x)  \, dx 
$$

and we have found the momentum operator in position representation.


***

### 4. Solving IVP with Laplace Transform Properties

Use the properties of the Laplace transform to obtain the solution of the differential equation 

$$
\frac{d^{2}f(t)}{dt^{2}}-2 \frac{df(t)}{dt}+2f(t)=\cos t
$$

with boundary conditions $f(0)=1$ and $\frac{df(t)}{dt}=0$ at $t=0$. 

If we take the Laplace transform of both sides of the differential equation, we find

$$
s^{2} \bar{f}(s) - sf(0) - f'(0) - 2\left( s \bar{f}(s) -f(0) \right) +2 \bar{f}(s) = \frac{s}{s^{2}+1}
$$
but we have initial conditions for $f(0)$ and $f'(0)$, so we can simplify to 

$$
s^{2} \bar{f}(s) - s - 2s \bar{f}(s) + 2 + 2\bar{f}(s) = \frac{s}{s^{2}+1}
$$

which we can solve for $\bar{f}(s)$, yielding 

$$
\bar{f}(s) =  \frac{s^{3}-2s^{2}+2s+2}{s ^{4}-2s^{3}+3s^{2}-2s+2}
$$
 which, using partial fractions, can be written as
$$
\frac{1}{5}\left( \frac{s}{s^{2}+1}-\frac{2}{s^{2}+1}-\frac{6}{s^{2}-2s+2}+\frac{4s}{s^{2}-2s+2} \right) 
$$
the inverse Laplace transform of which is given by 

$$
\frac{1}{5}\left((1 + 4 e^t) \cos(t) - 2 (1 + e^t) \sin(t)\right)
$$

which is the function $f(t)$. 

***

### 5. Properties of the Dirac Delta Function

Show that 

$$
\delta \left[  (t-a_{1})(t-a_{2}) \right] = \frac{1}{|a_{1}-a_{2}|}\left[ \delta (t-a_{1}) + \delta(t-a_{2}) \right] 
$$

The properties of the delta function imply that it only contributes when the argument is zero - hence, we have two peaks at $t=a_{1}$ and $t=a_{2}$. For example, for $a_{1},a_{2}=1,3$...

![[Pasted image 20231022215808.png]]

In the neighborhood of $t=a_{1}$, we can neglect the variation in $t$ around $t=a_{2}$, and vice versa. So we can treat the other term in $\delta \left[  (t-a_{1})(t-a_{2}) \right]$ as a constant $|a_{1}-a_{2}|$, and via the scaling property of delta functions:
$$
\delta \left[  c(t-a_{1}) \right] = \frac{1}{|c|}\left[ \delta (t-a_{1})\right] 
$$

...where $c=|a_{1}-a_{2}|$. The same can be said in the neighborhood of $t=a_{2}$: locally, the variation around $t=a_{1}$ is irrelevant, and we have 

$$
\delta \left[  c(t-a_{2}) \right] = \frac{1}{|c|}\left[ \delta (t-a_{2})\right] 
$$

...where now $c=|a_{2}-a_{1}|$ - but since the distance between the two remains constant, $|a_{2}-a_{1}|=|a_{1}-a_{2}|$. Thus the contributions of both of these are

$$
\delta \left[  (t-a_{1})(t-a_{2}) \right] = \frac{1}{|a_{1}-a_{2}|}\left[ \delta (t-a_{1}) + \delta(t-a_{2}) \right] 
$$

which was to be shown. 


***




