import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=2176f4eaf732e68041029dab0682c47e'.format(movie_id))
    data = response.json()
    print(data)
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

st.title('Movie Recommendation System')
movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl','rb'))

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:21]
    recommended_movies = []
    recommended_movie_posters = []
    for i in movies_list:
        movie_id  = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        # fetch poster from API
        recommended_movie_posters.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movie_posters



selected_movie_name = st.selectbox(
'Type or select a movie from the dropdown',
movies['title'].values)


if st.button('Recommend'):
    names,posters = recommend(selected_movie_name)

    # Define the number of movies to display per row
    movies_per_row = 5

    # Calculate the number of rows
    num_rows = len(posters) // movies_per_row + (len(posters) % movies_per_row > 0)

    # Loop through each row
    for row in range(num_rows):
        # Create a new row in the layout
        st.write(f"### Row {row + 1}")
        columns = st.beta_columns(movies_per_row)

        # Loop through each movie in the current row
        for col in range(movies_per_row):
            # Calculate the index of the current movie
            index = row * movies_per_row + col

            # Check if the index is within the range of the posters array
            if index < len(posters):
                # Display the movie image and name
                st.image(posters[index], caption=names[index], width=200)
                st.text(names[index])

    #col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11, col12, col13, col14, col15, col16, col17, col18, col19, col20 = st.columns(20)
    #with col1:
        st.text(names[0])
        st.image(posters[0])
    #with col2:
        st.text(names[1])
        st.image(posters[1])
    #with col3:
        st.text(names[2])
        st.image(posters[2])
    #with col4:
        st.text(names[3])
        st.image(posters[3])
    #with col5:
        st.text(names[4])
        st.image(posters[4])
    #with col6:
        st.text(names[5])
        st.image(posters[5])
    with col7:
        st.text(names[6])
        st.image(posters[6])
    with col8:
            st.text(names[7])
            st.image(posters[7])
    with col9:
        st.text(names[8])
        st.image(posters[8])
    with col10:
        st.text(names[9])
        st.image(posters[9])
    with col11:
        st.text(names[10])
        st.image(posters[10])
    with col12:
        st.text(names[11])
        st.image(posters[11])
    with col13:
        st.text(names[12])
        st.image(posters[12])
    with col14:
        st.text(names[13])
        st.image(posters[13])
    with col15:
        st.text(names[14])
        st.image(posters[14])
    with col16:
        st.text(names[15])
        st.image(posters[15])
    with col17:
        st.text(names[16])
        st.image(posters[16])
    with col18:
        st.text(names[17])
        st.image(posters[17])
    with col19:
        st.text(names[18])
        st.image(posters[18])
    with col20:
        st.text(names[19])
        st.image(posters[19])
    for i in recommend(selected_movie_name):
         st.write(i)


















