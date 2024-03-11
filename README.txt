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