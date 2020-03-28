import numpy as np
import matplotlib.pyplot as plt
from data_utils import *


class SEIRModel():
    '''
    Object representing the SEIR model functioning as an epidemic calculator.
    '''
    def __init__(self, num_steps, init_inf, t_inc, t_inf, r_t, rho, kappa_0, kappa):
        ### Call the DataLoader ###
        db = DataLoader()
        ### General ###
        # simulation time per day
        self.num_steps = num_steps

        ### Transmission Dynamics ###
        # population
        #self.N = float(db.compute_population())
        self.N = 1e7 + 10 + 5
        print(self.N)
        # Initial infection count
        self.init_inf = init_inf
        # t_inc: length of incubation period
        self.t_inc = t_inc
        # t_inf: Duration patient is infectious
        self.t_inf = t_inf
        # r_t: Basic reproduction number (measure of contagiousness)
        self.r_0 = r_t

        ### Clinical Dynamics ###
        # mu: The natural mortality rate (this is unrelated to disease).
        #self.mu = mu
        # t_rec: Recovery Times - Length of hospital stay
        #self.t_rec = t_rec


        # beta: The parameter controlling how often a susceptible-infected contact results in a new exposure.
        self.beta = (r_t / t_inf)
        # gamma: The rate an infected recovers and moves into the resistant phase.
        self.gamma = (1 / t_inf)
        # alpha: The rate at which an exposed person becomes infective.
        self.alpha = (1 / t_inc)


        # susceptiable ratio
        self.s = np.zeros([self.num_steps])
        # exposed ratio
        self.e = np.zeros([self.num_steps])
        # infective ratio
        self.i = np.zeros([self.num_steps])
        # remove ratio
        self.r = np.zeros([self.num_steps])

        # Initial susceptible: The number of susceptible individuals at the beginning of the model run.
        self.s[0] = 1e7 / self.N
        # Initial exposed: The number of exposed individuals at the beginning of the model run.
        self.e[0] = 40.0 / self.N
        # Initial infected: The number of infected individuals at the beginning of the model run.
        self.i[0] = self.init_inf / self.N
        # Initial recovered: The number of recovered individuals at the beginning of the model run.
        #self.r[0] = 0.0 / self.N


        ### Adapted Parameter specialized for germany / county germany. ###
        # Social Distancing Parameter
        self.rho = rho
        # Public containment
        self.kappa_0 = kappa_0
        # Quarantine measure only affecting infected people.
        self.kappa = kappa


    def run(self):
        '''
        Running the calcuation.
        '''

        # deterministic
        for t in range(self.num_steps - 1):
            self.s[t + 1] = self.s[t] - self.rho * self.beta * self.s[t] * self.i[t] - self.kappa_0 * self.s[t]
            self.e[t + 1] = self.e[t] + self.rho * self.beta * self.s[t] * self.i[t] - self.alpha * self.e[t] \
                                      - self.kappa_0 * self.i[t] - self.kappa * self.i[t]
            self.i[t + 1] = self.i[t] + self.alpha * self.e[t] - self.gamma * self.i[t]
            self.r[t + 1] = self.r[t] + self.gamma * self.i[t]

        # stochastisch

        '''
            Applying a differnential equation solver (e.g. Runge–Kutta methods)
        '''

        return (self.s, self.e, self.i, self.r)


    # Helper functions
    def visualization(self, n_pop = 1):
        # Visualizing the process. Just for testing it in the beginning.
        fig, ax = plt.subplots(figsize=(14,6))
        ax.plot(self.s*n_pop, c='b', lw=2, label='S')
        ax.plot(self.e*n_pop, c='orange', lw=2, label='E')
        ax.plot(self.i*n_pop, c='r', lw=2, label='I')
        ax.plot(self.r*n_pop, c='g', lw=2, label='R')

        ax.set_xlabel('Day', fontsize=10)
        ax.set_ylabel('Individuals', fontsize=10)
        ax.grid()

        plt.xticks(fontsize=20)
        plt.yticks(fontsize=20)
        plt.legend()
        plt.show()


if __name__ == "__main__":
    num_steps = 500
    init_inf = 1000
    t_inc = 14
    t_inf = 12
    r_t = np.random.normal(2.5, 1.0)
    print(r_t)
    rho = 1.0
    kappa_0 = 0.0
    kappa = 0.0

    seir = SEIRModel(num_steps, init_inf, t_inc, t_inf, r_t, rho, kappa_0, kappa)

    s, e, i, r = seir.run()
    print("s: ", s)
    print("e: ", s)
    print("i: ", s)
    print("r: ", s)

    seir.visualization()
