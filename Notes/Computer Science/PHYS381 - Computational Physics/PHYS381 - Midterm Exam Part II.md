# PHYS381 - Midterm Exam Part II
### Max Stronge (30064749)
#### Dr. Claudia Gomes da Rocha

***

## Code Workflow for Question 3:

The rocket trajectory was plotted in 4 different stages, with each stage corresponding to a particular part of the rocket's flight. Much of the physics-related derivation is contained within the Jupyter notebook in Markdown cells, and is reproduced here for convenience. The 4 stages of the rocket's flight are as follows:


- **Stage 1**: Launching from ground
- **Stage 2**: Ascending, burning fuel
- **Stage 3**: Preparing for descent after all fuel expended
- **Stage 4**: Falling and hitting the ground

The equation of motion is $ma = F_\text{net} \implies a = \dv{v_y}{t} = \frac{F_\text{net}}{m}$.

At time $t=0$, there is no thrust, no vertical velocity $\implies$ no drag, only gravity.

$F_\text{net} = F_\text{thrust} - F_g - F_\text{drag} = (v_e \frac{dm}{dt}) - M(t)g - \frac{1}{2}\rho v^2 CA$, where $v_e$ is the ejection velocity, $\frac{dm}{dt}$ is the rate of change of the mass as fuel burns, $M(t)$ is the total mass of the rocket + fuel at time $t$, $g$ is the gravitational acceleration on Earth, $\rho$ is the density of air, $C$ is the drag coefficient, and $A$ is the cross-sectional area. 

Constants:

- $v_e = 2000$ m/s
- $dm/dt = 130$ kg/s
- $g = 9.81$ m/s$^2$
- $\rho = 1.22$ kg/m$^3$
- $C = 0.125$
- $A = \pi r^2 = \pi (\frac{D}{2})^2 = 2.2698$ m$^2$

The variable

