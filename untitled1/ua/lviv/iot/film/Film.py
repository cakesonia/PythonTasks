class Film:
    total_box_office = 0

    def __init__(self, name_of_film="The Stronghold", genre_of_film="Fantasy", country="Ukraine", box_office=0.71,
                 running_time="100"):
        self.name_of_film = name_of_film
        self.genre_of_film = genre_of_film
        self.__country = country
        self.box_office = box_office
        self.running_time = running_time
        Film.total_box_office += box_office

    def to_string(self):
        print(
            "Name of film: " + self.name_of_film + "; Genre of film: " + self.genre_of_film + "; Country: " + self.country
            + "; Running time = " + self.running_time + " ")

    def print_sum(self):
        print("Box office of " + str(self.name_of_film) + " is " + str(self.box_office))

    @staticmethod
    def static_print_sum():
        print("Total box office is " + str(Film.total_box_office))


if __name__ == '__main__':
    stronghold = Film()
    avengers = Film("Avengers", "Comics movie", "USA", 1519.2)
    dunkirk = Film("Dunkirk", "War film", "USA", 527.3, "106")

    stronghold.to_string()
    avengers.to_string()
    dunkirk.to_string()

    stronghold.print_sum()
    avengers.print_sum()
    dunkirk.print_sum()

    Film.static_print_sum()
