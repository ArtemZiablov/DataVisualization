# **Data Visualization Project**

This project visualizes student data using an interactive map and statistical charts, with processed data stored in various formats and enhanced by custom scripts.

## Deployed to GitHub pages
https://artemziablov.github.io/DataVisualization/

---

## **Data Storage and Structure**

### 1. **CSV File (`final.csv`):**
- **Purpose:** Stores core information about students, including personal details and geographical coordinates.
- **Fields:**
  - `gender`: Student's gender.
  - `name.title`, `name.first`, `name.last`: Full name of the student.
  - `email`: Email address.
  - `dob.date`: Date of birth.
  - `city`: Student's city of residence.
  - `code`: Country code (ISO).
  - `timezone`: City's timezone.
  - `lat`, `lon`: Latitude and longitude for map visualization.
  - `avatar`: Identifier linking a student record to their avatar.

### 2. **ZIP File (`avatars.zip`):**
- **Purpose:** Contains PNG avatars of students for display on the interactive map.
- **Details:**
  - Files are named to match the `avatar` field in the CSV file for easy linking.

### 3. **Extracted Avatars (`extracted_avatars/`):**
- Avatars are extracted from the ZIP archive and stored in this directory.
- Each image is encoded in Base64 for embedding into the map's HTML file.

### 4. **Visualization Outputs:**
- **Interactive Map (`europe_map.html`):**
  - Displays student locations as markers.
  - Each marker contains student details: name, city, country, timezone, and avatar.
- **Charts:**
  - Show the distribution of students by countries and cities (top 20 cities).

---

## **Scripts Used**

### 1. **Script 1:** Processes data for Ukrainian students.
- Formats date of birth into `MM/DD/YYYY`.
- Adds avatars (first letter of the first name).
- Assigns the country code `UA` and timezone `Europe/Kyiv`.
- Filters Ukrainian cities with populations over 40,000 and assigns cities to students proportionally based on population.
- Adds city names and coordinates, saving results to `download_ua.csv`.

### 2. **Script 2:** Filters and analyzes European cities.
- Loads city data and filters cities with populations over 50,000 in European countries.
- Assigns unique identifiers to cities.
- Analyzes selected cities, checking for duplicates and population counts, and outputs results to the console.

### 3. **Script 3:** Enhances student data with geographical information.
- Removes the time portion from the date of birth.
- Converts gender to short forms (`M` and `F`).
- Adds avatars (first letter of the first name).
- Assigns cities from a filtered dataset, adding city names, coordinates, country codes, populations, and timezones.
- Saves the final processed data to `final.csv`.

### 4. **Script 4:** Generates avatar images.
- Creates PNG images for each letter of the English alphabet.
- Each image has a random background color with a white letter centered.
- Saves the images as files named by their respective letters (`A.png`, `B.png`, etc.). 

---

## **Technologies Used**
- **Python:** For data processing and visualization (using `pandas`, `folium`, `matplotlib`).
- **HTML:** For creating the interactive map.
- **GitHub Pages:** For hosting the project.
