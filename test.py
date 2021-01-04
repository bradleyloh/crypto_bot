import decimal

def reduceDecimalPlaces(quantity):
    # Check no. of decimal places
    decimalPlaces = abs(decimal.Decimal(quantity).as_tuple().exponent)
    if decimalPlaces == 0:
        return int(quantity)
    reducedSizeBy = str(1/(10**(int(decimalPlaces) - 1)))
    new = decimal.Decimal(quantity).quantize(decimal.Decimal(reducedSizeBy),rounding=decimal.ROUND_DOWN)
    print(decimalPlaces)
    print(new)
    return new

quantity = reduceDecimalPlaces("203.5665")
print(quantity)
