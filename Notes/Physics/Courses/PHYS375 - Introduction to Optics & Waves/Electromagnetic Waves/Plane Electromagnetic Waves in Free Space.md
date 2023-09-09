# Plane Electromagnetic Waves in Free Space:
***

We know that radio or TV signals can be transmitted through. We also know that solar energy is transmitted from the sun to the earth through vacuum in the form of radiation of electromagnetic waves with different frequencies/wavelengths. As noted previously, electromagnetic waves have an enormous range of frequencies. Surprisingly enough, they all propagate with the same velocity $c$. 

In a [[The Wave Equation for an LC Transmission Line|previous section]] we came very close to deriving the wave equation for electromagnetic waves in free space. If we take $L / \Delta x=\mu_{0}$, and $\frac{C}{\Delta x}=\eo$, we may indeed conclude that electromagnetic waves in free space should propagate with the velocity 

$$c=\frac{1}{\sqrt{\eo \mu_{0}}}=299,972,458 \text{ m/s}$$

However, it is far from obvious that we can analyze the propagation of electromagnetic waves in free space, which is a *continuous* medium for the waves, in terms of discrete inductances and capacitances. Also, the analogy does not tell us what the electric and magnetic field should be, which we will need to calculate the Poynting vector associated with electromagnetic waves. Here, we directly derive the the wave equation for electromagnetic waves in free space using the fundamental laws in electromagnetism, namely Faraday's law of induction and the Ampere-Maxwell current displacement law. 

For simplicity, we assume a *one-dimensional* or **plane** wave that is propagating in the +$x$-direction, which is also the direction of energy flow. From the arguments concerning the Poynting vector, and assuming that the electric field is polarized in the $y$-direction, we must have the magnetic field polarized in the $z$-direction, as shown below:


![[Pasted image 20221202165832.png]]

Let us assume a thin rectangle in the $xy$-plane having length of $1 \text{ m}$ and width $\Delta x$:

![[Pasted image 20221202170018.png]]

We can apply **Faraday's law** to the rectangle:

$$\curl \vec{E} = - \pdv{\vec{B}}{t} \iff \oint_{C}\vec{E} \cdot d \vec{l} = - \pdv{t}\iint_{A}\vec{B}\cdot d \vec{a} = - \pdv{\Phi_{\mathbf{B}}}{t}$$
Since the magnetic flux flowing through the rectangle is 

$$\Phi_\mathbf{B} = \mathbf{B}(x)(\Delta x \times1)$$

we have (using a Fourier series)

$$\oint \vec{E} \cdot d \vec{l} = \qty(E(x+\Delta x)\cdot 1) - \qty(E(x)\cdot 1) \simeq \Delta x \pdv{E}{x}$$

This must be equal by Faraday's law to $$- \pdv{\Phi_\mathbf{B}}{t}=- \Delta x \qty(\pdv{\mathbf{B}}{t})$$

So we have 

$$-\pdv{E}{x} =  \pdv{B}{t}$$

Next, consider a thin rectangle in the $xz$-plane:

![[Pasted image 20221202172051.png]]

There is an electric flux penetrating this rectangle given by

$$\Phi_{E}= E \Delta x \cdot 1$$

The Ampere-Maxwell law requires that 

$$\oint \mathbf{B} \cdot d \vec{l} = \qty(B(x,t) \times1 )-B(x+ \Delta x,t) \times1 = \eo \mu_{0}\pdv{\Phi_{E}}{t}= \eo \mu_{0}\Delta x \pdv{E}{t}$$

or 

$$- \pdv{B}{x} = \pdv{E}{t}$$

If we differentiate the above two equations w.r.t. $x$ and $t$, respectively, we can  eliminate either $B$ or $E$ to find a *wave equation* for the *electric and magnetic fields* in *free space*:

$$\begin{align*}
	\pdv[2]{E}{t} &= \frac{1}{\eo \mu_{0}} \pdv[2]{E}{x}\\\\

	\pdv[2]{B}{t} &= \frac{1}{\eo \mu_{0}} \pdv[2]{B}{x}
	
\end{align*}$$


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
   
    \draw[teal,thick] plot[domain=0:4.5,samples=200] (\x,0,{cos(deg(pi*\x))});
     \draw[yellow,thick] plot[domain=0:4.5,samples=200] (\x,{cos(deg(pi*\x))},0);

	   % Arrows
    \foreach \x in {0.1,0.3,...,4.4} {
      \draw[thick,->,help lines] (\x,0,0) -- (\x,{cos(deg(pi*\x))},0);
      \draw[->,help lines] (\x,0,0) -- (\x,0,{cos(deg(pi*\x))});
    }

	\node[above right] at (0,1,0) {$\bf{E}$};
    \node[below] at (0,0,1) {$\bf{B}$};

	\end{tikzpicture}
  \end{document}
```

***
