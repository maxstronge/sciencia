# PHYS449 - Assignment 6
### Max Stronge (30064749)
***

# 1. Random Walk

Consider a particle moving on a one-dimensional line along discrete locations $...,-2,-1,0,1,2,...$ . Assume that the particle starts at location $0$ at time $t_0=0$, and it makes a step at every discrete time step $t_i$ of length 1. A step to the right occurs with probablility $p$, and any step is independent of all previous steps.

- a) What is the probability that the particle returns to the origin after $N$ steps? How does this probability behave for large $N$ for the special case that $p = \frac{1}{2}$?
- b) What is the probability that the particle is at location $j$ after $N$ steps?


**Solution:**

If $p$ is the probability of a rightwards step, let $q$ denote the probability of a leftwards step. Since the two possibilities are mutually exclusive, we have:

$q = 1-p$

We can note that, if the amount of steps $N$ is odd, there is no possibility of returning to the origin - the closest result will still be $\pm1$ unit length away from $x=0$. 

For an even number of steps, we can see right away that the particle will return to the origin if and only if the number of rightward steps is equal to the number of leftward steps. Let $N=2n$. Then, for the object to return to the origin, it must take $n$ steps in each direction. Let us examine the probability of this situation. Since the probability of stepping once to the right is $p$, the probability of stepping twice to the right is $p^2$, thus the probability of stepping to the right $n$ times is $p^n$.

Following similar logic, the probability of stepping to the left $n$ times is $(1-p)^n$. 

Thus the probability of the particle returning to the origin follows a binomial distribution:

$$P_N(0) = \mqty(N \\ n)p^n(1-p)^n$$

$$= \mqty(N\\N/2)p^{N/2}(1-p)^{N/2}$$

$$ =  \frac{N!}{(N-N/2)!(N/2)!}p^{N/2}(1-p)^{N/2}$$

$$=\frac{N!}{(N/2)!^2} p^{N/2}(1-p)^{N/2}$$


In cases of large $N$, we can use Stirling's approximation to simplify the factorials, since the approximation becomes exact as $N\to \infty$. The theorem says


$$N!=\left(\frac{N}{e}\right)^N \sqrt{2\pi N}$$

Inserting this into our expression, we find

$$P_N(0) = \left(\frac{N}{e}\right)^N \sqrt{2\pi N} \left( \frac{1}{\left(\frac{n}{e}\right)^n \sqrt{2\pi n}}\right)p^n(1-p)^n$$


...which will luckily simplify to 

$$P(0)=\frac{2^{N+1/2}}{\sqrt{2 \pi N}}p^n(1-p)^n$$
...recalling that $n=N/2$.





For the special case that $p=q=\frac{1}{2}$, this reduces to 

$$P_N(n)=\mqty(N\\n)\frac{1}{2}^n\frac{1}{2}^n = \mqty(N\\n)2^{-2n} = \mqty(N\\N/2)2^{-N}$$

$$= \frac{N!}{(N/2)!^2}2^{-N}$$

and after applying Stirling's approximation as before,

$$= 2^{\frac{1}{2}-\frac{N}{2}} e^{-N/2} N^{N/2}.$$

Unfortunately, this does not converge to 1 as $N \to \infty$, and random walks in one and two dimensions (but not 3) should do that, so this is incorrect in an unfortunately unknown way.

b) 

To generalize our results to find the probability of the particle ending up at a location $j$, rather than the origin, we can dispense with the condition that the particle takes an equal amount of steps in either direction, and return to our more general binomial distribution:

$$P_N(j)=\mqty(N\\k)p^k(1-p)^{N-k}$$

where $k$ is not necessarily equal to $N-k$. We can see here that the final position $j$ is equal to the number of rightwards steps, $k$, minus the number of leftwards steps, $N-k$. 


***


# 2. Diode

The current $I$ across a diode is related to the applied voltage $V$ via

$$I=I_0 (e^{\frac{eV}{k_B T}}-1).$$

The diode is subject to a random potential $V$ of zero mean and variance $\ss^2$, which is Gaussian-distributed. Find the probability density $p(I)$ for the current $I$ flowing through the diode. Find the most probable value for $I$, the mean value of $I$, and indicate them on a sketch of $p(I)$.


**Solution:**

No solution for this question, apologies. 

***


# 3. World Series

- a) In the World Series in baseball and in the playoffs in the National Basketball Association and the National Hockey Association, the winner is determined by the best of seven games. That is, the first team that wins four games wins the series. Do a simple statistical calculation assuming that the two teams are evenly matched to determine the probability for a full seven game series.
- b) Most teams have better records at home. Assume that the two teams are evenly matched and each has a 60% chance of winning at home and a 40% chance of winning away. In principle, both teams should have an equal chance of winning a seven game series. Determine which pattern of home games is closer to giving each team a 50% chance of winning. Consider the two common patterns: (a) two home, three away, two home; and (b) two home, two away, one home, one away, one home.

**Solution:**

a)


Since the series will end whenever a team achieves 4 wins, it must be true that for a team to win the series in game $N$, they must have won exactly 3 of the first $N-1$ games. For the team to win in the 7th game, which is the situation we're interested in, there are $\mqty(6\\3)$ possible ways the series could go. Assuming a 50% chance of winning and 50% chance of losing:

$$P_{\text{7 game series}} = \mqty(6\\3)\left(\frac{1}{2}\right)^3\left(\frac{1}{2}\right)^3$$

$$= 20 (0.125)^2 = 0.3125 = 31.25\%$$

b) 

Consider the two game patterns separately. In both cases, for team $A$ to win the series, they must win 4 games - as we've seen, this can happen a number of different ways. Let the probability that $A$ wins at home be $p=0.6$, and the probability they win away be $q=0.6$. We can modify our earlier result to form an expression for the probability that A wins in the $N$-th game:

$$P_N(A) = \mqty(N-1\\3)p^iq^j$$


...where $i$ is the number of home games, $j$ is the number of away games, and $i+j=N.$

Since $N$ can only run from a minimum of 4 to a maximum of 7, we can find the probability that $A$ will win the series by summing the probabilities that: they win in game 7 OR they win in game 6 OR they win in game 5 OR they win in game 4:


$$P(A) = \sum_{n=4}^7P_n(A)$$

Let's look at this expression for each of the cases. 


## 1. HHAAAHH

First, for the case of 7 games, all games are played, 4 home and 3 away:

$$P_7(A) = \mqty(6\\3)p^4q^3 = 0.165888$$

Continuing in this way, if A wins in the 6th game, they will have played 3 home, 3 away:

$$P_6(A) = \mqty(5\\3)p^3q^3=0.13824$$

Similar logic (but remember this one as we'll come back to it):

$$P_5(A)=\mqty(4\\3)p^2q^3=0.09216$$

...and for a win in game 4, the combinations vanish and we have

$$P_4(A)=p^2q^2=0.0576$$


Thus the total probability for $A$ to win the series is $$P(A)=0.165888+0.13824+0.09216+0.0576$$

$$=0.453888 = 45.388\%$$


Let us now go through the same process for the second game arrangement.

### 2. HHAAHAH

The probability for $A$ to win in game 7 is exactly the same here - since all games are played, the order makes no difference. 
$$P_7(A)  = 0.165888$$

With 6 games played, we still have 3 away and 3 home, just as in the first case, so this probability is also the same as before:

$$P_6(A) = 0.13824$$

Interestingly, the probability that A wins in game 5 is *not* the same for both game distributions - indeed, if $A$ wins in game 5 in this arrangement, they have played 3 home games and 2 away games, whereas in the first scheme it was the reverse. So we have for the second scheme:

$$P_5(A)=\mqty(4\\3)p^3q^2 = 0.13824$$

again! 

Hopefully you can trust me when I say that the probability of A winning in game 4 is the same in both cases, since in both cases they play 2 home and 2 away games in the same order. 

Thus the sum for this second scheme is 

$$P(A)=0.165888+0.13824+0.13824+0.0576$$

$$=0.499968 = 49.9968\%$$


So the second scheme is more equitable. 
***

	