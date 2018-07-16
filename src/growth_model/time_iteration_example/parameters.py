import numpy as np

#====================================================================== 

# Depth of "Classical" Sparse grid
iDepth=1
iOut=6         # how many function values per grid point
which_basis = 1 #linear basis function (2: quadratic local basis)

# control of iterations
numstart = 0   # which is iteration to start (numstart = 0: start from scratch, number=/0: restart)
numits = 1     # which is the iteration to end

# How many random points for computing the errors
No_samples = 1000

# number of monomial sample points
nr_shock = 3

#====================================================================== 

# Model Paramters
n_dims=6  # number of continuous dimensions of the model

# parameters 
sigma = 5
eta = .7
beta = .98
zeta = .3
alpha = .3
chi = 2
gamma = 1
delta = .1
G_bar = .4
sigma_a = .03
sigma_b = .01
sigma_z = .01
rho_a = .9
rho_b = .6
rho_z = .1
L_hat = .4

# Ranges For States
range_cube=1 # range of [0..1]^d in 1D
k_bar=1.7
k_up=7.0
c_bar=0.3
c_up=1.1
i_bar=0.17
i_up=0.7
a_bar=np.exp(-0.21)
a_up=np.exp(0.21)
b_bar=np.exp(-0.0375)
b_up=np.exp(0.0375)
z_bar=np.exp(-0.03)
z_up=np.exp(0.03)

# Ranges for Controls
ck_bar=1.5
ck_up=8.0
cc_bar=0.25
cc_up=1.2
ci_bar=0.15
ci_up=0.8
cl_bar=0.1 # FIXME: MADE IT LOWER SINCE I LOWERED cl_up
cl_up=0.39 # FIXME: MADE IT LOWER THAN L_hat
cq_bar=0.2
cq_up=8
clam_bar=200
clam_up=100000

# Steady-state values
css = 1
lss = 0.2
iss = 1
kss = 1
qss = 1
lamss = 1

#====================================================================== 




