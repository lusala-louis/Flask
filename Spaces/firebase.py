import pyrebase

config = {
    "apiKey": "AIzaSyD_CN365IS1G3uVYUJ3gNw_EA9gsH99zlw",
    "authDomain": "ranger-29fa1.firebaseapp.com",
    "databaseURL": "https://ranger-29fa1-default-rtdb.firebaseio.com",
    "projectId": "ranger-29fa1",
    "storageBucket": "ranger-29fa1.appspot.com",
    "messagingSenderId": "344025321751",
    "appId": "1:344025321751:web:30cf5036f83bccca7e6752",
    "measurementId": "G-T4RJYC7FBJ"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()
