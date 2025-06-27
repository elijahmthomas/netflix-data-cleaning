import pandas as pd

# Load data
df = pd.read_csv('netflix_titles.csv')

# Clean column names
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# Fill missing values
for col in ['director', 'cast', 'country', 'date_added', 'rating', 'duration']:
    df[col] = df[col].fillna('Unknown')

# Filter to only movies
df['type'] = df['type'].str.strip().str.title()
df = df[df['type'] == 'Movie'].reset_index(drop=True)

# Extract runtime in minutes
df['duration_minutes'] = df['duration'].str.extract('(\d+)').astype(float)

# Create 30-minute bins
bins = range(0, int(df['duration_minutes'].max()) + 30, 30)
labels = [f'{i}-{i+29} min' for i in bins[:-1]]
df['movie_duration'] = pd.cut(df['duration_minutes'], bins=bins, labels=labels, right=False)

# Count number of movies in each runtime bin
duration_counts = df['movie_duration'].value_counts().sort_index()

# Display cleaned results
print("Movie Duration (Grouped by 30-Minute Ranges):\n")
print(duration_counts)

df.to_csv('netflix_cleaned.csv', index=False)