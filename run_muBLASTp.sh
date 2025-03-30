#!/bin/bash
#SBATCH -N 
#SBATCH -n 
#SBATCH -t 
#SBATCH --mem=
#SBATCH --error=
#SBATCH --output=
#SBATCH --mail-user=
#SBATCH --mail-type=

set -e

# Path to the program
mublast_path="path/to/mublastp/.../muBLASTp"

# Path to query files (use wildcard to select all starting with query or your choice)
queries="path/to/query/dir/.../query*"

# Path to sorted database
db_dir="/path/to/database/.../sorted"

# Number of threads for the tests (example with 1, 2, 4, 8, 16 threads)
threads="1 2 4 8 16"

# Run tests
for query in $queries; do
  for nth in $threads; do
   "$mublast_path" -i "$query" -d "$db_dir" -t $nth
  done
done
