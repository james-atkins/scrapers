import json
import pathlib

import cloudscraper

DATA_DIR = pathlib.Path("data")

WHERE = "worldwide"
SINCE = "last_6_hours"

APIS = [
    ("trending", "domain-ranking?trending=true&"),
    ("popular", "domain-ranking?trending=true&"),

    ("ddosattackchangerange", "netrep/ddos/ddosattackchangerange"),
    ("ddosattackbreakdownpercentscalar", "netrep/ddos/ddosattackbreakdownpercentscalar"),

    ("botvshumanpercentrange", "netrep/http/botvshumanpercentrange"),
    ("botvshumanpercentscalar", "netrep/http/botvshumanpercentscalar"),

    ("browserrankscalar", "netrep/http/browserrankscalar"),

    ("httpprotocolpercentrange", "netrep/http/httpprotocolpercentrange"),
    ("httpprotocolpercentscalar", "netrep/http/httpprotocolpercentscalar"),

    ("httpvshttpspercentrange", "netrep/http/httpvshttpspercentrange"),
    ("httpvshttpspercentscalar", "netrep/http/httpvshttpspercentscalar"),

    ("ipv4vsipv6percentrange", "netrep/http/ipv4vsipv6percentrange"),
    ("ipv4vsipv6percentscalar", "netrep/http/ipv4vsipv6percentscalar"),

    ("layer7attackbreakdownpercentscalar", "netrep/http/layer7attackbreakdownpercentscalar"),
    ("layer7attackchangerange", "netrep/http/layer7attackchangerange"),

    ("mobilevsdesktoppercentrange", "netrep/http/mobilevsdesktoppercentrange"),
    ("mobilevsdesktoppercentscalar", "netrep/http/mobilevsdesktoppercentscalar"),

    ("netflowchangerange", "netrep/http/netflowchangerange"),

    ("tlsprotocolpercentrange", "netrep/http/tlsprotocolpercentrange"),
    ("tlsprotocolpercentscalar", "netrep/http/tlsprotocolpercentscalar"),    
]


if __name__ == "__main__":
    with cloudscraper.create_scraper() as scraper:
        # Go to homepage first
        scraper.get(f"https://radar.cloudflare.com/?date_filter={SINCE}")

        for api, api_url_part in APIS:
            print(f"Scraping {api}.")
            r = scraper.get(f"https://radar.cloudflare.com/api/{api_url_part}?location_token={WHERE}&date_token={SINCE}")
            data = r.json()

            with open(DATA_DIR / f"{api}_{WHERE}_{SINCE}.json", "w", newline="\n", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
