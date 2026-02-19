"""Tests for similarity functions."""

import math
from ground_truth.similarity import cosine_similarity, dot_product, l2_norm, normalize


def test_dot_product():
    assert dot_product([1.0, 2.0, 3.0], [4.0, 5.0, 6.0]) == 32.0


def test_l2_norm():
    assert abs(l2_norm([3.0, 4.0]) - 5.0) < 1e-10


def test_cosine_similarity_identical():
    v = [1.0, 2.0, 3.0]
    assert abs(cosine_similarity(v, v) - 1.0) < 1e-10


def test_cosine_similarity_orthogonal():
    assert abs(cosine_similarity([1.0, 0.0], [0.0, 1.0])) < 1e-10


def test_normalize():
    normalized = normalize([3.0, 4.0])
    assert abs(l2_norm(normalized) - 1.0) < 1e-10


def test_normalize_zero():
    assert normalize([0.0, 0.0]) == [0.0, 0.0]
