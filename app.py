from flask import Flask,render_template,request
import tweepy
import config
from views import views
app = Flask(__name__)
#it shows that whenever we will mention slah or home in url it will go to home page

# return html file


@app.route('/')
@app.route("/home")
def home():
    return render_template("index.html")


client = tweepy.Client(consumer_key=config.API_KEY,consumer_secret=config.API_SECRET_KEY,
                       access_token=config.access_token,
                       access_token_secret=config.access_token_secret)
# text tweet
# response=client.create_tweet(text='hello world!')


@app.route('/result', methods=['GET', 'POST'])
def result():
    if request.method == 'GET':
        text_area_value=request.args.get('tweet_text')
        client.create_tweet(text=text_area_value)
        return "tweet successful"


@app.route('/result1', methods=['GET', 'POST'])
def result1():
    if request.method == 'GET':
        text_area_value=request.args.get('tweet_id')
        client.delete_tweet(text_area_value)
        return "tweet deleted"


@app.route('/result2', methods=['GET', 'POST'])
def result2():
    if request.method == 'GET':
        tweet_id=request.args.get('tweet_id')
        text_area_value=request.args.get('add_comments')
        client.create_tweet(text=text_area_value,quote_tweet_id=tweet_id)
        return "Added comments to the tweet"


if __name__ == '__main__':
    app.run(debug=True)
