# PHYS355 Lab 4
Max Stronge (30064749)
Minoda Fernando ()
Karina Hunt (30067042)


## Circuit Network Design:

![[Pasted image 20220316193237.png]]
## Data:
![[Pasted image 20220316192720.png]]

![[Pasted image 20220316192759.png]]


## Plots:
![[Pasted image 20220316192924.png]]

![[Pasted image 20220316192948.png]]
![[Pasted image 20220316193049.png]]

## Discussion:

1. Compare the three methods used to measure the equivalent capacitance of the network with the theoretical value calculated. Discuss any discrepancies. 


The theoretical calculation yields a result of $90\mu F$.

The first method was to directly derive the value of $C$ from the plot of $V(t)$ vs. $t$:

$$C = \frac{Q}{V} = \frac{I}{V(t)}t \implies C = 90.2\mu F$$

..where the values of V(t) and t were taken from the first collected datapoint, and $I$ was measured as $1.9 \ \mu A$. 

The second method used the graph of the log of $V(t)$ vs. $t$, as the slope of that graph is equivalent to $\frac{-1}{RC}$. This method obtained a result of $84.7 \ \mu F$.

The third method used the same logic as the second, but for the discharging phase rather than the charging section. This yielded a result of $87.7 \ \mu F$.

The first method was closest to our theoretical value - since it requires fewer steps, the uncertainty propagation will produce smaller error. 



