from person import import_check #이렇게 쓰면 해당 함수를 쉽게 가져올수있다
from person import Person #이렇게 쓰면 해당 함수를 쉽게 가져올수있다
import_check()
x=Person("Harry",52)
y=Person("viper",23)
z=Person("Jummy",24)
print(x.name)
print(x.age)
print(y.name)
print(y.age)
print(z.name)
print(z.age)