# Welcome! 

This repo demonstrates the basic usage of MongoDB via a small test database hosted on MLab. It is part of the Data Centric Development module for CodeInstitute.

#### Requirements:

- Python3
- Latest MongoDB server running locally (See install instructions for MongoDB to set this up) or, alternatively:
- An interactive environment like Cloud9 with MongoDB support
- PyMongo (`sudo pip3 install pymongo`)

#### Setup:

- Create a test MongoDB at https://www.mlab.com (Use the AWS free tier)
- Create a database called mytestdb (or change `mongo_crud.py` connection info to match your DB info)
- Create a collection called myFirstMDB (or change `mongo_crud.py` connection info to match your DB info)
- Add some documents to your collection (for faster rollout you may wish to use the sampledata.txt data. Just copy/paste it at your Mongo prompt)
- If you add your own, documents should have the following fields in order for `mongo_crud.py` to function properly:
    - first
    - last
    - dob
    - gender
    - hair_color
    - occupation
    - nationality
- `export MONGODB_URI=[your database url from mlab with username/password]` (for Windows machines, use `set` in place of `export`)

#### Usage:
    # Test your Mongo connection (you should see a data dump if it's configured correctly)
    python3 mongo_test.py
    
    # Run a simple command line app for CRUD operations on the DB
    python3 mongo_crud.py
