import requests


def get_public_ip():
    response = requests.get("https://api.ipify.org/?format=json")
    return response.json()["ip"]


def get_geo_info(ip):
    response = requests.get(f"https://ipinfo.io/{ip}/geo")
    data = response.json()
    loc = data["loc"].split(",")
    lat, long = float(loc[0]), float(loc[1])
    city = data.get("city", "Unknown")
    country = data.get("country", "Unknown")
    return country, city, lat, long


def main():
    ip_public = get_public_ip()
    country, city, lat, long = get_geo_info(ip_public)
    print(f"IP Public: {ip_public}")
    print(f"Country: {country}, City: {city}, Latitude: {lat}, Longitude: {long}")


if __name__ == "__main__":
    main()
