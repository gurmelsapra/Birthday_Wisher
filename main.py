import smtplib
import random

PASSWORD = "ayqmkmpgisoodwt"
USERNAME = "gssapra007@gmail.com"

with open("quotes.txt", "r") as quote:

    RANDON_QUOTE= random.choice(quote.readlines())
    print(RANDON_QUOTE)


with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connect:
    connect.login(USERNAME, PASSWORD)
    connect.sendmail(from_addr=USERNAME, to_addrs="gurmelsingh.sapra@gmail.com", msg= f"Subject:Hello\n\n {RANDON_QUOTE}")

