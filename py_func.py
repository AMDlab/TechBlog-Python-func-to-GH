# r: numpy
# venv: site-packages
import numpy as np

def project_vec(normal, vec):
    if np.linalg.norm(normal) == 0:
        return vec
    return vec - np.dot(normal, vec) / np.linalg.norm(normal)**2 * normal

func = project_vec

