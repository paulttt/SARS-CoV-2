import numpy as np
import matplotlib.pyplot as plt


class SEIRModel():
    '''
    Object representing the SEIR model functioning as an epidemic calculator.
    '''
    def __init__(self, num_steps, population, init_inf, t_inc, t_inf, r_0, mu, t_rec, ):
        ### General ###
        # simulation time per day
        self.num_steps = num_steps

        ### Transmission Dynamics ###
        # population
        self.N = population
        # Initial infection count
        self.init_inf = init_inf
        # t_inc: length of incubation period
        self.t_inc = t_inc
        # t_inf: Duration patient is infectious
        self.t_inf = t_inf
        # r_t: Basic reproduction number (measure of contagiousness)
        self.r_0 = r_0

        ### Clinical Dynamics ###
        # mu: The natural mortality rate (this is unrelated to disease).
        self.mu = mu
        # t_rec: Recovery Times - Length of hospital stay
        self.t_rec = t_rec


        # beta: The parameter controlling how often a susceptible-infected contact results in a new exposure.
        self.beta = 0.0
        # gamma: The rate an infected recovers and moves into the resistant phase.
        self.gamma = 0.0
        # sigma: The rate at which an exposed person becomes infective.
        self.sigma = 0.0


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
        self.r[0] = 0.0 / self.N


    def run(self):
        # Running the calcuation.
        for t in range(self.num_steps - 1):
            self.s[t + 1] = self.s[t] - self.beta * self.s[t] * self.i[t]
            self.e[t + 1] = self.e[t] + self.beta * self.s[t] * self.i[t] - self.sigma * self.e[t]
            self.i[t + 1] = self.i[t] + self.sigma * self.e[t] - self.gamma * self.i[t]
            self.r[t + 1] = self.r[t] + self.gamma * self.i[t]


    # Helper functions
    def visulatization(self):
        # Visualizing the process. Just for testing it in the beginning.
        fig, ax = plt.subplots(figsize=(14,6))
        ax.plot(self.s, c='b', lw=2, label='S')
        ax.plot(self.e, c='orange', lw=2, label='E')
        ax.plot(self.i, c='r', lw=2, label='I')
        ax.plot(self.r, c='g', lw=2, label='R')

        ax.set_xlabel('Day', fontsize=10)
        ax.set_ylabel('Individuals', fontsize=10)
        ax.grid()

        plt.xticks(fontsize=20)
        plt.yticks(fontsize=20)
        plt.legend()
        plt.shwo()
