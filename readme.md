# IMDb Movie Scraper

This project is a Python-based web scraper designed to fetch data from IMDb, including:

- Top 25 Movies
- Most Popular Movies
- Top Box Office Movies in the US
- Top TV Shows

The scraped data is saved in JSON files with timestamps, making it easy to track the latest data.

---

## Features

1. **Top 25 Movies**: Fetches the top 25 movies from IMDb's "Top 250" list.
2. **Most Popular Movies**: Fetches the most popular movies based on IMDb's "Most Popular Movies" chart.
3. **Top Box Office Movies in the US**: Retrieves the top-performing movies in the US box office.
4. **Top TV Shows**: Fetches the top-rated TV shows on IMDb.

Each dataset is stored in a timestamped JSON file for future reference.

---

## Technologies Used

- **Python**: Core programming language.
- **Requests**: For making HTTP requests to IMDb.
- **Beautiful Soup**: For parsing and extracting HTML data.
- **dotenv**: To manage environment variables securely.
- **JSON**: For storing the scraped data in a structured format.

---

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/imdb-movie-scraper.git
   cd imdb-movie-scraper

2. Create a virtual environment:
    ```bash
    python -m venv env
    source env/bin/activate   # On Windows, use `env\Scripts\activate`

3. Install the dependencies
    ```bash
    pip install

4. Create a .env file in the project root and configure it as follows:
    ```bash
    proxy_token=your-token-here
    proxy_module_url=http://{}:@proxy.scrape.do:8080

5. Run the Scraper:
    ```bash
    python main.py


## Output

- The script generates JSON files for each dataset. The file names include timestamps in the format dd-mm-yy. For eg:
    - top_25_movies_22-12-2024.json
    - Most_Popular_Movies22-12-2024.json
    - Top_Box_Office_US_22-12-2024.json
    - Top_TV_Shows_22-12-2024.json

## Program Structure
    ```bash
    imdb-movie-scraper/
    ├── main.py             # Main script for scraping IMDb data
    ├── requirements.txt    # List of required Python libraries
    ├── .env                # Environment variables (not tracked by Git)
    ├── .gitignore          # Ignore sensitive files like .env
    ├── output/             # Directory for storing JSON output files


## Notes
- Ensure you replace your-proxy-token-here in .env with your actual proxy token.
- The scraper uses a proxy service for better acces to IMDb data. If the proxy details change, update the .env file accordingly.

## Disclaimer
- This project is for educational purposes only. Please respect IMDb's Terms of Use when using this scraper. Excessive or unauthorized scraping may lead to IP bans or legal actions.