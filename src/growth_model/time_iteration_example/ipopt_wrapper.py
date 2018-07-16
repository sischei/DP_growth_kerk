from parameters import *
from econ import *
import numpy as np
import math as math

#=======================================================================
#   Objective Function to start VFI (in our case, the value function)
        
def EV_F(X, k_init, n_dims, currentapprox):
    
    return 0

#=======================================================================
#   Computation of gradient (first order finite difference) of initial objective function 

def EV_GRAD_F(X, k_init, n_dims, currentapprox):
    ret = 0.0*np.empty(n_dims)
    
    return ret
    
#======================================================================
#   Equality constraints for the first time step of the model
# Structure of G:
#     0-5  endogenous variables
            
def EV_G(X, state_vec, n_dims, currentapprox):
    N=len(X)
    M=N     # number of constraints
    G=np.empty(M, float)
    
    #Extract variables
    #State Variables
    k=state_vec[0]
    c_p=state_vec[1]
    i_p=state_vec[2]
    A=state_vec[3]
    B=state_vec[4]
    Z=state_vec[5]
    
    #Endogenous Variables
    c=X[0]
    l=X[1]
    i=X[2]
    k_n=X[3]
    q=X[4]
    lam=X[5]  #FIXME Thomas, is there not a second lambda missing
    
    # MONOMIAL INTEGRATION  -- there are 3 shocks (stored in shock_eps(:))
    int1 = 0.0
    int2 = 0.0
    int3 = 0.0
    int4 = 0.0
    int5 = 0.0
    int6 = 0.0

    for quad_count in range(1, 2*nr_shock + 1):  
 
        shock_eps=np.zeros(nr_shock) #shock 1: A, shock 2: B, shock 3: C
        
        for i in range(1, nr_shock + 1):
            if (quad_count%2 == 1) and (quad_count == (2*i -1)):
                shock_eps[i-1]=math.sqrt(nr_shock/2.0)
            elif (quad_count%2 == 0) and (quad_count == (2*i)):
                shock_eps[i-1]= -math.sqrt(nr_shock/2.0)
    
        # debug -- no shocks
        #A_n=np.exp(rho_a*np.log(A))  #+np.random.normal(0, sigma_a, 1)
        #B_n=np.exp(rho_b*np.log(B))  #+np.random.normal(0, sigma_b, 1)
        #Z_n=np.exp(rho_z*np.log(Z))  #+np.random.normal(0, sigma_z, 1)

        A_n=(np.exp(rho_a*np.log(A)))*np.exp(sigma_a*shock_eps[0])  
        B_n=(np.exp(rho_b*np.log(B)))*np.exp(sigma_b*shock_eps[1])  
        Z_n=(np.exp(rho_z*np.log(Z)))*np.exp(sigma_z*shock_eps[2]) 

        #exit(0)

        # Interpolate current approximation to get next period's variables
        nextperstate = np.empty(N,float)
        nextperstate[0]=k_n
        nextperstate[1]=c
        nextperstate[2]=i
        nextperstate[3]=A_n
        nextperstate[4]=B_n
        nextperstate[5]=Z_n
        nextperchoice=currentapprox.evaluate(nextperstate)
        c_n=nextperchoice[0]
        l_n=nextperchoice[1]
        i_n=nextperchoice[2]
        q_n=nextperchoice[4]
        lam_n=nextperchoice[5]
        
        MRS = zeta*(c-eta*c_p)/(lam*(1-l))
        
        Gamma_adjust=(1-(i/i_p)*((i/i_p)-gamma))*np.exp(-(chi/2)*((i/i_p)-gamma)**2)
        MRI = lam*q*Gamma_adjust+beta*ExpI_rhs(Z, Z_n, lam, lam_n, c_p, c, c_n, l, l_n, i, i_n, q_n)
        f_prod=output_f(A, k, l)
        ResConst = c + i + G_bar*B - f_prod

        # Equilibrium conditions -- not efficiently evaluated expectation
        int1 = (lam-Lagr(Z, Z_n, c_p, c, c_n, l, l_n)) + int1
        int2 = ((1-alpha)*output_f(A, k, l)/l - MRS) + int2
        int3 = (lam*q-eulerK_rhs(Z, Z_n, lam_n, c_p, c, c_n, l, l_n, A_n, k_n, q_n)) + int3
        int4 = (lam - MRI) + int4
        int5 = (k_n-((1-delta)*k+i*np.exp(-(chi/2)*((i/i_p)-gamma)**2))) + int5
        int6 = ResConst + int6
        
#...finish MONOMIAL integration        
    G[0]=int1/(2.0*nr_shock)
    G[1]=int2/(2.0*nr_shock)
    G[2]=int3/(2.0*nr_shock)
    G[3]=int4/(2.0*nr_shock)
    G[4]=int5/(2.0*nr_shock)
    G[5]=int6/(2.0*nr_shock)
    
    #print "G - from ipopt - wrapper" , G
    
# FIXME: MONOMIAL RULES FOR INTEGRATION FROM IPOPT_WRAPPER IN FORTRAN CODE
    return G
    
#======================================================================
#   Computation (finite difference) of Jacobian of equality constraints 
#   for first time step
    
def EV_JAC_G(X, flag, k_init, n_dims, currentapprox):
    N=len(X)
    M=N
    NZ=M*N
    A=np.empty(NZ, float)
    ACON=np.empty(NZ, int)
    AVAR=np.empty(NZ, int)    
    
    # Jacobian matrix structure
    
    if (flag):
        for ixM in range(M):
            for ixN in range(N):
                ACON[ixN + (ixM)*N]=ixM
                AVAR[ixN + (ixM)*N]=ixN
                
        return (ACON, AVAR)
        
    else:
        # Finite Differences
        h=1e-4
        gx1=EV_G(X, k_init, n_dims, currentapprox)
        
        for ixM in range(M):
            for ixN in range(N):
                xAdj=np.copy(X)
                xAdj[ixN]=xAdj[ixN]+h
                gx2=EV_G(xAdj, k_init, n_dims, currentapprox)
                A[ixN + ixM*N]=(gx2[ixM] - gx1[ixM])/h
        return A
  
#======================================================================

    
    
    
    
    
    
    
    
    
            
            
            
    
    
    
    
    
    
