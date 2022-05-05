engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voices', voices[len(voices) - 1].id)

# text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

# to convert voice into text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=5,phrase_time_limit=8)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")

    except Exception as e:
        speak("say that again please....")
        return "none"
    return query

# to wish
def wish():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%m/%d/%Y %T:%M %p")

    if hour >= 0 and hour <= 12:
        speak(f"good morning, its {tt}")
    elif hour >= 12 and hour <= 18:
        speak(f"good afternoon, its {tt}")
    else:
        speak(f"good evening, its {tt}")
    speak("i am you friend jarvis, please tell me how can i help you")

# to send email
def sendEmail(to, content):
    server = smtplib.SMTP('smtp@gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('mkmkavin2001@gmail.com', '9488536289')  # your email address , your password    server.sendmail('senderemail@gmail.com', to, content)  # your email address
    server.close()

# for news updates
def news():
# the news to speak link
#####     main_url = 'https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=code'

    main_page = requests.get(main_url).json()
    # print(main_page)
    articles = main_page["articles"]
    # print(articles)
    head = []
    day = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range(len(day)):
        # print(f"today's {day[i]} news is: ", head[i])
        speak(f"today's {day[i]} news is: {head[i]}")



if __name__ == "__main__":
    wish()
    while True:
    #if 1:

        query = takecommand().lower()

        #logic building for tasks

        if "open notepad" in query:
            npath = "C:\\Windows\\System32\\notepad.exe"
            os.startfile(npath)

        elif "open command prompt" in query or "open cmd" in query:
            os.system("start cmd")

        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('wedcam', img)
                k = cv2.waitkey(50)
                if k==27:
                    break;
            cap.release()
            cv2.destroyAllWindowa()



        elif "play music" in query:
            speak("Here you go with music")
            music_dir = "C:\\Users\\mkmka\\Music"
            songs = os.listdir(music_dir)
            # rd = random.choice(songs)
            for song in songs:
                if song.endswith('.mp3'):
                    os.startfile(os.path.join(music_dir, song))

        elif "ip address" in query or "what is my ip" in query:
            ip = get('http://api.ipify.org').text
            speak(f"your ip address is {ip}")

        elif "wikipedia" in query:
            speak("searching wikipedia....")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentnces=2)
            speak("according to wikipedia")
            speak(results)
            # print(results)

        elif "open youtube" in query:
            webbrowser.open("ww.youtube.com")

        elif "open instagram" in query:
            webbrowser.open("www.instagram.com")

        elif "open facebook" in query:
            webbrowser.open("www.facebook.com")

        elif "open google" in query:
            speak("sir, what should i search for you on google")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")

        elif "send message" in query:
            kit.sendwhatmsg("+919488536289", "this is test is testing protocol",4,13)
            time.sleep(120)
            speak("message has been sent sir")

#----------sleep jarvis
        elif "you can sleep" in query:
            speak("thanks for using me as your friend, have a good day.")
            sys.exit()

#------------to send file on email
        elif "email to you" in query:

            speak("sir what should i say")
            query = takecommand().lower()
            if "send a file" in query:
                email = 'youremail@gmail.com'  # Your email
                password = 'your pass'  # your email account password
                send_to_email = 'senderemail@gmail.com'  # Whom you are sending the message to
                speak("okay sir, what is the subject for this email")
                query = takecommand().lower()
                subject = query  # The Subject in the email
                speak("and sir, what is the message for this email")
                query2 = takecommand().lower()
                message = query2  # The message in the email
                speak("sir please enter the correct path of the file into the shell")
                file_location = input("please enter the path here:\n")  # The File attachment in the email

                speak("please wait,i am sending email now")

                msg = MIMEMultipart()
                msg['From'] = email
                msg['To'] = send_to_email
                msg['Subject'] = subject

                msg.attach(MIMEText(message, 'plain'))

                # Setup the attachment
                filename = os.path.basename(file_location)
                attachment = open(file_location, "rb")
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

                # Attach the attachment to the MIMEMultipart object
                msg.attach(part)

                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(email, password)
                text = msg.as_string()
                server.sendmail(email, send_to_email, text)
                server.quit()
                speak("email has been sent to monika")

            else:
                user_email = 'youremail@gmail.com'  # Your email
                user_password = 'your pass'  # Your email account password
                send2_to_email = 'senderemail@gmail.com'  # Whom you are sending the message to
                message = query  # The message in the email

                server = smtplib.SMTP('smtp.gmail.com', 587)  # Connect to the server
                server.starttls()  # Use TLS
                server.login(user_email, user_password)  # Login to the email server
                server.sendmail(user_email, send2_to_email, message)  # Send the email
                server.quit()  # Logout of the email server
                speak("email has been sent to avinash")

# to find my location using IP address

        elif "where i am" in query or "where we are" in query:
            speak("wait sir, let me check")
            try:
                ipAdd = requests.get('https://api.ipify.org/').text
                print(ipAdd)
#                 url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                geo_requests = requests.get(url)
                geo_data = geo_requests.json()
                # print(geo_data)
                city = geo_data['city']
                # state = geo_data['state']
                country = geo_data['country']
                speak(f"sir i am not sure, but i think we are in {city} city of {country} country")
            except Exception as e:
                speak("sorry sir, Due to network issue i am not able to find where we are")
                pass

#-------------------------- to take screenshot --------

        elif "take screenshot" in query or "take a screenshot" in query:
            speak("sir, please tell me the name for this screenshot file")
            name = takecommand().lower()
            speak("please sir hold the screen for few second, i am taking screenshot")
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"(name).png")
            speak("i am done sir, the screenshot is save in our main folder. now i am ready for next command")

# to close any application
        elif "close notepad" in query:
            speak("okay sir, closing notepad")
            os.system("taskkill /f /im notepad.exe")

        elif "close command prompt" in query or "close cmd" in query:
            speak("okay sir, closing command prompt")
            os.system("taskkill /f /im cmd.exe")

#to set an alarm
        elif "set alarm" in query:
            nn = int(datetime.datetime.now().hour)
            if nn==22:
                music_dir = 'E:\\music'
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir, songs[0]))

# to find a joke, news
        elif "tell me a joke" in query:
            speak(pyjokes.get_joke())

        elif "tell me a news" in query or "what is the news today" in query:
            speak("please wait, i am feteching the latest news")
            news()

# ----- my jobs
        elif "who are you" in query:
            speak("I am fine, Thank you for asking me what about you")

        elif "i am fine" in query or "i am good" in query:
            speak("It's good to know that your fine")

        elif "what your doing" in query:
            speak("i am helping using my voice ")
            query = takecommand().lower()
        elif "" in query:
            speak("i am sorry for that ")

        elif "what is my name" in query:
            speak("this kavin right")

        elif "who am i" in query or "do you know me" in query:
            speak("i think you are kavin")

        elif "fuck" in query:
            speak("")
        
# ---------------speak to text
        elif "write a note" in query:
            speak("What should i write, sir")
            query = takecommand().lower()
            file = open('jarvis.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = takecommand().lower()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
                file.write(strTime)
                file.write(" :- ")
                file.write(query)
            else:
                file.write(query)

        elif "show note" in query:
            speak("Showing Notes")
            file = open("jarvis.txt", "r")
            print(file.read())
            speak(file.read(6))
