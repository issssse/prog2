""" MA3.py

<<<<<<< HEAD
Student:
Mail:
=======
Student: Isac Carlsson
Mail: isac.carlsson.5508@student.uu.se
>>>>>>> 28411ed (MA3 solutions)
Reviewed by:
Date reviewed:

"""
<<<<<<< HEAD
import random
=======
from random import uniform, random
import numpy as np
>>>>>>> 28411ed (MA3 solutions)
import matplotlib.pyplot as plt
import math as m
import concurrent.futures as future
from statistics import mean 
from time import perf_counter as pc
<<<<<<< HEAD

def approximate_pi(n): # Ex1
    #n is the number of points
    # Write your code here
    return
=======
from scipy.special import gamma

def approximate_pi(n): # Ex1
    #n is the number of points
    points = np.random.uniform(-1, 1, (n, 2))
    inside_mask = np.pow(points[:,0], 2) + np.pow(points[:,1], 2) <= 1
    inside_points = points[inside_mask, :]

    colors = np.where(inside_mask, "red", "blue")
    fig, ax = plt.subplots()
    sc = ax.scatter(points[:,0], points[:,1], s=1, c=colors)
    ax.set_xlabel(f"With {n} points the approximation of pi is {inside_points.shape[0] * 4 / n}.")

    plt.savefig(f"monte-carlo-{n}-points.png")

    return inside_points.shape[0] * 4
>>>>>>> 28411ed (MA3 solutions)

def sphere_volume(n, d): #Ex2, approximation
    #n is the number of points
    # d is the number of dimensions of the sphere 
<<<<<<< HEAD

    return 

def hypersphere_exact(n,d): #Ex2, real value
     #n is the number of points
    # d is the number of dimensions of the sphere 
    return

#Ex3: parallel code - parallelize for loop
def sphere_volume_parallel1(n,d,np=10):
      #n is the number of points
    # d is the number of dimensions of the sphere
    #np is the number of processes

=======
    points = np.random.uniform(-1, 1, (n, d))
    inside_mask = np.sum(np.pow(points, 2), axis=1) <= 1
    inside_points = points[inside_mask, :]
    
    return inside_points.shape[0] * 2**d / n

def sphere_volume_naive(n, d):
    get_point = lambda _: (uniform(-1, 1) for _ in range(d))
    pow2 = lambda x: x**2
    is_inside = lambda p: sum(map(pow2, p)) <= 1
    number_inside = sum(map(is_inside, map(get_point, range(n))))

    return number_inside * 2**d / n

def sphere_volume_naive_alt(n,d):
    get_point = lambda _: (uniform(-1, 1) for _ in range(d))
    points = (get_point() for _ in range(n))
    is_inside = lambda p: sum(x*x for x in p) <= 1
    number_inside = sum(1 for p in points if is_inside(p))

    return number_inside * 2**d / n

def sphere_volume_oneliner(n,d):
    return sum(sum(random()**2 for _ in[0]*d)<1 for _ in[0]*n)*4/n

def hypersphere_exact(n,d): #Ex2, real value
    # n is the number of points
    # d is the number of dimensions of the sphere 
    return (np.pow(np.pi, d/2))/(gamma(d/2 + 1))

#Ex3: parallel code - parallelize for loop
def sphere_volume_parallel1(n,d,np=10):
    #n is the number of points
    # d is the number of dimensions of the sphere
    #np is the number of processes

    return

>>>>>>> 28411ed (MA3 solutions)
#Ex4: parallel code - parallelize actual computations by splitting data
def sphere_volume_parallel2(n,d,np=10):
    #n is the number of points
    # d is the number of dimensions of the sphere
    #np is the number of processes
<<<<<<< HEAD
     return 
=======
    return 
>>>>>>> 28411ed (MA3 solutions)
    
def main():
    #Ex1
    dots = [1000, 10000, 100000]
    for n in dots:
        approximate_pi(n)
    #Ex2
    n = 100000
    d = 2
<<<<<<< HEAD
    sphere_volume(n,d)
=======
    print(sphere_volume(n,d))
>>>>>>> 28411ed (MA3 solutions)
    print(f"Actual volume of {d} dimentional sphere = {hypersphere_exact(n,d)}")

    n = 100000
    d = 11
<<<<<<< HEAD
    sphere_volume(n,d)
=======
    print(sphere_volume(n,d))
    print(f"Actual volume of {d} dimentional sphere = {hypersphere_exact(n,d)}")
    
    n = 100000
    d = 11
    print(sphere_volume_naive_oneliner(n,d))
>>>>>>> 28411ed (MA3 solutions)
    print(f"Actual volume of {d} dimentional sphere = {hypersphere_exact(n,d)}")

    #Ex3
    n = 100000
    d = 11
    start = pc()
    for y in range (10):
        sphere_volume(n,d)
    stop = pc()
    print(f"Ex3: Sequential time of {d} and {n}: {stop-start}")
    print("What is parallel time?")

    #Ex4
    n = 1000000
    d = 11
    start = pc()
    sphere_volume(n,d)
    stop = pc()
    print(f"Ex4: Sequential time of {d} and {n}: {stop-start}")
    print("What is parallel time?")

    
    

if __name__ == '__main__':
	main()
