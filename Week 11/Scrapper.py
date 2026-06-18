import requests
from bs4 import BeautifulSoup
import csv

def get_car_data(car):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": "https://google.com"
    }
    url = f'https://www.pakwheels.com/new-cars/pricelist/{car}'

    response = requests.get(url, headers=headers)
    car_data = [] # List to store scraped data
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        tables = soup.find_all('table')
        
        for table in tables:
            rows = table.find_all('tr')
            for row in rows:
                cols = row.find_all('td')
                if len(cols) >= 2:
                    name = cols[0].get_text(strip=True)
                    price = cols[1].get_text(strip=True)
                    print(f"Car Name: {name} - Price: {price}")
                    car_data.append([name, price])
    else:
        print("Page not available!")
        
    return car_data



# Function to save data in a csv file
def save_to_csv(data, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Car Name", "Price"])
        for row in data:
            writer.writerow(row)
    print("Data saved successfully in", filename)





# Main execution block
if __name__ == "__main__":
    #Cae name e.g., 'suzuki', 'toyota', 'honda'
    car_name = input("Enter manufacturer name (e.g. suzuki): ")
    
    # Function call and get data
    scraped_data = get_car_data(car_name)
    

    if scraped_data:
        save_to_csv(scraped_data, "cars.csv")