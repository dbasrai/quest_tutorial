#!/bin/bash

#SBATCH --account=p32032
#SBATCH --partition=normal
#SBATCH --nodes=1 
#SBATCH --ntasks-per-node=20
#SBATCH --time=48:00:00
#SBATCH --mem=180g
#SBATCH --job-name=all


module purge all
module load python-miniconda3
eval "$(conda shell.bash hook)"
conda activate mp_opto

python --version
python coSweepRegsAll.py
