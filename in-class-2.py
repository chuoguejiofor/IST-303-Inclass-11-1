KG_IN_1_POUND = 0.54
KM_IN_1_MILE = 1.61
LITER_IN_1_GALLON = 3.79

CONVERSION_MAP = {('fahrenheit', 'celsius'): lambda f: 5 / 9 * (f - 32),
                  ('celsius', 'fahrenheit'): lambda c: c * 9 / 5 + 32,
                  ('pound', 'kilogram'): lambda p: p * KG_IN_1_POUND,
                  ('kilogram', 'pound'): lambda k: k / KG_IN_1_POUND,
                  ('mile', 'kilometer'): lambda k: k * KM_IN_1_MILE,
                  ('kilometer', 'mile'): lambda m: m / KM_IN_1_MILE,
                  ('gallon', 'liter'): lambda g: g * LITER_IN_1_GALLON,
                  ('liter', 'gallon'): lambda l: l / LITER_IN_1_GALLON}


def convert_units(amount, current_unit, converted_unit):
    return CONVERSION_MAP.get((current_unit, converted_unit))(amount)


if __name__ == '__main__' :
    print(convert_units(1, 'kilometer', 'mile'))