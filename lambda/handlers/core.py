from ask_sdk_core.dispatch_components import (
    AbstractExceptionHandler,
    AbstractRequestHandler,
)
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_core.utils import is_intent_name, is_request_type
from ask_sdk_model import Response
from ask_sdk_model.ui import SimpleCard


class LaunchRequestHandler(AbstractRequestHandler):
    def can_handle(self, handler_input: HandlerInput) -> bool:
        return is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input: HandlerInput) -> Response:
        speech_text = "Welcome to the Toast Chest! Try saying: give me a toast."
        handler_input.response_builder.speak(speech_text).set_card(
            SimpleCard("Toast Chest", speech_text)
        ).set_should_end_session(False)

        return handler_input.response_builder.response


class SessionEndedRequestHandler(AbstractRequestHandler):
    def can_handle(self, handler_input: HandlerInput) -> bool:
        return is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input: HandlerInput) -> Response:
        return handler_input.response_builder.response


class HelpIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input: HandlerInput) -> bool:
        return is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input: HandlerInput) -> Response:
        speech_text = "You can say: give me a toast!"
        handler_input.response_builder.speak(speech_text).ask(speech_text).set_card(
            SimpleCard("Toast Chest", speech_text)
        )

        return handler_input.response_builder.response


class CancelAndStopIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input: HandlerInput) -> bool:
        cancel_intent = is_intent_name("AMAZON.CancelIntent")(handler_input)
        stop_intent = is_intent_name("AMAZON.StopIntent")(handler_input)

        return cancel_intent or stop_intent

    def handle(self, handler_input: HandlerInput) -> Response:
        speech_text = "Thanks for using the Toast Chest! Goodbye!"
        handler_input.response_builder.speak(speech_text).set_card(
            SimpleCard("Toast Chest", speech_text)
        ).set_should_end_session(True)

        return handler_input.response_builder.response


class FallbackIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input: HandlerInput) -> bool:
        return is_intent_name("AMAZON.FallbackIntent")(handler_input)

    def handle(self, handler_input: HandlerInput) -> Response:
        speech = "I'm sorry, Toast Chest can't help you with that."
        reprompt = "Try saying: give me a toast."
        handler_input.response_builder.speak(speech).ask(reprompt)
        return handler_input.response_builder.response


class AllExceptionHandler(AbstractExceptionHandler):
    def can_handle(self, handler_input: HandlerInput, exception: Exception) -> bool:
        return True

    def handle(self, handler_input: HandlerInput, exception: Exception) -> Response:
        # TODO: Log error
        speech = "Sorry, there was a problem. Try asking me again!"
        handler_input.response_builder.speak(speech).ask(speech)

        return handler_input.response_builder.response
