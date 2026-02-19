"""Vector similarity functions — Python reference implementations.

These mirror the Rust implementations in src/lib.rs for cross-language
ground truth validation.
"""

import math


def dot_product(a: list[float], b: list[float]) -> float:
    """Compute dot product of two vectors."""
    if len(a) != len(b):
        raise ValueError("vectors must have equal length")
    return sum(x * y for x, y in zip(a, b))


def l2_norm(v: list[float]) -> float:
    """Compute L2 norm of a vector."""
    return math.sqrt(sum(x * x for x in v))


def cosine_similarity(a: list[float], b: list[float]) -> float:
    """Cosine similarity between two vectors."""
    dot = dot_product(a, b)
    norm_a = l2_norm(a)
    norm_b = l2_norm(b)
    if norm_a == 0.0 or norm_b == 0.0:
        return 0.0
    return dot / (norm_a * norm_b)


def normalize(v: list[float]) -> list[float]:
    """Normalize a vector to unit length."""
    norm = l2_norm(v)
    if norm == 0.0:
        return [0.0] * len(v)
    return [x / norm for x in v]
