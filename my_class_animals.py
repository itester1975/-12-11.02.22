class dog:
    'Создаем класс и прописываем в нутри параметры'
    
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
