from multiprocessing import Manager,Queue,Pool

#1.进程之间的通讯
q=Queue(3)    #初始化一个Queue队列，最多存储三个put消息
q.put("haha1") #放入任意数据类型消息（具有堵塞属性，如果添加第四个会堵塞）
q.qsize()     #获取队列里面的消息个数
q.get()       #塞先进先出，获取第一个消息内容（具有堵塞属性，如果里面没有消息，调用get会堵）
q.empty()    #判断是否空消息
q.full()     #判断队列的消息是否已满
q.get_nowait()  #不会堵塞，但是会抛出异常，所以要放在异常捕获try里面
q.put_nowait("haha2")  #不会堵塞，但是会抛出异常，所以要放在异常捕获try里面
