import os

import requests
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_core.utils import is_intent_name
from ask_sdk_model import Response
from ask_sdk_model.ui import SimpleCard

API_ENDPOINT = str(os.environ.get("API_ENDPOINT"))


class GetToastIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input: HandlerInput) -> bool:
        return is_intent_name("GetToast")(handler_input)

    def handle(self, handler_input: HandlerInput) -> Response:
        data = requests.get(API_ENDPOINT).json()
        speech_text = data["Toast"]

        handler_input.response_builder.speak(speech_text).set_card(
            SimpleCard("Toast Chest", speech_text)
        ).set_should_end_session(False)

        return handler_input.response_builder.response
