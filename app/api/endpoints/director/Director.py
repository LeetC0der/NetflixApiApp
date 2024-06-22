import os
import pandas as pd
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from collections import *
from app.api.endpoints.director.DirectorBst import DirectorTree, printTree
router = APIRouter()

newDirectorTree = DirectorTree()

def direction():
    try:
        # Adjust the file path as necessary
        file_path = os.path.join(os.path.dirname(__file__), 'netflix_titles.csv')
        # Read the CSV file with a specified encoding
        df = pd.read_csv(file_path, encoding='latin1')  # or encoding='cp1252' if 'latin1' doesn't work
        availableDirectors = set(df['director'].dropna().unique())
        for i in availableDirectors:
            eachDirectordetails = df[df['director'] == i]
            dataJson = { 
                "showid" :  eachDirectordetails['show_id'], 
                "title" : eachDirectordetails['title'], 
                "show/movie" : eachDirectordetails['type'], 
                "castMembers" :  eachDirectordetails['cast'], 
                "listed_in" :eachDirectordetails['listed_in'], 
                "description" : eachDirectordetails['description'] 
                }
            newDirectorTree.insert(eachDirectordetails['director'], dataJson)
        return ''
    except Exception as e:
        return str(e)
printTree(newDirectorTree.root)
print(direction())
@router.get("/directors")
def get_directors():
    directors = direction()
    if isinstance(directors, set):
        return JSONResponse(content=list(directors))
    else:
        return JSONResponse(content={"error": directors}, status_code=500)
