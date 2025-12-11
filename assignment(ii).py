#In the Book class, the constructor receives a list of reviews from the user, so I don’t need to create an empty list inside the class. Whatever list is passed as an argument is already a list, and I can directly store it using self.list_of_reviews = list_of_reviews. This lets the class start with the reviews given by the user.

#The add_review() method adds a new review to this list using append().
#The count_reviews() method simply returns how many reviews are in the list using len().
#The display_reviews() method prints each review using a loop.
class Book:
    def __init__(self, title, author, list_of_reviews):
        print("book constructor is called")
        self.title = title
        self.author = author
        self.list_of_reviews = list_of_reviews
        print(f"Book created by {self.author} with title '{self.title}' and reviews {self.list_of_reviews}")

    def add_review(self, review):
        self.list_of_reviews.append(review)
        return f"updated list of reviews: {self.list_of_reviews}"

    def count_reviews(self):
        return len(self.list_of_reviews)

    def display_reviews(self):
        for review in self.list_of_reviews:
            print("display reviews :",review,end=" , ")
b = Book("The Great Gatsby", "F. Scott Fitzerland", ["amazing book", "a classic one"])
print(b.add_review("must read"))
print(f"total reviews: {b.count_reviews()}")
b.display_reviews()