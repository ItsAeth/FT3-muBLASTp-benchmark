# FT3-muBLASTp-benchmark
Scripts for benchmarking muBLASTp on HPC systems with the slurm workload manager, tested on Finisterrae III (Galicia Supercomputing Center).

## How to use:
  1. Download muBLASTp from the repository: https://github.com/vtsynergy/muBLASTP
  2. Compile the binaries using and Intel C/C++ compiler (makefile)
  3. Download a protein sequence database such as UniprotKB, or NCBI nr DB. Must be a fasta file.
  4. Sample the database for queries and (IF NEEDED) a subset of the database. DO NOT modify sample.py or sampleDB.sh. Change these environment variables in the .env file:
     - `DB_FILE`: path to the database: "/path/to/dir/database.fasta"
     - `OUTFILE`: path to the output: "/path/to/dir/queries.fasta"
     - `LENGTH`: length of the protein sequences of the sample. Can be set to "mixed" or a number.
     - `SAMPLE_SIZES`: must be a string. Contains the size of the samples you want to obtain.
  5. Process the whole database or your subset as explained in the muBLASTp repository's readme.MD. Use formatdb, sortdb and indexdb.
  6. Run all the tests for the benchmark using run_muBLASTp.sh. Here you can change:
     - `db_dir`: directory where the processed database is located.
     - `threads`: string. Contains the thread counts for the tests.
  7. You will find the execution times at the log file (stderr).

## Requirements: 
- Intel C/C++ compiler
- UNIX/Linux operating system
- Python3 + Biopython
