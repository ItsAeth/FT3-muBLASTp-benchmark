#!/bin/bash
#SBATCH -N
#SBATCH -n
#SBATCH -t
#SBATCH --mem=
#SBATCH --error=
#SBATCH --output=
#SBATCH --mail-type=
#SBATCH --mail-user=

set -e
source sample.env
export DB_FILE OUTFILE LENGTH SAMPLE_SIZE

for SAMPLE_SIZE in $SAMPLE_SIZES; do
	# Run the sampler for different sample sizes
	python3 $PATH_TO_SAMPLER
done
