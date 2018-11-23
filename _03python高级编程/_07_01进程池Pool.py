from multiprocessing import Pool
import os,time,random

def main():
    def worker(arg):
        for i in range(5):
            s_time = time.time()
            print("开始执行%s,进程号%d" % (arg, os.getpid()))
            time.sleep(1)
            e_time = time.time()
            print("执行完毕，耗时%0.2f" % (e_time - s_time))

    pool=Pool(3)
    for i in range(10):
        #pool.apply(worker, ("hahahha",))  # 堵塞方式：cpu要等第一个进程执行完毕后再切换到第二个进程开始执行（只有一个参数时加个逗号，因为元组类型里面必须有逗号）
        pool.apply_async(worker,("hahahha",))  #并发方式：cpu按时间片轮流切换进程


    pool.close()   #关闭再添加其他的进程
    pool.join()    #等待所有的子进程完成后再执行

if __name__ == '__main__':
    main()
