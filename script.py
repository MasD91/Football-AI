import requests
from bs4 import BeautifulSoup

def get_football_results():
    url = 'https://www.espn.com/soccer/scoreboard/_/league/all'

    # Send a GET request to the website
    response = requests.get(url)

    if response.status_code == 200:
        # Parse HTML content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find football match results based on HTML structure
        match_results = soup.find_all('div', class_='scoreboard-container')

        for match in match_results:
            # Extract match details
            teams = match.find_all('span', class_='team-name')
            scores = match.find_all('span', class_='total')

            if len(teams) == 2 and len(scores) == 2:
                home_team = teams[0].text.strip()
                away_team = teams[1].text.strip()
                home_score = scores[0].text.strip()
                away_score = scores[1].text.strip()

                print(f"{home_team} {home_score} - {away_score} {away_team}")
    else:
        print("Failed to fetch data")

# Call the function to get football results
get_football_results()
