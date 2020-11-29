import numpy as np
from tools.psihdf4 import rdhdf_3d
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib as mpl


plt.rcParams['figure.figsize'] = [8.5, 7]  # default fig size.
plt.rcParams['axes.labelsize'] = 12
plt.rcParams['axes.titlesize'] = 12


def cmap():
    # an array of parameters, each of our curves depend on a specific value of parameters.
    parameters = np.linspace(0, 2 * np.pi, len(p))

    # norm is a class which, when called, can normalize data into the [0.0, 1.0] interval.
    norm = mpl.colors.Normalize(vmin=np.min(parameters), vmax=np.max(parameters))

    # create a ScalarMappable and initialize a data structure
    s_m = mpl.cm.ScalarMappable(cmap=mpl.cm.hsv, norm=norm)
    s_m.set_array([])
    return s_m


def apply_reverse_upwind_model(r_initial, omega_rot, dr_vec, dp_vec, alpha, rh, add_v_acc=True, r0=30 / (215.032)):
    """ Apply 1d upwind model to the inviscid burgers equation. r/phi grid."""

    v = np.zeros((len(dr_vec) + 1, len(dp_vec) + 1))  # initialize array vr.
    v[0, :] = r_initial

    for i in range(len(dr_vec)):
        for j in range(len(dp_vec) + 1):

            if j != len(dp_vec):
                if (omega_rot * dr_vec[i]) / (dp_vec[j] * v[i, j]) > 1:
                    print('CFL violated', dr_vec[i] - dp_vec[j] * v[i, j] / omega_rot)
                    raise ValueError('CFL violated')

                frac2 = (omega_rot * dr_vec[i]) / dp_vec[j]
            else:
                frac2 = (omega_rot * dr_vec[i]) / dp_vec[0]

            frac1 = (v[i, j - 1] - v[i, j]) / v[i, j]
            v[i + 1, j] = v[i, j] + frac1 * frac2

    if add_v_acc:
        v_acc = alpha * (v[-1, :] * (1 - np.exp(-r0 / rh)))
        v[-1, :] = -v_acc + v[-1, :]

    return v


def compute_phi_shift_forward(p, r, v, omega=2 * np.pi / 25.38, method=None):
    # initialize phi shift matrix.
    phi_shift_mat = np.zeros((len(r), len(p)))
    phi_shift_store = np.zeros((len(r), len(p)))

    # phi at index 0 is original phi grid
    phi_shift_mat[0, :] = p

    # compute the phi shift for each idx in r.
    for ii in range(len(r) - 1):
        if method == "ballistic":
            phi_shift = -(omega / v[:, 0]) * (r[ii + 1] - r[ii])
        else:
            phi_shift = -(omega / v[:, ii]) * (r[ii + 1] - r[ii])
        phi_shift_mat[ii + 1, :] = phi_shift_mat[ii, :] + phi_shift
        phi_shift_store[ii + 1] = phi_shift

    return phi_shift_mat


def compute_phi_shift_backward(p, r, v, omega=2 * np.pi / 25.38, method=None):
    # initialize phi shift matrix.
    phi_shift_mat = np.zeros((len(r), len(p)))

    # phi at last index is original phi grid
    phi_shift_mat[0, :] = p

    # delta r.
    dr = np.mean(r[1:] - r[:-1])
    # compute the phi shift for each idx in r.
    for ii in range(len(r) - 1):
        # delta r. (r_next-r_prev)
        if method == "ballistic":
            phi_shift = -(omega / v[:, -1]) * dr
        if method == "mhd":
            phi_shift = -(omega / v[:, -ii]) * dr
        if method == "hux":
            phi_shift = -(omega / v[:, ii]) * dr
        phi_shift_mat[ii + 1, :] = phi_shift_mat[ii, :] + phi_shift

    return phi_shift_mat


if __name__ == "__main__":
    # read the 3d hdf file.
    hdf_file_path = "data/vr002.hdf"
    r, t, p, f = rdhdf_3d(hdf_file_path)
    # Velocity profile: PSI convertion units conversion from MAS to cgs.
    # See: https://www.researchgate.net/figure/Converting-from-MAS-code-units-to-cgs-and-MKS_tbl1_228551881
    f = 481.3711 * f  # km/s

    # change units of vr to be solar radii per second, and radial mesh to be from km to solar radii.
    f = f / 695700

    # change units of f to be solar radii per day.
    f = 86400 * f

    # change units of f to be in AU per day.
    f = f / 215.032

    # convert to AU units from RS.
    r = r / 215.032

    # equator slice
    v_at_eq = f[:, 55, :]

    phi_shift_mat_bb = compute_phi_shift_backward(p, r, v_at_eq, method="mhd")
    phi_shift_mat_f = compute_phi_shift_forward(p, r, v_at_eq, method="mhd")
    plt.matshow(phi_shift_mat_f)
    plt.colorbar()
    plt.title("Forward")
    plt.matshow(phi_shift_mat_bb)
    plt.colorbar()
    plt.title("Backwards")
    plt.matshow(phi_shift_mat_f - phi_shift_mat_bb)
    plt.title("Forward - Backwards")
    plt.colorbar()
    plt.plot(p, v_at_eq[:, -1], label="velocity at 1 au")
    plt.plot(p, v_at_eq[:, 0], label="velocity at 30RS")
    plt.legend()
    plt.show()



    s_m = cmap()

    fig, ax = plt.subplots()

    for ii in range(len(p)):
        _ = ax.plot(np.cos(phi_shift_mat_bb[:, ii])*np.flip(r), np.sin(phi_shift_mat_bb[:, ii])*np.flip(r), color=s_m.to_rgba(p[ii]))

    _ = ax.set_title("Ballistic-b model")
    _ = ax.set_xlabel("Carrington X / AU ")
    _ = ax.set_ylabel("Carrington Y / AU ")
    _ = plt.axis("equal")

    plt.savefig('figures/ballistic_b.png')