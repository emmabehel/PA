# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 13:14:17 2024

@author: EOBehel
"""

import numpy as np

function_1 = np.poly1d([2,3,0,1])
print(function_1)
function_1_answer = np.polyval(function_1, 2)
print(function_1_answer)

function_2 = np.poly1d([1,0,1])
function_2_derivative = np.polyder(function_2)
function_2_answer = np.polyval(function_2_derivative, 1)
print(function_2_answer)
#%%
import numpy as np
 
def polynomial_eval(poly,x):
    return np.polyval(poly,x)

def derivative_eval(poly, x):
    der = np.polyder(poly)
    return np.polyval(der,x)

def Newtons_Method(poly, x1, x_n_p = 0, n_val = 1):
    f_xn = polynomial_eval(poly, x1)
    f_xp = derivative_eval(poly, x1)
    if n_val != 1 and abs(x_n_p - x1) < 0.001:
        return x1
    else:
        x_n_p = x1
        x1 = x1 - (f_xn/f_xp)
        n_val += 1 

        print(f'x_{n_val} = {x1}')
        return Newtons_Method(poly, x1, x_n_p, n_val)
    
def roots(poly):
    return np.roots(poly)   
    
 
def main():
    coefficents = input('Enter coefficients for a polynomial (with commas): ')
    coeffs = [float(coeffs) for coeffs in coefficents.split(',')]
    poly = np.poly1d(coeffs)    
    x1 = float(input("Enter a number for x1: "))
    newton = Newtons_Method(poly, x1)
    print(f'The final value with stablized thousandths place is: {newton:.3f}')
    root = roots(poly)
    print(f'With the numpy roots function the answer is: {root}')

main()
