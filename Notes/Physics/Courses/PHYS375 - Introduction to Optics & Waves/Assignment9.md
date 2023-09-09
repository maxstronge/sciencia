# PHYS375 Homework Assignment 9
### Max Stronge (30064749)
***

1. Write an expression for the real (as opposed to complex) electric and magnetic fields for a monochromatic electromagnetic plane wave of amplitude $E_{0}$, frequency $\oo$ in both of the following cases. The magnitude of the electric field is $E_0$ when $t=0$ at the origin in both cases.

**a.** When the electric field points in the $\hat{x}$ direction, and the wave travels in the $-\hat{z}$ direction.

**b.** When $\vec{E}$ points parallel to the xy-plane, and the wave travels from the origin to the point $(1,-2,3)$.


**Solutions:**

**a.** 

The configuration is pictured below (plot created with TikZ):


```tikz
\begin{document}
	\begin{tikzpicture}[x={(-10:1cm)},y={(90:1cm)},z={(210:1cm)}]

	 % Axes
    \draw (-1,0,0) node[above] {$z$} -- (5,0,0);
    \draw (0,0,0) -- (0,2,0) node[above] {$x$};
    \draw (0,0,-2) -- (0,0,2) node[left] {$y$};

	% Propagation
    \draw[->,ultra thick] (5,0,0) -- node[above] {$c$} (6,0,0);
	 % Waves
   
    \draw[teal,thick] plot[domain=0:5,samples=200] (\x,0,{cos(deg(pi*\x))});
     \draw[yellow,thick] plot[domain=0:5,samples=200] (\x,{cos(deg(pi*\x))},0);

	   % Arrows
    \foreach \x in {0.1,0.3,...,4.9} {
      \draw[thick,->,help lines] (\x,0,0) -- (\x,{cos(deg(pi*\x))},0);
      \draw[->,help lines] (\x,0,0) -- (\x,0,{cos(deg(pi*\x))});
    }

	\node[above right] at (0,1,0) {$\bf{E}$};
    \node[below] at (0,0,1) {$\bf{B}$};

	\end{tikzpicture}
  \end{document}
```


Because the electric field is polarized in $x$, $\vec{E} = E_{x}$. Since $E=E_{0}$ initially, a cosine function can describe the field as a function of position and time:

$$\vec{E} = E_{x}(z,t) = E_{0}\cos \qty(kz-\oo t)$$
	

The magnetic field must be proportional everywhere to the electric field, and the amplitude can be found with the following relation:
$$\frac{E_{x}}{B_{y}}= \frac{E_{0}}{B_{0}}=c$$

such that the magnetic field can be written 

$$\vec{B} = B_{y}= \frac{E_{0}}{c}\cos(kz-\oo t)$$
**b)**

Since $\vec{E}$ is parallel to the $xy$-plane, it points in the direction of the unit vector $\hat{e}=(0,1,0)$. The wave propagates (*i.e.* $S$ points) in the direction given by the unit vector $\hat{n} = \frac{(1,-2,3)}{\sqrt{1 + 4 + 9}}=\frac{1}{\sqrt{14}}(1,-2,3)$. 

If we take the cross product of these two vectors, we will end up with a vector orthogonal to both, which must be the direction of the magnetic field:

$$\hat{e} \cross \hat{n} = \vec{b} = \qty(\frac{3}{\sqrt{14}},0,\frac{-1}{\sqrt{14}}), \hat{b} = \left\{\frac{3}{\sqrt{10}},0,-\frac{1}{
   \sqrt{10}}\right\}$$

With these three orthogonal unit vectors, we can create a new orthonormal basis $\qty{\hat{e}, \hat{b}, \hat{n}}$ with the above transformations to the standard Cartesian basis ($\hat{e} = \hat{y}$). Then, the expressions for the field are much the same as before, in the new basis:

$$\vec{E} = E_{e} = E_{0}\cos \qty(kn-\oo t) \hat{e}$$
$$\vec{B} = B_{b}= \frac{E_{0}}{c}\cos(kn-\oo t) \hat{b}$$

***

2. Consider a point particle sitting in the $xy$ plane. The particle is moved by  an electromagnetic plane wave, of amplitude $E_{0}$, frequency $\oo$ perpendicular to the particle (pointing down onto the $xy$-plane). The wave is polarized in the $x$ direction, and you can take $\delta= 0$. The particle has mass $m$ and charge $q$. 

**a.** Find the velocity of the particle as a function of time. Why can you safely ignore the magnetic field for this calculation?



**b.** Assume that the particle is an electron, and the source of light is a laser pointer ($5\text{ mW}, \lambda= 700\text{ nm}$, beam radius $1\text{ mm}$). What's the maximum velocity of the electron in this situation?


**Solutions:**

**a.** 
From above:

$$E_{x}= E_{0}\cos(kz-\oo t)$$

The resultant electric force is $$F_{E}  = qE_{x}= qE_{0}\cos(kz- \oo t)$$

....and by Newton's 2nd, this is equal to the mass of the particle times its resulting acceleration:

$$F_{E}= m \dot{v}$$

So the velocity can be written as the time derivative of the electric force divided by the mass:

$$v = \frac{q E_{0}}{m} \pdv{t} \qty[\cos(kz- \oo t)] $$
$$ = -\frac{q E_{0}\oo}{m}\sin(kz-\oo t) \ \hat{x}$$

The magnetic force can be shown to have a time average of zero - in addition, the intensity of the magnetic field is so much smaller than that of the electric field due to the relation $\frac{E_{0}}{B_{0}}=c$.

***

3. For an electromagnetic plane wave with the electric field in the $y$ direction and the magnetic field in the $z$ direction:

$$- \pdv{\mathbf{E}}{x}= \pdv{\mathbf{B}}{t}$$
Show that this is equivalent to 

$$\mdet{\mathbf{u_{x}}& \mathbf{u_{y}}& \mathbf{u_{z}}\\ \pdv{x} & \pdv{y} & \pdv{z}\\ 0 & E & 0} =- \pdv{\mathbf{B}}{t}\mathbf{U_{z}}$$

if we assume $\pdv{E}{z}=0$. Similarly the following equation:

$$- \pdv{\mathbf{B}}{x}=\pdv{E}{t}$$
may be written as $$\mdet{\mathbf{u_{x}}& \mathbf{u_{y}}& \mathbf{u_{z}}\\ \pdv{x} & \pdv{y} & \pdv{z}\\ 0 & 0 & B}=\mu_{0}\eo \pdv{E}{t} \mathbf{u_{y}}$$
with $\pdv{\mathbf{B}}{y}=0$. 

**Solutions:**


The first determinant is alternative notation for the curl of $\vec{E}, \\ \curl \vec{E}$. By Faraday's law, this is equal to

$$\curl \vec{E} = - \pdv{\vec{B}}{t}$$
...or 0 when there is no time variance in the electric field. Since $\vec{B} = B_{z}$ and $\vec{E} = E_{y}$, the above equation is correct.

The second determinant is equivalent to the curl of $\vec{B}$ when $\vec{B}$ is polarized in $z.$ Via the Ampere-Maxwell law:

$$\curl \vec{B} = \mu_{0}J + \mu_{0}\eo \pdv{E}{t} $$

where $\vec{E}$ is already pointing entirely in the $y$ direction. If there is no enclosed current $J$, we have
$$\curl \vec{B} = \mu_{0}\eo \pdv{E_y}{t}$$
which was to be shown.


***


**11.1.** In Young's double slit experiment, a fringe spacing of $\Delta y=5\text{ mm}$ is observed. Assuming slit separation $d=0.1 \text{ mm}$, and the slit-screen distance $D = 1 \text{ m}$, find the wavelength $\ll$.

**Solution:**

The separation between adjacent extrema in Young's double split experiment is given by 

$$\Delta y = \frac{\lambda D}{d}\implies \lambda= \frac{\Delta y d}{D} = \frac{\qty(5 \times10^{-3})\qty(0.1 \times10^{-3})}{1}=5 \times10^{-7}\text{ m} = 500 \text{ nm.}$$



***

**11.8.** A spy satellite claims to be able to resolve two points on the Earth that are separated by a distance of $50 \text{ cm}$. Assuming the satellite is $200 \text{ km}$ high and $\lambda = 500 \text{ nm} = 5000 \ang$ , find the minimum diameter of the telescope carried by the satellite. 

**Solution:**

First, we need to find the angular resolution claimed by the satellite. From the diagram below (not to scale):


```tikz

\begin{document}
\begin{tikzpicture}
\draw (-0.5,0) coordinate (a) -- node[below] {$d=0.5$ m} (0.5,0) coordinate (b) -- (0,8) coordinate (c)  -- (a);
\draw (0,0) -- node[right] {$D=200 \times10^{3}$ m} (0,8);
\end{tikzpicture}
\end{document}
```



We can see that the resolution angle is 

$$\theta = 2 \tan \left(\frac{0.5}{200\times10^{3}}\right)= 5 \times10^{-6}\text{ rad}$$

So from the relation

$$\sin\theta \approxeq \theta= 1.22 \frac{\lambda}{a} $$

...where $a$ is the diameter of the telescope in this situation. Given $\lambda=500 \text{ nm}$, we have 

$$a=\frac{1.22\lambda}{\theta}=\frac{1.22  \qty(500 \times10^{-9})}{5 \times10^{-6}}=0.122 \text{ m} = 12.2 \text{ cm}.$$


***

**11.9.** In single-slit diffraction, what would happen if the slit opening is doubled?

**Solution:**
Since the condition for single-slit destructive interference is 

$$d \sin\theta = m \lambda$$
we note that $m$ represents the integers, which will not vary, and the wavelength of the light $\lambda$ will not change by varying $d$. The only thing that can change is the angle $\theta$, so if $d$ is doubled, the width of the central maximum in the diffraction pattern will be halved to retain the equality above.


***

**11.10.** Diffraction in double-slit experiment. 

Assume each slit has an opening $a$ with slit spacing $d$ in Young's double-slit experiment:

![[Pasted image 20221201212619.png]]

Then, in addition to the interference, we expect diffraction due to the finite aperture. Show that the intensity on the screen is given by 

$$I = I_{0}\cos^{2}\beta \qty(\frac{\sin\aa}{\aa})^{2}$$

...where 

$$\begin{align*}
\aa &= \frac{\pi a }{\lambda}\sin \theta\\
\beta &= \frac{\pi d}{\lambda}\sin\theta
\end{align*}$$


**Solution:**

For single slit diffraction with spacing $a$:

$$I = I_{0} \qty(\frac{\sin \qty(\pi a \sin \frac{\th}{\lambda}))}{\pi a \sin \frac{\theta}{\lambda}})$$

For a double slit interference:

$$I = I_{0}\cos^{2}\qty(\frac{\pi d \sin \theta}{\lambda})$$

If we now have two slits, with width $a$, separated by distance $d$, the intensity of the total pattern will be the product of the two:

$$I = I_{0}\cos^{2}\left(\frac{\pi d \sin \theta}{\lambda}\right) \qty(\frac{\sin \qty(\pi a \sin \frac{\theta}{\lambda})}{\pi a \sin \frac{\theta}{\lambda}})^{2}$$


If we start with the original expression given in the question:
$$I = I_{0}\cos^{2}\beta \qty(\frac{\sin\aa}{\aa})^{2}
$$

...and make the replacements for $\aa$ and $\bb$, we have


$$I = I_{0}\cos^{2}\left(\frac{\pi d \sin \theta}{\lambda}\right) \qty(\frac{\sin \qty(\pi a \sin \frac{\theta}{\lambda})}{\pi a \sin \frac{\theta}{\lambda}})^{2}$$

as before. 



***


**11.11.** In problem $10$, assuming $d=2a$, plot the light intensity as a function of $\theta$. 

**Solution:**


Plotting in Mathematica is currently yielding some strange behavior:

![[Pasted image 20221202233758.png]]

There is an error with the axes and scaling that is currently beyond my ability to diagnose. 

Here is what it should look like:


![[Pasted image 20221202233905.png]]

From MIT course notes under MIT license:
https://web.mit.edu/8.02t/www/802TEAL3D/visualizations/coursenotes/
***
