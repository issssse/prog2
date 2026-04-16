""" MA3.py

Student: Isac Carlsson
Mail: isac.carlsson.5508@student.uu.se
Reviewed by: Ivar Hammarberg
Date reviewed: 16 Apr

"""
from random import uniform, random
import numpy as np
import matplotlib.pyplot as plt
import math as m
import concurrent.futures as future
from statistics import mean
from time import perf_counter as pc
from functools import reduce
from os import cpu_count


def approximate_pi(n): # Ex1
    #n is the number of points
    points = np.random.uniform(-1, 1, (n, 2))
    inside_mask = np.pow(points[:,0], 2) + np.pow(points[:,1], 2) <= 1
    approximation = np.count_nonzero(inside_mask) * 4 / n

    print(n)
    print(approximation)

    colors = np.where(inside_mask, "red", "blue")
    fig, ax = plt.subplots()
    ax.scatter(points[:,0], points[:,1], s=1, c=colors)
    ax.set_title(f"Monte Carlo approximation of pi with n = {n}")
    ax.set_xlabel(f"Approximation of pi = {approximation}")

    plt.savefig(f"monte-carlo-{n}-points.png")
    plt.close(fig)

    return approximation


def sphere_volume(n, d): #Ex2, approximation
    #n is the number of points
    # d is the number of dimensions of the sphere
    points = ((uniform(-1, 1) for _ in range(d)) for _ in range(n))
    squared_norm = lambda p: reduce(lambda acc, x: acc + x*x, p, 0)
    number_inside = sum(1 for value in map(squared_norm, points) if value <= 1)

    return number_inside * 2**d / n


def sphere_volume_oneliner(n,d):
    return sum(sum(uniform(-1,1)**2 for _ in[0]*d)<=1 for _ in[0]*n)*2**d/n


def hypersphere_exact(n,d): #Ex2, real value
    # n is the number of points
    # d is the number of dimensions of the sphere
    return (np.pow(np.pi, d/2)) / (m.gamma(d/2 + 1))


#Ex3: parallel code - parallelize for loop
def sphere_volume_parallel1(n,d,np=cpu_count()):
    #n is the number of points
    # d is the number of dimensions of the sphere
    #np is the number of processes
    with future.ProcessPoolExecutor(max_workers=np) as ex:
        results = list(ex.map(sphere_volume, [n]*np, [d]*np))

    return mean(results)


#Ex4: parallel code - parallelize actual computations by splitting data
def sphere_volume_parallel2(n,d,np=cpu_count()):
    #n is the number of points
    # d is the number of dimensions of the sphere
    #np is the number of processes
    base, remainder = divmod(n, np)
    chunks = [base + (i < remainder) for i in range(np)]
    chunks = [chunk for chunk in chunks if chunk > 0]

    with future.ProcessPoolExecutor(max_workers=np) as ex:
        results = list(ex.map(sphere_volume, chunks, [d]*len(chunks)))

    return sum(result * chunk for result, chunk in zip(results, chunks)) / n


def main():
    #Ex1
    dots = [1000, 10000, 100000]
    for n in dots:
        approximate_pi(n)

    #Ex2
    n = 100000
    d = 2
    print(sphere_volume(n,d))
    print(f"Actual volume of {d} dimensional sphere = {hypersphere_exact(n,d)}")

    n = 100000
    d = 11
    print(sphere_volume(n,d))
    print(f"Actual volume of {d} dimensional sphere = {hypersphere_exact(n,d)}")

    #Ex3
    n = 100000
    d = 11
    start = pc()
    for _ in range(10):
        sphere_volume(n,d)
    stop = pc()
    print(f"Ex3: Sequential time of {d} and {n}: {stop-start}")
    

    start = pc()
    for _ in range(10):
        sphere_volume_parallel1(n,d)
    stop = pc()
    print(f"Ex3: Parallel time of {d} and {n}: {stop-start}")


    #Ex4
    n = 1000000
    d = 11
    start = pc()
    for _ in range(10):
        sphere_volume(n,d)
    stop = pc()
    print(f"Ex4: Sequential time of {d} and {n}: {stop-start}")

    start = pc()
    for _ in range(10):
        sphere_volume_parallel2(n,d)
    stop = pc()
    print(f"Ex4: Parallel time of {d} and {n}: {stop-start}")


if __name__ == '__main__':
    main()