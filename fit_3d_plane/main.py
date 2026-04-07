import numpy as np

def fit_3d_plane(points):
    """
    Fits an optimal plane to a set of points in 3D space, returns the plane normal vector and plane equation parameters.
    
    Parameters:
        points (np.ndarray/list): 3D point set with shape (N, 3), N ≥ 3
    Returns:
        normal (np.ndarray): Plane normal vector [a, b, c] (normalized)
        plane_params (np.ndarray): Plane equation parameters [a, b, c, d] for ax + by + cz + d = 0
    """
    # Convert to numpy array and check dimensions
    points = np.asarray(points, dtype=np.float64)
    if points.ndim != 2 or points.shape[1] != 3:
        raise ValueError("Points must be a 2D array of shape N×3")
    if points.shape[0] < 3:
        raise ValueError("At least 3 non-collinear points are required to fit a plane")
    
    # 1. Compute centroid of the point set
    centroid = np.mean(points, axis=0)
    
    # 2. Center the points (subtract centroid from all points)
    centered_points = points - centroid
    
    # 3. SVD decomposition to compute normal vector (least-squares optimal solution)
    _, _, vh = np.linalg.svd(centered_points)
    normal = vh[2, :]  # Right singular vector corresponding to the smallest singular value is the normal vector
    
    # 4. Normalize the normal vector
    normal = normal / np.linalg.norm(normal)
    
    # 5. Compute plane parameter d: ax+by+cz+d=0 → d = -(a*cx + b*cy + c*cz)
    d = -np.dot(normal, centroid)
    plane_params = np.hstack([normal, d])
    
    return normal, plane_params

# ------------------- Example Usage -------------------
if __name__ == "__main__":
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
    print("="*50)
    print(f"Fitted plane normal vector: {normal_vector}")
    print(f"Plane equation: {plane_eq[0]:.6f}x + {plane_eq[1]:.6f}y + {plane_eq[2]:.6f}z + {plane_eq[3]:.6f} = 0")
    print("="*50)