from models import User, Avans


def avans_saver(name: str, avans: str) -> bool:
    if name and avans:
        user = User.add(name)
        for avans in avans.split("/n"):
            Avans.add(avans, user)
        return True
    return False
