# Electromagnetic Theory - TikZ Recipes
***

### Electromagnetic Wave:

```tikz
\begin{document}
	\begin{tikzpicture}[x={(-10:1cm)},y={(90:1cm)},z={(210:1cm)}]

	 % Axes
    \draw (-1,0,0) node[above] {$z$} -- (5,0,0);
    \draw (0,0,0) -- (0,2,0) node[above] {$y$};
    \draw (0,0,-2) -- (0,0,2) node[left] {$x$};

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
