import sys
import os
import logging
import random as rd
import Bio.SeqIO as bio
from Bio.SeqIO.FastaIO import SimpleFastaParser

def get_env_vars():

    env_vars = ["DB_FILE", "OUTFILE", "LENGTH", "SAMPLE_SIZE"]

    # Check for missing variables
    missing = [var for var in env_vars if os.getenv(var) is None]
    missing = ",".join(missing)
    if len(missing) != 0:
        logging.error(f"Missing variables: {missing}")
        sys.exit(1)
    
    # Get variables from environment
    db_file = os.getenv("DB_FILE")
    outfile = os.getenv("OUTFILE")
    length = os.getenv("LENGTH")
    sample_size = os.getenv("SAMPLE_SIZE")

    logging.info("Environment variables loaded successfully. Now checking:")

    # Checking variable values
    if not os.path.exists(db_file):
            logging.error("Database file not found.")
            sys.exit(1)

    if length != "mixed":
        try:
            length = int(length)
            if length <= 0:
                logging.error("Length must be a positive integer or 'mixed'.")
                sys.exit(1)
        except ValueError:
            logging.exception("Length must be a positive integer or 'mixed'.")
            sys.exit(1)

    try:
        sample_size = int(sample_size)
    except ValueError:
        logging.exception("Sample size must me a positive integer.")
        sys.exit(1)

    if sample_size <= 0:
        logging.error("Sample size must be a positive integer.")
        raise ValueError("Sample size must be a positive integer.")

    outfile = f"{outfile}_s{sample_size}_l{length}.fasta"
    return [db_file, outfile, length, sample_size]

def reservoir_sampling(seq_iter, sample_size):
    # Step 1: Fill the reservoir with the first k elements
    reservoir = []
    for i, seq in enumerate(seq_iter):
        if i < sample_size:
            reservoir.append(seq)
        else:
            # Step 2: Replace elements with gradually decreasing probability
            j = rd.randint(0, i)
            if j < sample_size:
                reservoir[j] = seq
    return reservoir

def __main__():

    # Logger setup
    logging.basicConfig(level=logging.INFO, filename = "log.log", filemode = "w",
                        format="%(asctime)s - %(levelname)s - %(message)s")

    # Get and check environment variables
    db_file, outfile, length, sample_size = get_env_vars()

    logging.info("Variables correct. Now parsing database.")
    
    with open(db_file) as db_fasta:
        if length == "mixed":
            seq_iter = SimpleFastaParser(db_fasta)
        else:
            seq_iter = (seq for seq in SimpleFastaParser(db_fasta) if len(seq[1]) == length)

        logging.info("Finished parsing. Now sampling.")

        sample = reservoir_sampling(seq_iter, sample_size)

        logging.info("Sampled successfully. Now writing")

    with open(outfile, "w") as out:
        for seq in sample:
            out.write(f">{seq[0]}\n{seq[1]}\n")

    logging.info(f"{sample_size} sequences written successfully! Output: {outfile}.")

if __name__ == "__main__":
    __main__()
