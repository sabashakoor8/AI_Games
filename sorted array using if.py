
# Online Python - IDE, Editor, Compiler, Interpreter

def sort4(a, b,c,d):
    if(a>b):
        a,b=b,a
    if(c>d):
        c,d=d,c
    if(a>c):
        a,c=c,a
    if(b>d):
        b,d=d,b
    if(b>c):
        b,c=c,b
    return(a,b,c,d)
a = int(input('Enter 1st number: '))
b = int(input('Enter 2nd number: '))
c = int(input('Enter 3rd number: '))
d = int(input('Enter 4th number: '))

print(f'sorted values are {sort4(a, b,c,d)}')
