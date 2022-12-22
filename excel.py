
import pandas as pd

def to_excel(data):

    df = {
            "Дата регистрации": [],
            "Номер дела": [],
            "Суд": [],
            "Тип": [],
            "Суть": [],
            "Дело": []
        }

    for value in data:
        df["Дата регистрации"].append(value["RegistrationDate"])
        df["Номер дела"].append(value['CaseNumber'])
        df["Суд"].append(value["Court"])
        df["Тип"].append(value['Type'])
        df["Суть"].append(value['ContentTypes'][0])
        df["Дело"].append("https://ras.arbitr.ru/Document/Pdf/"+value['CaseId']+'/'+value['Id']+'/'+ value['FileName'])

    excel = pd.DataFrame(df)
    excel.to_excel('info.xlsx')
