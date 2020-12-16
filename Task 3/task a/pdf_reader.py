import tabula
import pymongo
import json

def read_my_pdf(filename):
    tables=[]
    try:
        tables= tabula.read_pdf(filename,pages =1,multiple_tables=True)
    except:
        print("Error: ", filename)
    return tables



if __name__ == '__main__':
    
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["mydatabase"]
    pdfs= ["Rec_Task/1c1edeee-a13e-4b2e-90be-eb1dd03c3384.pdf","Rec_Task/a6b29367-f3b7-4fb1-a2d0-077477eac1d9.pdf","Rec_Task/d9f8e6d9-660b-4505-86f9-952e45ca6da0.pdf","Rec_Task/EICHERMOT.pdf"]
    jsons=[]
    for pdf in pdfs:
        print("Converting:",pdf)
        tables_in_pdf=read_my_pdf(pdf)
        count=1
        for table in tables_in_pdf:
            print("table", count)
            filename=pdf.replace(".pdf",f"{count}.json")
            csvname=pdf.replace(".pdf",f"{count}.csv")
            c_name=pdf.replace(".pdf",f"{count}")
            table.to_json(filename)
            table.to_csv(csvname)
            jsons.append((filename,c_name))
            count+=1
        print("\n")
    for f,c in jsons:
        print(f,c)
        mycol = mydb[c]
        mycol.drop()
        with open(f) as file:
            file_data=json.load(file)
            if isinstance(file_data, list): 
                mycol.insert_many(file_data)   
            else: 
                mycol.insert_one(file_data) 
    myclient.close()


    
