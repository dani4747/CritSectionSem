from multiprocessing import Process
from multiprocessing import current_process
from multiprocessing import Value, Array, BoundedSemaphore
N = 8
def task(common, tid, bs):
    a = 0
    for i in range(100):
        print(f'{tid}−{i}: Non−critical Section')
        a += 1
        print(f'{tid}−{i}: End of non−critical Section')
        print(tid,'−',i,': Critical section')
        bs.acquire()
        v = common.value + 1
        print(f'{tid}−{i}: Inside critical section')
        common.value = v
        print(f'{tid}−{i}: End of critical section')
        bs.release()
def main():
    lp = []
    common = Value('i', 0)
    bs = BoundedSemaphore(1)
    for tid in range(N):
        lp.append(Process(target=task, args=(common, tid, bs)))
    print (f"Valor inicial del contador {common.value}")
    for p in lp:
        p.start()
    for p in lp:
        p.join()
    print ('Valor final del contador ',common.value)
    print ("fin")
if __name__ == "__main__":
    main() 