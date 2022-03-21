# author: 龚潇颖 Gong, Xiaoying
# IDE: PyCharm
# Time：2022/3/21 10:28
# Email: gongxiaoying5991@163.com
# des:

import numpy as np

# 进行最小二乘法圆拟合 solar_center在有些fits中是已知的，solar_r也有可能已知
def ls_fits_circle(pts, solar_center=None, solar_r=None):
    y, x = pts[:, 0], pts[:, 1]
    N = len(x)
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    u = x - x_mean
    v = y - y_mean
    # 圆心未知
    if solar_center is None:
        S_uuu = np.sum(u**3)
        S_vvv = np.sum(v**3)

        S_uu = np.sum(u ** 2)
        S_vv = np.sum(v ** 2)
        S_uv = np.sum(u * v)

        S_uvv = np.sum(u*(v**2))
        S_uuv = np.sum((u**2)*v)


        u_c = (S_uuu*S_vv + S_uvv*S_vv - S_vvv*S_uv - S_uuv*S_uv)/(2*(S_uu * S_vv - (S_uv)**2))
        v_c = (S_uu*S_vvv + S_uuv*S_uu - S_uuu*S_uv - S_uvv*S_uv)/(2*(S_uu * S_vv - (S_uv)**2))

        x_c = u_c + x_mean
        y_c = v_c + y_mean
    else:# 圆心已知
        x_c = solar_center[:, 1]
        y_c = solar_center[:, 0]
        u_c = x_c - x_mean
        v_c = y_c - y_mean

    if solar_r is None:#半径未知
        R = np.sum(np.sqrt((u - u_c)**2 + (v - v_c)**2)) / N
    else:#半径已知
        R = solar_r

    return R, x_c, y_c