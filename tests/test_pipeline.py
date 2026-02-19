"""Tests for data pipeline utilities."""

from ground_truth.data_pipeline import DataPoint, batch_iterator, compute_mean, standardize


def test_batch_iterator():
    data = [DataPoint(features=[float(i)], label=i) for i in range(10)]
    batches = list(batch_iterator(data, 3))
    assert len(batches) == 4  # 3 + 3 + 3 + 1
    assert len(batches[-1]) == 1


def test_compute_mean():
    vectors = [[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]]
    mean = compute_mean(vectors)
    assert abs(mean[0] - 3.0) < 1e-10
    assert abs(mean[1] - 4.0) < 1e-10


def test_standardize():
    data = [
        DataPoint(features=[1.0, 10.0], label=0),
        DataPoint(features=[3.0, 20.0], label=1),
        DataPoint(features=[5.0, 30.0], label=0),
    ]
    result = standardize(data)
    # Mean should be approximately 0
    mean_f0 = sum(d.features[0] for d in result) / len(result)
    assert abs(mean_f0) < 1e-10
