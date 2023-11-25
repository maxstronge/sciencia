Goal: finding solutions of Laplace's equation for the electric potential in a region that contains no net charge. The regions are rectangular cavities in which there is no dependence of the potential on $z$ (i.e. the potential is specified by $\phi(x,y)$). The vertices of the rectangular region have coordinates $(0,0), (0,b), (a,b)$, and $(a,0)$. We will be given boundary conditions that specify the value of the potential on the sides of the rectangle: i.e. $\phi(0,y)=0, \phi(x,0) =0$, etc. We are looking for an expression for the potential over the region that takes one of the following two forms: $$
\boxed{\phi_n = \left[C_n e^{k_n x} + D_n e^{-k_n x} \right] \sin(k_n y)}
$$ ...where $k_n = (n\pi)/b$, or... $$
\boxed{\phi_n = \left[C_n e^{k_n x} + D_n e^{-k_n x} \right] \sin(k_n x) }
$$...where $k_n = (n\pi)/a$. 


The simplest, most general form of these problems will have one nonzero boundary condition (i.e. $\phi(a,y) = g(y)$) and the rest of the sides will be zero. Using the systematic approach we need to build up, though, we can use this to find the potential for more complicated situations via superposition. 

___

## Step 1:

Determine which of the sides is nonzero (if multiple, break the problem into multiple problems, each with one nonzero side). Use the following decision procedure to determine which form of the above is needed:

**If:** 
- The nonzero side is on the left or right (i.e. $\phi(x,0)=\phi(x,b)=0$):
	- Use $\phi_n = \left[C_n e^{k_n x} + D_n e^{-k_n x} \right] \sin(k_n y)\text{, with }k_{n}=\frac{n\pi}{b}$
	- This is because $\sin(k_{n}y)$ will equal zero for both values of $y$ with this $k_{n}$.

- The nonzero side is on the top or bottom (i.e. $\phi(0,y)=\phi(a,y)=0$):
	- Use $\phi_n = \left[C_n e^{k_n y} + D_n e^{-k_n y} \right] \sin(k_n x)\text{, with }k_{n}=\frac{n\pi}{a}$
	- Same rationale: $\sin(k_{n} x)=0$ for both $x=0$ and $x=a$ with this $k_{n}$.

## Step 2:

With our choice of the form of $\phi$ and $k_{n}$, we have constrained the two opposite zero sides as required. We are now left with two sides to consider - the nonzero side and the zero side opposite it. Our next step is to constrain the side opposite the nonzero potential side to be zero.

Since the $\sin(k_{n} x)$ or $\sin(k_{n} y)$ is zero at the edges (as the other two sides must equal zero), we must ensure that it is zero everywhere between those edges, which we do by considering the other part of the solution form. For example, if we have selected the form for the left and right sides to be zero:
$$
\phi_n = \left[C_n e^{k_n y} + D_n e^{-k_n y} \right] \sin(k_n x)\text{, with }k_{n}=\frac{n\pi}{a}
$$

We must then have 
$$
\left[C_n e^{k_n y} + D_n e^{-k_n y} \right]=0
$$
for the value of $y$ that is a zero-potential side. 


**Case 1: zero-potential at zero coordinate**

For example, if $\phi(x,0)=0$, this would mean
$$
\left[C_n e^{k_n 0} + D_n e^{-k_n 0} \right]=0 \implies D_{n}=-C_{n}
$$

and we can factor the $C_{n}$ out to yield

$$
\phi_n(x,y) = \sum_{n=1}^\infty A_{n}C_{n}\sin(k_n x)\left[e^{k_n y} - e^{-k_n y} \right] 
$$

which we can simplify to 
$$

$$
$$
\phi_n(x,y) = \sum_{n=1}^\infty A_{n}\sin(k_n x)\left[e^{k_n y} - e^{-k_n y} \right] 
$$

because $A_{n}$ is an undetermined constant that can absorb $C_{n}$. 





**Case 2: zero potential at nonzero coordinate**

If the side where $x$ or $y=0$ is the nonzero potential side, the problem is a bit more complicated as we cannot simply say $D_{n}=-C_{n}$ in the same way as above. Instead, we note that if, for example, the left side is nonzero (meaning we have the form where $k_{n}=\frac{n\pi}{b}$) i.e $\phi(0,y)=f(y)$, then for the other side we must have 

$$
\phi(a,y)=0
$$
and therefore 

$$
\left[C_n e^{k_n a} + D_n e^{-k_n a} \right]=0 \implies C_{n}=G_{n}e^{-k_{n}a}\text{ and } D_{n}=-G_{n}e^{k_{n}a}
$$

where $G_{n}$ is just some undetermined constant that relates $C_{n}$ and $D_{n}$. This too can be factored out and absorbed into $A_{n}$, leaving us with 

$$

\phi_n(x,y) = \sum_{n=1}^\infty A_{n}\sin(k_n y)\left[e^{k_n (x-a)} - e^{-k_n (x-a)} \right] 
$$

