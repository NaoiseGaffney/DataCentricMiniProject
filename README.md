# Data-Centric Mini-Project ("Kicking the tyres")

1. brew install mongodb/brew/mongodb-community-shell

2. mongo "mongodb+srv://mdbcluster-vhvci.mongodb.net/TestMDB" --username mdb_c_root

3. coll = db.Names

4. coll.insert({first: "John", last: "Lennon", dob: "09/10/1940", gender: "m", hair_colour: "brown", nationality: "english", occupation: "beatle" });

## Search / View Collections

### Install MongoDB Client (see abocve for MacOSX)

> Download and install MongoDB client 4.0.6 for Atlas on AWS Cloud9
>
> wget -q https://git.io/fjzf1 -O /tmp/setupmongodb.sh && source /tmp/setupmongodb.sh
>
> Download and install MongoDB client 4.0.6 for Atlas on old Cloud9
>
> wget -q https://git.io/fh7vV -O /tmp/setupmongodb.sh && source /tmp/setupmongodb.sh

### Connect to MongoDB

> Connect to the Mongo Database on Atlas
>
> NOTE: REPLACE THE `<dbuser>` & `<dbname>` WITH YOUR OWN PERSONAL
>
> VALUES (WITHOUT THE ANGULAR BRACKETS)
>
> mongo "mongodb+srv://myfirstcluster-fsmjm.mongodb.net/<dbname>" --username <dbuser>

### Insert Data
````
db.Names.insert({
    first: 'john',
    last: 'lennon',
    dob: '09/10/1940',
    gender: 'm',
    hair_colour: 'brown',
    occupation: 'beatle',
    nationality: 'english'
});
db.Names.insert({
    first: 'eve',
    last: 'ryan',
    dob: '19/09/1992',
    gender: 'f',
    hair_colour: 'pink',
    occupation: 'developer',
    nationality: 'irish'
});
db.Names.insert({
    first: 'martha',
    last: 'fenton',
    dob: '15/05/1974',
    gender: 'f',
    hair_colour: 'brown',
    occupation: 'manager',
    nationality: 'irish'
});
db.Names.insert({
    first: 'Neil',
    last: 'Hanslem',
    dob: '14/07/1983',
    gender: 'm',
    hair_colour: 'blonde',
    occupation: 'actor',
    nationality: 'english'
});
db.Names.insert({
    first: 'Rocky',
    last: 'Persolm',
    dob: '19/12/1994',
    gender: 'f',
    hair_colour: 'black',
    occupation: 'activist',
    nationality: 'american'
});
````

````
  
// Show all collections in the current DB
show collections

// Use the `Names` collection and store a reference to it in a
// variable called `coll`
coll = db.Names;

// Create some data
coll.insert({
    first: 'john',
    last: 'lennon',
    dob: '09/10/1940',
    gender: 'm',
    hair_colour: 'brown',
    occupation: 'beatle',
    nationality: 'english'
});
coll.insert({
    first: 'eve',
    last: 'ryan',
    dob: '19/09/1992',
    gender: 'f',
    hair_colour: 'pink',
    occupation: 'developer',
    nationality: 'irish'
});
coll.insert({
    first: 'martha',
    last: 'fenton',
    dob: '15/05/1974',
    gender: 'f',
    hair_colour: 'brown',
    occupation: 'manager',
    nationality: 'irish'
});
coll.insert({
    first: 'Neil',
    last: 'Hanslem',
    dob: '14/07/1983',
    gender: 'm',
    hair_colour: 'blonde',
    occupation: 'actor',
    nationality: 'english'
});
coll.insert({
    first: 'Rocky',
    last: 'Persolm',
    dob: '19/12/1994',
    gender: 'f',
    hair_colour: 'black',
    occupation: 'activist',
    nationality: 'american'
});

// Find all of the documents in the collection
coll.find()

// Find all records that have a gender of `f`
coll.find({gender: 'f'});

// Find all records that have a gender of `f` and a
// nationality of `english`
coll.find({gender: 'f', nationality: 'english'});

// Find all records that have a gender of `f` and a
// nationality of `american` or `irish`
coll.find({gender: 'f', $or: [{nationality: 'american'}, {nationality: 'irish'}]});

// Find all records that have a gender of `f` and a
// nationality of `american` or `irish` and sort them in an
// ascending according to the nationality
coll.find({gender: 'f', $or: [{nationality: 'american'}, {nationality: 'irish'}]}).sort({nationality: 1});
```

## Update Collections

> Update the first matching record
>
> coll.update({nationality: 'irish'}, {$set: {hair_colour: 'blue'}});

> Update all matching records
>
> coll.update({nationality: 'irish'}, {$set: {hair_colour: 'purple'}},{multi:true});

## Delete Collections

> Delete a record that has a `first` of `kate` and a `last` of `bush`
>
> coll.remove({first: 'kate', last: 'bush'});
