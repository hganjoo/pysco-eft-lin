import cosmotable
import pandas as pd

path = '.'

p1 = pd.Series({
    "base":"./",
    "theory": "eft",
    "parametrized_mu0":-0.2,
    "alphaB0": 0.3,
    "alphaM0": 0.1,
    "Om_m":0.3,
    "nthreads": 1,
    "H0": 72,
    "T_cmb": 2.726,
    "N_eff": 3.044,
    "w0": -1.0,
    "wa": 0,
    "boxlen": 100,
    "ncoarse": 8,
    "npart": 256**3,
    "seed": 42,
    "evolution_table":'yes',
    "extra":"test"
    })

p2 = pd.Series({
 "theory": "eft",
    "alphaM0":0,"alphaB0":0.2,
 "H0": 70.0,
"Om_m": 0.3,
"T_cmb": 2.726,
"N_eff": 3.044,
"w0": -1.0,
"wa": 0,
"base": "./",
"extra": "test"})

tables = cosmotable.generate(p1)