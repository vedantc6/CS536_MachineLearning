'''
Experimentally verify your computations in the following way: Taking n = 100 and L = 10,
– For j = 1, . . . , 1000:
– Simulate X_i^j, . . . , X_n^j and compute values for Lˆj_MOM and Lˆj_MLE
– For n = 100, L = 10, simulate X_1, . . . , X_n, and compute values for Lˆ_MOM and Lˆ_
MLE.
– Estimate the mean squared error for each population of estimator values.
– How do these estimated MSEs compare to your theoretical MSEs?
'''
# Numpy has been imported to carry out basic arithmetic operations
import numpy as np

# Defining the global variables: n - number of features, L - uniform distribution parameter, m - samples
n = 100
L = 10
m = 1000

# Making the dataset
data = []
for i in range(m):
    data.append(np.random.uniform(0, L, n))

print("Data has {} rows and {} columns".format(len(data), len(data[0])))

# Creating estimated parameter vectors
l_mom_vec = []
l_mle_vec = []

# Storing the estimated parameter values
for i in range(len(data)):
    l_mom_vec.append(2*np.mean(data[i]))
    l_mle_vec.append(max(data[i]))

print("Estimated m.o.m. parameter is of size {}, Estimated m.l.e. paramter is of size {}".format(len(l_mom_vec), len(l_mle_vec)))

# Estimating M.S.E. through estimated parameters
estimated_mse_mom, estimated_mse_mle = 0, 0

for est_mean_mom, est_mean_mle in zip(l_mom_vec, l_mle_vec):
    estimated_mse_mom += (est_mean_mom - L)**2
    estimated_mse_mle += (est_mean_mle - L)**2

estimated_mse_mom = estimated_mse_mom/m
estimated_mse_mle = estimated_mse_mle/m

print("Estimated M.S.E. values from m.o.m. parameter is {:.3f}, and m.l.e. parameter is {:.3f}".format(estimated_mse_mom, estimated_mse_mle))

# From Q4 of assignment, we know the true values of MSE(l_mom) and MSE(l_mle). Let us see the difference
true_mse_mom = (L**2)/(3*n)
true_mse_mle = (2*(L**2))/((n+2)*(n+1))

print("True M.S.E. from m.o.m. estimation: {:.3f}, m.l.e. estimation: {:.3f}".format(true_mse_mom, true_mse_mle))
print("Difference between true and estimated M.S.E. with m.o.m. is {:.3f}".format(true_mse_mom - estimated_mse_mom))
print("Difference between true and estimated M.S.E. with m.l.e. is {:.3f}".format(true_mse_mle - estimated_mse_mle))
