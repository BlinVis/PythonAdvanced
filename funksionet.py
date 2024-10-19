def greeting(name='Njeri'):
    global message

    message=f'hello {name}'
    print(message)

greeting('Vjosa')


def mbledhje(nr1,nr2):
    return nr1+nr2
shuma=mbledhje(4,12345)
print(shuma)
print(message)
greeting()

totali=0
for n in range(1,51):
    totali+=n
print(totali)
def add_number_in_range(a,b):
    total=0
    for n in range(a,b):
        total+=n
    print(total)
add_number_in_range(20,30)




