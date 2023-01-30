# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk.events import SlotSet
from rasa_sdk import Action, Tracker, FormValidationAction
# from rasa_sdk.forms import FormAction
from rasa_sdk.executor import CollectingDispatcher

class ValidateNumberForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_number_form"

    def validate_number_1(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        number_1 =  tracker.get_slot("number_1")
        
        num1 = int(number_1.split('-')[0])
        if num1 > 10:
            dispatcher.utter_message(text="Invalid input please enter number again")
            return{"number_1": None}
        return{"number_1": num1}

    def validate_number_2(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        number_2 =  tracker.get_slot("number_2")
        num2 = int(number_2.split('-')[0])
        if num2 > 10:
            dispatcher.utter_message(text="Invalid input please enter again")
            return{"number_2": None}
        return{"number_2": num2}


class ActionAddTwoNumbers(Action):

    def name(self) -> Text:
        return "add_two_numbers"

    def run(
        self, 
        # slot_value: Any,
        # dispatcher: CollectingDispatcher,
        dispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
        ) -> List[Dict[Text, Any]]:

        operator_1 = (tracker.get_slot("operator"))
        num_1 = (tracker.get_slot("number_1"))
        num_2 = (tracker.get_slot("number_2"))
        if operator_1=="add":
            Total = num_1 + num_2
            print(Total)
            dispatcher.utter_message(text=f"result is {Total}" )
        elif operator_1=="multiply":
            Total = num_1 * num_2
            print(Total)
            dispatcher.utter_message(text=f"result is {Total}" )
        elif operator_1=="divide":
            Total = num_1 / num_2
            print(Total)
            dispatcher.utter_message(text=f"result is {Total}" )
        else:
            Total = num_1 - num_2
            print(Total)
            dispatcher.utter_message(text=f"result is {Total}" )
        return[]
       