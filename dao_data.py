from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/get-puffer-data', methods=['GET'])
def get_puffer_data():
    # Fetch the webpage
    response = requests.get('https://puffer-dao.vercel.app/')

    # Check if the page was retrieved successfully
    if response.status_code != 200:
        return jsonify({"error": "Failed to retrieve data from the website."}), 500

    # Parse the HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    try:
        # Extract proposal count
        proposal_count_element = soup.find('span', class_='text-2xl text-neutral-800 md:text-3xl')
        proposal_count = proposal_count_element.get_text(strip=True) if proposal_count_element else "N/A"
        
        # Extract total tokens locked
        total_tokens_locked_element = soup.find_all('span', class_='text-2xl text-neutral-800 md:text-3xl')[1]
        total_tokens_locked = total_tokens_locked_element.get_text(strip=True) if total_tokens_locked_element else "N/A"
        
        # Extract labels for proposal and tokens
        proposal_label_element = soup.find('span', class_='text-xl text-neutral-500')
        proposal_label = proposal_label_element.get_text(strip=True) if proposal_label_element else "N/A"

        tokens_label_element = soup.find_all('span', class_='text-xl text-neutral-500')[1]
        tokens_label = tokens_label_element.get_text(strip=True) if tokens_label_element else "N/A"

        # Return the scraped data with field names
        data = {
            "Puffer_Proposal_Count": f"{proposal_count} {proposal_label}",
            "Puffer_Total_Tokens_Locked": f"{total_tokens_locked} {tokens_label}"
        }

        return jsonify(data), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
