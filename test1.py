from queue import *

def test1():
    q = Queue(3)
    res = q.empty()
    if not res:
        print "test1 NOT OK"
        return
    res = q.enqueue(10)
    if not res:
        print "test1 NOT OK"
        return
    res = q.enqueue(11)
    if not res:
        print "test1 NOT OK"
        return
    x = q.dequeue()
    if x != 10:
        print "test1 NOT OK"
        return
    x = q.dequeue()
    if x != 11:
        print "test1 NOT OK"
        return
    res = q.empty()
    if not res:
        print "test1 NOT OK"
        return
    print "test1 OK"

def test2():
    ###Your code here.
    q = Queue(1)
    q.enqueue(5)
    res = q.full()
    if not res :
        print "test2 NOT OK"
        return
    print "test2 OK"

def test3():
    ###Your code here.
    q = Queue(1)
    q.enqueue(5)
    
    res = q.enqueue(6)

    if res :
        print "test3 NOT OK"
        return
    print "test3 OK"            
    
    
    
test1()
test2()
test3()