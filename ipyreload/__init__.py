import time,os,functools
from concurrent.futures import ThreadPoolExecutor
from IPython import get_ipython
ipython = get_ipython()


global future,filename,finish,executor


def CheckUpdate(x):
    global filename 
    filename=x
    modtime = os.path.getmtime(filename)
    x=0
    while True:
        time.sleep(1)
        if os.path.getmtime(filename) != modtime: return os.path.getmtime(filename)




def callback(x,call):
    global filename,finish
    if not finish:
        print '\033[34m Reloading \033[00m' + filename
        try:
            if callable(call):
                call()
                watch(filename,call)
            else:
                ipython.magic("run " + filename)
                watch(filename)
        except:None
        
    
    
def watch (filename,call=False):
    global future,finish,executor
    executor = ThreadPoolExecutor(max_workers=1)
    finish = False
    future = executor.submit(CheckUpdate,filename)
    if callable(call):
        future.add_done_callback(functools.partial(callback,call)) 
    else:
        future.add_done_callback(functools.partial(callback,False))
    


def kill():
    global finish,executor
    finish = True
    #add a newline to trigger last update before kill
    with open(filename, "a") as myfile:
        myfile.write("\n")
    
    executor.shutdown(False)  # non-blocking
    print '\033[34m Shutdown invoked \033[00m' + filename
