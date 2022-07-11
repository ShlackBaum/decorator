from datetime import datetime

def hw_decorator(pather):
    def _hw_decorator(old_function):
        def new_function(*args,**kwargs):
            logger = open(pather, "a")
            logger.write(f"Дата и время вызова функции - {datetime.today()}\n")
            logger.write(f"Имя функции - {old_function.__name__}\n")
            logger.write(f"Используемые аргументы функции:\n")
            print(f"Дата и время вызова функции - {datetime.today()}")
            print(f"Имя функции - {old_function.__name__}")
            print(f"Используемые аргументы функции:")
            if args:
                for arg in args:
                    logger.write(f"{arg}\n")
                    print(arg)
            if kwargs:
                for kwarg in kwargs:
                    logger.write(f"{kwarg}\n")
                    print(kwargs)
            result=old_function(*args, **kwargs)
            print(f"Результат выполнения функции {result}")
            logger.write(f"Результат выполнения функции {result}\n")
            logger.write(f"---Конец записи---\n")
            logger.close()
            return result
        return new_function
    return _hw_decorator