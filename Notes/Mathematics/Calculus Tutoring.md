1. The line tangent to $f(x)=\sqrt{x}$ at $x=36$ is written in the form 
$$y=mx+b$$

As in all linear equations, $m$ represents the slope of the line, which we can find by taking the derivative of $f(x)$. This can be done using the power rule:


$$\begin{align}
	f(x) &= \sqrt{x} =x^{\frac{1}{2}}
\\
\\

f'(x) &= \frac{1}{2}x^{\frac{-1}{2}} = \frac{1}{2\sqrt{x}}
	
\end{align}$$
This derivative $f'(x)$ is equal to $m$ when $x=36$, so we can find $m$ by substituting that value in for $x$:

$$m=f'(36)=\frac{1}{2\sqrt{36}}=\frac{1}{2*6}=\frac{1}{12}$$

Substituting this back into the linear equation for the tangent line, we have:


$$y=\frac{1}{12}x + b$$

Since the tangent line must touch the graph of the original function $f(x)$ at the point $x=36$, we know the $y$-value in the above equation will be $f(36)=6$. We can put both of those values in to isolate and solve for $b$:

$$\begin{align}
6&=\frac{1}{12} (36)+b \\ 
6 &= 3 + b \\ 
b &= 3
\end{align}$$

Thus, the equation of the tangent line to $f(x)$ at $x=36$ can be written$$y=\frac{1}{12}x +3.$$
For values of $x$ that are close to $36$ (sometimes referred to as 'in the neighborhood' of 36), this equation that we just found is a good approximation to the original function. To illustrate, I've graphed the original function $f(x)=\sqrt{x}$ in red, and the linear approximation we just found in blue:
![[Pasted image 20230522153201.png]]

You can see how at the point $(36,6)$, the two functions match exactly! but as you get further away from that point (moving out of the 'neighborhood'), our approximation gets further and further from the actual function.

But $36.4$ is very close to $36$, so our equation will be a helpful approximation, much easier to calculate by hand than finding the square root of 36.4:

$$y = \frac{1}{12}(36.4) + 3 = 6.033333$$

If we check the actual value on a calculator, we find

$$\sqrt{36.4}=6.03324125$$

So our approximation was really close! 

***


2. The linearization of a function is exactly what we just found - the (linear) equation of a tangent line to a function at a particular point. The linearization provides a very good approximation to the function at points very very close to that particular point that was chosen. We'll follow exactly the same logic as before and start with finding the first derivative of the function $f(x)$.

First, let's rewrite the function as an exponential rather than a radical, which will make it easier to work with:

$$f(x) =\sqrt[3]{3x+5}\\ \to \\  f(x) = (3x+5)^\frac{1}{3}$$

You might recognize this as a composition of functions, an 'inner' and an 'outer' function - we're going to need to use the chain rule to find the derivative $f'(x)$. Our function is a composition of two other functions of $x$ - we can write it as

$$\begin{align}
g(x) &= 3x+5 \\
h(x) &= x^\frac{1}{3}\\
\to f(x) &=h(g(x)) = (3x+5)^\frac{1}{3}
\end{align}$$

Having recognized this pattern, we can use the chain rule, which states that the derivative of a composition of functions is the derivative of the *outer function evaluated at the inner function*, multiplied by the *derivative of the inner function*.

$$f'(x) = h'(g(x)) * g'(x)$$

So let's find the derivative of $h(x)$:

$$h(x) = x^{\frac{1}{3}}\to h'(x) = \frac{1}{3}x^\frac{-2}{3}$$

And of $g(x)$:
$$g'(x) = 3$$

So we put those together to find:

$$f'(x)=h'(g(x)) * g'(x) = \frac{1}{3}(3x+5)^{\frac{-2}{3}} (3)$$


If we evaluate this at the point $x=1$, we find:

$$f'(1)=\frac{1}{3}(3∗1+5) ^\frac{-2}{3}∗3=1/4.$$

So our slope is $m=\frac{1}{4}$. Same as before:

$$y=\frac{1}{4}x + b$$
We just need values for $x$ and $y$. We know the value of $x$ we're looking for is 1, because that's the neighborhood we're approximating the function in. So we evaluate the original function at $x=1$ to find $y$:


$$f(1)=y=(3+5)^{\frac{1}{3}}= \sqrt[3]{8} = 2$$

We now have enough information to find the linearization - back to $y=mx+b$:

$$\begin{align}
y &=mx+b\\
2 &= \frac{1}{4}(1) + b \\ 

b &= \frac{7}{4}

\end{align}$$

With those values $m$ and $b$ known, our linearization $L(x)$ can be written as:

$$L(x)=\frac{1}{4}x + \frac{7}{4}$$


***

3. The Maclaurin series is a Taylor series expansion centered around $x = 0$. The general formula for the Maclaurin series expansion of a function $f(x)$ is:

$$T(x) = f(0) + f'(0)x + \frac{f''(0)}{2!}x^2 + \frac{f'''(0)}{3!}x^{3} + ...$$

So to calculate the Maclaurin series for $f(x)=e^{2x}$, we'll need to find the first three derivatives of $f(x)$, and then evaluate those three derivatives (plus $f(x)$ itself) at $x=0$ . 

$$f(0)=e^{0}=1$$

$$f'(x) =  2e^{2x} \to f'(0) = 2e^0 = 2(1) = 2$$

$$f''(x) =  4e^{2x} \to f''(0) = 4e^{0}= 4$$

$$f'''(x)= 8e^{2x} \to f'''(0)= 8e^0 = 8$$


Now that we know these terms, we can write out our Maclaurin series:

$$T_{3}(x) = 1 + 2x + \frac{4}{2}x^2 + \frac{8}{6}x^{3}$$

...which we can simplify to

$$T_{3}(x) =  1 +2x+2x^{2}+  \frac{4}{3}x^{3}$$

To approximate $e^4$, we substitute $x=2$ into this polynomial:

$$T_{3}(x)=1+4+8 + \frac{32}{3} = \frac{71}{3}$$
Therefore, using the Maclaurin polynomial up to degree 3, we can approximate $e^4$ as $\frac{71}{3}$ or ~ $23.6667$. The actual value of $e^{4}$ is ~ $54.6$, so this is not a great approximation - it could be improved by adding more terms from the Taylor series. 

***
