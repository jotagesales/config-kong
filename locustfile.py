import uuid
import json

from locust import HttpLocust, TaskSet, task


class MyTaskSet(TaskSet):
    api_key = None

    @task(5)
    def task1(self):
        transaction = str(uuid.uuid4())
        data = {
            "userId": "5510948416473",
            "serviceId": 98772320,
            "offerKey": "OFFER_KEY",
            "amountCharged": 399,
            "event": "RENEW",
            "digest": "SUBSCRIBED_BY_CHARGE",
            "channel": "SMS",
            "eventDate": "2018-01-14T10:10:33.001Z",
            "nextRenewalDate": "2018-01-21T10:10:33.001Z",
            "tags": {
               "property1": "tagValue",
               "property2": "tagValue"
             },
            "campaign": "PLATFORM_LAUNCH",
            "channelProviderId": 1,
            "protocol": "201801011405881",
            "subscriptionId": transaction,
            "transactionId": transaction
        }
        headers = {
            'Content-Type': 'application/json',
            'apikey': self.api_key
        }
        self.client.post('/v1/notification/claro', data=json.dumps(data), headers=headers)

    @task(3)
    def headers(self):
        headers = {
            'apikey': self.api_key
        }
        self.client.get('/headers', headers=headers)


class MyLocust(HttpLocust):
    task_set = MyTaskSet
    host = 'http://localhost:8000'
