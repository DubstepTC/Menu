import openpyxl
import requests
import keyboard
import pandas as pd
import json
import webbrowser

null = None
true = True

with open("pr.json", 'r', encoding="utf-8") as file:
    pro = json.load(file)

df = {
        "Дата регистрации": [],
        "Номер дела": [],
        "Суд": [],
        "Тип": [],
        "Суть": [],
        "Дело": []
    }

for value in pro["Result"]["Items"]:
    df["Дата регистрации"].append(value["RegistrationDate"])
    df["Номер дела"].append(value['CaseNumber'])
    df["Суд"].append(value["Court"])
    df["Тип"].append(value['Type'])
    df["Суть"].append(value['ContentTypes'][0])
    df["Дело"].append("https://ras.arbitr.ru/Document/Pdf/"+value['CaseId']+'/'+value['Id']+'/'+ value['FileName'])

excel = pd.DataFrame(df)
excel.to_excel('info.xlsx')
