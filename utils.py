import models
from models import User, Avans


def avans_saver(name: str, avans: str) -> bool:
    if name and avans:
        user = User.add(name)
        for avans in avans.split("\n"):
            Avans.add(avans, user)
        return True
    return False


def show_all_for_name(name: str):
    return [tuple([user.name, ", ".join([avans.avans for avans in user.avans])]) for user in models.User.find_by_name(name)]
