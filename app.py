import cv2
import tweepy
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
from flask import Flask, render_template, request
# from flask_ngrok import run_with_ngrok


consumer_key='fbR5kFHpU8qExKleXnefRzQfQ'
consumer_secret='T1c53pX0WDEgX7IEIwD4MhMwFBZ1HTZj5ZJKZ4WrzhDSehK2kg'
access_token_key='510740882-eI8mtDqxIlJlrl5QAkKRJWKsxfXTd3KhAHTFyUUI'
access_token_secret='4HGd0XyuEXMg8m0k2HoP4yjnqpCDZlvSOLi5NvLGme47g'

auth = tweepy.OAuthHandler(consumer_key=consumer_key, consumer_secret=consumer_secret)

auth.set_access_token(access_token_key, access_token_secret)

api = tweepy.API(auth)


app = Flask(__name__)
# run_with_ngrok(app)
@app.route('/')

def Hashtag():
   return render_template('Hashtag.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form['hash']
      tweets = tweepy.Cursor(api.search, q=result, lang="en").items(100)
      cloud = ""
      for each in tweets:
          cloud = cloud + each.text

      cloud = WordCloud(background_color="white").generate(cloud)

      # plt.imshow(cloud)

      image = np.array(cloud)
      cv2.imwrite('./static/cloud.jpg', image, [cv2.IMWRITE_JPEG_QUALITY, 100])

      return render_template("result.html",result = result)

if __name__ == '__main__':
   app.run()
