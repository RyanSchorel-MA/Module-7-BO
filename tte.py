import random
import json
import requests

def generate_mock_data():
    mock_data = []
    for _ in range(500):
        photo_url = get_random_shibe_photo()
        user = get_random_user()
        date = get_random_date()
        
        mock_data.append({
            'photo': photo_url,
            'user': user,
            'date': date
        })
    
    return mock_data

def get_random_shibe_photo():
    response = requests.get('http://shibe.online/api/shibes?count=1&urls=true&httpsUrls=true')
    photo_urls = response.json()
    return photo_urls[0]

def get_random_user():
    users = ['John', 'Jane', 'Alice', 'Bob', 'Mike']
    return random.choice(users)

def get_random_date():
    year = random.randint(2000, 2022)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    return f'{year}-{month:02d}-{day:02d}'

mock_data = generate_mock_data()

# Save the mock data to a JSON file
with open('mock_data.json', 'w') as f:
    json.dump(mock_data, f, indent=4)
