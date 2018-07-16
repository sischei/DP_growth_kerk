#!/bin/sh
#BATCH --job-name=job1
#SBATCH --output=job1.out
#SBATCH --error=job1.err
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
 
module load mpi4py/1.3+python-2.7-2015q2

python main.py

