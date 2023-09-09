# The Maximum Entropy Principle
***

The assertion of the second law of thermodynamics is that isolated systems strive for an equilibrium state which is characterized by a maximum in entropy. As we have seen, this is (from the microscopic point of view) the *most probable* state, *i.e.* the state with the largest number of microscopic realization possibilities.

All spontaneous (irreversible) processes in an isolated system increase the entropy, until the maximum is reached for the equilibrium state:

$$dS = 0 \qq{,} S=S_\text{max} $$

On the other hand, we know from mechanics/electrodynamics and quantum mechanics that systems which are not isolated want to *minimize their energy*.  A raindrop falls onto the Earth, where its kinetic energy (gained from initial potential energy from height) is transformed into heat. Similar arguments apply to a pendulum, which finally reaches its rest position (equilibrium) due to the influence of friction *i.e.* it assumes a state with a minimum of potential energy. However, if, in both cases, one also considers the heat energy created, the total energy is unchanged - it has merely been statistically distributed in the form of heat among a larger number of particles (Earth/support/air). During this process, the entropy of the *total* isolated system has increased. This leads us to the presumption of the *maximum entropy principle*, first formulated by E. T. Jaynes:

> The probability distribution which best represents the current state of knowledge about a system is the one with the largest **entropy** in the context of previously stated prior data. This corresponds to a minimum of energy.

This can be readily understood in terms of the laws of thermodynamics.

Consider an isolated system containing two partial subsystems:


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

		\node at (-2,2) {\LARGE $d U_{1}=\delta W_{1}$};
		\node at (-2,1) {\LARGE $\delta Q_{1}=0$};
		\node at (2,1.5) {\large $d U_{2}=\delta W_{2}+\delta Q_{2}$};

		


	\end{tikzpicture}
\end{document}

```


We remove a certain work $\delta W_{1} \lt 0$ from $S_{1}$, corresponding to a difference in potential energy.

The partial subsystem $S_{1}$ shall not exchange any heat with the surroundings during this process. For this reversible process, then, we have

$$\delta Q_{1} = T dS = 0$$

and so the entropy $S_{1}$ stays constant. If we now hand over a fraction $\epsilon$ of the work $\delta W_{1}$ as heat, and a fraction $(1-\epsilon)$ as work to subsystem $S_{2}$, we have:


$$\begin{align*}
dU_{2} &=  \delta Q_{2} + \delta W_{2} = -dU_{1}= -\delta W_{1} \gt 0\\
\\
\delta Q_{2}&= -\epsilon \ \delta W_{1} \gt 0 \qq{,} \delta W_{2}= -(1-\ee)\delta W_{1}
\end{align*}$$

If the heat is passed over to $S_{2}$ while the temperature $T$ stays constant, the following relation holds:

$$\delta Q_{2} = T \ dS_{2} \gt 0$$

Since now $S_{1} =$ const. and $d S_{2} \gt 0$, the total entropy of the isolated system has obviously increased due to the transformation of work from $S_{1}$ into heat in $S_{2}$, and the internal energy of $S_{1}$ has decreased. 

One will further note that this process will proceed **spontaneously** as long as $S_{1}$ can perform work, or, in other words, *until the system reaches the state of maximum entropy*. The transformation of work into heat is **always** an irreversible process associated with an increase of entropy - so systems that can perform work will always perform work until maximum entropy is achieved. 

