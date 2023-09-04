import requests
from faker import Faker
from bs4 import BeautifulSoup

def get_csrf_token(session, url):
    response = session.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    csrf_token = soup.find('input', {'name': 'csrfmiddlewaretoken'})['value']
    return csrf_token

def register_user(data):
    url = 'http://127.0.0.1:8000/reg/'  # Local registration URL
    with requests.session() as session:
        csrf_token = get_csrf_token(session, url)
        data['csrfmiddlewaretoken'] = csrf_token
        response = session.post(url, data=data)
        return response

def generate_sample_data(num_entries):
    fake = Faker()
    sample_data = []

    for _ in range(num_entries):
        data = {
            's_name': fake.name(),
            's_fathername': fake.name(),
            's_mothername': fake.name(),
            's_addr': fake.address(),
            'previous_school': fake.company(),
            's_phone': fake.phone_number(),
            's_gender': fake.random_element(['Male', 'Female']),
            's_class': fake.random_int(min=1, max=12),
        }
        sample_data.append(data)

    return sample_data

# Generate 10 sample entries
sample_data = generate_sample_data(20)

# Register users with the generated data
for data in sample_data:
    response = register_user(data)
    print(f"Registration Status: {response.status_code}, Response Text: {response.text}")
