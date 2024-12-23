
#=======================================
#           boolean or T,F
sm=" sundara moorthy "
print("Ture,False".center(20,"="))
print(type(sm)==str)                   # only arqument pasing the varible
print(isinstance(sm,int))              # only arqument pasing the varible
print(sm.startswith("  "))
print(sm.endswith("  "))

t=True
f=bool(False)
print(type(t)==bool)                   # only arqument pasing the varible
print(isinstance(t,bool))  
print(t==f)