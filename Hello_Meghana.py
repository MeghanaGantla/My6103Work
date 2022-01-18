#%%
print("Hello Meghana")
print(7 / 11)
print (5+11)
print(9/2, 2/9) # print numerical divisions
print(9//2, 2//9) # print quotients from divisions
print(9%2, 2%9) # print remainders from divisions

#%%
astring = "Good Morning"
numb = 3.1415926535
cnt = 1
# Many different ways to print out the same line
print("%d. I wish you a very %s" % (cnt,astring) )
cnt+=1
print(cnt,". I wish you a very " + astring )
cnt+=1
print(cnt, ". I wish you a very ",astring )
cnt+=1
print("%d. I wish you a very %s, we made apple %.3f for breakfast" % (cnt,astring,numb) )
cnt+=1
print("%d. I wish you a very %s, we have %d apples in the basket" % (cnt,astring,numb) )
cnt+=1
print("%d. I wish you a very %s, we made a long apple %f for you " % (cnt,astring,numb) )
cnt+=1
# For python 3.6+, we can use the f-string
print(f"{cnt}. I wish you a very {astring}, we made apple {numb.__round__(3)} for breakfast")
cnt+=1

# see https://python-reference.readthedocs.io/en/latest/docs/str/formatting.html