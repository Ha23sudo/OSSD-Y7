import requests
from bs4 import BeautifulSoup
import csv


def get_car_data(manufacturer):

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": "https://google.com"
    }

    url = f'https://www.pakwheels.com/new-cars/pricelist/{manufacturer}'

    response = requests.get(url, headers=headers)

    cars = []

    if response.status_code == 200:

        soup = BeautifulSoup(response.text, 'html.parser')

        tables = soup.find_all('table')

        for table in tables:

            rows = table.find_all('tr')

            for row in rows:

                cols = row.find_all('td')

                if len(cols) >= 2:

                    name = cols[0].get_text().strip()
                    price = cols[1].get_text().strip()

                    print(f"Car Name: {name} - Price: {price}")

                    cars.append({
                        'name': name,
                        'price': price
                    })

    else:

        print("Page not available!")

    return cars


def save_to_csv(data, filename):

    with open(filename, mode='w', newline='', encoding='utf-8') as file:

        writer = csv.writer(file)

        writer.writerow(["Car Name", "Price"])

        for item in data:

            writer.writerow([item['name'], item['price']])

    print("Data saved successfully!")


manufacturer = input("Enter manufacturer name: ")

data = get_car_data(manufacturer)

save_to_csv(data, "cars.csv")