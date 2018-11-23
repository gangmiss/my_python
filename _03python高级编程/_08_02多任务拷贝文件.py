from multiprocessing import Process,Pool,Queue,Manager
import os,time

__splet_code="gangmiss||gangmiss"

#读文件
def readFile(queue,file_name,path):
    f = open(path, "r")
    while True:
        res = f.read(4096)
        if res!="":
            while True:
                if queue.full():
                    time.sleep(0.01)
                    continue
                else:
                    queue.put(file_name+__splet_code+res)
                    break
        else:
            print("%s文件读取完成"%path)
            queue.put(file_name + "\\" + path + __splet_code + "finish")
            f.close()
            break
 #2.写文件
def async_write_file(queue,path):
    while True:
        if queue.full:
            time.sleep(0.01)
            continue
        else:
            ret=queue.get()
            rets=ret.rsplit(__splet_code)
            f = open(path+"\\"+rets[0], "a+")
            if rets[1]=="finish":
                f.close()
                break
            else:
                f.write(rets[1])

#1.读文件目录
def async_read_file(queue,path):
    file_lists=os.listdir(path)
    file_name=path.rsplit("\\")[1]
    for file in file_lists:
        if os.path.isfile(file):
            readFile(queue, file_name, file)
        else:
            file_lists2 = os.listdir(file)
            async_read_file(queue, file_lists2)

def main():
    pool=Pool(5)
    queue=Manager().Queue()
    pool.apply_async(async_read_file,(queue,"E:\英雄时刻\\2287817946"))
    pool.apply_async(async_write_file,(queue,"D:\\"))
    pool.close()
    pool.join()
    print("复制目录完成")

if __name__ == '__main__':
    main()