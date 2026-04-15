from datetime import datetime
current_time = datetime.now()

movie_box= []
rating_box = []

def add_movies(movie_name):
    movie_box.append(movie_name)
    return "Movie Added Successfully"

def rate_movies(ratings):
    rating_box.append(ratings)
    return "Rates will be reviewed"

def average_ratings_for_a_movie(movie_name):
    sums = 0
    average = 0
    for rating in rating_box:
        sums +=  rating
        average = sums  / len(rating_box)
    return average

def average_ratings():
    sums= 0
    average = 0
    for rating in rating_box:
        sums += rating
        average = sums / len(rating_box)
    return average


def main():
    is_running = True
    while is_running:
        menu = """
        ____________________________________________
       |WELCOME TO NAIJA MOVIE BOX RATING SYSTEM    |
       |____________________________________________|
       |         1. Add a Movie                    |
       |         2. Rate a Movie                   |
       |         3. View Average Ratings           |
       |         4: View All Movies                |
       |         5. Exit                           |
       |___________________________________________|
       """
        print(menu)
        print()
        user_input = int(input("Enter your choice: "))

        match user_input:
            case 1:
                running  = True
                while running:
                    user_choice = input("Enter Movie Name : ").strip()
                    if user_choice.strip() == "":
                        print("No White Spaces ")
                    else:
                        print(f"Movie {add_movies(user_choice).title()} Added \n Time Added :{current_time}")

                        user_input_to_add_movie = input("Do you want To Add Another Movie ? : ").strip()
                        if user_input_to_add_movie.strip() == "":
                            print("No White Spaces ")
                        else:
                            if user_input_to_add_movie == "yes":
                                continue
                            elif user_input_to_add_movie == "no" or "No" or "NO" or "nO" :
                                running  = False
                        print()

            case 2:
                user_choice = input("Enter Movie Name : ").strip()
                if user_choice.strip() == "":
                    print("No White Spaces ")
                else:
                    if user_choice  in movie_box:
                        user_ratings = float(input("Enter your Ratings (1-5) :"))
                        if user_ratings < 0 or user_ratings > 5:
                            print("invalid input !!")
                        else:
                             print(rate_movies(user_ratings))
                             print(f"Rating Added For {user_choice} {user_ratings}")
                    else:
                        print("Movie Not Found")
                        user_input_to_add_movie = input("Do you want To Add This Movie ? : ").strip()
                        if user_input_to_add_movie.strip() == "":
                            print("No White Spaces ")
                        else:
                            print(add_movies(user_choice))
                            print()

            case 3:
                print("Average Ratings ")
                for movies in movie_box:
                    print(f"-inception :{round(average_ratings(),2)}\n-{movies} :{round(average_ratings(),2)} ")
                print()

            case 4:
                count = 0
                for movies in  movie_box:
                    count += 1
                    print(f"{count}- { movies} ")
                print()

            case 5:
                 print("Exiting .......")
                 is_running = False

            case _:
                print("Invalid Input")


main()

