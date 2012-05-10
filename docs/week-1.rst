Week 1: Reading about the general theory of graphical models
============================================================

Many different books explains the theory of graphical models. The main source for this project will be chapter 8 in [bishop06]_.


The EM algorithm
----------------

These are some of the questions that have appeared while reading about the EM
algorithm in [bishop06]_ (esp. section 9.4).

In the decomposition

.. math::

    \ln{p(X|\theta)} = \mathcal{L}(q, \theta) + KL(q||p)

why do we maximize :math:`\mathcal{L}` instead of :math:`KL` wrt. :math:`q`?
And likewise wrt. :math:`\theta`?
