import mysql.connector
import matplotlib.pyplot as plt

conn = mysql.connector.connect(host='127.0.0.1', database='movies', user='root', password='mynewpassword',
                               auth_plugin='mysql_native_password')

data = None
if conn.is_connected():
    sql_statement = ("SELECT title, release_date, rating FROM movie WHERE release_date BETWEEN '1995-01-01' and "
                     "'1995-12-31' AND rating>=7.0;")
    cursor = conn.cursor()
    cursor.execute(sql_statement)
    rv = cursor.fetchall()
    data = rv

new_data = []
header = ['title', 'date', 'rating']
for dataset in data:
    dataset = list(dataset)
    rv = dict(zip(header, dataset))
    new_data.append(rv)

new_data.sort(key=lambda item: item['date'], reverse=False)


x_axis = []
titles = []
y_axis = []
for dataset in new_data:
    x_axis.append(str(dataset['date']))
    titles.append(dataset['title'])
    y_axis.append(dataset['rating'])

print(x_axis)
print(y_axis)
print(titles)

numbers = [str(i) for i in range(1, 20)]
plt.plot(x_axis, y_axis, marker='o', label="Movie Titles:")
for x, y in (zip(x_axis, y_axis)):
    plt.text(x, y, str(y) + ' ({}.)'.format(numbers.pop(0)), color="red", fontsize=10)
for i, text_title in enumerate(titles, start=1):
    plt.plot([], [], ' ', label='{}'.format(str(i)) + '. ' + text_title)
plt.legend()
plt.show()
