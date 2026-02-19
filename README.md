# Mixed Python + Rust Ground Truth

Ground truth corpus for testing PMAT's mixed Python+Rust analysis.

## Structure

- `src/lib.rs` — Rust native implementations (vector math)
- `src/ground_truth/` — Python reference implementations (same algorithms)
- `tests/` — Python pytest suite
- `Cargo.toml` + `pyproject.toml` — Dual build systems

## Purpose

Validates that `pmat comply check` and `pmat context` correctly:
- Detect both `.py` and `.rs` files in the same project
- Run Rust AND Python quality checks simultaneously
- Handle mixed Cargo.toml + pyproject.toml project roots
- Analyze cross-language function correspondence
