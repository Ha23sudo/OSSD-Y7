import requests
from bs4 import BeautifulSoup
import csv


def get_car_data(manufacturer):

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept-Language": "en-US,en;q=0.9"
    }

    url = f"https://www.pakwheels.com/new-cars/pricelist/{manufacturer}"

    cars = []

    try:
        response = requests.get(url, headers=headers, timeout=10)

        if response.status_code != 200:
            print("Page not found!")
            return cars

        soup = BeautifulSoup(response.text, "html.parser")

        tables = soup.find_all("table")

        if not tables:
            print("No tables found on page.")
            return cars

        for table in tables:

            rows = table.find_all("tr")

            for row in rows:

                cols = row.find_all("td")

                if len(cols) >= 2:

                    name = cols[0].get_text(strip=True)
                    price = cols[1].get_text(strip=True)

                    if name and price:

                        print(f"Car Name: {name}")
                        print(f"Price: {price}")
                        print("-" * 40)

                        cars.append({
                            "name": name,
                            "price": price
                        })

    except requests.exceptions.RequestException as e:
        print("Request Error:", e)

    return cars


def save_to_csv(data, filename):

    if not data:
        print("No data available to save.")
        return

    try:
        with open(filename, "w", newline="", encoding="utf-8") as file:

            writer = csv.writer(file)

            writer.writerow(["Car Name", "Price"])

            for item in data:

                writer.writerow([
                    item["name"],
                    item["price"]
                ])

        print(f"\nData saved successfully in {filename}")

    except Exception as e:
        print("Error saving CSV:", e)


def main():

    print("===== PakWheels Car Scraper =====")

    manufacturer = input(
        "Enter manufacturer (toyota, honda, suzuki, kia): "
    ).lower().strip()

    data = get_car_data(manufacturer)

    if data:
        save_to_csv(data, f"{manufacturer}_cars.csv")
    else:
        print("No car data found.")


if __name__ == "__main__":
    main()