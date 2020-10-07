from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse
app = Flask(__name__)
@app.route('/bot',methods=['post'])
def bot():
    incoming_msg = request.values.get('Body','').lower()
    response = MessagingResponse()
    msg = response.message()
    responded = False
    if "hi" in incoming_msg or "hey" in incoming_msg or "menu" in incoming_msg:
        result = f'Hello humans🙋‍♂‍🙋‍♀‍,\nIm a bot who is here to fight your boredom you can get the latest news from me and currently trending stuffs on the internet, \n👉To get the latest INDIAN news enter *inews* \n👉for american news enter *unews* \n👉for news from bbc enter *bbc*\n👉And for Indian science news enter *ins* or *insc*\n👉for American science news enter *usc* or *us*\n👉for Indian technological news enter *it*\n👉for American technological news enter *ut*\n----------------------------------\n        Hello 🙋‍♂‍🙋‍♀‍, \nAnd also im  a Covid-Bot to provide latest information updates i.e cases in different countries and create awareness to help you and your family stay safe.\n For any emergency 👇 \n 📞 Helpline: 011-23978046 | Toll-Free Number: 1075 \n 📩 Email: ncov2019@gov.in \n\n Please enter one of the following option 👇(1,2,3,4,5,6,7)\n *1*. Covid-19 statistics *Worldwide*. \n *2*. Covid-19 cases in *India*. \n *3*. Covid-19 cases in *China*. \n *4*. Covid-19 cases in *USA*. \n *5*. Coronavirus cases in *Italy*. \n *6*. How does it *Spread*? \n *7*. *Preventive measures* to be taken.'
        msg.body(result)
        responded = True
    if "unews" in incoming_msg or "un" in incoming_msg:
        r = requests.get("http://newsapi.org/v2/top-headlines?country=us&apiKey=d4de648fb6424879b36e8ff41c9aa5f1")
        if r.status_code == 200:
          data = r.json()
          for i in data["articles"]:
              tex = f'{i["title"], ":"}{"by "}{i["author"]} \n {i["description"]} \n{i["url"]}'
              tr = 'please type "hey" or "hi" or "menu" to view the options'
              response.message(tex)
        else:
          tex = "sorry i didnt get you , enter something valid or just enter hi or hey"
        msg.body(tex)
        responded = True

    if "inews" in incoming_msg or "in" in incoming_msg:
        r = requests.get("http://newsapi.org/v2/top-headlines?country=in&apiKey=d4de648fb6424879b36e8ff41c9aa5f1")
        if r.status_code == 200:
            data = r.json()
            for i in data["articles"]:
                tex = f'{i["title"], ":"}{"by "}{i["author"]} \n {i["description"]} \n{i["url"]}'
                response.message(tex)
        else:
            tex = "sorry i didnt get you , enter something valid or just enter hi or hey"
        msg.body(tex)
        responded = True
    if "bbc" in incoming_msg or "bb" in incoming_msg:
        r = requests.get("https://newsapi.org/v1/articles?source=bbc-news&apiKey=d4de648fb6424879b36e8ff41c9aa5f1")
        if r.status_code == 200:
            data = r.json()
            for i in data["articles"]:
                tex = f'{i["title"], ":"}{"by "}{i["author"]} \n {i["description"]} \n{i["url"]}'
                response.message(tex)
        else:
            tex = "sorry i didnt get you , enter something valid or just enter hi or hey"
        msg.body(tex)
        responded = True

    if "insc" in incoming_msg or "ins" in incoming_msg:
        r = requests.get("http://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=d4de648fb6424879b36e8ff41c9aa5f1")
        if r.status_code == 200:
            data = r.json()
            for i in data["articles"]:
                tex = f'{i["title"], ":"}{"by "}{i["author"]} \n {i["description"]} \n{i["url"]}'
                response.message(tex)
        else:
            tex = "sorry i didnt get you , enter something valid or just enter hi or hey"
            msg.body(tex)
            responded = True

    if "usc" in incoming_msg or "us" in incoming_msg:
        r = requests.get("http://newsapi.org/v2/top-headlines?country=us&category=science&apiKey=d4de648fb6424879b36e8ff41c9aa5f1")
        if r.status_code == 200:
            data = r.json()
            for i in data["articles"]:
                tex = f'{i["title"], ":"}{"by "}{i["author"]} \n {i["description"]} \n{i["url"]}'
                response.message(tex)
        else:
            tex = "sorry i didnt get you , enter something valid or just enter hi or hey"
            msg.body(tex)
            responded = True

    if "it" in incoming_msg:
        r = requests.get("http://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=d4de648fb6424879b36e8ff41c9aa5f1")
        if r.status_code == 200:
            data = r.json()
            for i in data["articles"]:
                tex = f'{i["title"], ":"}{"by "}{i["author"]} \n {i["description"]} \n{i["url"]}'
                response.message(tex)
        else:
            tex = "sorry i didnt get you , enter something valid or just enter hi or hey"
            msg.body(tex)
            responded = True
    if "ut" in incoming_msg:
        r = requests.get("http://newsapi.org/v2/top-headlines?country=us&category=technology&apiKey=d4de648fb6424879b36e8ff41c9aa5f1")
        if r.status_code == 200:
            data = r.json()
            for i in data["articles"]:
                tex = f'{i["title"], ":"}{"by "}{i["author"]} \n {i["description"]} \n{i["url"]}'
                response.message(tex)
        else:
            tex = "sorry i didnt get you , enter something valid or just enter hi or hey"
            msg.body(tex)
            responded = True
    if "1" in incoming_msg:
        # return total cases
        r = requests.get('https://coronavirus-19-api.herokuapp.com/all')
        if r.status_code == 200:
            data = r.json()
            text = f'_Covid-19 Cases Worldwide_ 🌏 \n\nConfirmed Cases : *{data["cases"]}* \n\nDeaths : *{data["deaths"]}* \n\nRecovered : *{data["recovered"]}*  \n\n 👉 Type *2* to check cases in *India* \n 👉 Type *2, 3, 4, 5, 6, 7* to see other options \n 👉 Type *Menu* to view the Main Menu'
            print(text)
        else:
            text = 'I could not retrieve the results at this time, sorry.'
        msg.body(text)
        responded = True
    if "2" in incoming_msg:
        # return cases in india
        r = requests.get('https://coronavirus-19-api.herokuapp.com/countries/india')
        if r.status_code == 200:
            data = r.json()
            text = f'_Covid-19 Cases in India_ \n\nConfirmed Cases : *{data["cases"]}* \n\nToday Cases : *{data["todayCases"]}* \n\nDeaths : *{data["deaths"]}* \n\nRecovered : *{data["recovered"]}* \n\n 👉 Type *3* to check cases in *China* \n 👉 Type *1, 3, 4, 5, 6, 7* to see other options \n 👉 Type *Menu* to view the Main Menu'
        else:
            text = 'I could not retrieve the results at this time, sorry.'
        msg.body(text)
        responded = True
    if "3" in incoming_msg:
        # return cases in china
        r = requests.get('https://coronavirus-19-api.herokuapp.com/countries/china')
        if r.status_code == 200:
            data = r.json()
            text = f'_Covid-19 Cases in China_ \n\nConfirmed Cases : *{data["cases"]}* \n\nToday Cases : *{data["todayCases"]}* \n\nDeaths : *{data["deaths"]}* \n\nRecovered : *{data["recovered"]}* \n\nActive Cases : *{data["active"]}* \n\n 👉 Type *4* to check cases in *USA* \n 👉 Type *1, 2, 4, 5, 6, 7* to see other options \n 👉 Type *Menu* to view the Main Menu'
        else:
            text = 'I could not retrieve the results at this time, sorry.'
        msg.body(text)
        responded = True
    if "4" in incoming_msg:
        # return cases in usa
        r = requests.get('https://coronavirus-19-api.herokuapp.com/countries/usa')
        if r.status_code == 200:
            data = r.json()
            text = f'_Covid-19 Cases in USA_ \n\nConfirmed Cases : *{data["cases"]}* \n\nToday Cases : *{data["todayCases"]}* \n\nDeaths : *{data["deaths"]}* \n\nRecovered : *{data["recovered"]}* \n\nActive Cases : *{data["active"]}*  \n\n 👉 Type *5* to check cases in *Italy* \n 👉 Type *1, 2, 3, 5, 6, 7* to see other options \n 👉 Type *Menu* to view the Main Menu'
        else:
            text = 'I could not retrieve the results at this time, sorry.'
        msg.body(text)
        responded = True
    if "5" in incoming_msg:
        # return cases in italy
        r = requests.get('https://coronavirus-19-api.herokuapp.com/countries/italy')
        if r.status_code == 200:
            data = r.json()
            text = f'_Covid-19 Cases in Italy_ \n\nConfirmed Cases : *{data["cases"]}* \n\nToday Cases : *{data["todayCases"]}* \n\nDeaths : *{data["deaths"]}* \n\nRecovered : *{data["recovered"]}* \n\nActive Cases : *{data["active"]}* \n\n 👉 Type *6* to check how *Covid-19 Spreads?* \n 👉 Type *1, 2, 3, 4, 6, 7* to see other options \n 👉 Type *Menu* to view the Main Menu'
        else:
            text = 'I could not retrieve the results at this time, sorry.'
        msg.body(text)
        responded = True
    if "6" in incoming_msg:
        text = f'_Coronavirus spreads from an infected person through_ 👇 \n\n 💧 Small droplets from the nose or mouth which are spread when a person coughs or sneezes \n\n 🤝 Touching an object or surface with these droplets on it and then touching your mouth, nose, or eyes before washing your hands \n \n 👬👫 Close personal contact, such as touching or shaking hands \n Please watch the video for more information ?? https://youtu.be/0MgNgcwcKzE \n\n 👉 Type 7 to check the *Preventive Measures* \n 👉 Type *1, 2, 3, 4, 5, 7* to see other options \n 👉 Type *Menu* to view the Main Menu'
        msg.body(text)
        msg.media('https://user-images.githubusercontent.com/34777376/77290801-f2421280-6d02-11ea-8b08-fdb516af3d5a.jpeg')
        responded = True
    if "7" in incoming_msg:
        text = f'_Coronavirus infection can be prevented through the following means_ 👇 \n 👉 Clean hand with soap and water or alcohol-based hand rub \n https://youtu.be/EJbjyo2xa2o \n\n 🙊 Cover nose and mouth when coughing & sneezing with a tissue or flexed elbow \n https://youtu.be/f2b_hgncFi4 \n\n 👉 Avoid close contact & maintain 1-meter distance with anyone who is coughing or sneezin \n https://youtu.be/mYyNQZ6IdRk \n\n 👉 Isolation of persons traveling from affected countries or places for at least 14 day \n https://www.mohfw.gov.in/AdditionalTravelAdvisory1homeisolation.pdf \n\n 👉 Quarantine if advise \n https://www.mohfw.gov.in/Guidelinesforhomequarantine.pdf \n\n 👉 Type *1, 2, 3, 4, 5, 6* to see other option \n 👉 Type *Menu* to view the Main Menu'
        msg.body(text)
        msg.media('https://user-images.githubusercontent.com/34777376/77290864-1c93d000-6d03-11ea-96fe-18298535d125.jpeg')
        responded = True
    if not responded:
        msg.body("sorry i didnt get you , enter something valid or just enter hi or hey")
    return str(response)
if __name__ == "__main__":
    app.run(host="localhost",port=5000,debug=True)





















