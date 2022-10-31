# define User class
class User:
    def __init__(self, id, name, cityId):
        self.id = id
        self.name = name
        self.cityId = cityId

# define User class
class City:
    def __init__(self, id, name):
        self.id = id
        self.name = name

# initialize users & cities
users = []
users.append(User(1, "John", 1))
users.append(User(2, "Amy", 1))
users.append(User(3, "Eric", 2))
users.append(User(4, "Tina", 1))
users.append(User(5, "Lisa", 2))

cities = []
cities.append(City(1, "Taipei"))
cities.append(City(2, "Berlin"))


# Start main logics
# filter berlin users
berlinUsers = filter(lambda u: u.cityId == 2, users)
berlinUsersNames = [u.name for u in berlinUsers]

# print message
print('User', end=' ')
print(*berlinUsersNames, sep=', ', end=' ')
print('live in Berlin')