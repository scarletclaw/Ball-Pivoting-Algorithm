from bpa import BPA

bpa = BPA(path='data/bunny_with_normals.txt', radius=0.001, visualizer=True)
bpa.create_mesh(limit_iterations=10000)

# bpa = BPA(path='data/large_bunny_with_normals.txt', radius=0.005, visualizer=True)
# bpa.visualizer.draw_with_normals(percentage=20, normals_size=2)