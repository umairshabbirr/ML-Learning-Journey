dict={}
for i in range(10):
    if i%2==0:
        dict[i]=i*i
        print(dict)
// comprehensive dictionary
dict={i:i*i for i in range(10) if i%2==0}
print(dict)
