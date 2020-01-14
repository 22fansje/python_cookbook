import csv
with open('movies.csv', 'w', newline='') as file:
    movies = "Monty Python and the Hole Grail",1975,
    movies2 = "Cat on a Hot Tin Roof",1958,
    movies3 = "On the Waterfront",1954
    writer = csv.writer(file)
    writer.writerow(movies)
    writer.writerow(movies2)
    writer.writerow(movies3)