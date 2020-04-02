# Stan

This readme explains how the statistical modeling language stan can be used to implement the PMCMC algorithm and thereby to solve the SARS-CoV-2 model. 

Details about how to use Pystan can be found here: https://towardsdatascience.com/an-introduction-to-bayesian-inference-in-pystan-c27078e58d53

User guide for HMM:https://mc-stan.org/docs/2_18/stan-users-guide/hmms-section.html





Prior recommendations:

https://github.com/stan-dev/stan/wiki/Prior-Choice-Recommendations



Paper about using STAN for SIR model:

https://www.sciencedirect.com/science/article/pii/S1755436519300325

https://github.com/anastasiachtz/COMMAND_stan

- Stan has built-in ode solvers:

SIR- model observations: 

y[t] ~ Poisson(lambda) where lambda depends on I(t) 



to do after solving:
1) check for convergence by expectation of trace plots  and by checking the Rˆ convergence statistic reported by Stan. If the chains have not yet converged to a common distribution the Rˆ statistic will be greater than one

2) check for sufficient exploration by calculating effective sample sizes for each model parameter which are an estimate of the number of independent draws from the marginal posterior distributions that are represented in the numerical output

errors:

```
WARNING:pystan:n_eff / iter below 0.001 indicates that the effective sample size has likely been overestimated
WARNING:pystan:Rhat above 1.1 or below 0.9 indicates that the chains very likely have not mixed
WARNING:pystan:84 of 2000 iterations ended with a divergence (4.2 %).
WARNING:pystan:Try running with adapt_delta larger than 0.8 to remove the divergences.
WARNING:pystan:264 of 2000 iterations saturated the maximum tree depth of 10 (13.2 %)
WARNING:pystan:Run again with max_treedepth larger than 10 to avoid saturation
```

