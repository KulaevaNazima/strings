# problem 23
name = input ("Как тебя зовут? ")
print ("Привет, ", name)
age = input ("Сколько тебе лет? ")
favorite_film = input ("Какой твой любимый фильм? ")
print ("Мне тоже нравится ", favorite_film, "У тебя хороший вкус")

#problem 31
line1= "Google создаст специальную команду для поиска багов в особо важных приложениях."
x= line1.split ()
print (len(x))

# problem 25
line8= "Прошли те времена, когда компьютер был грязно-белой офисной коробкой."
#x= line8.split (" ")
x=" ".join(line8)
print (x)
print (type(x))

#problem 11
line3= "хакеры слили в сеть данные пакистанской энергетической компании k-Electric"
x= line3.title ()
print (x)

# problem 2
line4 = "GitHub"
y= input ("Введите символ")
x= y.join (line4)
print (x)

# problem 5
line5= "Ботнет IPStorm , в который ранее входили лишь Windows-машины, увеличился до 13 500 зараженных систем"
x=line5.replace ("е", "3")
print (x)

# problem 0
txt= "Жизнь коротка, "
txt1= "Искусство вечно"
x= txt.lower ()
y= txt1. upper ()
print (x, y)

# problem 1
line4= "GitHub"
x= line4.isalpha ()
print ("Это " , format (x))

# Задание №1
high= int(input ("Введите свой рост: "))
helf= int(input ("Введите свой текущий вес: "))
if helf > (high -110):
	print ("Вам нужно сбросить ", helf - (high-110),  "киллограмм")
elif helf < (high-110):
	print ("Вам нужно набрать ", (high-110)- helf,  "киллограмм")
else:
	print ("У вас идеальный вес")

#Задание2:
z = 'z'
x = 'x'
c = 'c'
# Из 3 переменных сделать строку: zxxxxxccccccccc
string = z + (x * 5) + (c * 9)
print (string)

txt= "Жизнь коротка, искусство вечно"
x= ",".join (txt)
print (x)