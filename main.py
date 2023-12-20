import requests
import selectorlib
import smtplib
import ssl
import os
import time
import sqlite3


URL = "https://programmer100.pythonanywhere.com/tours/"
connection = sqlite3.connect("data.db")


class Event:
    def scrape(self, url):
        """Scrape the page source from url"""
        response = requests.get(url)
        source = response.text
        return source

    def extract(self, source):
        extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
        value = extractor.extract(source)["tours"]
        return value


class Email:
    def send(self, message):
        host = "smtp.gmail.com"
        port = 465

        username = "timep2199@gmail.com"
        password = "oaxefxldwryllhep"

        receiver = "timep2199@gmail.com"
        context = ssl.create_default_context()

        with smtplib.SMTP_SSL(host, port, context=context) as server:
            server.login(username, password)
            server.sendmail(username, receiver, message)


def store(extracted):
    row = extracted.split(",")
    row = [item.strip() for item in row]
    cursor = connection.cursor()
    cursor.execute("INSERT INTO events VALUES(?,?,?)", row)
    connection.commit()


def read(extracts):
    row = extracted.split(",")
    row = [item.strip() for item in row]
    band, city, date = row
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM events WHERE band=? AND city=? AND date=?", (band, city, date))
    rows = cursor.fetchall() #fetchall returns list of string when used with exceute and returns list of tuple when used with executeany
    print(rows)
    return rows


if __name__ == '__main__':
    while True:
        event = Event()
        scraped = event.scrape(URL)
        extracted = event.extract(scraped)
        print(extracted)

        if extracted != "No upcoming tours":
            row = read(extracted)
            if not row:
                store(extracted)
                email = Email()
                email.send(message="New event Found!")
        time.sleep(2)