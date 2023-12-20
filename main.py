import requests
import selectorlib
import smtplib
import ssl
import os
import time


URL = "https://programmer100.pythonanywhere.com/tours/"


def scrape(url):
    """Scrape the page source from url"""
    response = requests.get(url)
    source = response.text
    return source


def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)["tours"]
    return value


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "timep2199@gmail.com"
    password = "oaxefxldwryllhep"

    receiver = "timep2199@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)


def store(extractor):
    with open("data.txt", "a") as file:
        file.write(extractor + "\n")


def read(extracts):
    with open("data.txt", "r") as file:
        return file.read()


if __name__ == '__main__':
    while True:
        scraped = scrape(URL)
        extracted = extract(scraped)
        print(extracted)

        content = read(extracted)
        if extracted != "No upcoming tours":
            if extracted not in content:
                store(extracted)
                send_email(message="New event Found!")
        time.sleep(2)