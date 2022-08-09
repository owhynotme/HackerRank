list1=[1,2]
list2=[3,4]

# possible [1,3][1,4][2,3][2,4]
ans=[[x,y] for x in list1 for y in list2]
print(ans)


# https://www.hackerrank.com/challenges/list-comprehensions/problem?isFullScreen=true

# if __name__ == '__main__':
#     x = int(input())
#     y = int(input())
#     z = int(input())
#     n = int(input())
#     res=[[i,j,k] for i in range(0,x+1) for j in range(0,y+1) for k in range(0,z+1) if(i+j+k !=n)]
#     print(res)
