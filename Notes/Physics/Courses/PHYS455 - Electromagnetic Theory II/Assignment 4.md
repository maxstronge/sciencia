# PHYS455 Assignment 4
### Max Stronge (30064749)
***

1. Consider the loop in the figure below:


```tikz
\begin{document}
	\begin{tikzpicture}

	\draw (3,0) arc (0:90:3) ;
	\draw (4,0) arc (0:90:4) ;
	\draw (3,0) -- node[below] {$\vec{I} \ \rightarrow$} (4,0) ;
	\draw (0,3) -- node[left] {$\vec{I}\ \downarrow$} (0,4) ;
	

	\node (P) at (0,0) [below] {$P$} ;
	\filldraw [black] (0,0) circle [radius=1pt] ;

	\draw[thin,->] (0,0) -- node[left] {$a$} ++(60:3)  ;
	\draw[thin,->] (0,0) -- node[below] {$b$} ++(22:4)  ;
	
	\end{tikzpicture}
\end{document}
```

A steady state current $\vec{I}$ is flowing counterclockwise around the loop. Find the magnetic field at point $P$. 

**Solution:**

Via the Biot-Savart law, we have:

$$\mathbf{B}(\vec{r}) = \frac{\mu_{0}}{4 \pi}\int \frac{\vec{I}\cross (\vec{r}- \vec{r'})}{|\vec{r} -  \vec{r'}|}dl'=\frac{\mu_{0}I}{4 \pi}\int\frac{d \vec{l}\cross ( \vec{r} - \vec{r'})}{|\vec{r} - \vec{r'}|}$$

...where $I$ has been pulled out of the integral because the current is steady state. 



On the two side pieces of the loop, $d \mathbf{l}$ is parallel to $d \vec{r}$, so the cross product is zero in those sections. 


We can thus evaluate the magnetic field by integrating over the two quarter-loops. For the loop of radius $a$, the current is running clockwise, and because of partial radial symmetry, $d \vec{l}$ is parallel everywhere on the two segments to $\vec{r}$ - so for segment $a$, the field contribution is
$$\mathbf{B}_{a} = \frac{\mu_{0}I_{0}}{4 \pi a^2} \int^{0}_{\frac{\pi}{2}} d \vec{l} = \frac{\mu_{0}I_{0}}{4 \pi a^{2}}(\frac{-\pi a}{2})

= 

-\frac{\mu_{0} I_{0} }{8a} \hat{z}

$$
where the right hand rule verifies the negative sign. 

Similar logic applies for the other loop, with the current going in the opposite direction:


$$\mathbf{B}_{b} = \frac{\mu_{0}I_{0}}{4 \pi b^2} \int^{\frac{\pi}{2}}_{0} d \vec{l} = \frac{\mu_{0}I_{0}}{4 \pi b^{2}}(\frac{\pi b}{2})

= 

\frac{\mu_{0} I_{0} }{8b} \hat{z}

$$

...and so the total magnetic field produced by the current loop at point $P$ is 

$$\mathbf{B} = \mathbf{B}_{a}+\mathbf{B}_{b} = \frac{\mu_{0} I_{0} }{8b} \hat{z}-\frac{\mu_{0} I_{0} }{8a} \hat{z} = \frac{\mu_{0} I_{0} }{8} \left( \frac{1}{b}-\frac{1}{a}\right)\hat{z}.$$

***

2. A hole of radius $a$ is bored parallel to the axis of a current-carrying cylinder of radius $b \gt a$. The axes of the cylinders are a distance $d$ apart. A total current of $\vec{I}$  flows in the cylinder (assume uniform current density).  What is the magnetic field $\mathbf{B}$ at a point $P$ on the surface of the current-carrying cylinder, directly above the hole? Give direction in terms of CW/CCW. 

```tikz
\begin{document}
	\begin{tikzpicture}

	\filldraw [gray] (0,0) circle [radius=50pt] ;
	\filldraw [white] (0.45,0.70) circle [radius=0.5cm] ;

	\draw[dashed,->] (0.45,0.70) -- (57:1.75cm) node[above] {$P$} ;
	\draw[thick,->] (0.45,0.70) -- node[right] {$a$}  (-0.005,1) ;
	\draw[thick,->] (0,0) -- node[right] {$d$} (0.45,0.70)  ;
	\draw[thick,->] (0,0) -- node[right] {$b$} (-45:1.75cm)   ;
	
	\end{tikzpicture}
\end{document}
```


**Solution:**

We can model the hole in the cylinder as another conducting cylinder with the same current density flowing in the opposite direction, such that the net charge current is cancelled out in the region of the hole. The magnetic filed at $P$ can then be found via superposition of the fields produced by the two conducting cylinders.

The magnetic field at the surface of a conducting cylinder (which is the case for $P$, on the surface of cylinder $b$) is given by

$$\mathbf{B}_\text{surface}  = \frac{\mu_{0}\vec{I_{b}}}{2\pi R} = \frac{\mu_{0}\vec{I_{b}}}{2\pi b^2}$$

To this, we add the contribution of the cylinder with antiparallel current, for which the point $P$ is a distance outside the surface. The magnetic field at this point is given by

$$\mathbf{B} = \frac{\mu_{0}\vec{I_{a}}}{2\pi r'}$$
...where $r'$ is the distance from the center of the cylinder to the point of interest, which, per the geometry in the figure, is $b-d$. 

In order for the currents to cancel out in the way we want for this problem, the current density in the smaller conducting cylinder must be the same as the current density $J$ within that region in the larger conducting cylinder. 

Relating current to current density:

$$\begin{align*}
\mathbf{I} = J\pi R^{2} \implies \frac{\vec{I_b}}{\vec{I_{a}}} &= \frac{J_{b}\pi b^2}{J_{a}\pi a^2}

\\
\\

\frac{J_{a}}{J_{b}}&=  \frac{\vec{I_{a}} b^{2}}{\vec{I_{b}} a^2}\\
\\
\vec{I_{a}}&= \vec{I_{b}}\frac{a^{2}}{b^{2}} \frac{J_{b}}{J_{a}}

\end{align*}$$

...and since the current densities must be equal to cancel out, the current density $\vec{I_{b}}$ is that of the original cylinder $\vec{I}$, and the currents must be opposite in direction, we have (hopefully)

$$\vec{I_{a}}= -\frac{a^{2}}{b^{2}}\vec{I}$$
so the magnetic field due to the cylinder of radius $a$ is 

$$\mathbf{B_{a}} = \frac{-\mu_{0}a^{2}\vec{I}}{2\pi (b-d)b^2}$$
such that the net magnetic field at point $P$ is given by

$$\mathbf{B} = \frac{\mu_{0}\vec{I}}{2\pi b^{2}}- \frac{\mu_{0}a^{2}\vec{I}}{2\pi (b-d)b^{2}}= \frac{\mu_{0}I}{2\pi b^{2}}\left(1 - \frac{a^{2}}{b-d}\right),\text{ CCW}$$

...where the direction is taken from the right hand rule, assuming that the flow of current in the conducting cylinder is moving out of the page. 

***

3. There is a constant uniform surface current $\vec{\kk}=\kk \hat{x}$ flowing on the $z=0$ plane. Use the Biot-Savart law to show the magnetic field above the plane ($z\gt0$) is in the $-\hat{y}$ direction. Support your answer with a diagram. 



**Solution:**

Consider the following figure from Griffiths:
![[Pasted image 20221130223921.png]]

Depicted is a sheet of current similar as described. The direction of the Biot-Savart law is given by the right-hand rule pertaining to an imaginary Amperian loop used to probe the magnetic field. Since the current in the figure above is coming into the page towards the reader, the direction of integration around the Amperian loop can be found by pointing one's right thumb in the direction of the current (the fingers will curl in the direction of integration). Outstretching one's index finger in this configuration will then reveal the direction of $\mathbf{B}$, which is indeed in the $-\hat{y}$ direction. 

***

4. There is a cylindrical shell of inner radius $a$ and outer radius $a+d$ centered on the $z$-axis. For radii $s$ in between $a$ and $a+d$, there is a uniform volume current $$\vec{J}=J\hat{z}$$ Show that, in the limit of very small $d$, the magnetic field satisfies the boundary condition 
$$\vec{B}(s=a+d)-\vec{B}(s=a)=\mu_{0}\vec{\kk}\cross\vec{s}$$

where $\vec{\kk}=\vec{J}d$. 

**Solution:**

Apologies, this question was not attempted because the flu has absolutely knocked me out and I can no longer do physics under the influence of this much cold medicine. Question 5 was luckily finished(?) first. Apologies again. 

***

5. The relationship between $\vec{B}$ and the vector potential $\vec{A}$ is 
$$\vec{B} = \curl \vec{A}$$

If the vector potential is given by 

$$\vec{A}=\vec{r}\cross \vec{C}$$

where $\vec{C}$ is a constant, what is $\vec{B}$?

**Solution:**

$$\begin{align*}
\vec{A} &= \vec{r} \cross \vec{C} \\
\\
&= (r_{y}C_{z}-r_{z}C_{y})\hat{x} + (r_{x}C_{z}-r_{z}C_{x})\hat{y} + (r_{x}C_{y}-r_{y}C_{x})\hat{z}\\
\\
\curl \vec{A} &= \curl \left((r_{y}C_{z}-r_{z}C_{y})\hat{x} + (r_{x}C_{z}-r_{z}C_{x})\hat{y} + (r_{x}C_{y}-r_{y}C_{x})\hat{z}\right)\\
\\
\mathbf{B}&= \begin{bmatrix}
\hat{x} & \hat{y} & \hat{z} \\
\pdv{x} & \pdv{y} & \pdv{z} \\
(r_{y}C_{z}-r_{z}C_{y}) & (r_{x}C_{z}-r_{z}C_{x}) & (r_{x}C_{y}-r_{y}C_{x})
\end{bmatrix}
\end{align*}$$

***


