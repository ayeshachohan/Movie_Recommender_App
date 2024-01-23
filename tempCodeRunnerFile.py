import pandas as pd
import streamlit as st
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics.pairwise import cosine_similarity
import joblib  # Import joblib for model persistence

# Load dataset
df = pd.read_csv("preprocessed_movies_dataset.csv")

# Custom label encoder that gracefully handles unseen labels
class SafeLabelEncoder(LabelEncoder):
    def fit_transform(self, y):
        try:
            return super().fit_transform(y)
        except ValueError:
            unseen_labels = list(set(y) - set(self.classes_))
            self.classes_ = sorted(self.classes_.tolist() + unseen_labels)
            return super().transform(y)

# Label encode movie titles using the custom encoder
label_encoder = SafeLabelEncoder()
df['Title_encoded'] = label_encoder.fit_transform(df['title'])

# Create a user-movie matrix
user_movie_matrix = df.set_index('Title_encoded').drop(columns=['title', 'Released Year'])

# Save the model
cosine_sim = cosine_similarity(user_movie_matrix, user_movie_matrix)
cosine_sim_df = pd.DataFrame(cosine_sim, index=user_movie_matrix.index, columns=user_movie_matrix.index)
joblib.dump(cosine_sim_df, 'cosine_similarity_model.joblib')

# Function to load the model and get movie recommendations
def get_movie_recommendations_with_loaded_model(input_movie):
    # Load the model
    loaded_model = joblib.load('cosine_similarity_model.joblib')

    # Preprocess input movie
    input_movie_cleaned = input_movie.strip()  # Remove leading/trailing whitespaces

    # Check if the input movie is in the dataset
    if input_movie_cleaned not in df['title'].values:
        st.warning(f"Movie '{input_movie_cleaned}' not found in the dataset. Please try another movie.")
        return None

    # Get movie recommendations using the loaded model
    input_movie_encoded = label_encoder.transform([input_movie_cleaned])
    movie_index = df[df['title'] == input_movie_cleaned]['Title_encoded'].iloc[0]
    similar_movies = loaded_model[movie_index].sort_values(ascending=False)

    # Check if there are recommendations available
    if len(similar_movies) > 1:
        recommendations = similar_movies.index[1:4]  # Get top 3 recommendations (excluding the input movie itself)
        recommended_movies_df = df[df['Title_encoded'].isin(recommendations)][['title', 'Released Year']]
        return recommended_movies_df
    else:
        st.warning(f"Sorry, no recommendations found for '{input_movie_cleaned}'. Please try another movie.")
        return None

# Streamlit App
st.set_page_config(page_title="Movie Recommendation App", page_icon="🎬")
st.title("Movie Recommendation App 🍿")

# User input for the movie title
input_movie_to_recommend = st.text_input("Enter your favorite movie:")

# Button to get recommendations
if st.button("Get Recommendations"):
    if input_movie_to_recommend:
        recommended_movies_df = get_movie_recommendations_with_loaded_model(input_movie_to_recommend)

        # Display recommendations in a colorful card layout
        if recommended_movies_df is not None and not recommended_movies_df.empty:
            st.subheader(f"🌟 Recommended movies for '{input_movie_to_recommend}':")
            for idx, (movie, year) in enumerate(recommended_movies_df.values, start=1):
                st.success(f"{idx}. {movie} ({year}) 🎥")
        else:
            st.warning(f"Sorry, no recommendations found for '{input_movie_to_recommend}'. Please try another movie.")
    else:
        st.warning("Please enter a movie title first.")
