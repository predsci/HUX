# ![Icon](figures/rsz_psi_logo.png)<!-- .element height="10%" width="10%" --> HUX (Heliospheric Upwind Extrapolation)

The following notebooks include an analysis of the HUX model (Heliospheric Upwind Extrapolation) developed by Riley et al [1]. 
The HUX model is a technique to map solar wind streams from the Sun to 1 AU. By neglecting magnetic field, pressure gradient and gravity, the fluid momentum equation reduces to the inviscid Burgers' equation.

In order, to understand the weight of adding thermal pressure and proton mass density to forecast solar wind streams, I applied PDE-FIND a parsimonious algorithm developed by Rudy et al [2]. Given a large library of candidate terms consisting partials and nonlinearities in spatial domain, PDE-FIND finds the optimal subset of active library terms from a time sequential data-set.

The results verify that the HUX model is a parsimonious model which matches the dynamical evolution captured by global models, yet is as simple as the ballistic approximation.


# References
[1] [Riley, P. and Lionello, Roberto. Mapping solar wind streams from the Sun to 1 AU: A comparison of techniques. Solar Physics, 270(2), 575–592, 2011.](https://www.researchgate.net/publication/226565167_Mapping_Solar_Wind_Streams_from_the_Sun_to_1_AU_A_Comparison_of_Techniques)

[2] [Samuel H. Rudy, Steven L. Brunton, Joshua L. Proctor, and J. Nathan Kutz. Data-driven discovery of partial differential equations. Science Advances, 3(4):e1602614, 2017.](https://arxiv.org/abs/1609.06401)


# Dependencies
1. [Python >= 3.7](https://www.python.org/downloads/)
1. [numpy >= 1.19.1](https://numpy.org/install/)
3. [matplotlib >= 3.3.1](https://matplotlib.org/users/installing.html)
4. [scipy >= 1.5.0](https://www.scipy.org/install.html)


# Authors
[Predictive Science Inc.](https://www.predsci.com/portal/home.php)

- Pete Riley, pete@predsci.com

- Opal Issan, oissan@predsci.com

# License
MIT


