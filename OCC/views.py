from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
# Create your views here.


def calculate(request):
    if request.method == "POST":
        # sgpa
        s1 = request.POST.get('s1')
        s2 = request.POST.get('s2')
        s3 = request.POST.get('s3')
        s4 = request.POST.get('s4')
        s5 = request.POST.get('s5')
        s6 = request.POST.get('s6')
        s7 = request.POST.get('s7')
        s8 = request.POST.get('s8')
        s9 = request.POST.get('s9')
        s10 = request.POST.get('s10')
        s11 = request.POST.get('s11')
        s12 = request.POST.get('s12')

        s1 = float(s1)
        s2 = float(s2)
        s3 = float(s3)
        s4 = float(s4)
        s5 = float(s5)
        s6 = float(s6)
        s7 = float(s7)
        s8 = float(s8)
        s9 = float(s9)
        s10 = float(s10)
        s11 = float(s11)
        s12 = float(s12)

        # credits
        c1 = request.POST.get('c1')
        c2 = request.POST.get('c2')
        c3 = request.POST.get('c3')
        c4 = request.POST.get('c4')
        c5 = request.POST.get('c5')
        c6 = request.POST.get('c6')
        c7 = request.POST.get('c7')
        c8 = request.POST.get('c8')
        c9 = request.POST.get('c9')
        c10 = request.POST.get('c10')
        c11 = request.POST.get('c11')
        c12 = request.POST.get('c12')

        c1 = float(c1)
        c2 = float(c2)
        c3 = float(c3)
        c4 = float(c4)
        c5 = float(c5)
        c6 = float(c6)
        c7 = float(c7)
        c8 = float(c8)
        c9 = float(c9)
        c10 = float(c10)
        c11 = float(c11)
        c12 = float(c12)

        totalCredit = c1+c2+c3+c4+c5+c6+c7+c8+c9+c10+c11+c12
        totalSGPA = ((s1*c1)+(s2*c2)+(s3*c3)+(s4*c4)+(s5*c5)+(s6*c6) +
                     (s7*c7)+(s8*c8)+(s9*c9)+(s10*c10)+(s11*c11)+(s12*c12))

        cgpa = totalSGPA/totalCredit
        if cgpa <= 4:
            print(cgpa)
            return render(request, 'calculate.html', {'cgpa': cgpa})
        else:
            return redirect('/')
            return messages(request, "Please enter correct sgpa again")

        return redirect('/')

    return render(request, 'calculate.html')
