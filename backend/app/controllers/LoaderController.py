from masonite.controllers import Controller
from masonite.views import View


class LoaderController(Controller):
    def show(self, view: View):
        return view.render("")
