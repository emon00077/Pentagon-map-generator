import matplotlib.pyplot as plt
import numpy as np
import random

def draw_pentagon(center_x, center_y, radius, color):
    points = []
    for i in range(5):
        angle = 2 * np.pi * i / 5
        x = center_x + radius * np.cos(angle)
        y = center_y + radius * np.sin(angle)
        points.append((x, y))
    polygon = plt.Polygon(points, closed=True, edgecolor='black', facecolor=color)
    plt.gca().add_patch(polygon)

# Map settings
rows, cols = 10, 10
radius = 1
land_ratio = 0.6

plt.figure(figsize=(12, 12))
plt.axis('equal')
plt.axis('off')

for row in range(rows):
    for col in range(cols):
        cx = col * 2.2
        cy = row * 2.2
        color = 'green' if random.random() < land_ratio else 'blue'
        draw_pentagon(cx, cy, radius, color)

plt.title('Procedural Pentagon Map (Land & Water)', fontsize=15)
plt.show()
