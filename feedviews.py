from django.shortcuts import render
from django.views import View

class Feedback(View):
    def post(self,request):
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

      return render(request,"formexample/feedback.html",{"key":res,"gen":gender,"course":course})  

    def get(self,request):
     return render(request,"formexample/feedback.html")
