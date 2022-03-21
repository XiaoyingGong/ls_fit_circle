import numpy as np

import ls_fits_circle
import matplotlib.pyplot as plt

def without_noise():
    r_gt = 4
    x_c_gt = 5
    y_c_gt = 5

    pts_x = np.linspace(1, 9, 1000)
    pts_y_1 = np.sqrt(r_gt**2 - (pts_x - x_c_gt)**2) + y_c_gt
    pts_y_2 = -1 * np.sqrt(r_gt**2 - (pts_x - x_c_gt)**2) + y_c_gt

    pts_1 = np.hstack((pts_x[:, None], pts_y_1[:, None]))
    pts_2 = np.hstack((pts_x[:, None], pts_y_2[:, None]))
    pts = np.vstack((pts_1, pts_2))
    pts = pts[:, [1, 0]]

    R, x_c, y_c = ls_fits_circle.ls_fits_circle(pts, solar_center=None, solar_r=None)


    plt_x = np.linspace(x_c - R, x_c + R, 100000)
    plt_y_1 = np.sqrt(R**2 - (plt_x - x_c)**2) + y_c
    plt_y_2 = -1 * np.sqrt(R**2 - (plt_x - x_c)**2) + y_c



    print("R:{}, x_c:{}, y_c:{}".format(R, x_c, y_c))
    plt.figure()
    plt.axis("equal")
    plt.scatter(pts[:, 1], pts[:, 0], c='b')
    plt.plot(plt_x, plt_y_1, c='r')
    plt.plot(plt_x, plt_y_2, c='r')
    plt.show()


def with_noise():
    r_gt = 4
    x_c_gt = 5
    y_c_gt = 5

    gaussian_noise = np.random.rand(2000, 2)
    gaussian_noise = gaussian_noise - np.mean(gaussian_noise)
    pts_x = np.linspace(1, 9, 1000)

    pts_y_1 = np.sqrt(r_gt**2 - (pts_x - x_c_gt)**2) + y_c_gt
    pts_y_2 = -1 * np.sqrt(r_gt**2 - (pts_x - x_c_gt)**2) + y_c_gt

    pts_1 = np.hstack((pts_x[:, None], pts_y_1[:, None]))
    pts_2 = np.hstack((pts_x[:, None], pts_y_2[:, None]))
    pts = np.vstack((pts_1, pts_2))
    pts = pts[:, [1, 0]]
    pts += gaussian_noise

    R, x_c, y_c = ls_fits_circle.ls_fits_circle(pts, solar_center=None, solar_r=None)


    plt_x = np.linspace(x_c - R, x_c + R, 100000)
    plt_y_1 = np.sqrt(R**2 - (plt_x - x_c)**2) + y_c
    plt_y_2 = -1 * np.sqrt(R**2 - (plt_x - x_c)**2) + y_c



    print("R:{}, x_c:{}, y_c:{}".format(R, x_c, y_c))
    plt.figure()
    plt.axis("equal")
    plt.scatter(pts[:, 1], pts[:, 0], c='b')
    plt.plot(plt_x, plt_y_1, c='r')
    plt.plot(plt_x, plt_y_2, c='r')
    plt.show()


if __name__ == "__main__":
    with_noise()
