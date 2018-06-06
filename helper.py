from scipy.spatial.distance import cdist
from copy import deepcopy


def _remove_from_rows(element, m):
    for key, values in m.items():
        m[key] = list([val for val in values if val != element])
    return m


def _remove_rows_without(value, m):
    m_ = m.copy()
    for key, values in m_.items():
        if value not in values:
            del m[key]
    return m


def _remove_smaller_keys(value, m):
    keys = sorted(m.keys())
    for key in keys:
        if key < value:
            del m[key]
        else:
            break
    return m


def rough_matrix(coords):
    m = cdist(coords, coords, 'euclidean')
    m = 2.6 * m / 0.04260164
    return m


def recursive(m, group, clusters):
    key = group[-1]
    m_ = deepcopy(m)

    values = m_.pop(key)
    m_ = _remove_rows_without(key, m_)
    m_ = _remove_from_rows(key, m_)
    m_ = _remove_smaller_keys(key, m_)

    if not m_:
        return group
    for value in values:
        if value not in m_ or value < key:
            continue
        group_ = group + [value]
        clusters.append(recursive(m_, group_, clusters))
    return []


def start(m):
    groups = []
    for i in range(len(m)):
        group = [i]
        output = recursive(m, group, groups)
        del m[i]
        if output:
            groups.append(output)
    unique_groups = [val for val in groups if not
    any(set(val) < set(i) for i in groups)]
    return unique_groups
