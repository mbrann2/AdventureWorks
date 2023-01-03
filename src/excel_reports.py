import argparse
import functions
import psycopg2 as pg2
import pandas as pd
import numpy as np
from dotenv import load_dotenv
from pathlib import Path
import os

import sys
sys.path.insert(0, '../src')
sys.path.insert(0, '../data')


parser = argparse.ArgumentParser(
    description="The file paths needed."
)

parser.add_argument("-i", "--input", type=str,
                    required=True, help="input file")
parser.add_argument("-o", "--output", type=str,
                    required=True, help="output file")


args = parser.parse_args()

functions.sql_to_excel(args.input, args.output)
