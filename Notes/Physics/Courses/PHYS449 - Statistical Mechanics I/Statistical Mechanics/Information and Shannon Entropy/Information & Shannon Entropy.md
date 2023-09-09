# Information and Shannon Entropy:
***
Closely related to the notion of probabilities and probability theory is **information theory**. From a computer science perspective, information is something that can be stored using bits - we can make this a little more rigorous in the following way:

**Information** is defined in statistical mechanics as the *average number* of *minimal yes/no questions* one has to ask to determine the state of the system. 

For example, consider a chessboard:

![[how-to-set-up-a-chessboard-1a.jpg]]

Consider a single piece on the board. The state of this system would correspond to the location of the piece. In total, the system can be in $M=8^2$ different states. How many yes-no questions do we have to ask to determine the state of the system? We could ask a yes/no question for each square, but depending on the state of the system, this could be answered in one question or a maximum of 64 (if it was on the last square you asked about). This is **not** the minimal amount of questions, though - you could do this more intelligently by asking if the piece is on the upper half of the board, then based on the answer, if it is on the left or right side of that half, etc. This way, we half the number of remaining states by each question, such that we will always have to ask 6 questions. It can be shown that this is indeed the average number of yes/no questions to determine the state of the system, so we have for the chessboard:

$$I=6$$

We can generalize this further:

$$I = 6 = 6\log_{2}2 = \log_{2}2^{6}= \log_{2}8^{2}= \log_{2}M$$

which shows that the **information $I$ is simply the logarithm with base $2$ of the number of states.** 

An equivalent definition: **Information** is the amount of knowledge one obtains if the state of a system is revealed. 

This definition is the starting point to address the question of how much information one gains if the **probability distribution associated with the states of the system** is revealed, rather than just one state. 

***

### Information content of a probability distribution

Let us consider a random variable $X$ with a discrete and finite *set of outcomes* $\Omega$, where the size of the set $|\Omega| = M$, and associated probabilities $\{P(i)\}$ for all events $1\leq i \leq M$ consisting of a single outcome. For example, the flipping of a single coin would have $M=2$, $\Omega= \{H,T\}$. A die would have $M=6, \ \Omega= \{1,2,3,4,5,6\}$. 

Now consider that we do $N$ trials s.t. we have $N$ independent outcomes ($N$ flips of a coin or $N$ rolls of a die). Then the **apparent information** is:

$$I=\log_{2}{M^{N}}=N\log_{2}M.$$

Clearly in the absence of trials, we have no information ($N=0$). However, because of the central limit theorem / law of large numbers, we know that the number of times we observe a certain outcome $i$ is:

$$N_{i}\approx NP_{i} \qq{for} N\to\infty.$$

Thus, in this limit, the number of typical sequences of outcomes (*i.e.* the only sequences we will observe with nonzero probability in this limit) corresponds to the number of ways of rearranging the $N_i$ outcomes for all $i$:

$$g=\frac{N!}{\prod^{i=1}_{M}N_i!}$$

This quantity $g$ is known as the **multinomial coefficient.** We can modify this expression using **Stirling's formula** and the law of large numbers to find:

$$\log_{2}g \approx -N\sum\limits_{i=1}^{M}P_{i}\log_{2}P_i$$

...which becomes exact as $N\to\infty$. 

Now we can quantify the **information content of a probability distribution** as the *difference* between the *apparent information* and the logarithm of the number of typical sequences of outcomes given the probability distribution:

$$I(\{P_i\})=\frac{I-\log_{2}g}{N} = \log_{2}M + \sum\limits_{i=1}^{M}P_{i}\log_{2}P_i.$$
To see that this definition makes sense, consider 2 examples:

First, imagine the state of the system never changes - in this case, the information content reduces to $\log_{2}M$. This is the maximum information content a probability distribution can have. 

Next, imagine a completely uniform distribution, *i.e.* $P_{i}= \frac{1}{M}$. In this case, the above formula gives an information content of $0$. This is the minimum possible information content, consistent with the expectation that a uniform distribution does not tell us anything, since that would be our guess anyways absent further information (subjective interpretation of probability). 

Instead of $I$, one often considers an 'inverse' quantity to characterize a probability distribution. In this sense, this quantity does not *directly* measure the information content, but rather the lack of knowledge (or uncertainty) of the system. This brings us to an important definition:


The **Shannon entropy** $S$ for a probability distribution of a random variable is defined as $$S=-\sum\limits_{i=1}^{M} P_{i}\ln P_{i}= -\left<{\ln p}\right> \propto \frac{\log_{2g}}{N} $$
***
### Maximum Entropy Principle:


