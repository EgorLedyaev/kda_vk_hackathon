from masonite.request import Request
from masonite.response import Response
from masonite.controllers import Controller
from masonite.views import View
import sys
import json

class LoaderController(Controller):
    def result(self, view: View, request: Request, response: Response):
        
        inputJson = request.input('inputJson')
        isValid = False
        textError = "Error: Данная строка JSON недействительна"
        outputJson = ""
        try:
            json.loads(inputJson)
            isValid = True
            outputJson = inputJson
            return view.render("welcome",{"inputData": inputJson,  "outputData": outputJson, "isValid": isValid})
        except ValueError as err:
            return view.render("welcome",{"inputData": inputJson,  "outputData": textError, "isValid": isValid})
