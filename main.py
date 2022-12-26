import models
from fastapi import FastAPI ,Request
from fastapi.templating import Jinja2Templates
from database import *
#from database import SessionLocal,engine
#from sqlalchemy.orm import Session,engine


app = FastAPI()
#models.Base.metadata.create_all(bind=engine)
templates = Jinja2Templates(directory="Templates")
@app.get("/")
def dashboard(request: Request):
    """
    Displays the stock screener dashboard/homepage
    """
    return templates.TemplateResponse("Dashboard.html",{
        "request": request
    })

@app.post("/stock")
def create_stock():
    """
    Creates a stock and stores it in the data base
    """

    return {
       "code": "success",
       "message": "stock created"
    }

@app.get("/db")
def database():

    print("hello")

    mycursor = conn.cursor()
    mycursor.execute('''select * from roles ''')
    myresult = mycursor.fetchall()
    print(myresult)
    #Avf_cart_value = pd.DataFrame(myresult)

    return {
        "code": "success",
        "data": myresult
     }