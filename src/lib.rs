//! Native Rust implementations for Python bindings
//!
//! This library provides high-performance Rust implementations
//! that are called from Python via PyO3 or subprocess.

/// Compute dot product of two vectors
pub fn dot_product(a: &[f64], b: &[f64]) -> f64 {
    assert_eq!(a.len(), b.len(), "vectors must have equal length");
    a.iter().zip(b.iter()).map(|(x, y)| x * y).sum()
}

/// Compute L2 norm of a vector
pub fn l2_norm(v: &[f64]) -> f64 {
    v.iter().map(|x| x * x).sum::<f64>().sqrt()
}

/// Cosine similarity between two vectors
pub fn cosine_similarity(a: &[f64], b: &[f64]) -> f64 {
    let dot = dot_product(a, b);
    let norm_a = l2_norm(a);
    let norm_b = l2_norm(b);
    if norm_a == 0.0 || norm_b == 0.0 {
        return 0.0;
    }
    dot / (norm_a * norm_b)
}

/// Normalize a vector to unit length
pub fn normalize(v: &[f64]) -> Vec<f64> {
    let norm = l2_norm(v);
    if norm == 0.0 {
        return vec![0.0; v.len()];
    }
    v.iter().map(|x| x / norm).collect()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_dot_product() {
        assert_eq!(dot_product(&[1.0, 2.0, 3.0], &[4.0, 5.0, 6.0]), 32.0);
    }

    #[test]
    fn test_l2_norm() {
        let norm = l2_norm(&[3.0, 4.0]);
        assert!((norm - 5.0).abs() < 1e-10);
    }

    #[test]
    fn test_cosine_similarity_identical() {
        let v = &[1.0, 2.0, 3.0];
        let sim = cosine_similarity(v, v);
        assert!((sim - 1.0).abs() < 1e-10);
    }

    #[test]
    fn test_cosine_similarity_orthogonal() {
        let sim = cosine_similarity(&[1.0, 0.0], &[0.0, 1.0]);
        assert!(sim.abs() < 1e-10);
    }

    #[test]
    fn test_normalize() {
        let normalized = normalize(&[3.0, 4.0]);
        let norm = l2_norm(&normalized);
        assert!((norm - 1.0).abs() < 1e-10);
    }

    #[test]
    fn test_normalize_zero_vector() {
        let normalized = normalize(&[0.0, 0.0]);
        assert_eq!(normalized, vec![0.0, 0.0]);
    }
}
