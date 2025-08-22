import open3d as o3d

# 🔹 Replace this with the path to your .off file
file_path = r"C:\Users\jkarafotis\Desktop\MyDev\Projects\DeepLearning\data\ModelNet40\airplane\train\airplane_0003.off"

# Load the mesh
mesh = o3d.io.read_triangle_mesh(file_path)

if not mesh.has_triangles():
    raise ValueError("The file does not contain a valid mesh!")

print(mesh)
print("Number of vertices:", len(mesh.vertices))
print("Number of triangles:", len(mesh.triangles))

# Compute normals (optional but useful if you want shading or later processing)
mesh.compute_vertex_normals()

# Convert mesh to point cloud by sampling points on the surface
pcd = mesh.sample_points_uniformly(number_of_points=2048)

print(pcd)
print("Number of points in point cloud:", len(pcd.points))

# Visualize point cloud
o3d.visualization.draw_geometries([pcd],
                                  window_name="OFF Point Cloud Viewer",
                                  point_show_normal=False,
                                  width=800,
                                  height=600,
                                  left=50,
                                  top=50)
