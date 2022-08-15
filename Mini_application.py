class Movie:
    def __init__(self,title,hero,heroine):
        self.title=title
        self.hero=hero
        self.heroine=heroine
    def info(self):
        print(f'The movie name is {self.title}')
        print(f'The Actor Name is {self.hero}')
        print(f'The Actress name is {self.heroine}')
list_of_movies=[]
while(True):
    title=input('Enter the Movie Name: ')
    hero=input('Enter the Hero Name: ')
    heroine=input('Enter the Heroine name: ')
    m=Movie(title,hero,heroine)
    list_of_movies.append(m)
    option=input('Do you want to add one more movie?[Yes/No]')
    if option.lower()=='no':
        print('Thank you')
        break
for movie in list_of_movies:
    movie.info()
    print()


        