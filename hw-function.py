from hw_decorator import hw_decorator

@hw_decorator("C:/pylogs/logger.txt")
def squaring(lister):
    return [item ** 2 for item in lister]

# squaring = hw_decorator(squaring, "C:/pylogs/logger.txt")
squaring([10,20,30])