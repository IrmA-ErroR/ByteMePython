def filter_by_age(users: dict, min_age: int) -> list:
    return [(user, value) for user, value in users.items()]
