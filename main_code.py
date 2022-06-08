import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import os
import glob

config = open('config.txt').read()
print(config)
files = sorted(glob.glob(os.path.join("data","*.csv")))
print(files)
