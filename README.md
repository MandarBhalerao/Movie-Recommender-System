
# Movie Recommendation System

This project is an end-to-end content-based movie recommendation system, built using Python and the Streamlit framework. It uses cosine similarity to analyze the similarities among 5000 movies and provides personalized recommendations based on user input.

## Features

- **End-to-End Machine Learning Pipeline**: 
  - Developed a complete machine learning system that processes movie data from [Kaggle](https://www.kaggle.com/), builds a recommendation model, and presents results to the user.
  
- **Content-Based Recommendation**:
  - Used cosine similarity to analyze the textual descriptions and features of 5000 movies to provide recommendations based on user preferences.

- **Real-Time Deployment**:
  - Successfully deployed the application on the Streamlit Community Cloud, allowing users to interact with the system in real time and receive personalized movie recommendations.

## Watch Live

You can access the live version of the Movie Recommendation System [here](https://mandar-movie-recommender-system.streamlit.app/).

## Setup and Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/MandarBhalerao/Movie-Recommender-System.git
    cd Movie-Recommender-System
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the Streamlit app locally:
    ```bash
    streamlit run app.py
    ```

## Technologies Used

- **Python**: Core programming language.
- **Streamlit**: For building and deploying the interactive dashboard.
- **Pandas & NumPy**: For data manipulation and preprocessing.
- **Scikit-learn**: For implementing the cosine similarity algorithm.

## Future Improvements

- Expand the dataset to include more movies.
- Incorporate user feedback to enhance recommendation accuracy.
- Add filtering options based on genres, ratings, and release year.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
