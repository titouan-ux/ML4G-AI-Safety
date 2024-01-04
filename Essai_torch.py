import torch
import numpy as np
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
from numpy import random as rd

N = 2

# ls=[1,2,3,4,5,6,7,8,9]
# ls2=ls[8:1:-1]
# # print(ls2)`
# training_set=torch.tensor([[1]+[rd.randint(3,10) for i in range(8)]+[2] for i in range(N)]).to(device)

# print(training_set)

# list_training_set=training_set.tolist()

# trg_set=torch.tensor([[1]+list_training_set[i][8:0:-1]+[2] for i in range(N)]).to(device)
# print(trg_set)


print(torch.mean([[1,2,3],[1,1,1]]))