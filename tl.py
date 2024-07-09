import streamlit as st

# Dummy data for hill stations, waterfalls, nearby hotels/resorts, and adventure activities
hill_stations = {
    'Mahabaleshwar': {
        'temperature': 28,
        'hotels': ['Hotel Dreamland', 'Le Meridien Mahabaleshwar', 'Brightland Resort'],
        'adventures': ['Trekking', 'Paragliding', 'Boating']
    },
    'Matheran': {
        'temperature': 27,
        'hotels': ['The Byke Heritage', 'Westend Hotel', 'Usha Ascot'],
        'adventures': ['Rappelling', 'Trekking', 'Horse Riding']
    },
    'Lonavala': {
        'temperature': 26,
        'hotels': ['Della Resorts', 'Fariyas Resort', 'Rhythm Lonavala'],
        'adventures': ['Camping', 'Trekking', 'Hot Air Balloon Ride']
    },
    'Panchgani': {
        'temperature': 25,
        'hotels': ['Ravine Hotel', 'Blue Country Resort', 'Hotel Millennium Park'],
        'adventures': ['Paragliding', 'Trekking', 'Camping']
    },
    'Bhandardara': {
        'temperature': 24,
        'hotels': ['Anandvan Resort', 'Yash Resort', 'MTDC Resort'],
        'adventures': ['Trekking', 'Boating', 'Camping']
    }
}

waterfalls = {
    'Vihigaon Waterfall': {
        'temperature': 26,
        'hotels': ['Hotel Sai', 'Hill Zill Resort', 'Silent Hills Resort'],
        'adventures': ['Rappelling', 'Swimming', 'Photography']
    },
    'Thoseghar Waterfall': {
        'temperature': 27,
        'hotels': ['Jeevan Village Resort', 'Hotel Saptashrungi', 'Wind Chalet Resort'],
        'adventures': ['Trekking', 'Bird Watching', 'Photography']
    },
    'Lingmala Waterfall': {
        'temperature': 25,
        'hotels': ['Evershine Resort', 'Regenta MPG Club', 'Bella Vista Resort'],
        'adventures': ['Trekking', 'Photography', 'Swimming']
    },
    'Dhobi Waterfall': {
        'temperature': 24,
        'hotels': ['Hotel Shreyas', 'Grand Resort', 'Ramsukh Resorts'],
        'adventures': ['Trekking', 'Photography', 'Bird Watching']
    },
    'Dugarwadi Waterfall': {
        'temperature': 28,
        'hotels': ['Sahyadri Guest House', 'Green Paradise Resort', 'Hirkani Garden Resort'],
        'adventures': ['Trekking', 'Swimming', 'Photography']
    }
}

# Streamlit app
st.title('Hill Stations and Waterfalls in Maharashtra with Temperature Below 30°C')

# Sidebar for user input
st.sidebar.header("Add Adventure Activities")
location_type = st.sidebar.selectbox("Select Type", ["Hill Station", "Waterfall"])
location = st.sidebar.selectbox("Select Location", list(hill_stations.keys()) if location_type == "Hill Station" else list(waterfalls.keys()))
adventure = st.sidebar.text_input("Adventure Activity")
add_adventure = st.sidebar.button("Add Adventure")

if add_adventure and adventure:
    if location_type == "Hill Station":
        hill_stations[location]['adventures'].append(adventure)
    else:
        waterfalls[location]['adventures'].append(adventure)

st.header('Hill Stations')
for hill_station, details in hill_stations.items():
    if details['temperature'] < 30:
        st.write(f"**{hill_station}**: {details['temperature']}°C")
        st.write("**Nearby Hotels/Resorts:**")
        for hotel in details['hotels']:
            st.write(f"- {hotel}")
        if details['adventures']:
            st.write("**Adventure Activities:**")
            for adv in details['adventures']:
                st.write(f"- {adv}")

st.header('Waterfalls')
for waterfall, details in waterfalls.items():
    if details['temperature'] < 30:
        st.write(f"**{waterfall}**: {details['temperature']}°C")
        st.write("**Nearby Hotels/Resorts:**")
        for hotel in details['hotels']:
            st.write(f"- {hotel}")
        if details['adventures']:
            st.write("**Adventure Activities:**")
            for adv in details['adventures']:
                st.write(f"- {adv}")
