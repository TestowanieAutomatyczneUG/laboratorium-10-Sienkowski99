class Note:
    def __init__(self, name, note):
        if not isinstance(name, str) or not name:
            raise ValueError
        if note > 6 or note < 2:
            raise ValueError
        self.name = name
        self.note = note

    def get_name(self):
        return self.name

    def get_note(self):
        return self.note
