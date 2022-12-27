import models
from fastapi import FastAPI ,Request, Header
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


@app.get("/db")
def database():
    mycursor = conn.cursor()
    mycursor.execute('''select * from roles ''')
    myresult = mycursor.fetchall()
    print(myresult)
    #Avf_cart_value = pd.DataFrame(myresult)

    return {
        "code": "success",
        "data": myresult
     }
#
@app.get("/api/roles")
def read_items(my_header1: str = Header(default=None), my_header2: str = Header(default=None)):
    # my_header1 = request.headers.get("my_header1")
    print(my_header1)
    return {"Authorization values": my_header1, "head 2": my_header2}


#
# @app.put('/')
# async def root():
#     return {"message":"success"}
#
# @app.delete('/')
# async def stem():
#     return {"message": "success"}
