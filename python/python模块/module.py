def print_dicts(first, last, **people):
    user = {}
    user["firstname"] = first
    user["lastname"] = last
    for key, value in people.items():
        user[key] = value
    # return user
    print(user)


def print_list(lists):
    for list in lists:
        print(list)
