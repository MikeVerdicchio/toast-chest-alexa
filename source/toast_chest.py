import os
import requests


APPLICATION_ID = os.environ.get("APPLICATION_ID")
API_ENDPOINT = os.environ.get("API_ENDPOINT")


def lambda_handler(event, context):
    if event["session"]["application"]["applicationId"] != APPLICATION_ID:
        raise ValueError("Invalid Application ID")

    if event["session"]["new"]:
        on_session_started({"questId": event["request"]["requestId"]}, event["session"])

    if event["request"]["type"] == "LaunchRequest":
        return on_launch(event["request"], event["session"])
    elif event["request"]["type"] == "IntentRequest":
        return on_intent(event["request"], event["session"])
    elif event["request"]["type"] == "SessionEndedRequest":
        return on_session_ended(event["request"], event["session"])


def on_session_started(session_started_request, session):
    return get_welcome_response()


def on_launch(launch_request, session):
    return get_welcome_response()


def on_intent(intent_request, session):
    intent = intent_request["intent"]
    intent_name = intent_request["intent"]["name"]

    if intent_name == "GetToast":
        return get_toast(intent)
    elif intent_name == "AMAZON.HelpIntent":
        return get_welcome_response()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    else:
        raise ValueError("Invalid intent")


def on_session_ended(session_ended_request, session):
    return handle_session_end_request()


def handle_session_end_request():
    card_title = "Toast Chest"
    speech_output = "Thanks for using the Toast Chest!"
    should_end_session = True
    return build_response(
        {},
        build_speechlet_response(card_title, speech_output, None, should_end_session),
    )


def get_welcome_response():
    session_attributes = {}
    card_title = "Toast Chest"
    speech_output = "Welcome to the Toast Chest! Try saying: give me a toast."
    reprompt_text = speech_output
    should_end_session = False
    return build_response(
        session_attributes,
        build_speechlet_response(
            card_title, speech_output, reprompt_text, should_end_session
        ),
    )


def get_toast(intent):
    session_attributes = {}
    card_title = "Toast Chest"
    speech_output = ""
    reprompt_text = ""
    should_end_session = False

    try:
        data = requests.get(API_ENDPOINT).json()
        speech_output = data["Toast"]
    except Exception:
        speech_output = "Sorry, there was a problem."
        reprompt_text = "Try asking me again."

    return build_response(
        session_attributes,
        build_speechlet_response(
            card_title, speech_output, reprompt_text, should_end_session
        ),
    )


def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        "outputSpeech": {"type": "PlainText", "text": output},
        "card": {"type": "Simple", "title": title, "content": output},
        "reprompt": {"outputSpeech": {"type": "PlainText", "text": reprompt_text}},
        "shouldEndSession": should_end_session,
    }


def build_response(session_attributes, speechlet_response):
    return {
        "version": "1.0",
        "sessionAttributes": session_attributes,
        "response": speechlet_response,
    }
