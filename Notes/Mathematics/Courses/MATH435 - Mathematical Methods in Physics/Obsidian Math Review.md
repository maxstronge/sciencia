## Basics:

$x^{2}$ 

$y^{3}$ 

$z^{8}$ 

$\theta_{0}$ 

$\frac{x}{y}$ 

Double backslash does a quick fraction and lets you tab through arguments:

$\frac{x}{y}$ 

$\text{Text is done with te}$ 


following a letter immediately by a number defaults to subscript:
$x_{1}$ $x_{3}$ 

Boldface with {},.
$\mathbf{R}$

dot/hat can be made by immediately following the character with 'dot' or 'hat':

$\hat{x}$ $\hat{y},\hat{z}$ 

$\dot{y}\dot{p}$

e to a power can be quickly done by ee:

$e^{ x }$ 

Vectors are followed by 'vec':

$\vec{x}$  

$\pi$ 

## Electrodynamics:

- Vectors:
	- $\vec{v}, \vec{a},\vec{F},\vec{p}$
- Vector operations:
	- $\vec{A}+\vec{B}=\vec{C}$ 
	- $(\vec{A}+\vec{B})+\vec{C}=\vec{A}+(\vec{B}+\vec{C})$
	- $a\vec{A} +a \vec{B} =a(\vec{A}+\vec{B})$
	- $\vec{A}\cdot \vec{B}=AB\cos\theta$ 
	- $\vec{A} \cross\vec{B}=AB\sin{\theta}\hat{n}$

Matrices:
$$
\begin{pmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{pmatrix}$$
## Differential Calculus:

### 1.2.1 - Derivatives

Given a function of one variable, $f(x)$, the derivative $\frac{df}{dx}=f'$ denotes the instantaneous rate of change of $f$ when $x$ is varied by a tiny amount $dx$. 

$$
df = \left( \frac{df}{dx} \right)dx
$$
i.e. if we increment $x$ by an infinitesimal amount $dx$, then $f$ changes by an amount $df$. Geometrically, $f(x)$ is the slope of the tangent line to $f$ at $x$. 

### 1.2.2 - The Gradient of a Function

Suppose we now have a function of three variables, say, for example, the temperature in this room as a function of spatial coordinates, $T(x,y,z)$. The gradient is the generalized notion of a derivative in multivariate calculus. 

A theorem on partial derivatives states:

$$
dT = \left( \frac{ \partial T }{ \partial x }  \right)dx + \left( \frac{ \partial T }{ \partial y }  \right)dy + \left( \frac{ \partial T }{ \partial z }  \right)dz
$$
i.e. the total derivative is the sum of the derivatives of each dependent variable multiplied by the differential of that variable. This is reminiscent of a dot product, and indeed, it is convenient to define the gradient operator:

$$
dT = \left( \frac{ \partial T }{ \partial x } \hat{x} + \frac{ \partial T }{ \partial y } \hat{y}+\frac{ \partial T }{ \partial z } \hat{z} \right) \cdot(dx \hat{x} +dy \hat{y}+dz \hat{z}) = (\nabla T)\cdot dl$$

where $\nabla T$ is the gradient of $T$. 