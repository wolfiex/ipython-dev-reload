import time,os
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




def callback(x):
    global filename,finish
    if not finish:
        print '\033[34m Reloading \033[00m' + filename
        try:ipython.magic("run " + filename)
        except:None
        watch(filename)
    
    
def watch (filename):
    global future,finish,executor
    executor = ThreadPoolExecutor(max_workers=1)
    finish = False
    future = executor.submit(CheckUpdate,filename)
    future.add_done_callback(callback)
    


def kill():
    global finish,executor
    finish = True
    #add a newline to trigger last update before kill
    with open(filename, "a") as myfile:
        myfile.write("\n")
    
    executor.shutdown(False)  # non-blocking
    print '\033[34m Shutdown invoked \033[00m' + filename
