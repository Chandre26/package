def sum_array(array):

    '''Return sum of all items in array'''
    if len(array) == 0:
        return 0
    else:
        return array[0] + sum_array(array[1:])

def fibonacci(n):

    '''Return nth term in fibonacci sequence'''
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def factorial(n):

    '''Return n!'''
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n-1)

def reverse(word):

    '''Return word in reverse'''

    if len(word) == 0:
        return word
    else:
        return word[-1] + reverse(word[:-1])
