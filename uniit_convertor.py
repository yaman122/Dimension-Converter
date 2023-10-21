print("1.length:\n2.time:\n3.mass:\n4.energy:\n5.R:\n6.temperature:\n7.angle(degree,radian,gradian):\n")
a=int(input("Enter the menu no.:"))
if a!=2:
  n=int(input("Enter the value:"))
if  a==1:
    l=int(input("In which unit you want to enter:\n1.km\n2.m\n3.cm\n4.inch\n5.mm\n"))
    if l==1:
         print(n*1000,"m")
         print(n*100000,"cm")
         print(n*39370.07,"inch")
         print(n*1000000,"mm")
    elif l==2:
         print(n/1000,"km")
         print(n*100,"cm")
         print(n*39.37,"inch")
         print(n*1000,"mm")
    elif l==3:
         print(n/100000,"km")
         print(n/100,"m")
         print(n*0.3937,"inch")
         print(n*10,"mm")
    elif l==4:
         print(n/39370,"km")
         print(n/39.37,"m")
         print(n/0.3937,"cm")
         print(n*25.4,"mm")
    elif l==5:
         print(n/1000000,"km")
         print(n/1000,"m")
         print(n*10,"cm")
         print(n/25.4,"inch")
if a==2:
     l=str(input("enter time in format hh:mm:ss"))
     a=[]
     a.append(l.split(":"))
     i=int(input("enter in which unit you want:\n1.hh\n2.mm\n3.ss\n"))
     t=int(a[0][0])
     u=int(a[0][1])
     v=int(a[0][2])
     if i==1:
         print(t+(u/60)+(v/3600),"hr")
     if i==2:
         print((t*60)+u+(v/60),"min")
     if i==3:
         print((t*3600)+v+(u*60),"sec")
     
if  a==3:
     l=int(input("In which unit you want to enter:\n1.kg\n2.gm\n3.pound\n4.mg\n"))
     if l==1:
         print(n*1000,"gm")
         print(n*2.204,"pound")
         print(n*1000000,"mg")
     elif l==2:
         print(n/1000,"kg")
         print(n*0.00220462,"pound")
         print(n*1000,"mg")
     elif l==3:
         print(n/2.204,"kg")
         print(n/0.00220462,"gm")
         print((n*2.204)/1000000,"mg")
     elif l==4:
         print(n/1000000,"kg")
         print(n/1000,"gm")
         print(n*0.00220462,"pound")    

if a==4:
       l=int(input("In which unit you want to enter:\n1.erg\n2.joule\n3.calorie\n"))
       if l==1:
          print(n/10000000,"joule")
          print((n*2.39)/100000000000,"calorie")
       if l==2:
          print(n*10000000,"erg")
          print(n*0.239,"calorie")
       if l==3:
          print((n*100000000000)/2.39,"erg")
          print(n/0.239,"joule")
  
    