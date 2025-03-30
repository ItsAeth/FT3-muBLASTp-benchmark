# muBLASTp-benchmark
Template scripts for benchmarking muBLASTp on HPC systems. Includes a header to run the script on a system with the slurm workload manager.

## How to use:
  1. Download muBLASTp from the repository: https://github.com/vtsynergy/muBLASTP
  2. Compile the binaries using and Intel C/C++ compiler (makefile)
  3. Download a protein sequence database such as UniprotKB, or NCBI nr DB. Must be a fasta file.
  4. Sample the database for queries and (IF NEEDED) a subset of the database. DO NOT modify sample.py or sampleDB.sh. All the config variables are in the sample.env file:
     - `PATH_TO_SAMPLER`: path to the sampler script: "/path/to/dir/.../query_sampler.py"
     - `DB_FILE`: path to the database
     - `OUTFILE`: path to the output. "/path/to/dir/.../queries". The program will complete the filename by adding l_(length)_s(sample_size).
     - `LENGTH`: length of the protein sequences of the sample. Can be set to "mixed" if filtering is not needed.
     - `SAMPLE_SIZES`: must be a string. Contains the size of the samples you want to obtain.
  6. Process the whole database or your subset as explained in the muBLASTp repository's readme.MD. Use formatdb, sortdb and indexdb.
  7. Run all the tests for the benchmark using run_muBLASTp.sh. Here you can change:
     - `mublast_path`: path to the muBLASTp binary
     - `queries`: "path/to/query/dir/.../query*"
     - `db_dir`: directory where the processed database is located.
     - `threads`: string. Contains the thread counts for the tests.
  9. You will find the execution times at the log file (stderr).

## Requirements: 
- Intel C/C++ compiler
- UNIX/Linux operating system
- Python3 + Biopython
