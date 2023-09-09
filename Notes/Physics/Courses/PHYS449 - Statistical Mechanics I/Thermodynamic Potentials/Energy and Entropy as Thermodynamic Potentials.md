# Energy and Entropy as Thermodynamic Potentials
***

In many examples, we have already seen that the entropy or the internal energy, respectively, are the central state quantities. If they are known as functions of the *natural variables*$(U,S,V,N,...)$ of an isolated system, it is **guaranteed** that all other thermodynamic quantities are *also* uniquely determined. 

For example, if we know $U(S,V,N,...)$, it holds that:

$$dU = T dS - pdV + \mu dN$$ ^2fa770
$$\begin{align*}
T &= \left (\pdv{U}{S} \right)_{V,N,...} \\
\\
-p &= \left (\pdv{U}{V} \right)_{S,N,...} \\
\\
\mu &= \left (\pdv{U}{N} \right)_{S,V,...}\\
\\

\end{align*}$$

^36db76

such that the **temperature,** **pressure**, and **chemical potential** of the system are known as functions of the natural variables. 

A similar assertion holds for the **entropy** as well - if we rearrange [[#^2fa770|the fundamental thermodynamic relation]], we find:

$$dS = \frac{1}{T}dU + \frac{p}{T}dV - \frac{\mu}{T}dN$$

$$\begin{align*}
\frac{1}{T}&= \left (\pdv{S}{U} \right)_{V,N,...} \\
\frac{p}{T}&= \left (\pdv{S}{V} \right)_{U,N,...} \\
- \frac{\mu}{T}&= \left (\pdv{S}{N} \right)_{U,V,...}
\end{align*}$$

^f40d41


The two [[#^36db76|sets]] of [[#^f40d41|equations]] above are the equations of state of the system. 

On the other hand, knowing all equations of state, we may calculate the entropy and internal energy, respectively, as functions of the natural variables via *integration*. 

***
# Example: The entropy of the ideal gas

 The entropy of the ideal gas is derived in an exercise elsewhere:
$$S(N,T,p)=Nk \qty[s_{0}(T_{0},p_{0})+ \ln \qty(\qty(\frac{T}{T_{0}})^{\frac{5}{2}}\qty(\frac{p_0}{p}))]$$ If we rewrite this in terms of the independent variables $U,N$, and $V$, using the following relations:
$$\begin{align*}
	U &= \frac{3}{2}NkT\\
	pV &= NkT\\
	
	\end{align*}$$
  with the constraints:
  
$$\begin{align*}
U_{0}&= \frac{3}{2}N_{0}k T_{0}\\
p_{0}V_{0}&= N_{0}k T_{0}
\end{align*}$$
 we obtain:
 
 > $$S(N,V,U) = Nk \qty[s_{0}(N_{0},V_{0},U_{0}) + \ln \qty(\qty(\frac{N_{0}}{N})^{\frac{5}{2}} \qty(\frac{U}{U_{0}})^{\frac{3}{2}}\qty(\frac{V}{V_{0}}))]$$

Knowing the above equation, we may obtain all equations of state for this ideal gas by partial differentiation according to [[#^f40d41|the system of entropy derivatives above]]:


*to add later*

one obtains the ideal gas law + chemical considerations again
***

However, the knowledge of the *fundamental state relation* $S(U,N,V,...)$ yields even more information than this!

If the entropy *can* be enlarged by some change in the variables $U,N,V,...$ , the *corresponding process will happen spontaneously and irreversibly*. The equilibrium state is finally given by a maximum of the entropy as a function of the variables $(U,N,V,...)$. 

Because of these properties, the entropy is known as a **thermodynamic potential**. We will become acquainted with other thermodynamic potentials shortly. Like the potential energy does in mechanics, the entropy gives information regarding the most stable equilibrium position of the system. And just as with differences in potential energy, *entropy differences* are the reason why a thermodynamic process happens in an isolated system.

As a consequence: knowledge of the entropy state function $S(U,N,V)$ (or, equivalently, the internal energy state function $U(S,N,V)$ ) guarantees knowledge of the main equations of state for a system.


The *extensive* state variables $U,S,V,N$ are very useful for *isolated* systems, where they assume constant values in equilibrium, but in practice (*e.g.* in a heat bath), thee state variables are often not appropriate. It is, for example, much much easier to experimentally control a corresponding intensive variable, like the temperature, instead of manipulating the entropy, which is challenging to do directly.  Quite analogously, in many cases one may prefer to work with the pressure $p$ (*e.g.* atmospheric pressure) of a system rather than its volume $V$.  Therefore it is reasonable to look for *other* thermodynamic potentials which have analogous properties to the entropy or internal energy, but which depend on the conjugated *intensive* variables. Our aim is therefore (in the case of internal energy $U(S,V,N,...)$, to perform a transformation from the entropy $S$ to the intensive variable $T=\left (\pdv{U}{S} \right)_{V,N,...}$. We will find such a transformation in the [[Legendre Transformation|Legendre transformation]], well known from classical mechanics.

[[The Hamiltonian Formalism]] is developed by means of a **Legendre transformation** on the Lagrangian $\mathcal{L}(\vec{q_{v}},\vec{\dot{q_{v}}})$ to replace the generalized velocities $\vec{\dot{q_{v}}}$ with the new variables $\vec{p_{v}}=\pdv{\mathcal{L}}{\vec{\dot{q_{v}}}}$, the *generalized momenta*. The Hamiltonian is generated via the relation below:

$$H(\vec{q_{v}},\vec{p_{v}}) = \sum\limits_{v}\vec{\dot{q_{v}}}\vec{p_{v}}-\mathcal{L}(\vec{q_{v}},\vec{\dot{q_{v}}})$$
One obtains a new function $H(\vec{q_{v}},\vec{p_{v}})$ (the Hamiltonian) that is completely equivalent to the Lagrangian, but which depends on the new variable $\vec{p_{v}}$. The proof is given by simple differentiation:

$$\begin{align*}
dH &=  \sum\limits_{v} \qty(\vec{p_{v}}d \vec{\dot{q_{v}}} + \vec{\dot{q_{v}}}d \vec{p_{v}} - \pdv{\mathcal{L}}{\vec{q_{v}}}d \vec{q_{v}} - \pdv{\mathcal{L}}{\vec{\dot{q_{v}}}}d \vec{\dot{q_{v}}})\\
\\
&= \sum\limits_{v}\qty(\vec{\dot{q_{v}}}d \vec{p_{v}} - \pdv{\mathcal{L}}{\vec{q_{v}}}d \vec{q_{v}})
\end{align*}$$

Here, only the changes $d \vec{p_{v}}$ and $d \vec{q_{v}}$ occur. We now consider the Legendre transformation more extensively in the context of thermodynamics. 
***





