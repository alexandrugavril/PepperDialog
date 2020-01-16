# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.forms import FormAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, AllSlotsReset, UserUtteranceReverted

class HealthInformationAction(Action):

    def name(self) -> Text:
        return "action_health_information"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        #Slots are being sent to the backend to respond to the query.
        slots = tracker.current_slot_values()
        dispatcher.utter_message("General Health Information!")
        return [AllSlotsReset()]

class ActuationQueryAction(Action):

    def name(self) -> Text:
        return "action_actuation_query"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        #Slots are being sent to the backend to respond to the query.
        slots = tracker.current_slot_values()
        dispatcher.utter_message("ActuationQueryAction!")
        return [AllSlotsReset()]

 