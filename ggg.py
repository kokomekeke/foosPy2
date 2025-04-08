x = [2,3,3,4,5,3,4,5,6,7,8,4,5,6,7,6,7,7]
y = [2,2,3,3,3,4,4,4,4,4,4,5,5,5,5,6,6,7]

r = 0
for a in x:
    r = r + (a - 5.11) ** 2

print(r/18)

r=0
for a in y:
    r = r + (a - 4.22) ** 2

print(r / 18)

r=0
for a,b in zip(x, y):
    r = r + (a - 5.11) * (b - 4.22)

print(r / 18)


import numpy as np

# A megadott mátrix
image = np.array([
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
])

# Az objektum koordinátáinak meghatározása
y_coords, x_coords = np.where(image == 1)

# Tömegközéppont kiszámítása
x_c = np.mean(x_coords)
y_c = np.mean(y_coords)

# Kovariancia mátrix számítása
x_diff = x_coords - x_c
y_diff = y_coords - y_c
cov_xx = np.mean(x_diff ** 2)
cov_yy = np.mean(y_diff ** 2)
cov_xy = np.mean(x_diff * y_diff)
cov_matrix = np.array([[cov_xx, cov_xy], [cov_xy, cov_yy]])

# Sajátértékek és sajátvektorok
eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)

# A főtengely irányvektora (a legnagyobb sajátértékhez tartozó sajátvektor)
principal_axis = eigenvectors[:, np.argmax(eigenvalues)]

# Az x-tengellyel bezárt szög kiszámítása
theta = np.arctan2(principal_axis[1], principal_axis[0])  # Radiánban

print(x_c, y_c, theta)


# Második feladat

import numpy as np

# Adott pontok
points = np.array([[-20, 0], [0, -20], [20, 0], [0, 20]])

# Kiszámoljuk a középpontot (tömegközéppont)
centroid = np.mean(points, axis=0)

# Eltérések a középponttól
deviations = points - centroid

# Kovarianciamátrix kiszámítása
cov_matrix = np.cov(deviations.T)

# Sajátértékek kiszámítása
eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)

# Számoljuk meg a pozitív, negatív és nulla sajátértékeket
positive_eigenvalues = np.sum(eigenvalues > 0)
negative_eigenvalues = np.sum(eigenvalues < 0)
zero_eigenvalues = np.sum(np.isclose(eigenvalues, 0))

# Szignatúra meghatározása
signature = (positive_eigenvalues, negative_eigenvalues, zero_eigenvalues)

print("Szignatúra:", signature)

