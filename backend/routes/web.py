from masonite.routes import Route

ROUTES = [
            Route.get("/", "WelcomeController@show").name('welcome'),
            Route.post("/result", "LoaderController@result").name('result')
        ]


