list1=[1,2]
list2=[3,4]

# possible [1,3][1,4][2,3][2,4]
ans=[[x,y] for x in list1 for y in list2]
print(ans)