import smtplib
import random
import datetime as dt

with open("quotes.txt", "r") as q_file:
    data = q_file.readlines()
    random_quote = random.choice(data)

now = dt.datetime.now()
year = now.year
month = now.month
day = now.day

if(year == 2021, month == 10, day==8):
    my_email = "lazizbekfayziyev@gmail.com"
    my_password = "lazizjonsh97"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user = my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="laziz.fayziev@mail.ru",
            msg=f"subject:Hello Mr.Lazizbek\n\n {random_quote}"
        )











