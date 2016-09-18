# This code was written by Maya Schlesinger(maya.schlesinger@gmail.com)
# on 7/7/2016.
# This is a library for basic dealings with vectors space (R^n)
import itertools
import random
import math


def get_random_vector(coords_lims):
    """
    Returns a random vector  within given limits.
    :param coords_lims: Array of pairs [min <Int>, max <Int>] - Limits of x_i-s values.
    :return: Tuple - A random vector.
    """
    return (random.randrange(*coord_lims) for coord_lims in coords_lims)


def get_n_random_vectors(coords_lims, n):
    """
    Returns n random vectors within given limits.
    :param coords_lims: Array of pairs [min <Int>, max <Int>] - Limits of x_i-s values.
    :param n: Int - The number of vectors to generate.
    :return: List of Tuples - n random vectors.
    """
    return [get_random_vector(coords_lims) for _ in xrange(n)]


def get_mass_center(vectors):
    """
    Returns the mass center of the given vector list.
    :param vectors: List of Tuples - The vectors of which to calculate the mass center.
    :return: Tuple - The mass center of the vectors.
    """
    n = len(vectors)
    return [sum(vec[i] for vec in vectors)/n for i in xrange(len(vectors[0]))]


def calc_dist(vec1, vec2):
    """
    This method returns the distance between 2 vectors.
    :param vec1: Tuple - The first vector.
    :param vec2: Tuple - The second vector.
    :return: Double - The distance between the two vectors.
    """
    return math.sqrt(sum(pow(e1-e2, 2) for e1, e2 in itertools.izip(vec1, vec2)))


def calc_n_dists(vec, vec_list):
    """
    This method returns the distance between a vector and n vectors.
    :param vec: Tuple - The vector.
    :param vec_list: List of Tuples- The n vectors to caculate the distance from.
    :return: List of Doubles - At the index i is the distance between the vector and the vector at vec_list[i].
    """
    return [calc_dist(vec, other) for other in vec_list]


def get_closest_vec(vec, vec_list):
    """
    This method returns which of n vectors is closest to a specified vector.
    :param vec: Tuple - The vector the return vector is closest to.
    :param vec_list: List of Tuples - The n vectors from which to find the one closest to vec.
    :return: Int - The index of the closest vector to vec.
    """
    dists_list = calc_n_dists(vec, vec_list)
    return dists_list.index(min(dists_list))


def get_max_value(coord_index, vectors):
    return max([i[coord_index] for i in vectors])


def get_min_value(coord_index, vectors):
    return min([i[coord_index] for i in vectors])


def get_limits(vectors):
    return [(get_max_value(i, vectors), get_min_value(i, vectors)) for i in xrange(len(vectors[0]))]


def get_random_mass_centers(vectors, k):
    return get_n_random_vectors(get_limits(vectors), k)
