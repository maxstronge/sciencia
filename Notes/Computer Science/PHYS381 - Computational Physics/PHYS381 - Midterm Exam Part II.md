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

The variable F_thrust was declared as $v_e*\frac{dm}{dt}$, and a function F_drag(v) was defined to determine the drag force for a certain velocity $v$. When working with the floating point numbers for this question, several Overflow errors emerged, making it necessary to round the velocity to 3 decimal places before squaring the velocity. 

Another function was declared to handle the evolution of the total mass of the rocket-fuel system with respect to time, M(t). Assuming the rocket begins burning fuel immediately at time $t=0$, the mass evolves according to the following equation:

$$M(t) = M - \dv{m}{t}t$$

where $M$ is the initial total mass of the rocket and fuel, given by the randomizer as $13285$ kg. For each time $t$, the mass of the rocket at that time is thus the total mass minus the product of the rate of fuel burning and the time $t$.

The initial conditions were then set: the initial time t was initialized at zero, as was the initial vertical velocity $v_y$ and the initial height above the ground $h$. The time-step $dt$ was set to $0.01$ seconds, and arrays were created to store values as the rocket's trajectory evolves.

The first stage, the initial takeoff, ends (by definition) when the rocket leaves the ground - this occurs  immediately, as we assume the rocket begins burning fuel (and thus generating thrust) at time $t=0$. This was accomplished by enclosing the Euler method in a while loop that executes while $h=0$, terminating once the rocket leaves the ground.

The second stage is much longer, and lasts until the rocket has burnt 100% of it's fuel supply, which occurs at time $t\approx69.2$ seconds. For stage two, the same Euler method was again applied to the equation of motion as derived above, enclosed in a while loop that executes while the mass of the rocket-fuel system $M(t)$ is greater than the mass of the rocket alone, which was given by the randomizer as $4291$ kg. When this loop has finished executing, the rocket has expended all of its mass, and the thrust force is zero for the remainder of the evolution (though the rocket continues to rise for some time after).

The third stage, in which the rocket prepares for descent once thrust has ceased, lasts until the vertical velocity shrinks to zero, corresponding to the turnaround point at which the rocket will begin to fall. Therefore, the same equation of motion is solved numerically via the Euler method (neglecting the thrust now, since it is zero) in a while loop that executes while $v_y>0$. When this loop stops executing, the rocket has obtained its maximum height, and begins to fall.

The fourth and final stage lasts until the rocket impacts the ground, at which time the height of the rocket is $h=0$. Therefore, the same equation of motion was enclosed within a while loop that executes while the height is greater than zero, with the small difference that the drag force is now acting in the opposite direction, as the rocket is now moving downwards. 

This stage is separated into two components: first, the rocket will fall until it reaches terminal velocity, at which time it will cease gaining downwards velocity at fall at the same rate until it impacts the ground. 

The terminal velocity is given by:

$$\va{v}_\text{term} = \sqrt{\frac{2 M_r g}{\rho A C}}$$

And so the first part of the fourth stage is enclosed in a while loop that executes while $v_y \leq v_\text{term}$, and then the second stage executes while $h\gt 0$. 

For the second case in which the rocket is launched on Mars, the exact same code was used, with the values for the air density $\rho$ and the gravitational acceleration $g$ tuned to the correct values for that planet. 

***

**Plots:**
On Earth:

![[Pasted image 20220310111123.png]]
On Mars:

![[Pasted image 20220310111037.png]]

It can be seen from the plots that on Mars, the rocket attains a much greater maximum velocity and maximum height due to the decreased values for air density and gravitational acceleration. The flight on Mars also lasts much longer than the flight on Earth.