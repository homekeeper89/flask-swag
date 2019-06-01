import traceback
import sys
def hoge():
    list[0]

def fuh():
    try:
        hoge()
        fuh2()
    except IndexError:
        print("---error")
        traceback.print_exc(limit=None)

def fuh2():
    try:
        print("im2")
        hoge()
    except Exception  as ex:
        # print('>>> '.join(traceback.format_exception(etype=type(ex), value=ex, tb=ex.__traceback__)))
        # print(exception_to_string(ex))
        T, V, TB = sys.exc_info()
        print (''.join(traceback.format_exception(T,V,TB)))

def exception_to_string(excp):
    stack = traceback.extract_stack()[:-3] + traceback.extract_tb(excp.__traceback__)  # add limit=?? 
    pretty = traceback.format_list(stack)
    return ''.join(pretty) + '\n  {} {}'.format(excp.__class__,excp)

if __name__=='__main__':
    # fuh()
    fuh2()