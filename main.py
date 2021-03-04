from pyrebase import pyrebase
from pusher_push_notifications import PushNotifications


config = {
    'apiKey': "AIzaSyCmqsRepRaR0ozZif_nCFnfd2td5gYnks0",
    'authDomain': "esp8-14574.firebaseapp.com",
    'databaseURL': "https://esp8-14574-default-rtdb.firebaseio.com",
    'projectId': "esp8-14574",
    'storageBucket': "esp8-14574.appspot.com",
    'messagingSenderId': "662104445951",
    'appId': "1:662104445951:web:9c9676d8023b379f54cdca"
  }
firebase = pyrebase.initialize_app(config)
db=firebase.database()
beams_client = PushNotifications(
    instance_id='dce41b63-324d-43ae-99d8-83b480bd483b',
    secret_key='151EAE37153AE47AE76ED3751222C16C23B055B623F7D2D33677281ABD7659AB',
)
def stream_handler(message):
    print(message)
    if(message['data'] is 1):
        response = beams_client.publish_to_interests(
            interests=['hello'],
            publish_body={
                'apns': {
                    'aps': {
                        'alert': {
                            'title': 'Dhaka School Of Science And Techlogy',
                            'body': 'The Lock Has Been Broken   ||   Laxmi Bazar, Old Dhaka || +8801728877232',



                        },
                    },
                },
                'fcm': {
                    'notification': {
                         'title': 'Dhaka School Of Science And Technology',
                            'body': 'The Lock Has Been Broken    ||    Laxmi Bazar, Old Dhaka || +8801728899232 ',

                    },
                },
                'web': {
                    'notification': {
                         'title': 'Dhaka School Of Science And Technology',
                            'body': 'The Lock Has Been Broken   ||    Laxmi Bazar, Old Dhaka || +8801729988232',

                    },
                },
            },
        )

        print(response['publishId'])

my_stream = db.child("ALERT").stream(stream_handler,None)