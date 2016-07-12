class Movie:
    CHILDREN = 2
    REGULAR = 0
    NEW_RELEASE = 1

    def __init__(self, title, price_code):
        assert isinstance(title, str)
        self._title = title
        assert isinstance(price_code, int)
        self._price_code = price_code

    def get_price_code(self):
        return self._price_code

    def set_price_code(self, arg):
        assert isinstance(arg, int)
        self._price_code = arg

    def get_title(self):
        return self._title


class Rental:
    def __init__(self, movie, days_rented):
        assert isinstance(movie, Movie)
        self._movie = movie
        assert isinstance(days_rented, int)
        self._days_rented = days_rented

    def get_days_rented(self):
        return self._days_rented

    def get_movie(self):
        return self._movie


class Customer:
    def __init__(self, name):
        assert isinstance(name, str)
        self._name = name
        self._rentals = []

    def add_rental(self, arg):
        assert isinstance(arg, Rental)
        self._rentals.append(arg)

    def get_name(self):
        return self._name


    def statement(self):
        totalAmount = 0
        frequentRenterPoints = 0
        rentals = iter(self._rentals)

        result = "Учет аренды для" + self.get_name() + "\n"

        while (rentals.hasMoreElements()):
            thisAmount = 0
            each = next(rentals)

            if each.getMovie().getPriceCode() == Movie.REGULAR:
                thisAmount += 2
                if each.getDaysRented() > 2:
                    thisAmount += (each.getDaysRented() - 2) * 15

            elif each.getMovie().getPriceCode() == Movie.NEW_RELEASE:
                thisAmount += each.getDaysRented() * 3

            elif each.getMovie().getPriceCode() ==  Movie.CHILDREN:
                thisAmount += 15
                if (each.getDaysRented() > 3):
                    thisAmount += (each.getDaysRented() - 3) * 15

            # добавить очки для активного арендатора
            frequentRenterPoints += 1

            #бонус за аренду новинки на два дня
            if ((each.getMovie().getPriceCode() == Movie.NEW_RELEASE) &
                        each.getDaysRented() > 1):
                frequentRenterPoints +=1

            #показать результаты для этой аренды
            result += "\t" + each.getMovie().getTitle()+ "\t" + str(thisAmount) + "\n"
            totalAmount += thisAmount

        #добавить нижний колонтитул
        result += "Сумма задолженности составляет" + str(totalAmount) + "\n"
        result += "Вы заработали " + str(frequentRenterPoints) + "очков за активность"

        return result


def run():
    movie = Movie('Terminator', 500)
    movie2 = Movie('Terminator', 800)

    customer1 = Customer("Иван Иваныч")
    customer2 = Customer("Василий Петрович")

    
    print("Just hello")
