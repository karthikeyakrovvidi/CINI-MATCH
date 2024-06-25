import tkinter as tk
from tkinter import messagebox

class Movie:
    def __init__(self, title, genre, rating):
        self.title = title
        self.genre = genre
        self.rating = rating

class MovieRecommendationSystem:
    def __init__(self):
        self.movies = []

    def add_movie(self, title, genre, rating):
        movie = Movie(title, genre, rating)
        self.movies.append(movie)

    def search_movies_by_title(self, title):
        return [movie for movie in self.movies if title.lower() in movie.title.lower()]

    def search_movies_by_genre(self, genre):
        return [movie for movie in self.movies if genre.lower() in movie.genre.lower()]

    def delete_movie(self, title):
        initial_length = len(self.movies)
        self.movies = [movie for movie in self.movies if movie.title.lower() != title.lower()]
        return initial_length != len(self.movies)

    def recommend_top_n_movies(self, n):
        sorted_movies = sorted(self.movies, key=lambda movie: movie.rating, reverse=True)
        return sorted_movies[:n]

system = MovieRecommendationSystem()

def add_movie():
    title = entry_title.get()
    genre = entry_genre.get()
    rating = entry_rating.get()
    if not title or not genre or not rating:
        messagebox.showwarning("Input Error", "Please fill in all fields.")
        return
    try:
        rating = float(rating)
        system.add_movie(title, genre, rating)
        messagebox.showinfo("Success", f"Movie '{title}' added successfully.")
        entry_title.delete(0, tk.END)
        entry_genre.delete(0, tk.END)
        entry_rating.delete(0, tk.END)
    except ValueError:
        messagebox.showwarning("Input Error", "Rating must be a number.")

def search_movie():
    search_by = var_search_by.get()
    keyword = entry_search.get()
    if not keyword:
        messagebox.showwarning("Input Error", "Please enter a search keyword.")
        return
    if search_by == "Title":
        found_movies = system.search_movies_by_title(keyword)
    else:
        found_movies = system.search_movies_by_genre(keyword)
    display_movies(found_movies)

def recommend_movie():
    top_n = entry_top_n.get()
    if not top_n:
        messagebox.showwarning("Input Error", "Please enter the number of top movies to recommend.")
        return
    try:
        top_n = int(top_n)
        recommended_movies = system.recommend_top_n_movies(top_n)
        display_movies(recommended_movies)
    except ValueError:
        messagebox.showwarning("Input Error", "Number must be an integer.")

def delete_movie():
    title = entry_delete_title.get()
    if not title:
        messagebox.showwarning("Input Error", "Please enter the title of the movie to delete.")
        return
    if system.delete_movie(title):
        messagebox.showinfo("Success", f"Movie '{title}' deleted successfully.")
        entry_delete_title.delete(0, tk.END)
    else:
        messagebox.showwarning("Error", f"Movie '{title}' not found.")

def display_movies(movies):
    text_display.delete(1.0, tk.END)
    if not movies:
        text_display.insert(tk.END, "No movies found.\n")
    else:
        for movie in movies:
            text_display.insert(tk.END, f"Title: {movie.title}, Genre: {movie.genre}, Rating: {movie.rating}\n")

root = tk.Tk()
root.title("Movie Recommendation System")

# Add Movie Section
frame_add = tk.Frame(root)
frame_add.pack(padx=10, pady=5, fill="x")

label_add = tk.Label(frame_add, text="Add Movie")
label_add.pack(anchor="w")

label_title = tk.Label(frame_add, text="Title:")
label_title.pack(anchor="w")

entry_title = tk.Entry(frame_add)
entry_title.pack(anchor="w", fill="x")

label_genre = tk.Label(frame_add, text="Genre:")
label_genre.pack(anchor="w")

entry_genre = tk.Entry(frame_add)
entry_genre.pack(anchor="w", fill="x")

label_rating = tk.Label(frame_add, text="Rating:")
label_rating.pack(anchor="w")

entry_rating = tk.Entry(frame_add)
entry_rating.pack(anchor="w", fill="x")

button_add = tk.Button(frame_add, text="Add Movie", command=add_movie)
button_add.pack(anchor="w", pady=5)

# Search Movie Section
frame_search = tk.Frame(root)
frame_search.pack(padx=10, pady=5, fill="x")

label_search = tk.Label(frame_search, text="Search Movie")
label_search.pack(anchor="w")

var_search_by = tk.StringVar(value="Title")
radio_title = tk.Radiobutton(frame_search, text="Title", variable=var_search_by, value="Title")
radio_title.pack(anchor="w")

radio_genre = tk.Radiobutton(frame_search, text="Genre", variable=var_search_by, value="Genre")
radio_genre.pack(anchor="w")

entry_search = tk.Entry(frame_search)
entry_search.pack(anchor="w", fill="x")

button_search = tk.Button(frame_search, text="Search", command=search_movie)
button_search.pack(anchor="w", pady=5)

# Recommend Movie Section
frame_recommend = tk.Frame(root)
frame_recommend.pack(padx=10, pady=5, fill="x")

label_recommend = tk.Label(frame_recommend, text="Recommend Top N Movies")
label_recommend.pack(anchor="w")

entry_top_n = tk.Entry(frame_recommend)
entry_top_n.pack(anchor="w", fill="x")

button_recommend = tk.Button(frame_recommend, text="Recommend", command=recommend_movie)
button_recommend.pack(anchor="w", pady=5)

# Delete Movie Section
frame_delete = tk.Frame(root)
frame_delete.pack(padx=10, pady=5, fill="x")

label_delete = tk.Label(frame_delete, text="Delete Movie")
label_delete.pack(anchor="w")

label_delete_title = tk.Label(frame_delete, text="Title:")
label_delete_title.pack(anchor="w")

entry_delete_title = tk.Entry(frame_delete)
entry_delete_title.pack(anchor="w", fill="x")

button_delete = tk.Button(frame_delete, text="Delete", command=delete_movie)
button_delete.pack(anchor="w", pady=5)

# Display Movies Section
frame_display = tk.Frame(root)
frame_display.pack(padx=10, pady=5, fill="both", expand=True)

text_display = tk.Text(frame_display, height=10)
text_display.pack(fill="both", expand=True)

root.mainloop()