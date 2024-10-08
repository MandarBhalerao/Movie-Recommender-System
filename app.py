import streamlit as st
import pickle
import pandas as pd
import requests

@st.cache_data
def download_and_load_pickle(url):
    """
    Download a pickle file from a direct Google Drive link and load it into memory.
    
    Args:
    url (str): Direct download URL for the Google Drive file.
    
    Returns:
    object: The object loaded from the pickle file.
    """
    # Send a GET request to the URL
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        # Load the content of the file into a Python object
        return pickle.loads(response.content)
    else:
        print("Failed to download the file.")
        return None


# Function to download and load data (parquet file) from a Google Drive link
@st.cache_data  # Cache the function output to avoid re-downloading
def load_data(url):
    """
    Load data from a direct Google Drive download link.
    
    Args:
    url (str): Direct download URL for the Google Drive file.
    
    Returns:
    DataFrame or None: Loaded data as a pandas DataFrame, or None if an error occurs.
    """
    r = requests.get(url, allow_redirects=True)
    if r.status_code == 200:
        # Write the content to a .parquet file
        with open('new_similarity.parquet', 'wb') as f:
            f.write(r.content)
        # Load the .parquet file into a DataFrame
        return pd.read_parquet('new_similarity.parquet')
    else:
        print("Failed to download the file.")
        return None

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(
        movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path


def recommend(movie):
    # explained in jupyter notebook
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]

    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]  # explained below

    recommended_movies = []
    recommended_movies_posters = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id

        recommended_movies.append(movies.iloc[i[0]].title)

        # fetch poster from API
        recommended_movies_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_movies_posters


# Construct the direct download URL using the file ID from Google Drive
file_id = "1tRu4UXhsFR5noyT8wpvKitQnEZsDkIjA"
direct_url = f"https://drive.google.com/uc?export=download&id={file_id}"

# Download and load the data using the above function
movies_dict = download_and_load_pickle(direct_url)


# movies_dict = pickle.load(open('new_movie_dict.pkl', 'rb'))
# rb means read binary mode

movies = pd.DataFrame(movies_dict)
# converting the dictionary to dataframe


# Construct the direct download URL using the file ID from Google Drive
file_id = "1qHP8bzIiYve-z9KdFf43L-_zQ6UUWeJ-"
direct_url = f"https://drive.google.com/uc?export=download&id={file_id}"

# Load the data using the above function
similarity = load_data(direct_url)

# similarity = load_similarity('new_similarity.parquet')

# similarity = pickle.load(open('new_similarity.pkl', 'rb'))
# similarity = pd.read_parquet('new_similarity.parquet')

# for title
# st.title('Movie Recommender System')

# st.set_page_config(page_title="Movie Recommender System", page_icon="logo.jpeg", layout="centered")
st.image("logo2.jpg", caption="Created by Mandar Bhalerao", use_column_width=True)
# st.header('Movie Recommender System')


# making a select box
selected_movie_name = st.selectbox(
    'Type or select a movie from the dropdown',

    # passing the title of all movies in the selected_movie_name select box
    movies['title'].values)

st.write('You selected:', selected_movie_name)

# making a button Recommend
if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])
