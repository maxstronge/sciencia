# Orthogonal Complements and Projections:
***
If $S=\qty{\vb{v}_1,\vb{v}_2,\dots, \vb{v}_m}$ is *linearly independent* in a general vector space, and if $\vb{v}_{m+1}$ is *not* in $\span S$, then $\qty{\vb{v}_1, \dots, \vb{v}_m, \vb{v}_{m+1}}$ is independent. Here is a lemma that is an analog for *orthogonal sets* in $\Rn$:

> ### Lemma 8.1.1: Orthogonal Lemma
> Let $S=\qty{\vb{f}_1,\vb{f}_2,\dots, \vb{f}_m}$ be an orthogonal set in $\Rn$. Given some vector $\vb{x}$ in $\Rn$, write
> $$\vb{f}_{m+1} = \vb{x} - \frac{\vb{x} \cdot \vb{f}_1}{\|\vb{f}_1\|^2} \ \vb{f}_1 - \frac{\vb{x} \cdot \vb{f}_2}{| \vb{f}_2 \|^2} \ \vb{f}_2 - \cdots - \frac{\vb{x} \cdot \vb{f}_m}{\| \vb{f}_m \| ^2} \ \vb{f}_m.$$
> This is a Fourier expansion of the set. 
> 
> Then:
> 1. $\vb{f}_{m+1} \cdot \vb{f}_k = 0$ for all $k=1,2,\dots, m$.
> 2. If $\vb{x}$ is not in $\span S$, then $\vb{f}_{m+1} \neq 0$ and $\qty{\vb{f}_1, \vb{f}_2, \dots, \vb{f}_m, \vb{f}_{m+1}}$ is an orthogonal set.

**Proof:**

For convenience, let $t_i = \frac{\vb{x} \cdot \vb{f}_i}{\|\vb{f}_i \|^2}$ for each $i$. Given $1 \leq k \leq m$:

$$\begin{align} \vb{f}_{m+1}\cdot \vb{f}_k &= (\vb{x} - t_1 \vb{f}_1 - \cdots - t_m \vb{f}_m) \cdot \vb{f}_k \\ &= \vb{x} \cdot \vb{f}_k - t_1 (\vb{f}_1 \cdot \vb{f}_k) - \cdots - t_k (\vb{f}_k \cdot \vb{f}_k) - \cdots -t_m (\vb{f}_m \cdot \vb{f}_k) \\ &= \vb{x} \cdot \vb{f}_k - t_k \|\vb{f}_k \| ^2 \\ &= 0. \end{align}$$

This orthogonal lemma has three important consequences for $\Rn$. The first is an extension for orthogonal sets of the fundamental fact that any independent set is part of a basis:

> ### Theorem 8.1.1
> Let $U$ be a subspace of $\Rn$.
> 1. Every orthogonal subset $S=\qty{\vb{f}_1,\vb{f}_2,\dots, \vb{f}_m}$ in $U$ is a subset of an orthogonal basis of $U$. 
> 2. $U$ has an orthogonal basis. 