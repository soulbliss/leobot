import os
import slack
import schedule
import time
import random
from threading import Thread


quote_list = []


with open('quotes', 'r') as file:
    quote_list = file.readlines()
   
    quote_list = [line.strip() for line in quote_list]




TIO_FOR_WEEK = ''


@slack.RTMClient.run_on(event='message')
def tio(**payload):
    global TIO_FOR_WEEK
    data = payload['data']
    rtm_client = payload['rtm_client']
    web_client = payload['web_client']
    channel_id = data['channel']

    print(data.get('text', []), '\tOn Channel:', data['channel'])

    if 'tio' in data.get('text', []):
        channel_id = data['channel']
        thread_ts = data['ts']
        #user = data['user']
        tio_string = data.get('text', [])
        tio_string = tio_string.strip('tio').strip()
        TIO_FOR_WEEK = tio_string
        print(tio_string)
        web_client.chat_postMessage(
            channel=channel_id,
            text=f"Deeps we got the idea message :)"
            #text=f"Hi <@{user}>!"
        )


def tio_push_notifs():

    client = slack.WebClient(token=slack_token)


    def relay_strength_quote():
        #print('tio for week is :' ,TIO_FOR_WEEK)
        pick_quote = random.choice(quote_list)
        tism = client.chat_postMessage(
        channel='C014EQ2GREX',
        text=f""+pick_quote+"",
    )


     
    '''
    def think_ten_ideas_send_message():
        print('tio for week is :' ,TIO_FOR_WEEK) 
        tism = client.chat_postMessage(
        channel='DQV2E35LG',
        text=f"Think about "+TIO_FOR_WEEK+" dude..."
    )

        assert tism['ok']
    

    def tio_for_week_message():
        tfwm = client.chat_postMessage(
        channel='DQV2E35LG',
        text=f"Deeps, whats the Tio for the week, eh?",
    )

        assert tfwm['ok']
        assert tfwm['message']['text'] == 'Deeps, whats the Tio for the week, eh?'
    '''

    #the server is at +5:30


    schedule.every().day.at("23:50").do(relay_strength_quote)
    schedule.every().day.at("01:05").do(relay_strength_quote)
    schedule.every().day.at("08:30").do(relay_strength_quote)
    schedule.every().day.at("12:00").do(relay_strength_quote)
    schedule.every().day.at("15:00").do(relay_strength_quote)
    schedule.every().day.at("18:50").do(relay_strength_quote)

    #schedule.every().monday.at("12:15").do(think_ten_ideas_send_message)
   

    #schedule.every().monday.at("5:15").do(tio_for_week_message) 

    




    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    slack_token = os.environ["SLACK_API_TOKEN"]

    Thread(target= tio_push_notifs).start()

    rtm_client = slack.RTMClient(token=slack_token)
    rtm_client.start()
    


