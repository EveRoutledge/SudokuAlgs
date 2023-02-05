s =''
n=3

# as defined
#for i in range(0,n**2):
#    for j in range(0,n**2):
#        s=s+' ' + str(((i%n)*n+i//n+j)%(n**2))
#    s=s+'\n'
#    print(s)
#    s=''

#print('\n\n')

for i in range(1, n**2+1):
    for j in range(1,n**2+1):
        s=s+' '+str((((i-1)%n)*n+(i-1)//n+j-1)%(n**2)+1)
    s=s+'\n'
    print(s)
    s=''