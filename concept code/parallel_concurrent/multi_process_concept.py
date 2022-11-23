from concurrent.futures import process
import multiprocessing
import time 
import concurrent.futures

def my_fun(sec):
    print(f'Sleeping for {sec} seconds')
    time.sleep(sec)
    print('Awaken !')
    return sec

def mp_1():
    processes = []
    for _ in range(5):
        p = multiprocessing.Process(target=my_fun, args=[1.5])
        p.start()
        processes.append(p)

    for p in processes:
        p.join()

def mp_2():
    with concurrent.futures.ProcessPoolExecutor() as executor:
        res = [executor.submit(my_fun, 1) for _ in range(5)]
        for f in concurrent.futures.as_completed(res):
            print(f.result())  # awaited future

def mp_3():
    with concurrent.futures.ProcessPoolExecutor() as executor:
        # map() will return based on when task was started
        res = executor.map(my_fun, [5,3,4,1,2]) 
        # for f in concurrent.futures.as_completed(res):
        #     print(f.result())  #

        # though we are not accessing the result, it will still join all the tasks in map() method

    print('done mp_3')

if __name__ == '__main__': 
    #mp_1()   # Need to compulsory use this in main other wise it will give below like err
    '''
    An attempt has been made to start a new process before the
    current process has finished its bootstrapping phase.

    This probably means that you are not using fork to start your
    child processes and you have forgotten to use the proper idiom
    in the main module:
    '''

    mp_2()

