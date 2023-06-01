'''Создайте класс Касса, который хранит текущее количество денег в кассе, у него есть методы:

top_up(X) - пополнить на X
count_1000() - выводит сколько целых тысяч осталось в кассе
take_away(X) - забрать X из кассы, либо выкинуть ошибку, что не достаточно денег'''

class Till:
    def __init__(self):
        self.casa = 0
        
    def top_up(self, x): # пополнить на X
        self.casa += x
        return self.casa
            
    def count_1000(self): # выводит сколько целых тысяч осталось в кассе
        count = self.casa // 1000
        return count
    
    def take_away(self, y): # забрать Y из кассы, либо выкинуть ошибку, что не достаточно денег
        if self.casa < y:
            print('В кассе меньше денег чем Вы хотите забрать!')
        else:
            self.casa -= y
        return self.casa
    
    def summ(self):
        return self.casa
    
    
Casa = Till()   
while True:
    comand = input('\n"1" - пополнить на\n"2" - выводит сколько целых тысяч осталось в кассе\n"3" - забрать  из кассы, либо выкинуть ошибку, что не достаточно денег\n"4" - сколько в кассе\n"Esc" - выйход\n\nВведите команду:\n') 
    if comand == '1':
        print('Пополньть кассу на: ')
        print(f'В кассе: {Casa.top_up(int(input()))}')
    elif comand == '2':
        print(f'{Casa.count_1000()} целых тысячи осталось в кассе.')
    elif comand == '3':
        print('Забрать из кассы: ')
        print(f'В кассе: {Casa.take_away(int(input()))}')
    elif comand == '4':
        print(f'В кассе: {Casa.summ()}')
    elif (comand == 'Esc') or (comand == 'esc'):
        break
    else:
        print('Не верная команда!\n"1" - пополнить на\n"2" - выводит сколько целых тысяч осталось в кассе\n"3" - забрать  из кассы, либо выкинуть ошибку, что не достаточно денег\n"4" - сколько в кассе\n"Esc" - выйход')
            
        