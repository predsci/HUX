# ![Icon](figures/rsz_psi_logo.png)<!-- .element height="10%" width="10%" --> HUX (Heliospheric Upwinding eXtrapolation)

The following notebooks include an analysis of the HUX Technique (Heliospheric Upwind eXtrapolation) developed by Riley et al [1]. 


# Abstract
Understanding how coronal structure propagates and evolves from the Sun and into the
heliosphere has been thoroughly explored using sophisticated MHD models. From these, we
have a reasonably good working understanding of the dynamical processes that shape the
formation and evolution of stream interaction regions and rarefactions, including their locations,
orientations, and structure. However, given the technical expertise required to produce, maintain,
and run global MHD models, their use has been relatively restricted. In this study, we refine a
simple Heliospheric eXtrapolation Technique (HUX) to include not only forward mapping from the
Sun to 1 AU (or elsewhere), but backward mapping towards the Sun. We demonstrate that this
technique can provide substantially more accurate mappings than the standard, and often applied
“ballistic” approximation. We also use machine learning (ML) methods to explore whether the
HUX approximation to the momentum equation can be refined without loss of simplicity, finding
that it likely provides the optimum balance. We suggest that HUX can be used, in conjunction
with coronal models (PFSS or MHD) to more accurately connect measurements made at 1 AU,
Stereo-A, Parker Solar Probe, and Solar Orbiter with their solar sources. In particular, the HUX
technique: (1) provides a substantial improvement over the “ballistic” approximation for connecting
to the source longitude of streams; (2) is almost as accurate, but considerably easier to implement
than MHD models; and (3) can be applied as a general tool to magnetically connect different
regions of the inner heliosphere together, as well as providing a simple 3-D reconstruction.


# References
[1] [Riley, P. and Lionello, Roberto. Mapping solar wind streams from the Sun to 1 AU: A comparison of techniques. Solar Physics, 270(2), 575–592, 2011.](https://www.researchgate.net/publication/226565167_Mapping_Solar_Wind_Streams_from_the_Sun_to_1_AU_A_Comparison_of_Techniques)


# Dependencies
1. [Python >= 3.7](https://www.python.org/downloads/)
1. [numpy >= 1.19.1](https://numpy.org/install/)
3. [matplotlib >= 3.3.1](https://matplotlib.org/users/installing.html)
4. [scipy >= 1.5.0](https://www.scipy.org/install.html)
5. [pyhdf >= 0.10.2](https://pypi.org/project/pyhdf/)


# Authors
[Predictive Science Inc.](https://www.predsci.com/portal/home.php)

- Pete Riley, pete@predsci.com

- Opal Issan, oissan@predsci.com

# License
MIT
