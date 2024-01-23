# Movie Recommendation App 🎬🍿

Welcome to the Movie Recommendation App! This application suggests movies based on user input using a cosine similarity model. It's built with Streamlit, Pandas, and scikit-learn, providing a user-friendly and interactive experience.

## Features

- **Cosine Similarity Model:** Recommends movies by calculating the cosine similarity between movies.
- **User-Friendly Interface:** Built with Streamlit for a clean and intuitive user experience.
- **Robust Handling:** Deals gracefully with cases where the input movie is not found in the dataset.

## Project Structure

The project is organized as follows:

- `app.py`: The main script for the Streamlit app.
- `movies_dataset.csv`: Original dataset containing movie information.
- `preprocessed_movies_dataset.csv`: Preprocessed dataset with movie titles and release years.
- `cosine_similarity_model.joblib`: Saved model for cosine similarity.

## Getting Started

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/your-username/movie-recommendation-app.git
    ```

2. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Run the App:**

    ```bash
    streamlit run app.py
    ```

## Usage

1. Enter your favorite movie in the text input.
2. Click the "Get Recommendations" button to receive movie suggestions.

## Example

![Car Image](https://github.com/ayeshachohan/Car_Prediction_Regression_Model/assets/123968536/d9beb7ce-a67d-4b34-a2ac-1ac91effd7ac)


## Credits

- Developed by [Your Name]
- Dataset sourced from [Source Name/Link]
- Icons from [Icon Source/Link]

## License

Feel free to contribute, report issues, or provide suggestions!

