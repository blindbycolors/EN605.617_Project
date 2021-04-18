from random import uniform
import numpy as np
import Utilities
import constants


def cpuIfsTransform(transformation=constants.ifsFractals["fern"], width=600,
                    height=600, num_points=100000, output_file="cpuOut.png"):
    """
    This function will perform the Iterated Function System (IFS) fractal
    algorithm in the traditional, iterative process
    :param transformation: transformation: A transformation matrix with 7 columns
        representing [a, b, c, d, e, f, prob] for the IFS function
        x_(n+1) = ax_n + by_n + e and y_(n+1) = cx_n + dy_n + f
    :param width: Width of the image in pixels
    :param height: Height of the image in pixels
    :param num_points: Number of points in the fractal
    :param output_file: File to save the image to
    :return: none
    """
    probabilityJoin = sum(t[6] for t in transformation)
    points = set([(0, 0)])
    while len(points) <= num_points:
        newPoints = set()
        x = 0
        y = 0

        # for each point
        for point in points:
            # decide which transformation to apply
            rnd = uniform(0, probabilityJoin)
            pSum = 0
            for i in range(len(transformation)):
                pSum += transformation[i][6]
                if rnd <= pSum:
                    # x_(n+1) = ax_n + by_n + e
                    x0 = x * transformation[i][0] + y * transformation[i][1] + \
                         transformation[i][4]
                    # y_(n+1) = cx_n + dy_n + f
                    y = x * transformation[i][2] + y * transformation[i][3] + \
                        transformation[i][5]
                    x = x0
                    newPoints.add((x, y))
                    break

        points.update(newPoints)

    Utilities.drawImage(points, width, height, output_file)


def cpuDivergentFractal(c=constants.juliaFractals["set1"], iterations=200,
                        divergence_value=10, width=300, output_file="cpuOut.png"):
    """
    CPU implementation of divergent quadratic map 'z = z^2 + c' for nIterations
    :param c: Complex value representation
    :param iterations: total number of iterations
    :param divergence_value: divergence value for algorithm
    :param width: Width of the image in pixels. The same value will be used for
        the image height
    :param output_file: Filename to save image as
    :return:
    """

    height = width
    points = np.zeros((width, height),
                      dtype=np.float32)

    for w in range(width):
        for h in range(height):
            cX = 1.5 * (w - width / 2) / (0.5 * width)
            cY = (h - height / 2) / (0.5 * height)
            z = complex(cX, cY)
            count = 0
            for i in range(iterations):
                z = (z * z) + c
                count += 1
                if abs(z) > divergence_value:
                    break
                points[w, h] = count

    Utilities.plotFractal(points, output_file=output_file)
