"""Data pipeline utilities.

Demonstrates typical Python data processing patterns
for PMAT complexity analysis ground truth.
"""

from dataclasses import dataclass
from typing import Iterator


@dataclass
class DataPoint:
    """A single data point with features and label."""
    features: list[float]
    label: int


def batch_iterator(data: list[DataPoint], batch_size: int) -> Iterator[list[DataPoint]]:
    """Yield successive batches from data."""
    for i in range(0, len(data), batch_size):
        yield data[i : i + batch_size]


def compute_mean(vectors: list[list[float]]) -> list[float]:
    """Compute element-wise mean of vectors."""
    if not vectors:
        return []
    n = len(vectors)
    dim = len(vectors[0])
    return [sum(v[i] for v in vectors) / n for i in range(dim)]


def standardize(data: list[DataPoint]) -> list[DataPoint]:
    """Standardize features to zero mean and unit variance."""
    if not data:
        return []
    features = [d.features for d in data]
    mean = compute_mean(features)
    dim = len(mean)
    n = len(features)

    # Compute std dev
    variance = [
        sum((features[j][i] - mean[i]) ** 2 for j in range(n)) / max(n - 1, 1)
        for i in range(dim)
    ]
    std = [v ** 0.5 if v > 0 else 1.0 for v in variance]

    return [
        DataPoint(
            features=[(d.features[i] - mean[i]) / std[i] for i in range(dim)],
            label=d.label,
        )
        for d in data
    ]
