from client import SchoolClient, UserClient

if __name__ == '__main__':
    school = SchoolClient("58.192.192.3")
    try:
        user: UserClient = school.user_login("21320316", "jtp19980521")
    except Exception as e:
        print(e)
    course = user.get_schedule(year=2023, term=1)
    score = user.get_score(year=2023, term=1)

    try:
        print(course)
        print(score)
    except Exception as e:
        print(e)
