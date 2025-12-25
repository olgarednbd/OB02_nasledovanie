class User():
    def __init__(self, user_id, name):
        self._id = user_id
        self._name = name
        self._access_level = "user"

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_access_level(self):
        return self._access_level

    def set_name(self, name):
        self._name = name


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self._access_level = "admin"

    def add_user(self, user_list, user):
        user_list.append(user)
        print(f"Пользователь {user.get_name()} добавлен")


    def remove_user(self, user_list, user_id):
        for user in user_list:
            if user.get_id() == user_id:
                user_list.remove(user)
                print(f"Пользователь c ID {user_id} удалён")
                return
        print("Пользователь не найден")

users = []

admin = Admin(0, "Мальвина")

user1 = User(1, "Буратино")
user2 = User(2, "Пьеро")
user3 = User(3, "Артемон")
user4 = User(4, "Арлекин")

admin.add_user(users, user1)
admin.add_user(users, user2)
admin.add_user(users, user3)
admin.add_user(users, user4)

user5 = User(5, "Карабас Барабас")
admin.add_user(users, user5)

print(users)
admin.remove_user(users, 4)
print(users)

print(user1.get_name())
