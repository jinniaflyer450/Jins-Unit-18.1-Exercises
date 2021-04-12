def convert_temp(unit_in, unit_out, temp):
    """Convert farenheit <-> celsius and return results.

    - unit_in: either "f" or "c" 
    - unit_out: either "f" or "c"
    - temp: temperature (in f or c, depending on unit_in)

    Return results of conversion, if any.

    If unit_in or unit_out are invalid, return "Invalid unit [UNIT_IN]".

    For example:

      convert_temp("c", "f", 0)  =>  32.0
      convert_temp("f", "c", 212) => 100.0
    """
    # https://www.metric-conversions.org/temperature/celsius-to-fahrenheit.htm Got conversion factors from here.

    if (unit_in != "c" and unit_in != "f"):
      return f'Invalid unit {unit_in}.'
    elif (unit_out != "c" and unit_out != "f"):
      return f'Invalid unit {unit_out}'
    elif(unit_in == "c" and unit_out == "c") or (unit_in == "f" and unit_out == "f"):
      return f'{temp} degrees {unit_in}.'
    elif(unit_in == "c" and unit_out == "f"):
      return f'{(temp * 1.8) + 32} degrees {unit_out}.'
    else:
      return f'{(temp -32)/1.8} degrees {unit_out}.'



print(convert_temp("c", "f", 0))
print(convert_temp("f", "c", 212))
print(convert_temp("z", "f", 32))
print(convert_temp("c", "z", 32))
print(convert_temp("f", "f", 75.5))

