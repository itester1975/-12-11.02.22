mas='пупок','муха','кот','собака','штаны','карандаш','барабулька','му'
new_mas=[]

def ban(new_mas)
    for i in mas:
        stop_word='пупок','муха'
        if i not in stop_word:
            new_mas.append(i)
    return new_mas

#...........................................

words=['карандаши','барабан','машинка','свист','жук','ум','бабушка','мука','дуб','1']
len_words=[len(word) for word in words]
new_words=[]

for word in range(len(words)):
    min_word = min(len_words)
    index_min_word=len_words.index(min_word)
    new_words.append(words[index_min_word])
    len_words.remove(min_word)
    words.pop(index_min_word)
    
print(new_words)

#...........................................

s=['пупок','муха','кот','собака','штаны']
def cat(s):
    while 'кот' in s:
        s.remove('кот')
    return s

#...........................................

p=[1,2,3,4,5,6,7,8,9,5,3,8,5,0,9,2,1,5]
def number():
    while 5 in p:
        p.remove(5)
    return p

#..........................................

y=[]
x=[[],[],[],[],[]]
def users(x,y):
    for i in range(2):
        a=input('Ваше имя:')
        y.append(a)
        b=int(input('Ваш возраст:'))
        y.append(b)
        c=input('Ваш город:')
        y.append(c)
        if b<=18:
            x[0].append(a)
            x[0].append(b)
            x[0].append(c)
        if b>=19 and b<=30: 
            x[1].append(a)
            x[1].append(b)
            x[1].append(c)
        if b>=31 and b<=45: 
            x[2].append(a)
            x[2].append(b)
            x[2].append(c)
        if b>=46 and b<=65: 
            x[3].append(a)
            x[3].append(b)
            x[3].append(c)
        if b>=66 and b<=90: 
            x[4].append(a)
            x[4].append(b)
            x[4].append(c)
    print('массив y:',y)
    return'массив x:',x
#.......................................

def fun(dct2):
    dct2.pop('Сеня')
    dct2.pop('Маничка')
    return dct2
#......................................

q=['мама','папа','дочка','бабушка','муж','женщина','кот','собаченка','кот']
s=[[],[],[],[],[],[],[]]

def sorting(w):
    for i in q:
        k='кот'
        if i not in k and len(i)==3:
            w[0].append(i)
        if i not in k and len(i)==4:
            w[1].append(i)
        if i not in k and len(i)==5:
            w[2].append(i)
        if i not in k and len(i)==6:
            w[3].append(i)
        if i not in k and len(i)==7:
            w[4].append(i)
        if i not in k and len(i)==8:
            w[5].append(i)
        if i not in k and len(i)==9:
            w[6].append(i)
    return w
#.............................................

b = 'карамультук'
s = ''

for i in b:
    u = ['а','у']
    if i not in u:
        s += i
print(s)

#............................................

st='В нашей стране терроризм и экстремизм запрещены'
def prov_sl(sl):
    z='терроризм','экстремизм'
    if sl in z:
        return'**'if len(sl)<=2 else sl[0] +'*'*(len(sl)-2) + sl[-1]
    else:
        return sl
        
def prov_st(st):
    v=st.split()
    print(v)
    for i in range(len(v)):
        v[i]=prov_sl(v[i])
    return ' '.join(v)

#............................................


 s=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
def funce1(s):
    print('Сумма всех чисел:',sum(s),'Минимальное число:',min(s),'Максимальное число:',max(s),'Среднее арифметическое:',sum(s)/15)
    
#............................................

import random as number_id
id=[(number_id.randint(1, 50)) for i in range(100)]
slov={}

def id_het(id):
    return id%2==0
def id_not_het(id):
    return id%2!=0

def funce5():
    for i in id:
        if id_het(i):
            slov[i] = []
        if id_not_het(i):
            slov[i] = []
    for i2 in range(3):
        a=input('Ваше имя:')
        b=input('Ваш возраст:')
        c=input('Ваш пол:')
        slov[a]={'возраст:':b,'пол':c}
        slov[i]=slov[a]
    return slov

#.............................................

q=(1,2,3,4,5,5,3,1,2,4)
for i in q:
    if i==5:
        print(i,'-''отлично')
    if i==4:
        print(i,'-''хорошо')
    if i==3:
        print(i,'-''так себе')
    if i==2:
        print(i,'-''плохо')
    if i==1:
        print(i,'-''очень плохо')

#............................................

a1=[-67, -22, -13, -6, -1, 0, 1, 2, 4, 6, 8, 11, 15, 21, 23, 34, 45, 55, 65, 75, 76, 99]
a2=[[],[]]
def a1_het(a1):
    return a1%2==0
def a1_nehet(a1):
    return a1%2!=0
for i in a1:
    if a1_het(i):
        a2[0].append(i)
    else:
        a2[1].append(i) 
print(a2)

#...........................................

mas=[[],[]]
def funce1():
    a=input('Ваше имя:')
    b=input('Ваш возраст:')
    c=input('Ваш пол:')
    print('И так: Вы','женщина.' if c=='ж' else 'мужчина.','Вас зовут', a, 'вам', b, 'лет')
    if c =='ж':
        mas[0].append(a)
        mas[0].append(b)
        mas[0].append(c)
    else:
        mas[1].append(a)
        mas[1].append(b)
        mas[1].append(c)
    return mas

#.............................................


mas=[1, 2, 3, 4, 6, 7, 8, 5, 5, 6, 7, 8, 9, 7, 4, 3,5]
new_mas=[[],[],[],[],[],[],[],[],[]]
def funce2(massiv,new_massiv):
    for i in massiv:
        if i == 1:
            new_mas[0].append(i)
        if i == 2:
            new_mas[1].append(i)
        if i == 3:
            new_mas[2].append(i)
        if i == 4:
            new_mas[3].append(i)
        if i == 5:
            new_mas[4].append(i)
        if i == 6:
            new_mas[5].append(i)
        if i == 7:
            new_mas[6].append(i)
        if i == 8:
            new_mas[7].append(i)
        if i == 9:
            new_mas[8].append(i)
    print ('старый массив:',massiv)
    print ('новый массив:',new_massiv)

#.....................................
    
line ='Давай завтра сходим погуляем в парке. Будем жечь костер и жарить мясо'
ban='жечь костер'

def ban(line):
    new_line=line.replace('жечь костер','ж**ь к****р')
    return new_line

#.....................................

line='Давай завтра сходим погуляем в парке. Будем жечь костер и жарить мясо. Мусорить не будем. Мусор за собой уберем. Курить и пить алкоголь не будем. В лесу мусор загрязняет природу'.lower()

def check_s(s):
    '''функция check_s()проверяет на наличие слова в запрете и меняет их на звездочки
       функция check_line() удаляет запретные слова 
       строка переведена в нижний регистр .lower()'''
    
    ban=['жечь', 'костер','мусорить','курить','алкоголь','мусор']
    if s in ban:
        return '***'if len(s)<=2 else s[0]+ '*'*(len(s)-2)+s[-1]
    else:
        return s

def check_line(q):
    w=q.split()
    print(w)
    for i in range(len(w)):
        w[i]=check_s(w[i])
    return ' '.join(w)

#........................................


femeli=['конарейка',{'молоток':'инструмент'},'мама','папа','дочка',[4,5,6,7],'суслик', 'бабушка', 10, 20, 'пес', 30, 'хомячек', 40, 'уж', 'уж',[1,2,3]]
femeli_str=[]
femeli_int=[]
femeli_dict=[]
femeli_list=[]

def sorting():
    '''Функция сортирует по типам
    str-строка
    int-числа
    dict-словарь
    list-список(массив)'''
    for i in femeli:
        if type(i)==str:
            femeli_str.append(i)
        elif type(i)==int:
            femeli_int.append(i)
        elif type(i)==dict:
            femeli_dict.append(i)
        elif type(i)==list:
            femeli_list.append(i)

    print(femeli)
    print(femeli_str)
    print(femeli_int)
    print(femeli_dict)
    return(femeli_list)

#........................................

class dog:
    'Создаем класс и прописываем в нутри данные'
    
    def __init__(self,name):
        self.name=name
        self.breed='Я English bulldog.'
        self.color='бело рыжий'
        print('Привет. Меня зовут,',self.name,'!.',self.breed,'. Мой окрас,',self.color)
        
    def weight(self,kg):
        'Я покушал и уже вешу'
        print(self.name,'покушал и уже весит',kg,'кг')

    def food(self,pric):
        'Люблю покушать'
        print(self.name,'хорошо питается !. Моя еда стоит',pric,'у.е. за мешок')
        
    def time(self,clock):
        'Время гулять'
        print('Уже',clock,'часов. Мне пора гулять. Если не пойдем гулять, я вам написаю дома !.')
        
    def walk(self,clock,km):
        'Гуляем'
        print(self.name, 'любит гулять. Я гуляю уже',clock,'часа и протопал уже',km,'км.')
        
    def NewColor(self,newcolor):
        newcolor='черный'
        print('Я так здорово погулял ! Раньше у меня был окрас',self.color,',а теперь',newcolor,'!')
        
senya=dog('Сеня')

#..............................................

class cat:
    
    def __init__(self,name):
        self.name=name
        self.sex='кошечка'
        self.color='бело рыжый'
        self.size='очень маленькая'
        print('Привет! Меня зовут',self.name,'.','Я',self.sex,'. У меня окрас',self.color,'. И я еще,',self.size,'.')
        
    def  info(self,eat,morning_time,evening_time):
        affectionate='ласковая'
        play='люблю играть'
        scratch='чешут'
        hunter='прерожденный охотник'
        catch='поймаю'
        dream='сплю'
        love='очень любят'
        
        print('Я очень',affectionate,'.','У меня много игрушек. И я',play,'.''Я люблю когда мне',scratch,'животик.\
        И еще люблю когда',scratch,'за ушком.''Я',hunter,'. Когда я выросту, я',catch,'большую мыш. Я кушаю',eat,'раза в день.\
        И набираюсь сил. А еще, я днем много',dream,'. Утром я просыпаюсь в',morning_time,'часов, \
        а вечером ложусь спать в',evening_time,'часов. В моей семье, меня',love,'.')
        
manihka=cat('Маничка')

#...............................................
    
class menu:
    '''Создаем сервис Mail'''

    def __init__(self):
        mn=['Главное меню:',['Регистрация:',['Логин:'],['Пароль:']],['Вход:'],['Написать:'],['Прочитать:'],['Отправить:'],['Просмотреть черновик:'],['Удалить:']]
        user_office=[['Написать:'],['Прочитать:'],['Отправить:'],['Просмотреть черновик:'],['Удалить:'],['Выйти']] #личный кабинет
        q={}
        
        self.q=q
        self.mn=mn
        self.user_office=user_office
        self.registration=self.mn[1]
        self.login=self.mn[1][1] #логин
        self.password=self.mn[1][2] #пароль
        self.entrance=self.mn[2] #вход
        self.write=self.mn[3] #написать
        self.read=self.mn[4] #прочитать
        self.send=self.mn[5] #отправить
        self.draft=self.mn[6] #черновик
        self.delete=self.mn[7] #удалить
        print('Сначало регистрация:','Ваш:',self.login,'Ваш:',self.password)
        
        
    def us_registr(self,login,password):#регистрация
        self.bdul=[] #База Данных пользователей для хранения логинов.
        self.bdup=[] #База Данных пользователей для хранения паролей.
        self.bdul.append(login)
        self.bdup.append(password)
        print('Ваш логин (',login,') и пароль (',password,') успешно зарегистрированы:',self.bdul,self.bdup,'.Войдите под своей учетной записью.')
            
    def us_entrance(self,login,password):#вход
        for log in self.bdul:
            if log==login:  
                for pas in self.bdup:
                    if pas==password:
                        print('Вы вошли в личный кабинет:',self.user_office)
        else:
            print('Не верный логин или пароль')
                
    def us_write(self):#написать
        for i in range(1):
            a = input('Напишите сообщение:')
            self.q[a] = {}
            b = input('Мой телефон:')
            self.q[a]['телефон'] = b
            c = input('Мой Mail:')
            self.q[a]['Mail'] = c
            print('С уважением к вам. Ваш доктор Барменталь.')

.............................................................................

zapret=['нацизм','экстремизм','терроризм','взрыв']
alphabet='А','а','Б','б','В','в','Г','г','Д','д','Е','е','Ё','ё','Ж','ж','З','з','И','и','Й','й','К','к','Л','л','М','м','Н','н','О','о','П','п','Р','р','С','с','Т','т','У','у','Ф','ф','Х','х','Ц','ц','Ч','ч','Ш','ш','Щ','щ','ъ','ь','Э','э','Ю','ю','Я','я'
def test_st_name(x):
    if x in zapret:
        return('Это слово писать нельзя')
    for n in x:
        if n in alphabet:
            print('Ошибок нет:',n)
        else:
            print('Тут ошибка: **')
            return 'Исправьте ошибку'
        
..............................................................................

zapret=[' ','!','&','(',')','*','-','+','=','%','$','#','""',',','№',';',':','<','>','|',']','[]','[','|','{}','{','}']
alphabet='А','а','Б','б','В','в','Г','г','Д','д','Е','е','Ё','ё','Ж','ж','З','з','И','и','Й','й','К','к','Л','л','М','м',\
'Н','н','О','о','П','п','Р','р','С','с','Т','т','У','у','Ф','ф','Х','х','Ц','ц','Ч','ч','Ш','ш','Щ','щ','ъ','ь','Э','э',\
'Ю','ю','Я','я','@','_',0,1,2,3,4,5,6,7,8,9,'.','A','a','B','b','C','c','D','d','E','e','F','f','G','g','H','h','I','i',\
'J','j','K','k','L','l','M','m','N','n','O','o','P','p','Q','q','R','r','S','s','T','t','U','u','V','v','W','w','X','x',\
'Y','y','Z','z'


def test_st_mail(m):
    '''Афто тест. Строка Mail'''
    mm=list(m)
    for i in mm:
        if i in zapret:
            return 'Ошибка. Не верный mail'
    for i in mm:
        if i in alphabet:
            return 'Ваш mail:',' '.join(mm)

................................................................................
       
       
