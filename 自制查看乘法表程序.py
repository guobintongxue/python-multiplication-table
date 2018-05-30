print ("请选择你想要查看的乘法表，输入1-9")
print ("输入：",end=' ')
someoneinput = input ()
while someoneinput <= '9' :
        for i in range (1,10):
                print (someoneinput,"*",i,"=",int(someoneinput) * i)
                
        print ("输入:",end=' ')
        someoneinput = input ()
        if someoneinput >= '10' : break
print ('数字大于9，无法查询')
