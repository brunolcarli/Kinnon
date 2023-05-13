import json
import requests
import numpy as np
from kinnon.settings import URL, LISA


class Query:
    """
    Sends read operations to backend API server.
    """
    @staticmethod
    def query_sentiment_value(text):
        """
        Extract text sentiment value from LISA API
        """
        payload = f'''
        query{{
            sentimentExtraction(text: "{text}")
        }}'''
        response = requests.post(LISA, json={'query': payload}).json()['data']['sentimentExtraction']
        return bool(np.clip([response], 0, 1)[0])

    @staticmethod
    def query_scope_questions(scope):
        """
        Query a set of questions by a given scope.
        """
        payload = f'''
        query{{
            questions(scope: "{scope}"){{
                id
                question
            }}
        }}
        '''
        response = requests.post(URL, json={'query': payload})
        return response.json()['data']['questions']

    @staticmethod
    def query_question_by_id(id):
        """
        The method is self explainable
        """
        payload = f'query{{questions(id: "{id}"){{ id question }} }}'
        response = requests.post(URL, json={'query': payload})
        return response.json()['data']['questions'][0]


class Mutation:
    """
    Sends write operations to backend API server
    """

    @staticmethod
    def create_answer(data):
        payload = f'''
        mutation {{
            createAnswer(input: {{
                userId: "{data['user_id']}"
                username: "{data['username']}"
                textAnswer: "{data['answer']}"
                questionId: "{data['id']}"
                sentiment: {json.dumps(data['sentiment'])}
            }}){{
                answer{{
                    datetime
                    sentiment
                    textAnswer
                }}
            }}
        }}
        '''
        response = requests.post(URL, json={'query': payload}).json()['data']['createAnswer']
        return response
