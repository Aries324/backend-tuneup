#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tuneup assignment"""

__author__ = "Tiffany McLean with the help of a lot of Google-fu and Janell's & Karen's awesome handout that covered the profile portion "

import cProfile
import pstats
import functools
import timeit


def profile(func):
    """A function that can be used as a decorator to measure performance"""
    @functools.wraps(func)
    def profile_wrapper(*args, **kwargs):
        performance_object = cProfile.Profile()
        performance_object.enable()
        result = func(*args, **kwargs)
        performance_object.disable

        get_stats_obj = pstats.Stats(performance_object)
        get_stats_obj.strip_dirs()
        get_stats_obj.sort_stats('cumulative')
        get_stats_obj.print_stats()

        return result

    return profile_wrapper

    # You need to understand how decorators are constructed and used.
    # Be sure to review the lesson material on decorators, they are used
    # extensively in Django and Flask.


def read_movies(src):
    """Returns a list of movie titles"""
    print('Reading file: {}'.format(src))
    with open(src, 'r') as f:
        return f.read().splitlines()


@profile
def find_duplicate_movies(src):
    """Returns a list of duplicate movies from a src list"""

    # create an object to hold the movies
    movie_obj = {}
    movies = read_movies(src)

    for movie in movies:
        if movie_obj.get(movie):
            # if it's already there we need to increment it
            movie_obj[movie] += 1
        else:
            # if the movie is already there we need to add it
            movie_obj[movie] = 1

    return [k for k, v in movie_obj.items() if v > 1]


def timeit_helper():
    """
    Part A:  Obtain some profiling measurements using timeit

    Measure the total amt of CPU time required to run the main function

    so main would be stmt and it needs to be imported as part of the set up

    """

    t = timeit.Timer(stmt="main()", setup="from __main__ import main")
    results = min(t.repeat(repeat=7, number=5)) / 5
    print("Best time across 7 repeats of 5 runs per repeat " + str(results) + " sec")


def main():
    """Computes a list of duplicate movie entries"""
    result = find_duplicate_movies('movies.txt')
    print('Found {} duplicate movies:'.format(len(result)))
    print('\n'.join(result))


if __name__ == '__main__':
    main()
