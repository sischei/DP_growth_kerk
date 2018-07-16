from parameters import *                      #parameters of model
import init_val as initval              #interface to sparse grid library/terminal VF
import interpolation as interpol    #interface to sparse grid library/iteration
import postprocessing as post                 #computes the L2 and Linfinity error of the model

import TasmanianSG                            #sparse grid library
import numpy as np


#======================================================================
# Start with Policy Fuction Iteration

# Policy function function
endvars=TasmanianSG.TasmanianSparseGrid()
if (numstart==0):
    endvars=initval.initialize(n_dims, iDepth)
    endvars.write("endvars_1." + str(numstart) + ".txt") #write file to disk for restart

# Policy function during iteration
else:
    endvars.read("endvars_1." + str(numstart) + ".txt")  #read file from disk
    
endvarsold=TasmanianSG.TasmanianSparseGrid()
endvarsold=endvars

for i in range(numstart, numits):
    endvars=TasmanianSG.TasmanianSparseGrid()
    endvars=interpol.sparse_grid(n_dims, iDepth, endvarsold)
    endvarsold=TasmanianSG.TasmanianSparseGrid()
    endvarsold=endvars
    endvars.write("endvars_1." + str(i+1) + ".txt")
    print " step ", i, " computed  "
    print "========================"
    
#======================================================================
print "==============================================================="
print " "
print " Computation of RBC model of dimension ", n_dims ," finished after ", numits , " steps"
print " "
print "==============================================================="
#======================================================================

# compute errors   
#avg_err=post.ls_error(n_dims, numstart, numits, No_samples)

#======================================================================
print "==============================================================="
print " "
print " Errors are computed -- see errors.txt"
print " "
print "==============================================================="
#======================================================================
