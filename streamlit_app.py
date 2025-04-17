import streamlit as st
from PIL import Image

# Dummy game data
games = [
    {
        "title": "Elden Ring",
        "genre": ["RPG", "Action"],
        "platform": ["PC", "PS5", "Xbox"],
        "image": "https://upload.wikimedia.org/wikipedia/en/b/b9/Elden_Ring_Box_art.jpg",
        "description": "An epic dark fantasy action RPG from FromSoftware."
    },
    {
        "title": "Hades",
        "genre": ["Roguelike", "Indie"],
        "platform": ["PC", "Switch", "PS5"],
        "image": "https://upload.wikimedia.org/wikipedia/en/e/e0/Hades_cover_art.jpg",
        "description": "A fast-paced rogue-like dungeon crawler from Supergiant Games."
    },
    {
        "title": "Stardew Valley",
        "genre": ["Simulation", "Casual"],
        "platform": ["PC", "Switch", "Mobile"],
        "image": "https://upload.wikimedia.org/wikipedia/en/1/1f/Stardew_Valley_cover_art.png",
        "description": "A charming farming simulator with RPG elements."
    }
]

# Sidebar for user input
st.sidebar.title("🎮 Game Preferences")
selected_genres = st.sidebar.multiselect(
    "Select Genre(s):", ["RPG", "Action", "Roguelike", "Indie", "Simulation", "Casual"]
)
selected_platforms = st.sidebar.multiselect(
    "Select Platform(s):", ["PC", "PS5", "Xbox", "Switch", "Mobile"]
)

st.title("🔥 PlayNext")
st.markdown("Discover games based on your preferences.")

# Filter games
def filter_games(games, genres, platforms):
    return [
        game for game in games
        if (not genres or any(g in game['genre'] for g in genres)) and
           (not platforms or any(p in game['platform'] for p in platforms))
    ]

filtered_games = filter_games(games, selected_genres, selected_platforms)

# Display recommended games
if filtered_games:
    for game in filtered_games:
        st.image(game["image"], width=150)
        st.subheader(game["title"])
        st.caption(", ".join(game["genre"]) + " | " + ", ".join(game["platform"]))
        st.write(game["description"])
        st.markdown("---")
else:
    st.warning("No games match your filters. Try adjusting them in the sidebar.")
