
#=======================================
# upper(),lower(),replace(),strip(),len()

s="sundar"
m="moorthy"
print(s+" "+m)
print(s[0].upper()+s[1:])   # s[0].upper() -> 0 index change uppercase
print(s.lower())            #upper(can't using arqument)
print(s.upper())            #upper(can't using arqument)
print(len(s[0:4]))
sm="     " +s+"    "+m+"        "
print(len(sm))              # only arqument pasing the varible
print(sm)
print(sm.title())           #upper(can't using arqument)
print(sm.strip())           #strip() just call the funtion s:e space  clear 
h = "--hello--"
print(h.strip("-"))         # Output: "hello"
print(s.replace(s[0],"S"))  #replace() using specipc possion or  letter or sentance 
print(m.replace("m","M"))

#=======================================
#           center,rjust,ljust
M=" menu "
print((M.upper()).center(20,"="))
print("Coffee".ljust(16,"."),"$1")
print("Tea".ljust(16,"."),"$2")
print("Muffin".ljust(16,"."),"$3")

#=======================================
#           index
print("Index".center(20,"="))
print(s[1])
print(s[1:])
print(s[-1])
print(s[:-1])
print(s[1:-1])





