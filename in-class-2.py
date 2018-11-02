KG_IN_1_POUND = 0.54
KM_IN_1_MILE = 1.61
LITER_IN_1_GALLON = 3.79

CONVERSION_MAP = {('Fahrenheit', 'Celsius'): lambda f: 5 / 9 * (f - 32),
                  ('Celsius', 'Fahrenheit'): lambda c: c * 9 / 5 + 32,
                  ('Pound', 'Kilogram'): lambda p: p * KG_IN_1_POUND,
                  ('Kilogram', 'Pound'): lambda k: k / KG_IN_1_POUND,
                  ('Mile', 'Kilometer'): lambda k: k * KM_IN_1_MILE,
                  ('Kilometer', 'Mile'): lambda m: m / KM_IN_1_MILE,
                  ('Gallon', 'Liter'): lambda g: g * LITER_IN_1_GALLON,
                  ('Liter', 'Gallon'): lambda l: l / LITER_IN_1_GALLON}


def convert_units(amount, current_unit, converted_unit):
    return CONVERSION_MAP.get((current_unit, converted_unit))(amount)


if __name__ == '__main__' :
    print(convert_units(1, 'Kilometer', 'Mile'))