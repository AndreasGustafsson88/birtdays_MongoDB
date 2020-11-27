from Data.Models.gifts import Gift


def add_gifts(gift):
    present = Gift(gift)
    present.save()
    return present


def show_gifts():
    return Gift.all()
