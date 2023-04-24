# define functions to convert unit


def kg_lb(weight):
    result = float(weight) * 2.20462
    return result


def lb_kg(weight):
    result = float(weight) * 0.453592
    return result


def m_ft(length):
    result = float(length) * 3.28084
    return result


def ft_m(length):
    result = float(length) * 0.3048
    return result


def sqm_sqft(area):
    result = float(area) * 10.7639
    return result


def sqft_sqm(area):
    result = float(area) * 0.092903
    return result
