import requests
from bs4 import BeautifulSoup

# URL of the webpage to scrape
url = 'https://example.com'  # Replace this with the actual URL

# Send a GET request to fetch the webpage content
response = requests.get(url)

# Parse the content with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Extract the number of proposals
proposal_count = soup.find('span', class_='text-2xl text-neutral-800 md:text-3xl').get_text(strip=True)

# Extract the total tokens locked
total_tokens = soup.find_all('span', class_='text-2xl text-neutral-800 md:text-3xl')[1].get_text(strip=True)

# Extract additional label (e.g., Proposal, PUFFER)
proposal_label = soup.find('span', class_='text-xl text-neutral-500').get_text(strip=True)
tokens_label = soup.find_all('span', class_='text-xl text-neutral-500')[1].get_text(strip=True)

# Print the extracted data
print(f"Proposal Count: {proposal_count} {proposal_label}")
print(f"Total Tokens Locked: {total_tokens} {tokens_label}")
