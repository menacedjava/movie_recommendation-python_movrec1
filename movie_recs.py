# Movie Recommendation System (simple content-based)
movies = {
    "Inception": ["sci-fi", "thriller"],
    "Titanic": ["romance", "drama"],
    "Matrix": ["action", "sci-fi"]
}

def recommend(genre):
    return [m for m, g in movies.items() if genre in g]

print("Recommended sci-fi:", recommend("sci-fi"))
