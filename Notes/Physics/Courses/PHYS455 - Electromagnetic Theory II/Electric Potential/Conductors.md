# Conductors:
***
### Electrostatic properties of conductors:

In an **insulator**, eg. glass or rubber, one can think of each electron as being attached by a very short leash to a particular atom. In a metallic **conductor**, by contrast, one or more electrons per atom are free to roam in a 'sea of electrons' (in ionic solutions, it is the ions that move rather than electrons). A perfect conductor would contain an unlimited supply of free electrons - this does not occur in reality, but metals come close enough for most practical purposes.


From this definition, the following basic electrostatic properties of conductors follow:

#### 1. $\mathbf{E}=0$ inside a conductor.

Why? If there were a field inside, those free charges would move, and then we would be out of the domain of electrostatics. Maybe all this proves is that one can't have electrostatics when conductors are present - we should further examine what happens when one places a conductor into an external electric field $\mathbf{E}_0$.  


```tikz


\usepackage{tikz,pgfplots}

\usepackage{xcolor}
\usetikzlibrary{decorations.markings}
\usetikzlibrary{angles,quotes}
\tikzset{>=latex}


\colorlet{Ecol}{orange!90!black}
\colorlet{EcolFL}{orange!80!black}
\colorlet{veccol}{green!45!black}
\colorlet{EFcol}{red!60!black}


\tikzstyle{metal}=[top color=black!20,bottom color=black!50,shading angle=45]
\tikzstyle{EField}=[->,thick,Ecol]
\tikzstyle{EField dashed}=[dashed,Ecol,line width=0.6]
\tikzstyle{vector}=[->,thick,veccol]
\tikzstyle{normalvec}=[->,thick,blue!80!black!80]
\tikzstyle{EField}=[->,thick,Ecol]
\tikzstyle{EField dashed}=[dashed,Ecol,line width=0.6]
\tikzstyle{charge-}=[very thin,top color=blue!50,bottom color=blue!70!white!90!black,shading angle=10]
\tikzstyle{charge+}=[very thin,top color=red!80,bottom color=red!80!black,shading angle=-5]

\tikzset{
  EFieldLine/.style={thick,EcolFL,decoration={markings,
                     mark=at position #1 with {\arrow{latex}}},
                     postaction={decorate}},
  EFieldLine/.default=0.5}
\tikzstyle{measure}=[fill=white,midway,outer sep=2]


\begin{document}
\begin{tikzpicture}
	
\def\H{3.5}
\def\W{1.4}
\def\NE{6}
\def\NQ{7}
\def\E{1.8}
\def\R{0.1}


 \draw[metal] (-\W/2,-\H/2) rectangle ++(\W,\H);;

 \foreach \i [evaluate={\y=-\H/2+(\i-0.5)*\H/\NE;}] in {1,...,\NE}{
    %\draw[EFieldLine=0.62] (-\E,\y) -- (-\W/2,\y);
    %\draw[EFieldLine=0.56] (-\W/2,\y) -- (\W/2,\y);
    %\draw[EFieldLine=0.62] (\W/2,\y) -- (\E,\y);
    \draw[EFieldLine=0.54] (-\E,\y) -- (\E,\y);
  }
\node[Ecol,above right] at (\E,0.43*\H) {$\bf{E}_0$};

  \foreach \i [evaluate={\y=-0.92*\H/2+(\i-1)*0.92*\H/(\NQ-1);}] in {1,...,\NQ}{
    \draw[charge-] (-0.4*\W,\y) circle (\R) node[scale=0.6] {$-$};
    \draw[charge+] ( 0.4*\W,\y) circle (\R) node[scale=0.6] {$+$};
    \draw[EFieldLine=0.54,line width=0.5] (0.35*\W,\y) -- (-0.35*\W,\y);
}

\end{tikzpicture}
\end{document}

```

```tikz

```

Initially, $\mathbf{E}_0$ will drive any 'free positive' charges to the right, and negative ones to the left (this doesn't actually happen, it's just the electrons moving, but the effect is similar enough). An excess of charge piles up on each side, as in the figure above - positive on the right, negative on the left. These **induced charges** produce a field of their own inside the conductor, also shown in the figure above, in the opposite direction of $\mathbf{E}_0$. The field of the induced charges tends to cancel out the original field - charge will continue to flow until the cancellation is complete and we are left with precisely zero electric field inside the conductor. This process happens quickly enough to be considered instantaneous for most purposes.

#### 2. $\rho = 0$ inside a conductor.

This follows from Gauss's Law:
$$\grad\cdot \mathbf{E} = \frac{\rho}{\eo}.$$

If $\mathbf{E}$ is zero, then $\rho$ must be too. There is still charge around, but the positive and negative cancel entirely, leaving no *net* charge density inside the conductor. 

#### 3. Any net charge resides on the surface of a conductor.

This is simply the only place left that it could reside. 

#### 4. A conductor is an equipotential.

If $a$ and $b$ are two points within (or on the surface of) a conductor, $V(b)-V(a)=-\int^{b}_{a}\mathbf{E}\cdot d \mathbf{l}=0$, so $V(b)=V(a)$ . 


#### 5. $\mathbf{E}$ is perpendicular to the surface just outside a conductor. 


![[Pasted image 20221115143650.png]]

If the situation were any different, charge would immediately redistribute around the surface to kill off any tangential component, near instantaneously. 

The fact that the charge is located entirely on the surface of a conductor is true regardless of the size/shape of the conductor.


These considerations can also be put in terms of energy - like any other free dynamical system, the charge on a conductor will seek the arrangement that minimizes the potential energy. Property **3** asserts that the electrostatic energy of a solid object, with specified shape and total charge, is a minimum when the charge is spread uniformly across the surface. 


This state where no charge is moving is the **steady state** of the conductor.

***

