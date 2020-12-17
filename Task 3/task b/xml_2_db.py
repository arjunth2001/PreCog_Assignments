import xml.parsers.expat
import pymongo

files = [  "Posts", "Badges", "Users", "Tags", "Votes" ]
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["stackoverflow"]
chunk_size=100000
current_chunk_size=0
chunk=[]
count=0


for file in files:
    collection = mydb[file]
    print("Starting collection:",file)
    collection.drop()
    def start_element(name, attrs):
        global chunk
        global chunk_size
        global current_chunk_size
        global count
        chunk.append(attrs)
        current_chunk_size+=1
        if current_chunk_size==chunk_size:
            collection.insert_many(chunk)
            count+=1
            print("Inserted a chunk",count)
            chunk.clear()
            current_chunk_size=0
    parser = xml.parsers.expat.ParserCreate()
    parser.StartElementHandler = start_element
    parser.ParseFile(open( "./stackoverflow.com/"+ file + ".xml", "rb"))
    try:
        if len(chunk)!=0:
            collection.insert_many(chunk)
    except Exception as e:
        #print("error with chunk: ", chunk)
        print(e)
    print("Ended collection:",file)
myclient.close()
