# This program is needed in Problem 6.5 Interpret output from a program.

from math import sin, cos, pi

def f(x):
	return sin(x)

def df_approx(f, x, delta_x):
	return (f(x+delta_x)-f(x))/delta_x

x = pi/3
for n in range(1, 20):
    delta_x = 10**(-n)
    calculated = df_approx(f, x, delta_x)
    exact = cos(x)
    rel_err = abs(calculated - exact)/abs(exact)
    abs_err = abs(calculated - exact)

    print("delta_x: %e, df_approx: %13.10e, df_exact: %13.10e, abs_error: %e, \
rel_error: %e, n=%d" % (delta_x, calculated, exact, abs_err, rel_err, n))


"""
printed:

delta_x: 1.000000e-01, df_approx: 4.5590188541e-01, df_exact: 5.0000000000e-01, abs_error: 4.409811e-02, rel_error: 8.819623e-02, n=1
delta_x: 1.000000e-02, df_approx: 4.9566157577e-01, df_exact: 5.0000000000e-01, abs_error: 4.338424e-03, rel_error: 8.676848e-03, n=2
delta_x: 1.000000e-03, df_approx: 4.9956690400e-01, df_exact: 5.0000000000e-01, abs_error: 4.330960e-04, rel_error: 8.661920e-04, n=3
delta_x: 1.000000e-04, df_approx: 4.9995669790e-01, df_exact: 5.0000000000e-01, abs_error: 4.330210e-05, rel_error: 8.660421e-05, n=4
delta_x: 1.000000e-05, df_approx: 4.9999566987e-01, df_exact: 5.0000000000e-01, abs_error: 4.330133e-06, rel_error: 8.660266e-06, n=5
delta_x: 1.000000e-06, df_approx: 4.9999956686e-01, df_exact: 5.0000000000e-01, abs_error: 4.331391e-07, rel_error: 8.662783e-07, n=6
delta_x: 1.000000e-07, df_approx: 4.9999995699e-01, df_exact: 5.0000000000e-01, abs_error: 4.300676e-08, rel_error: 8.601353e-08, n=7
delta_x: 1.000000e-08, df_approx: 4.9999999696e-01, df_exact: 5.0000000000e-01, abs_error: 3.038736e-09, rel_error: 6.077471e-09, n=8
delta_x: 1.000000e-09, df_approx: 5.0000004137e-01, df_exact: 5.0000000000e-01, abs_error: 4.137019e-08, rel_error: 8.274037e-08, n=9
delta_x: 1.000000e-10, df_approx: 5.0000004137e-01, df_exact: 5.0000000000e-01, abs_error: 4.137019e-08, rel_error: 8.274037e-08, n=10
delta_x: 1.000000e-11, df_approx: 5.0000004137e-01, df_exact: 5.0000000000e-01, abs_error: 4.137019e-08, rel_error: 8.274037e-08, n=11
delta_x: 1.000000e-12, df_approx: 5.0004445029e-01, df_exact: 5.0000000000e-01, abs_error: 4.445029e-05, rel_error: 8.890058e-05, n=12
delta_x: 1.000000e-13, df_approx: 4.9960036108e-01, df_exact: 5.0000000000e-01, abs_error: 3.996389e-04, rel_error: 7.992778e-04, n=13
delta_x: 1.000000e-14, df_approx: 4.8849813084e-01, df_exact: 5.0000000000e-01, abs_error: 1.150187e-02, rel_error: 2.300374e-02, n=14
delta_x: 1.000000e-15, df_approx: 5.5511151231e-01, df_exact: 5.0000000000e-01, abs_error: 5.511151e-02, rel_error: 1.102230e-01, n=15
delta_x: 1.000000e-16, df_approx: 0.0000000000e+00, df_exact: 5.0000000000e-01, abs_error: 5.000000e-01, rel_error: 1.000000e+00, n=16
delta_x: 1.000000e-17, df_approx: 0.0000000000e+00, df_exact: 5.0000000000e-01, abs_error: 5.000000e-01, rel_error: 1.000000e+00, n=17
delta_x: 1.000000e-18, df_approx: 0.0000000000e+00, df_exact: 5.0000000000e-01, abs_error: 5.000000e-01, rel_error: 1.000000e+00, n=18
delta_x: 1.000000e-19, df_approx: 0.0000000000e+00, df_exact: 5.0000000000e-01, abs_error: 5.000000e-01, rel_error: 1.000000e+00, n=19
"""
