# PreCog_Assignments

Assignments for PreCog Selections 2020

## Brownie Points Submission

- The webapp for Twitter Analysis is live at [Arjun's Twitter Analysis](https://arjuntwitter.herokuspp.com). It is deployed on Heroku. The code is in WebApp folder. It uses a Jupyter Notebook and Voila to deploy the notebook to Heroku. The site collects 200 tweets on the Trending Hashtag in HYD and does analysis on it. It will take some time to load depending on the availability of 200 tweets on the trending topic since it uses streaming to collect the tweets.
- Insightful Extra Analysis has been done on each task and has been explained in their respective files.

## Submission Structure

### Task 1

In Task 1, I wrote a report on “How Community Feedback Shapes User Behaviour”by Justin Cheng,Cristian Danescu-Niculescu-Mizil,JureLeskovecof Stanford Universityand Max Planck Institute SWS. The submission is a pdf in the repo as Task1.pdf. All the requirements have been met.

### Task 2

The submissions for Task 2 are in the folder `Task2`
The files and their details are as follows

- twitter_analysis.ipynb - The Jupyter Notebook with Analysis on collected 10k Tweets on the hashtag #INDvAUS which was trending in HYD on 17th December Morning.
- Task2.pdf - The PDF version of the Jupyter Notebook with Analysis
- tweets.json - The 10K tweets collected on the hashtag #INDvAUS. The file has each line as a JSON string.
- twitter.py - The Python code that uses tweepy library Streaming and Twitter API to get the trending Hashtag and collect 10k tweets on that from around the globe due to the limitations of Twitter API mentioned in PDF.
- requirements.txt - Lists the python3 libraries that are required to run Task2 code. Use pip to install these.

### Task 3

#### Task A

The Task3/task_a has the submissions for Task 3 Subtask a.
The files and their details are as follows:

- pdf_reader.py - The python code that reads the PDFs and pushes them into mongodb database. It uses the tabula python library to do the same. In this file following can be changed:
  - `pdfs= ["Rec_Task/1c1edeee-a13e-4b2e-90be-eb1dd03c3384.pdf","Rec_Task/a6b29367-f3b7-4fb1-a2d0-077477eac1d9.pdf","Rec_Task/d9f8e6d9-660b-4505-86f9-952e45ca6da0.pdf","Rec_Task/EICHERMOT.pdf"]` change this to the paths of the PDF files.
  - `myclient = pymongo.MongoClient("mongodb://localhost:27017/") mydb = myclient["mydatabase"]` Change this to the mongodb and database required. It is worth noting that if the collection already exists the code drops it.
- `mongodatabase` is the mongodb dump for the given files. It can be restored using `mongorestore` command
- `Rec_Task` is the folder containing the given PDFs
- requirements.txt- has the python3 modules required to run the code. Install them using pip.

#### Task B

The Task3/task_b has the submissions for Task 3 Subtask b.The files and their details are as follows:

- Task3b.pdf - The PDF Report and Analysis done on the given dump . Includes answers and figures required.
- xml_2_db.py - The python code that parses the XML files of the dump and stores the data in mongodb. The following could be changed while executing

  - `files = [ "Posts", "Badges", "Users", "Tags", "Votes" ] ` These are the file names of .xml
  - `myclient = pymongo.MongoClient("mongodb://localhost:27017/") # Change the client if required mydb = myclient["stackoverflow"] # Database name`
  - `chunk_size=100000 # The chunk size to deposit with insert_many.. We are using insert_many because in my testing insert_one is taking lot of time`

- StackOverflowAnalysis.ipynb - The jupyter notebook containing the analysis and python code for the same.
- StackOverflowAnalysis.pdf - The PDF version of the Jupyter Notebook
- requirements.txt - as the python3 modules required to run the code. Install them using pip.
- Mongodump is uploaded on Google Drive. [Link](https://drive.google.com/drive/folders/1y_liiyeZsoFEdyG6ChLRLTIQLSpJ9gfz?usp=sharing)

##### External Resources Used

- W3 Schools for Pymongo
- Tweepy Documentation
- StackOverflow
- Mongodb Documentation
- and Documentation of other Libraies used
