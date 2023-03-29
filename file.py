# import numpy as np
# import pickle
# import pandas as pd

# p = np.array([[0,67,145,84,116,128,98,97.8]])
# pickled_model = pickle.load(open('hhcs_rfc.sav', 'rb'))
# print(pickled_model.predict(p))

# fah = 104
# cel = (fah-32)/1.8

# print(cel)

# f=96
# temp = f*9/5+32
# print(temp)


import json
with open('hdata.json') as user_file:
  file_contents = user_file.read()

# print(file_contents)

parsed = json.loads(file_contents)
ex = 'lowsugar'
# print(parsed['th'])
data = parsed[ex]

for i in data:
  print(i)

