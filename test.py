import dataset
import pandas as pd

data = pd.read_csv('TestInput.csv')
df = pd.DataFrame(data, columns=['Name', 'Country', 'Age'])

print(df)

db = dataset.connect('sqlite:///testdb.db')

table = db['user']
for row in df.itertuples():
    table.insert(dict(Name=row.Name,
                      Age=row.Age,
                      Country=row.Country
                      )
                 )

users = db['user'].all()

for user in db['user']:
    print(user)

# db = dataset.connect('sqlite:///mydatabase.db')

# print(db.tables)
# print(db['user'].columns)
# print(len(db['user']))
# get a reference to the table 'user'
# table = db['user']

# Insert a new record.
# table.insert(dict(name='John Doe', age=46, country='China'))

# dataset will create "missing" columns any time you insert a dict with an unknown key
# table.insert(dict(name='Jane Doe', age=37, country='France', gender='female'))

# users = db['user'].all()

# for user in db['user']:
#   print(user)
