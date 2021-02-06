from ask_sdk_core.skill_builder import SkillBuilder

from .handlers import amazon, exceptions, intent

sb = SkillBuilder()


sb.add_request_handler(amazon.LaunchRequestHandler())
sb.add_request_handler(amazon.SessionEndedRequestHandler())
sb.add_request_handler(amazon.HelpIntentHandler())
sb.add_request_handler(amazon.CancelAndStopIntentHandler())
sb.add_request_handler(amazon.FallbackIntentHandler())

sb.add_request_handler(intent.GetToastIntentHandler())
sb.add_exception_handler(exceptions.AllExceptionHandler())

handler = sb.lambda_handler()
