#unittests for create_tweet and delete_tweet written by Kurapati Sai Pranavi
from application import create_app

def test_create_tweet():
    with create_app().test_client() as c:
        response = c.get('/result', query_string= {
                    "tweet_text": "FinalTestTweet1"
        })
        
        print(response)
        
        assert response.status_code ==  200

def test_delete_tweet():
    route = '/result1'

    tweet_id= '1703514850864017756'

    with create_app().test_client() as c:
        response = c.get(route, query_string={
            "tweet_id": tweet_id
        })
        
        print(response)

        assert response.status_code == 200 
        
if __name__ == '__main__':
    test_create_tweet()
    test_delete_tweet()