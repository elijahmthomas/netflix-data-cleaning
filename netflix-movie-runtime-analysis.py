# 1. Import Libraries
import pandas as pd
from rapidfuzz import process

# 2. Load Data
df = pd.read_csv('netflix_titles.csv')

# 3. Initial Cleaning
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
for col in ['director', 'cast', 'country', 'date_added', 'rating', 'duration']:
    df[col] = df[col].fillna('Unknown')
df['type'] = df['type'].str.strip().str.title()

# 4. Filter to Only Movies
df = df[df['type'] == 'Movie'].reset_index(drop=True)

# 5. Advanced Cleaning: Standardize Country Names with RapidFuzz
# Format the country column first
df['country'] = (
    df['country']
    .astype(str)
    .str.strip()               # Removes leading/trailing spaces
    .str.rstrip(',')           # Removes trailing commas
    .str.title()               # Fixes case: "united states" → "United States"
)

# Define your known clean list
correct_countries = ['United States', 'India', 'United Kingdom', 'France', 'Canada',
                     'Japan', 'Germany', 'Australia', 'Mexico', 'Spain', 'Unknown']

# Function to match fuzzy names to correct values
def fix_country_name(name):
    if name == 'Unknown':
        return name
    match, score, _ = process.extractOne(name, correct_countries)
    return match if score > 85 else name

df['country'] = df['country'].apply(fix_country_name)

# 5.5 Clean 'listed_in' Genres into 10 Fixed Categories

# Define exact mapping from Netflix genre phrases to your 10 categories
genre_map = {
    'Action': ['Action', 'Action & Adventure', 'Martial Arts Movies'],
    'Comedy': ['Comedies', 'Stand-Up Comedy'],
    'Drama': ['Dramas'],
    'Fantasy': ['Fantasy'],
    'Horror': ['Horror Movies'],
    'Sci-fi': ['Sci-Fi & Fantasy', 'Science Fiction'],
    'Thriller': ['Thrillers', 'Crime TV Shows'],
    'Western': ['Western'],
    'Romantic comedy': ['Romantic Comedies'],
    'Romantic drama': ['Romantic Movies', 'Romantic Dramas']
}

# Define fixed set of 10 allowed genres
allowed_genres = set(genre_map.keys())

# Function to map raw Netflix 'listed_in' strings to your fixed categories
def map_strict_genres(listed_str):
    if pd.isna(listed_str):
        return ['Other']
    listed_genres = [g.strip() for g in listed_str.split(',')]
    matched = set()
    for broad_genre, keywords in genre_map.items():
        for kw in keywords:
            if any(kw in genre for genre in listed_genres):
                matched.add(broad_genre)
    return list(matched) if matched else ['Other']

# Apply to dataset
df['broad_genres'] = df['listed_in'].apply(map_strict_genres)

df = df[~df.apply(lambda row: row.astype(str).str.contains('Unknown')).any(axis=1)]

# 6. Clean Duration & Convert to Minutes
df['duration_minutes'] = df['duration'].str.extract(r'(\d+)').astype(float)

# 7. Group by 30-Minute Bins
bins = range(0, int(df['duration_minutes'].max()) + 30, 30)
labels = [f'{i}-{i+29} min' for i in bins[:-1]]
df['duration_bin'] = pd.cut(df['duration_minutes'], bins=bins, labels=labels, right=False)

# 8. Count and Export Cleaned Data
df['count'] = 1
df.to_csv('netflix_cleaned.csv', index=False)

# 9. Output Summary (Optional)
duration_counts = df['duration_bin'].value_counts().sort_index()
print("🎬 Movie Duration Distribution (Grouped by 30-Minute Ranges):\n")
print(duration_counts)