from fastapi import FastAPI

from wbpillargpt.z_utils import url_api_wb, data_from_country, get_content

import time
import random

app = FastAPI()

@app.get("/")
def read_root():
    return {"hola": "mundo"}

@app.get("/country/{country_code}")
def projects_inside(country_code:str):
    docs, total = data_from_country(cod_country=country_code)
    return{"country_code": country_code, "total": total, "content": docs}


# P039086
@app.get("/project_id/{proj_id}")
def process_project_id(proj_id):
    url = url_api_wb(project_id=proj_id)
    print(url)
    return get_content(url)



