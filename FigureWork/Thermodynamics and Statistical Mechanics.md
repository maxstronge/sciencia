# Thermodynamics and Statistical Mechanics - TikZ Recipes
***

### Isolated System with 2 Subsystems:

```tikz

\begin{document}
	\begin{tikzpicture}
		\draw[thick] (-4,-1) -- (-4,4);
		\draw[thick] (-4,4) -- (4,4);
		\draw[thick] (4,4) -- (4,-1);
		\draw[thick] (4,-1) -- (-4,-1);
		\draw[thick] (0,4) -- (0,-1);
		
		\node at (-2, 3.5) {\LARGE $\mathbf{S_{1}}$};
		\node at (2, 3.5) {\LARGE $\mathbf{S_{2}}$};


	\end{tikzpicture}
\end{document}

```

