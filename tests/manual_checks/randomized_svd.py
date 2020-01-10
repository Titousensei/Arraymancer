import numpy as np
from sklearn.utils.extmath import randomized_svd
from scipy.linalg import hilbert

np.set_printoptions(linewidth = 120)

Observations = 10
Features = 4000
N = max(Observations, Features)
k = 7

# Create a known ill-conditionned matrix for testing
H = hilbert(N)[:Observations, :Features]

print(f'Matrix of shape: [{Observations}, {Features}]')
print(f'Target SVD: [{Observations}, {k}]')

(U, S, Vh) = randomized_svd(H, n_components=k, n_oversamples=5, n_iter=2)

print("\n#################################\n")
print("U - left singular vectors")
print(U)
print("\n#################################\n")
print("S - Singular values diagonal")
print(S)
print("\n#################################\n")
print("Vh - transposed right singular vectors")
print(Vh)

# ----------------------------------------------------------------------------------------

# Matrix of shape: [10, 4000]
# Target SVD: [10, 7]

# #################################

# U - left singular vectors
# [[ 0.65162684  0.65057201 -0.35719096 -0.14773729  0.05033365  0.01357759 -0.00296539]
#  [ 0.42054159  0.02898395  0.50750611  0.59765148 -0.40750871 -0.19173922  0.06681127]
#  [ 0.32674677 -0.15267669  0.42101639 -0.02198219  0.4953174   0.55403911 -0.34685306]
#  [ 0.27292653 -0.22893528  0.24491001 -0.3214986   0.3209642  -0.23439855  0.5691567 ]
#  [ 0.23706497 -0.26561986  0.08146976 -0.37608302 -0.05439897 -0.4247088  -0.03363757]
#  [ 0.21105978 -0.28402146 -0.05560319 -0.29353114 -0.30613449 -0.13405599 -0.42604752]
#  [ 0.19114047 -0.29290377 -0.16808681 -0.13962608 -0.36103414  0.23170113 -0.18873756]
#  [ 0.17528455 -0.29644065 -0.26022741  0.04847158 -0.23050751  0.38922779  0.27809253]
#  [ 0.16229759 -0.29682494 -0.33602574  0.24992016  0.05106607  0.19516204  0.39712243]
#  [ 0.15142323 -0.29529245 -0.39875135  0.45303184  0.44752782 -0.39941109 -0.31300087]]

# #################################

# S - Singular values diagonal
# [1.90675907e+00 4.86476625e-01 7.52734238e-02 8.84829787e-03 7.86824889e-04 3.71028924e-05 1.74631562e-06]

# #################################

# Vh - transposed right singular vectors
# [[ 6.31451684e-01  3.90868629e-01  2.93466320e-01 ...  3.67020834e-04  3.66929129e-04  3.66837470e-04]
#  [ 6.47654515e-01  8.23647773e-02 -6.54029135e-02 ... -7.35287384e-04 -7.35103911e-04 -7.34920529e-04]
#  [-3.79908478e-01  4.07402710e-01  3.85879850e-01 ... -1.06080782e-03 -1.06054399e-03 -1.06028030e-03]
#  ...
#  [ 7.29134760e-02 -4.95875991e-01  2.71271575e-01 ...  1.18814815e-03  1.24326269e-03  1.68559884e-03]
#  [ 1.85040565e-02 -2.31238429e-01  4.94397948e-01 ... -4.38379629e-04 -6.19474967e-04 -1.01713827e-03]
#  [-6.14168775e-03  1.28596821e-01 -5.31211518e-01 ... -4.70909618e-04 -1.29102280e-04 -2.21526985e-04]]