"""A WelcomeController Module."""
from masonite.views import View
from masonite.request import Request
from masonite.response import Response
from masonite.controllers import Controller


class WelcomeController(Controller):
    """WelcomeController Controller Class."""

    def show(self, view: View):
        inputJson = ""
        outputJson = ""
        return view.render("welcome")

    