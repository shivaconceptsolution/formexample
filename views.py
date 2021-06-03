from django.shortcuts import render

def index(request):
	return render(request,"formexample/index.html")
def addlogic(request):
	a = request.GET["txtnum1"]
	b = request.GET["txtnum2"]
	c = int(a)+int(b)
	return render(request,"formexample/index.html",{'r':c})

def fact(request):
    if request.method=="POST":
        num = int(request.POST["txtnum1"])
        s=""
        f=1
        for i in range(num,0,-1):
           f=f*i
           s = "result is "+str(f)
        return render(request,"formexample/fact.html",{'res':s})
    return render(request,"formexample/fact.html")

    

def fibo(request):
    if request.method=="POST":
        num = int(request.POST["txtnum"])
        a=-1
        b=1
       # s = " "
        s =[]
        for i in range(1,num):
            c=a+b
           # s = s+str(c)
            s.append(c)
            a=b
            b=c
        return render(request,"formexample/fibo.html",{"res":s})    

    return render(request,"formexample/fibo.html")    


def marksheet(request):
    if request.method=="POST":
        mark = {"PHYSICS":int(request.POST["txtnum1"]),"CHEMISTRY":int(request.POST["txtnum2"]),"MATHS":int(request.POST["txtnum3"]),"English":int(request.POST["txtnum4"]),"Hindi":int(request.POST["txtnum5"])}
        flag = True
        total=0
        sub = ''
        dist = ''
        result = ''
        c=0
        for m in mark:
            if mark.get(m)<0 or mark.get(m)>100:
                result = "ALL Subject marks should be 0 to 100"
                break
            elif mark.get(m)<33:
                c=c+1
                sub = sub + m
            elif mark.get(m)>75:     
                dist = dist + m
            total=total+mark.get(m) 
        else:
            if c==0:
              per = total/5  
              if per>33 and per<45:
                 result = "PASS WITH THIRD DIVISION "
              elif per<60:
                 result = "PASS WITH SECOND DIVISION"
              else:
                  result = "PASS WITH FIRST DIVISION"
            elif c==1:
                  result = "SUPPL "
            else:
                  result = "FAIL"
        return render(request,"formexample/marksheet.html",{"key":result,"m1":request.POST["txtnum1"],"m2":request.POST["txtnum2"],"m3":request.POST["txtnum3"],"m4":request.POST["txtnum4"],"m5":request.POST["txtnum5"],"data":mark})
    return render(request,"formexample/marksheet.html")

def feedback(request):
    if request.method=="POST":
      name = request.POST["txtname"]
      gender = request.POST["gender"]
      course = request.POST.getlist("course[]")
      branch = request.POST.getlist("branch[]")
      feed = request.POST["feed"]
      c=""
      for data in course:
        c = c+data
      b=""
      for data in branch:
         b = b + data + " "  
      res = "Name is "+name + "Gender is "+gender + "Courses is "+c + "Branch is "+b + "feedback is "+feed

      return render(request,"formexample/feedback.html",{"key":res})  


    return render(request,"formexample/feedback.html")
