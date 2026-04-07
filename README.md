# fit_3d_plane
Given a set of discrete points in 3D space (with at least three non-collinear points), fit a plane using these points.

## Installation

```bash
pip install fit_3d_plane
```

## Usage

```python
from fit_3d_plane import fit_3d_plane

# Test 3D points (these points lie on the z=0 plane)
test_points = [
    [0, 0, 0],
    [1, 0, 0],
    [0, 1, 0],
    [1, 1, 0],
    [2, 3, 0]
]

# Fit plane
normal_vector, plane_eq = fit_3d_plane(test_points)

# Print results
print(f"Fitted plane normal vector: {normal_vector}")
print(f"Plane equation: {plane_eq[0]:.6f}x + {plane_eq[1]:.6f}y + {plane_eq[2]:.6f}z + {plane_eq[3]:.6f} = 0")
```
