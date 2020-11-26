from Data.Models.people import People


def show_all_people():
    return People.find_all()
    # return db.people.find({})


def update_people():
    return


def exists(people):
    return People.find(dob=people["dob"]).exists()
