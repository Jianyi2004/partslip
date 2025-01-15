import open3d as o3d

# 读取 PLY 文件
mesh = o3d.io.read_triangle_mesh("Chair.ply")

# 可视化
o3d.visualization.draw_geometries([mesh])