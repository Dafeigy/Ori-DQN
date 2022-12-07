import time

def ActionInfo(func):
    
    def wrapper(*args, **kwargs):
        print('\033[1;37;44m ▶  Testing func: \033[0m {}.'.format(func.__name__))
        t1 = time.time()
        func(*args, **kwargs)
        print("\033[1;37;44m ▶  Execute Time: \033[0m {}.".format('%.4f' % (time.time() - t1)))
 
    return wrapper