# Radiative Transfer:

***

The propogation of radiation in a medium, *i.e.* **radiative transfer**, is one of the central problems in astrophysics. The subject is too complicated for a full treatment in this course, but we can easily derive the fundamental equation for radiative transfer in this chapter. 

Assume we have a small cylinder, the bottom of which has an area $dA$ and the length of which is $dr$. 

Let $I_\nu$ be the *intensity* of radiation *perpendicular to the bottom surface* going into a *solid angle* $d\oo$ ($[I_\nu] = Wm^{-2}Hz^{-1}\text{ sterad}^{-1}$). If the intensity changes by an amount $dI_\nu$ in the distance $dr$, the *energy* changes by:

$$dE = dI_\nu \ dA\ d\nu\  d\oo\  d t$$

in the cylinder in time $dt$. This is equal to the emission minus the absorption in the cylinder. The absorbed energy is:

#### $$dE_{\text{abs}} = \aa_\nu \ I_\nu \ dr \ dA \ d\nu \ d\oo \ dt,$$

where $\aa_\nu$ is the **opacity** of the medium at frequency $\nu$.	

Let the amount of energy emitted per hertz at frequency $\nu$ into unit solid angle from unit volume and per unit time be $j_\nu$ ($[j_\nu] = W m^{-3} \ Hz^{-1} \ \text{ sterad}^{-1}$). 

This value, $j_\nu$, is the **emission coefficient** of the medium.

The energy emitted into solid angle $d\oo$ from the cylinder is then:

$$dE_{\text{emitted}} = j_\nu \  dr \ dA \ d\nu \ d \oo \ d t.$$

The equation:

$$dE = -dE_{\text{abs}} + dE_{\text{emitted}}$$

then gives us:

$$dI_\nu = -\aa_\nu I_\nu  dr + j_\nu dr$$

or:

$$\frac{dI_v}{\aa_\nu dr} =  -I_\nu + \frac{j_\nu}{\aa_\nu}.$$

We shall denote the ratio of the *emission coefficient* $j_\nu$ to the *absorption coefficient / opacity* $\aa_\nu$ by $S_\nu$:

$$S_\nu = \frac{j_\nu}{\aa_\nu}.$$

$S_\nu$ is called the **source function**. 

Because $\aa_\nu dr = d\tau_\nu$, where $d\tau_\nu$ is the **optical thickness** at frequency $\nu$, the above equation can be rewritten as:

> ### $$\frac{dI_\nu}{d\tau_\nu} =-I_\nu+S_\nu.$$

The above is the basic equation of radiative transfer