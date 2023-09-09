# General TikZ Recipes:
***
## 3D Coordinate Axis:

```tikz
\begin{document}

\begin{tikzpicture}
    \coordinate (O) at (0,0,0);
    \draw[thick,->] (0,0,0) -- (5,0,0) node[anchor=north east]{$y$};
    \draw[thick,->] (0,0,0) -- (0,5,0) node[anchor=north west]{$z$};
    \draw[thick,->] (0,0,0) -- (0,0,5) node[anchor=east]{$x$};
\end{tikzpicture}


\end{document}
```

