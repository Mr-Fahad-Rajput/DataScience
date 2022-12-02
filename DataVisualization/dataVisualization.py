import sqlite3  # Import the SQLite3 module
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Connect to the database
conn = sqlite3.connect('usedcars.db')

# Create a cursor object
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS usedcars (price int, brand text,model text, year int, title_status, milage float, color text,vin text, lot int, state text, country text, condition text)''')

# Read the csv file and insert the data into the table
df = pd.read_csv('usedcars.csv')
df.to_sql('usedcars', conn, if_exists='replace', index = False)

#plot average price of distinct brands and use different colors for each brand
cursor.execute('''SELECT brand, AVG(price) FROM usedcars GROUP BY brand''')
df = pd.DataFrame(cursor.fetchall())
df.columns = [x[0] for x in cursor.description]
df.plot.bar(x='brand', y='AVG(price)', color=['red', 'blue', 'green', 'yellow', 'orange', 'purple', 'pink', 'brown', 'black', 'grey'])
plt.title('Average Price of Different Brands')
plt.xlabel('Brand')
plt.ylabel('Average Price')
plt.show()

colortest= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28]
#plot mileage vs price of brands with average price and use different colors for each brand
cursor.execute('''SELECT brand, AVG(price), AVG(mileage) FROM usedcars GROUP BY brand''')
df = pd.DataFrame(cursor.fetchall())
df.columns = [x[0] for x in cursor.description]
df.plot.scatter(x='AVG(mileage)', y='AVG(price)', c= colortest , colormap='viridis')
plt.title('Mileage vs Price of Different Brands')
plt.xlabel('Mileage')
plt.ylabel('Price')
plt.show()

#plot each state with most cars and use different colors for each state
cursor.execute('''SELECT state, COUNT(*) FROM usedcars GROUP BY state''')
df = pd.DataFrame(cursor.fetchall())
df.columns = [x[0] for x in cursor.description]
df.plot.bar(x='state', y='COUNT(*)', color=['red', 'blue', 'green', 'yellow', 'orange', 'purple', 'pink', 'brown', 'black', 'grey'])
plt.title('Number of Cars in Each State')
plt.xlabel('State')
plt.ylabel('Number of Cars')
plt.show()

#plot each state with average mileage and use different colors for each state
cursor.execute('''SELECT state, AVG(mileage) FROM usedcars GROUP BY state''')
df = pd.DataFrame(cursor.fetchall())
df.columns = [x[0] for x in cursor.description]
df.plot.bar(x='state', y='AVG(mileage)', color=['red', 'blue', 'green', 'yellow', 'orange', 'purple', 'pink', 'brown', 'black', 'grey'])
plt.title('Average Mileage of Cars in Each State')
plt.xlabel('State')
plt.ylabel('Average Mileage')
plt.show()




#plot each state with average price and use different colors for each state
cursor.execute('''SELECT state, AVG(price) FROM usedcars GROUP BY state''')
df = pd.DataFrame(cursor.fetchall())
df.columns = [x[0] for x in cursor.description]
df.plot.bar(x='state', y='AVG(price)', color=['red', 'blue', 'green', 'yellow', 'orange', 'purple', 'pink', 'brown', 'black', 'grey'])
plt.title('Average Price of Cars in Each State')
plt.xlabel('State')
plt.ylabel('Average Price')
plt.show()

colortest= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44]

#plot mileage vs price of state  and use different colors for each state
cursor.execute('''SELECT state, AVG(price), AVG(mileage) FROM usedcars GROUP BY state''')
df = pd.DataFrame(cursor.fetchall())
df.columns = [x[0] for x in cursor.description]
df.plot.scatter(x='AVG(mileage)', y='AVG(price)', c= colortest , colormap='viridis')
plt.title('Mileage vs Price of Different States')
plt.xlabel('Mileage')
plt.ylabel('Price')   
plt.show()

#plot brands where title_status is salvage Insuance and use different colors for each brand
cursor.execute('''SELECT brand, COUNT(*) FROM usedcars WHERE title_status = 'salvage insurance' GROUP BY brand''')
df = pd.DataFrame(cursor.fetchall())
df.columns = [x[0] for x in cursor.description]
df.plot.bar(x='brand', y='COUNT(*)', color=['red', 'blue', 'green', 'yellow', 'orange', 'purple', 'pink', 'brown', 'black', 'grey'])
plt.title('Number of Cars in Each Brand with Title Status Salvage Insurance')
plt.xlabel('Brand')
plt.ylabel('Number of Cars')
plt.show()


#plot state where title_status is salvage insurance and use different colors for each state
cursor.execute('''SELECT state, COUNT(*) FROM usedcars WHERE title_status = 'salvage insurance' GROUP BY state''')
df = pd.DataFrame(cursor.fetchall())
df.columns = [x[0] for x in cursor.description]
df.plot.bar(x='state', y='COUNT(*)', color=['red', 'blue', 'green', 'yellow', 'orange', 'purple', 'pink', 'brown', 'black', 'grey'])
plt.title('Number of Cars in Each State with Title Status Salvage Insurance')
plt.xlabel('State')
plt.ylabel('Number of Cars')
plt.show()

#plot state with most cars with color red and use different colors for each state
cursor.execute('''SELECT state, COUNT(*) FROM usedcars WHERE color = 'red' GROUP BY state''')
df = pd.DataFrame(cursor.fetchall())
df.columns = [x[0] for x in cursor.description]
df.plot.bar(x='state', y='COUNT(*)', color=['red', 'blue', 'green', 'yellow', 'orange', 'purple', 'pink', 'brown', 'black', 'grey'])
plt.title('Number of Cars in Each State with Color Red')
plt.xlabel('State')
plt.ylabel('Number of Cars')
plt.show()

#plot brand with most cars with color red and use different colors for each brand
cursor.execute('''SELECT brand, COUNT(*) FROM usedcars WHERE color = 'red' GROUP BY brand''')
df = pd.DataFrame(cursor.fetchall())
df.columns = [x[0] for x in cursor.description]
df.plot.bar(x='brand', y='COUNT(*)', color=['red', 'blue', 'green', 'yellow', 'orange', 'purple', 'pink', 'brown', 'black', 'grey'])
plt.title('Number of Cars in Each Brand with Color Red')
plt.xlabel('Brand')
plt.ylabel('Number of Cars')
plt.show()


# Close the connection  
conn.close()


