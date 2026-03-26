# break try finally in loop
#this example basically represent that even continue and breck exist in loop finally code block gets executed
a=0
b=2

while a<4:
    print('-------------------')
    a+=1
    b-=1
    try:
        a/b
    except ZeroDivisionError:
        print('{0},{1} exception'.format(a,b))
        break #if break exist it will still executes finally and end the loop
    finally:
        print('{0},{1} excutes finally'.format(a,b))
    print('{0},{1} inside main loop'.format(a,b))
else:
    print('this will get excuted if brek not get excuted try with b =10')
    #else block gets executed when while block reaches to end without break



