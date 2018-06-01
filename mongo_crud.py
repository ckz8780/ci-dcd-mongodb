# A little command line script for manipulating a MongoDB database

import pymongo
import os

MONGODB_URI = os.getenv('MONGO_URI')
DBS_NAME = "mytestdb"
COLLECTION_NAME = "myFirstMDB"

# Connect to DB
def mongo_connect(url):
   try:
       conn = pymongo.MongoClient(url)
       return conn
   except pymongo.errors.ConnectionFailure as e:
       print("Could not connect to MongoDB: %s") % e

# Display options for the user
def show_menu():
    print("")
    print("1. Add a record")
    print("2. Find a record by name")
    print("3. Edit a record")
    print("4. Delete a record")
    print("5. Exit")
    
    option = input("Enter option: ")
    return option

# Get a record from the database
def get_record():
    print("")
    first_name = input("Enter first name > ").lower()
    last_name = input("Enter last name > ").lower()
    
    try:
        doc = coll.find_one({'first': first_name, 'last': last_name})
    except:
        print("Error accessing the database")
    
    if not doc:
        print("")
        print("Error! No results found.")
    
    return doc

# Add a record to the database
def add_record():
    print("")
    first_name = input("Enter first name > ").lower()
    last_name = input("Enter last name > ").lower()
    dob = input("Enter date of birth > ")
    gender = input("Enter gender > ").lower()
    hair_color = input("Enter hair colour > ").lower()
    occupation = input("Enter occupation > ").lower()
    nationality = input("Enter nationality > ").lower()
    
    new_doc = {'first': first_name, 'last': last_name, 'dob': dob, 'gender': gender, 'hair_color': hair_color, 'occupation': occupation, 'nationality': nationality}
    
    try:
        coll.insert(new_doc)
        print("")
        print("Document inserted")
    except Exception as e:
        print("Error entering data: {}".format(e))

# Find a specific record by first/last name
def find_record():
    doc = get_record()
    if doc:
        print("")
        for k, v in doc.items():
            if k != "_id":
                print(k.capitalize() + ": " + v.capitalize())

# Update/edit a specific record by first/last name
def edit_record():
    doc = get_record()
    if doc:
        update_doc = {}
        print("")
        for k, v in doc.items():
            if k != "_id":
                update_doc[k] = input(k.capitalize() + " [" + v + "] > ")
                
                # Leave data the same if user enters nothing
                if update_doc[k] == "":
                    update_doc[k] = v
        
        try:
            coll.update_one(doc, {'$set': update_doc})
            print("")
            print("Document updated")
        except Exception as e:
            print("Error updating record: {}".format(e))

# Delete a record by first/last name, with confirmation        
def delete_record():
    doc = get_record()
    if doc:
        print("")
        for k, v in doc.items():
            if k != "_id":
                print(k.capitalize() + ": " + v.capitalize())
        
        print("")
        confirmation = input("Is this the document you want to delete?\nY or N > ")
        print("")
        
        if confirmation.lower() == 'y':
            try:
                coll.remove(doc)
                print("Document deleted")
            except Exception as e:
                print("Error deleting record: {}".format(e))
        else:
            print("User cancelled operation...document not deleted!")

# Menu loop            
def main_loop():
    while True:
        option = show_menu()
        if option == "1":
            add_record()
        elif option == "2":
            find_record()
        elif option == "3":
            edit_record()
        elif option == "4":
            delete_record()
        elif option == "5":
            conn.close()
            break
        else:
            print("Invalid option")
        print("")

# Script init
conn = mongo_connect(MONGODB_URI)
coll = conn[DBS_NAME][COLLECTION_NAME]
main_loop()