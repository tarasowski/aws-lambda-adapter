import json
import unittest
from business import add, subtract, multiply, divide

# handler is a slim adapter
# takes event data
# and passes only details that matter to your business logic


# here is my handler 👇
# a slim adapter
def handler(event,  context):
    action = event.get("action")
    if action == "add":
        return add(event.get("number1"), event.get("number2"))
    return "success"


if __name__ == "__main__":
    event = json.loads(open("event.json").read())
    print(
        handler(event, None)
    )