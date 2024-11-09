from time import sleep


class Video:
    video_list = []

    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode
        self.__str__()

    def __str__(self):
        return f'Видео: {self.title}, длительность: {self.duration}'


class User:
    users_list = []

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age
        self.__str__()

    def __str__(self):
        return f'Сейчас активен(на) {self.nickname}'


class UrTube:

    def __init__(self):
        self.current_user = None
        self.user = User(None, None, None)
        self.users = self.user.users_list
        self.video = Video(None, None)
        self.videos = self.video.video_list

    def register(self, nickname: str, password: str, age: int):
        if len(self.users) == 0:
            self.users.append([nickname, hash(password), age])
            self.current_user = User(nickname=nickname, password=password, age=age)
        else:
            for i in range(0, len(self.users)):
                if nickname == self.users[i][0]:
                    print(f'Пользователь {nickname} уже существует')
                    break
                else:
                    self.users.append([nickname, hash(password), age])
                    if self.current_user is None:
                        self.current_user = User(nickname=nickname, password=password, age=age)
                        break
                    else:
                        self.log_out()
                        self.current_user = User(nickname=nickname, password=password, age=age)
                        break

    def log_in(self, nickname: str, password: str):
        password = hash(str(password))
        if len(self.users) == 0:
            print(f'На данный момент никаких пользователей не существует, сначала зарегестрируйтесь')
        else:
            if self.current_user is None:
                for i in range(0, len(self.users)):
                    if self.users[i][0] == nickname and password == self.users[i][1]:
                        self.current_user = User(nickname=nickname, password=password, age=self.users[i][2])
                    elif self.users[i][0] == nickname and password != self.users[i][1]:
                        print(f'Неверный пароль')
                    else:
                        print(f'Такого пользователя не существует')
            else:
                print(f'Выйдите из аккаунта, чтобы зайти в другой')

    def log_out(self):
        self.current_user = None
        return self.current_user

    def add(self, *video_datas):
        for i in video_datas:
            self.videos.append([i.title, i.duration, i.time_now, i.adult_mode])

    def get_videos(self, prompt):
        if len(self.videos) == 0:
            print(f'На данный момент нет никаких видео, но вы можете загрузить новое!')
        else:
            temp_list = list()
            for i in range(0, len(self.videos)):
                if prompt.lower() in self.videos[i][0].lower():
                    temp_list.append(self.videos[i][0])
            if len(temp_list) == 0:
                return f'Видео по вашему запросу не обнаружено'
            else:
                return temp_list

    def watch_video(self, title):
        if self.current_user is not None:
            for i in range(0, len(self.videos)):
                if title == self.videos[i][0]:
                    if self.videos[i][3] == True and self.current_user.age < 18:
                        return print(f'Вам нет 18 лет, пожалуйста, покиньте страницу')
                    else:
                        current_video = Video(self.videos[i][0], self.videos[i][1], self.videos[i][2], self.videos[i][3])
                        for current_video.time_now in range(0, current_video.duration + 1):
                            print(current_video.time_now, end=' ')
                            sleep(1)
                        return print(f'Конец видео')
        else:
            return print(f'Войдите в аккаунт, чтобы смотреть видео')


ur = UrTube()

v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
