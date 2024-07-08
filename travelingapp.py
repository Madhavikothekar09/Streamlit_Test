import streamlit as st
import pandas as pd

# Sample data
destinations = {
    'City': ['Paris', 'New York', 'Tokyo', 'Sydney', 'Cape Town'],
    'Country': ['France', 'USA', 'Japan', 'Australia', 'South Africa'],
    'Continent': ['Europe', 'North America', 'Asia', 'Australia', 'Africa'],
    'Average Temperature': [15, 12, 16, 20, 17],
    'Activities': ['Museums, Sightseeing', 'Shopping, Broadway', 'Anime, Technology', 'Beaches, Opera House', 'Safari, Beaches']
}

df = pd.DataFrame(destinations)

st.title('Traveling App')

st.sidebar.header('User Input Features')

# User input: select continent
continent = st.sidebar.selectbox('Select a continent', df['Continent'].unique())

# User input: select temperature range
temperature = st.sidebar.slider('Select preferred average temperature', min_value=0, max_value=30, value=(10, 20))

# Filter data based on user input
filtered_df = df[(df['Continent'] == continent) & 
                 (df['Average Temperature'] >= temperature[0]) & 
                 (df['Average Temperature'] <= temperature[1])]

st.header('Suggested Destinations')

if not filtered_df.empty:
    for index, row in filtered_df.iterrows():
        st.subheader(f"{row['City']}, {row['Country']}")
        st.write(f"Continent: {row['Continent']}")
        st.write(f"Average Temperature: {row['Average Temperature']}°C")
        st.write(f"Activities: {row['Activities']}")
else:
    st.write('No destinations match your criteria.')

if st.sidebar.button('Show all destinations'):
    st.header('All Destinations')
    st.table(df)

st.sidebar.markdown('---')
st.sidebar.header('About')
st.sidebar.info('This is a simple traveling app created using Streamlit.')
