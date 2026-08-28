# Repository Security Guidelines

1. **Input Validation:** All financial transactions must strictly reject negative or zero values.
2. **Boundary Testing:** Unit tests must explicitly cover boundary inputs (e.g., negative transfers, zero values, integer overflow).
3. **Automated Verification:** Any patch must pass `pytest` before being merged into production.