from collections import OrderedDict
from .response import *
import json


class SalesIQResponse():
    """
   "fulfillmentMessages": [
        {
          "payload": {
            "replies": [TextResponse, ...],
            "action": "reply",
            "platform": "ZOHOSALESIQ"
          }
        }
    ]
    """

    def __init__(self) -> None:
        self.sales_response = OrderedDict()
        self.response_payload = OrderedDict()
        self.payload = OrderedDict()
        self.replies = []
        self.fulfillment_messages = []
        self.sales_response["fulfillmentMessages"] = self.fulfillment_messages
        self.response_payload["payload"] = self.payload
        self.fulfillment_messages.append(self.response_payload)
        self.payload["platform"] = "ZOHOSALESIQ"
        self.payload["action"] = "reply"

    def __str__(self) -> str:
        return json.dumps(self.sales_response)

    def get_final_response(self):
        self.payload["replies"] = self.replies
        return self.sales_response

    def add(self, response_reply):
        if isinstance(response_reply, TextResponse):
            self.replies.append(response_reply.single_response)
        elif isinstance(response_reply, ImageResponse):
            self.replies.append(response_reply.image_response) 
        elif isinstance(response_reply, SuggestionsChips):
            self.payload["suggestions"] = response_reply.suggestions
        elif isinstance(response_reply, CarouselItems):
            self.replies.append(response_reply.caritems)