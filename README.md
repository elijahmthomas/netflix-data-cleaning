# Netflix Data Analysis Dashboard

This project explores and transforms Netflix’s catalog data (up to 2021) using Python (`pandas`, `rapidfuzz`) for cleaning and Power BI for visualization.

---

## Dashboard Features

- Top movie-producing countries
- Distribution of movie durations (grouped into 30-minute bins)
- Most common genres (consolidated into 8 core categories)
- Production trends over time

> View the Power BI dashboard: `netflix-final.pbix`

---

## Tools & Technologies

- **Python** (Pandas, RapidFuzz) – for data cleaning, transformation, and fuzzy matching  
- **Power BI** – for interactive data visualization and Power Query

---

## Data Cleaning Steps

- Removed non-movie entries  
- Standardized column names and cleaned missing data  
- Used `RapidFuzz` to fix inconsistent country names (e.g., `"Unites States"` → `"United States"`)  
- Cleaned and grouped genres into 8 simplified categories  
- Removed rows with `'Unknown'` values (optional step)  
- Extracted and converted movie durations into minutes  
- Grouped durations into 30-minute bins  
- Added a `count` column for use in visualizations

---

## Summary

Cleaned Netflix data to focus on movies, fixed messy values like countries and genres, handled missing data, and prepared it for easy analysis and visualization.

## About Me

Hi, I'm Elijah Thomas — a data analyst with a background in finance and a passion for turning messy data into meaningful insights. I created this project to showcase my skills in Python data wrangling/cleaning and Power BI dashboard design.

I'm actively looking for data-focused roles where I can help teams make smarter decisions through clean, visual analytics.

Connect with me on [LinkedIn](https://www.linkedin.com/in/elijahmthomas) or email me directly at [emthomas519@gmail.com]
