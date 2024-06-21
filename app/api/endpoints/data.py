from fastapi import APIRouter, HTTPException
import pandas as pd
import numpy as np
import os
router = APIRouter()

@router.get("/data-summary")
def data_summary():
    # Create a sample DataFrame using Pandas
    data = {
        'A': np.random.rand(10),
        'B': np.random.rand(10),
        'C': np.random.rand(10)
    }
    df = pd.DataFrame(data)

    # Calculate summary statistics
    summary = df.describe().to_dict()

    return summary


@router.get("/csvFile")
def fileSummary():
    return {"message" : "sucess"}