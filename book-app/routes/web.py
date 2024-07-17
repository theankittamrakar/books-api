from masonite.authentication import Auth
from masonite.routes import Route

ROUTES = [Route.get("/", "DashboardController@show"),

          Route.group([
              Route.get("/dashboard", "DashboardController@show").name("dashboard"),

              # Books Routes
              Route.get("/books", "BookController@index"),
              Route.get("/books/@id:int", 'BookController@show'),
              Route.post("/books", "BookController@store"),
              Route.post("/books/@id:int", 'BookController@update'),
              Route.delete("/books/@id:int", 'BookController@destroy'),

              # Authors Routes
              Route.get("/authors", "AuthorController@index"),
              Route.get("/authors/@id:int", 'AuthorController@show'),
              Route.post("/authors", "AuthorController@store"),
              Route.post("/authors/@id:int", 'AuthorController@update'),
              Route.delete("/authors/@id:int", 'AuthorController@destroy'),
          ], middleware=['auth']),
          ]

ROUTES += Auth.routes()
