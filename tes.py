# pip install zenrows
from zenrows import ZenRowsClient
from twilio.rest import Client
import time
from data import credentials
client = ZenRowsClient(credentials["zenid"])

account_sid = credentials["account_sid"]
auth_token = credentials["auth_token"]
phone_No=credentials["phone_No"]
numberSID=credentials["numberSID"]

url = "https://in.bookmyshow.com/sports/india-vs-australia-icc-mens-cwc-2023/ET00367551"


def Call_buddy(delay):
    try:
        time.sleep(delay)
        client = Client(account_sid, auth_token)
        call = client.calls.create(
                                url='http://demo.twilio.com/docs/voice.xml',
                                to='+ 918072515664',
                                from_=phone_No
                            )
        print(call.sid)
    except Exception as df:
        print(df)


def The_Main():
    while True:
        time.sleep(10)
        try:
            response = client.get(url)
            rep=response.text
            if response.status_code == 200 :
                if "coming-soon-button"  in rep:
                    print("Booking not yet open")
                else :
                    print("Time To Book")
                    Call_buddy(0)
                    time.sleep(60)
        except Exception as df:
            print(df)

if __name__ == "__main__":
    The_Main()  