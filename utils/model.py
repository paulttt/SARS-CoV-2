import numpy as np
import matplotlib.pyplot as plt
from data_utils import *

import scipy # to integrate the ode



class SEIRModel():
    '''
    Object representing the SEIR model functioning as an epidemic calculator.
    '''
    def __init__(self, num_steps, N , init_inf, t_inc, t_inf, r_t, rho, kappa_0, kappa):
        ### Call the DataLoader ###
        db = DataLoader()
        ### General ###
        # simulation time per day
        self.num_steps = num_steps

        ### Transmission Dynamics ###
        # population
        #self.N = float(db.compute_population())
        self.N = N
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

        # states: num_steps x [s,e,i,r]
        self.Z = np.zeros([self.num_steps,4])
        # susceptiable ratio
        #self.s = np.zeros([self.num_steps])
        # exposed ratio
        #self.e = np.zeros([self.num_steps])
        # infective ratio
        #self.i = np.zeros([self.num_steps])
        # remove ratio
        #self.r = np.zeros([self.num_steps])
        
        

        # Initial susceptible: The number of susceptible individuals at the beginning of the model run.
        self.Z[0,0] = 1.0-(self.init_inf / self.N)
        #self.s[0] = 1.0-(self.init_inf / self.N)
        # Initial exposed: The number of exposed individuals at the beginning of the model run.
        #self.e[0] = 0.0 / self.N
        # Initial infected: The number of infected individuals at the beginning of the model run.
        self.Z[0,2] = self.init_inf / self.N
        #self.i[0] = self.init_inf / self.N
        # Initial recovered: The number of recovered individuals at the beginning of the model run.
        #self.r[0] = 0.0 / self.N


        ### Adapted Parameter specialized for germany / county germany. ###
        # Social Distancing Parameter
        self.rho = rho
        # Public containment
        self.kappa_0 = kappa_0
        # Quarantine measure only affecting infected people.
        self.kappa = kappa

        # compute the gradient dZ_dt for a specific time instant:
    def gradient(self,t, Z_t):
        dZ_dt = np.zeros(4)
        dZ_dt[0] = - self.rho * self.beta * Z_t[0] * Z_t[2] - self.kappa_0 * Z_t[0]
        dZ_dt[1] = + self.rho * self.beta * Z_t[0] * Z_t[2] - self.alpha * Z_t[1] - self.kappa_0 * Z_t[2] - self.kappa * Z_t[2]
        dZ_dt[2] = + self.alpha * Z_t[1] - self.gamma * Z_t[2]
        dZ_dt[3] = self.gamma * Z_t[2]
        return dZ_dt

    def run(self, solver = 'explicit Euler'):
        '''
        Running the calcuation.
        '''
        if (solver == 'RK45'): # Runge Kutta 45 method
             Z = scipy.integrate.RK45(self.gradient, 0, self.Z[0,:], self.num_steps - 1, vectorized=False)
        else: # use rungeKutta
            for t in range(self.num_steps - 1):
                self.Z[t+1,:] = self.Z[t,:] + self.gradient( 0,self.Z[t,:])
                #self.s[t + 1] = self.s[t] - self.rho * self.beta * self.s[t] * self.i[t] - self.kappa_0 * self.s[t]
                #self.e[t + 1] = self.e[t] + self.rho * self.beta * self.s[t] * self.i[t] - self.alpha * self.e[t] \
                #                          - self.kappa_0 * self.i[t] - self.kappa * self.i[t]
                #self.i[t + 1] = self.i[t] + self.alpha * self.e[t] - self.gamma * self.i[t]
                #self.r[t + 1] = self.r[t] + self.gamma * self.i[t]
                
                
        # stochastisch

        '''
            Applying a differnential equation solver (e.g. Runge–Kutta methods)
        '''

        return (self.Z)


    # Helper functions
    def visualization(self, n_pop = 1, X = 0):
        # Visualizing the process. Just for testing it in the beginning.
        fig, ax = plt.subplots(figsize=(14,6))
        ax.plot(self.Z[:,0]*n_pop, c='b', lw=2, label='S')
        ax.plot(self.Z[:,1]*n_pop, c='orange', lw=2, label='E')
        ax.plot(self.Z[:,2]*n_pop, c='r', lw=2, label='I')
        ax.plot(self.Z[:,3]*n_pop, c='g', lw=2, label='R')
        
        if (X.any() != 0):
            ax.plot(X, c='black', lw=2, label='I_X')

        ax.set_xlabel('Day', fontsize=10)
        ax.set_ylabel('Individuals', fontsize=10)
        ax.grid()

        plt.xticks(fontsize=20)
        plt.yticks(fontsize=20)
        plt.legend()
        plt.show()


if __name__ == "__main__":
    num_steps = 500
    init_inf = 5
    t_inc = 5
    t_inf = 9
    r_t = 2.5 #np.random.normal(2.5, 1.0)
    rho = 1.0
    kappa_0 = 0.0
    kappa = 0.0
    
    n_pop = 2000

    seir = SEIRModel(num_steps,n_pop, init_inf, t_inc, t_inf, r_t, rho, kappa_0, kappa)

    s, e, i, r = seir.run()
    print("s: ", s)
    print("e: ", e)
    print("i: ", i)
    print("r: ", r)

    seir.visualization()
