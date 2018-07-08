# Grido database

## Local env:

#### Setup mongo

- Get mongo https://www.mongodb.com/
- Run mongo:
```
[sudo] mongod [--dbpath /path/to/db/files]
```
e.g. 
```
sudo mongod --dbpath /Users/jacekdalkowski/Dev/grido/server/db/local_db_data
```
- Run mongo console client:
```
mongo
```

#### Create db and schema via console client:
```
use grido
db.createCollection('users')
db.users.insertOne({"test_key" : "test_value"})
```

#### Query db via console client:
```
show dbs
use grido
// show collections
// db.getCollectionNames()
db.users.find()
```

#### Remove via console client:
```
db.users.remove( { } )
db.users.remove( {fbId : "100000204641942" } )
db.users.remove( {"_id" : ObjectId("59c81e6e2733c03f7d0afb72")})
```
