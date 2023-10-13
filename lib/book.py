class Book:
    def __init__(self, title, page_count):
        self.title = title
        self._page_count = None  # Initialize _page_count to None initially
        self.current_page = 0

        # Set the page_count using the setter method
        self.page_count = page_count

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        if not isinstance(value, int):
            print("page_count must be an integer")
        else:
            self._page_count = value

    def turn_page(self):
        self.current_page += 1
        print("Flipping the page...wow, you read fast!")







        