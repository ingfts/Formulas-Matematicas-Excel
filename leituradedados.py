import pandas as pd 

caminho_csv = r"C:\\Users\\ingri\\OneDrive\\Documentos\\certificados\\Analise de dados\\PESSOAS.csv"
caminho_excel = r"C:\\Users\\ingri\\OneDrive\\Documentos\\certificados\\Analise de dados\\excel.xlsx"


df = pd.read_csv(caminho_csv, sep = ",")
# print(df)
print("Arquivo lido com sucesso \n")
# funcionando bem


df.to_excel(caminho_excel, index = False)
print("Arquivo excel criado com sucesso\n")



    


