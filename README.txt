Skillo course - final project exam

Project Definition
Project Title: "Movie Database Application"
Project Description:
In this project, you have to create a CLI Python application that serves as a movie database.
The application has to use SQLite as a database and provide features for listing, viewing,
searching, adding, and categorizing movies. Here are the key components and requirements
of this project:

Functionality ( CLI ):
Movie Listing Page: movlst
When executed this command should return a structured representation of all the
movies in the database
Movie Details Page: movdt <movie_id>
Users should be able to get the details of a movie if it exists in the database. Details
may include the movie's title, description, release date, director, genre, and user
ratings.
Search Functionality: movsrch <query>
Users should be able to search for movies based on their titles.
Search results should be a structured representation of all the movies that match the
search query.
Adding New Movies: movadd <title> <desc> <date> <director> <genre>
Users can add new movies to the database.
They should provide details such as the movie's title, description, release date,
director, and genre
Favorites: movfv <movie_id>
Users should be able to mark movies as their favorites.
Movie Categories: movcat <category: [liked, newest, genre]>
Movies will be categorized by genres.
Sections like "Most Liked," "Newest," and "Genres" will feature the top 5 movies in
each category.
Technical Requirements:
★ Follow all the OOP principles and good practices
★ Implement SQLite as the database to store movie information.
★ Have a good database structure including tables and relations
★ Have well-written project documentation
★ Have proper project and apps structure and separation

Functionality ( Django ):
Movie Listing Page:
The application will have a main page that lists all the movies in the database.
Each movie will be displayed with its title and a brief description.
Movie Details Page:
When a user clicks on a movie from the listing, it will open a new page with detailed
information about that movie.
Details may include the movie's title, description, release date, director, genre, and
user ratings.
Search Functionality:
Users can search for movies based on their titles, directors, or genres.
Search results will be displayed on a separate page.
Adding New Movies:
Users can add new movies to the database.
They should provide details such as the movie's title, description, release date,
director, genre, and upload a cover image.
Favorites:
Users can mark movies as their favorites.
There will be a section where users can view and manage their favorite movies.
Movie Categories:
Movies will be categorized by genres.
Sections like "Most Liked," "Newest," and "Genres" will feature the top 5 movies in
each category.
Technical Requirements:
★ Use Django for building the web application.
★ Implement SQLite as the database to store movie information.
★ Utilize Django models for defining the movie data structure.
★ Create views and templates for displaying movie details and listing.
★ Implement search functionality using Django's query capabilities.
★ Allow user registration and login for managing favorites.
★ Use Django's ORM for database operations.
★ Have well-written project documentation
★ Have proper project and apps structure and separation



PROJECT SOLUTION DESCRIPTION

1. Models DB. My main starting point for building the project is the database models. The project building over 3 related models:
    - Movie model. Keeps all the needed information about a movie. A real case problem I met is movies with the same titles.
      The logic to keep each movie unique is around the release date. Movies with the same titles are allowed, but the release date must be different.
    - Django build-in User model. I'm implementing the build-in model by inheritance UserCreationForm functionality in my RegisterForm class.
      This way I do not have to create custom rules for example customer registration validation, DB hashing passwords, etc.
      Via built-in User model and Django restricting my app functionality for non-registered users.
    - Favorites model. This model handles the user's favorite movie logic. It is a connecting table between the Movie and the User via a foreign key to each table.
      This way the model keeps the unique pair of user ID and movie ID. Cascade delete is allowed so if a movie or user is deleted the favorite record will be removed.
      Movie likes are determined by the user's favorite movies. Each movie added to any registered user's favorite is counted as one like for this movie.
2. Project structure. As the task definition required the project is split into two interfaces. One is Django-HTML and the other one is Django-CLI. Both interfaces interact with the same Sqlite3 DB.
   This way some code functionality is used in both logics. For example DB queries and forms for validation.
3. Django-HTML interface. Is structured in maine page with few sections.
    - Available movies: contains the list of movies, searching, categories sorting, and full movie details information.
    - Library movies management: contains adding and removing movies from the library DB.
    - Favorite movies management: contains adding a movie to favorite and viewing/removing favorite movies. Required user authentication.
    - Application messages: HTML pop-up messages allowing users to know once a task is completed/not complete or when the user violates an app rule.
4. Django-CLI interface. I'm implementing Django BaseCommand functionality that allows commands to be executed via project manage.py. Each command is represented py file located in management/commands:
    - movadd: adding a movie to the DB.
    - movcat: sorting movies list in a certain order.
    - movdel: deleting a movie from teh DB.
    - movdt: displaying full movie details.
    - movfv: adding a movie to user favorite.
    - movfvdel: remove a movie from a user favorite.
    - movfvlst: displaying favorite movies for a given user.
    - movlst: displaying all available movies in the library.
    - movsrch: search a movie by title or director.
5. Users logic: allowing users registration and log in/log out, and displaying currently logged user.
