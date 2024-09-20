#!/bin/bash

#SBATCH --account=p32032
#SBATCH --partition=short
#SBATCH --nodes=1 
#SBATCH --ntasks-per-node=10
#SBATCH --time=00:00:05
#SBATCH --mem=16g
#SBATCH --job-name=quest_tutorial


module purge all
module load python-miniconda3
eval "$(conda shell.bash hook)"
conda activate quest_tutorial

python --version
python myFirstScript.py
