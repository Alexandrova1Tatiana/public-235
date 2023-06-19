def read_zalgo(zalgotext):
    return "".join(i for i in zalgotext if i.isalnum() or i in ".,!? ")