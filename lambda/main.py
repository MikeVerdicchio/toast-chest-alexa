from ask_sdk_core.skill_builder import SkillBuilder

from .handlers import core, intent

sb = SkillBuilder()


sb.add_request_handler(core.LaunchRequestHandler())
sb.add_request_handler(core.SessionEndedRequestHandler())
sb.add_request_handler(core.HelpIntentHandler())
sb.add_request_handler(core.CancelAndStopIntentHandler())
sb.add_request_handler(core.FallbackIntentHandler())

sb.add_request_handler(intent.GetToastIntentHandler())
sb.add_exception_handler(core.AllExceptionHandler())

handler = sb.lambda_handler()
