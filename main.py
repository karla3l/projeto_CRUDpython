import config.sql_functions as sqlfun
import models.book as book
import controllers.book_controller as controller
import config.routers as fastapi


app = fastapi.Routers()
app.crud_routers()

if __name__ == '__main__':
    import uvicorn 
    uvicorn.run(app.app, host="127.0.0.1", port = 8000)
