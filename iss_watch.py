import json
import time
import urllib.request
from pathlib import Path

BASE_DIR = Path(__file__).parent
LOG_FILE = BASE_DIR / "iss_watch.log"
ERR_FILE = BASE_DIR / "iss_watch_err.log"
ISS_API = "https://api.wheretheiss.at/v1/satellites/25544"
GEO_API = "https://api.bigdatacloud.net/data/reverse-geocode-client"

INTERVAL = 60


def fetch(url):
    with urllib.request.urlopen(url, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def describe_location(lat, lon):
    try:
        data = fetch(f"{GEO_API}?latitude={lat}&longitude={lon}&localityLanguage=en")
        city = data.get("locality") or data.get("city") or data.get("principalSubdivision")
        country = data.get("countryName")
        if city:
            return f"near {city}, {country}" if country else f"near {city}"
        return "over an ocean or remote area"
    except Exception:
        return "location lookup failed"


def utc_now():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())


def main():
    while True:
        try:
            iss = fetch(ISS_API)
            lat, lon = iss["latitude"], iss["longitude"]
            location = describe_location(lat, lon)
            line = f"{utc_now()} UTC | Lat: {lat:.4f} | Lon: {lon:.4f} | Location: {location}"
            print(line)
            with open(LOG_FILE, "a", encoding="utf-8") as f:
                f.write(line + "\n")
        except Exception as exc:
            with open(ERR_FILE, "a", encoding="utf-8") as f:
                f.write(f"{utc_now()} UTC | Error: {exc}\n")
        time.sleep(INTERVAL)


if __name__ == "__main__":
    main()
