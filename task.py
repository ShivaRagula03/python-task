# *        *
# *  *     *
# *    *   *
# *     *  *
# *        *
rows = 5
for i in range(1,rows+1):
    res=""
    for j in range(1,rows+1):
        if j==1 or j==rows or i==j:
         res+="*"+" "
        else:
            res+=" "+" "
    print(res)
print("\n")


# * * * * *
#       *
#     *
#   *
# * * * * *


rows2=5
for k in range(1,rows2+1):
    res1=""
    for l in range(1,rows2 +1):
     if k == 1 or k == rows2  or k+l == rows2+1:
        res1+="*"+" "
     else:
         res1+=" "+" "
    print(res1)
print("\n")
    
    

# *        *
# *        *
# * * * * *       
# *        *
# *        *


rows3 = 5
mid = rows3 // 2 + 1
for r  in range(1,rows3 + 1):
     result=""
     for c in range(1,rows3 + 1):
         if c == 1 or c == rows3  or r == mid :
             result += "*"+" "
         else:
             result +=" "+" "
     print(result)
     
print("\n")
    
    
    
    
    
    
# * * * * *
#     *
#     *
#     *
#     *
# * * * * *



rows4 = 5
mid = rows4 // 2 + 1
for a in range(1,rows4+1):
    res1=""
    for b in range(1,rows4+1):
        if a == 1 or a == rows or b == mid:
            res1+="*"+" "
        else:
            res1+=" "+" "
    print(res1)
        
         
      