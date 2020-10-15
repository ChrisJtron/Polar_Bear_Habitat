
import pandas as pd
import json
data=pd.read_csv("Polar_bear_data.csv")
ids=data["BearID_mcp"].drop_duplicates()
outDict={}
for currId in ids:
    currData=data[data["BearID_mcp"]==currId]
    outDict[currId]=currData.to_dict(orient="records")
with open("bears.json","w") as f:
    json.dump(outDict,f,indent=4)