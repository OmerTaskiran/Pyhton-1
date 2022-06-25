def realroot(a,b,c,):
  delta=(b**2-4*a*c)
  if (delta <0):
    print("No find realfoot")
    return
    
  x1=(-b-delta**0.5)/2*a
  x2=(-b-delta**0.5)/2*a
  
  return(x1,x2)
  
  
  
a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))
result=realroot(a,b,c)

print(result)
  
