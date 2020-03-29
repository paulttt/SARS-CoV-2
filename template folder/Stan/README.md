# Stan

This readme explains how the statistical modeling language stan can be used to implement the PMCMC algorithm and thereby to solve the SARS-CoV-2 model. 

Details about how to use Pystan can be found here: https://towardsdatascience.com/an-introduction-to-bayesian-inference-in-pystan-c27078e58d53

User guide for HMM:https://mc-stan.org/docs/2_18/stan-users-guide/hmms-section.html





Prior recommendations:

https://github.com/stan-dev/stan/wiki/Prior-Choice-Recommendations



Paper about using STAN for SIR model:

https://www.sciencedirect.com/science/article/pii/S1755436519300325

- Stan has built-in ode solvers:

SIR- model observations: 

y[t] ~ Poisson(lambda) where lambda depends on I(t) 



to do after solving:
1) check for convergence by expectation of trace plots  and by checking the Rˆ convergence statistic reported by Stan. If the chains have not yet converged to a common distribution the Rˆ statistic will be greater than one

2) check for sufficient exploration by calculating effective sample sizes for each model parameter which are an estimate of the number of independent draws from the marginal posterior distributions that are represented in the numerical output



