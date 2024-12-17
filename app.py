import streamlit as st
import pickle

# Load movie data and similarity matrix
movies = pickle.load(open("movies_list.pkl", 'rb'))
similarity = pickle.load(open("similarity.pkl", 'rb'))
movies_list = movies['title'].values

# Add custom CSS for styling and background image
st.markdown(f"""
    <style>
        body {{
            background: url("https://www.freecodecamp.org/news/content/images/size/w2000/2024/08/pexels-nathan-engel-50858-436413.jpg");
            background-size: cover;
            background-position: center bottom; /* Shift image downward */
            background-attachment: fixed; /* Make background cover the whole page */
            margin: 0;
            padding-top: 100px; /* Add space at the top */
            color: #f5f5f5;
        }}
        .stApp {{
            background-color: rgba(0, 0, 0, 0.7); /* Add overlay for better readability */
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.4);
        }}
        .main-header {{
            color: #ffdd59;
            font-size: 50px;
            font-family: 'Georgia', serif;
            text-align: center;
            margin-bottom: 20px;
            text-shadow: 2px 2px 8px rgba(255, 255, 255, 0.6);
        }}
        .recommend-title {{
            font-size: 24px;
            font-family: 'Verdana', sans-serif;
            font-weight: bold;
            color: #00d4ff;
            margin-top: 20px;
            text-align: center;
        }}
        .movie-title {{
            font-size: 18px;
            color: white;
            background-color: #333333;
            border-radius: 10px;
            padding: 10px;
            text-align: center;
            font-family: 'Courier New', Courier, monospace;
            font-weight: bold;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.5);
        }}
        .stButton>button {{
            background-color: #ff4500;
            color: white;
            font-size: 18px;
            font-family: 'Verdana', sans-serif;
            border: none;
            padding: 10px 20px;
            border-radius: 10px;
            cursor: pointer;
            transition: 0.3s ease;
        }}
        .stButton>button:hover {{
            background-color: #d14000;
        }}
        footer {{
            font-size: 14px;
            font-family: 'Arial', sans-serif;
            color: #bfbfbf;
            text-align: center;
            margin-top: 50px;
        }}
        footer a {{
            color: #00d4ff;
            text-decoration: none;
        }}
        footer a:hover {{
            text-decoration: underline;
        }}
    </style>
""", unsafe_allow_html=True)

# Header for the app
st.markdown("<h1 class='main-header'>🎥 Movie Recommender System</h1>", unsafe_allow_html=True)

# Dropdown for movie selection
selectvalue = st.selectbox("Select a movie from the dropdown", movies_list)

# Define the recommend function
def recommend(movie):
    if movie not in movies['title'].values:
        return ["Movie not found in the database"]  # Handle invalid input
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector: vector[1])
    recommend_movie = []
    for i in distances[1:6]:
        recommend_movie.append(movies.iloc[i[0]].title)
    return recommend_movie

# Show recommendations when button is clicked
if st.button("Show Recommendations"):
    selected_movie = selectvalue
    movie_name = recommend(selected_movie)

    # Display recommendations in a grid layout with styles
    if "Movie not found in the database" in movie_name:
        st.error("❌ Movie not found. Please try another movie name.")
    else:
        st.markdown("<div class='recommend-title'>🌟 Recommended Movies:</div>", unsafe_allow_html=True)
        
        # Create a stylish grid for movie recommendations
        cols = st.columns(5)  # Create 5 equally spaced columns
        for i, col in enumerate(cols):
            with col:
                col.markdown(f"<div class='movie-title'>{movie_name[i]}</div>", unsafe_allow_html=True)

# Footer with copyright and GitHub link
st.markdown("""
    <footer>
        &copy; 2024 <a href="https://github.com/akansh30" target="_blank">akansh30</a>
    </footer>
""", unsafe_allow_html=True)
