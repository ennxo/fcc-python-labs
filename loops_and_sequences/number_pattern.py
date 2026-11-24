# Build a Number Pattern Generator
# https://www.freecodecamp.org/learn/python-v9/lab-number-pattern-generator/build-a-number-pattern-generator

def number_pattern(n):
    if not isinstance(n, int):
        return 'Argument must be an integer value.'
    elif n < 1:
        return 'Argument must be an integer greater than 0.'
    else:
        numbers = range(1, n + 1)
        results = []
        for number in numbers:
            results.append(str(number))
        return ' '.join(results)
