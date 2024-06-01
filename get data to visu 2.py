import mysql.connector
import matplotlib.pyplot as plt

conn = mysql.connector.connect(host='127.0.0.1', database='movies', user='root', password='mynewpassword',
                               auth_plugin='mysql_native_password')

new_data = []
all_data_to_print = []
all_actors = []
if conn.is_connected():
    sql_statement = ("SELECT kharakter.character_name, movie.title, actor.name FROM kharakter, movie, actor "
                     "WHERE kharakter.movieid=movie.movieid AND kharakter.actorid=actor.actorid;")
    cursor = conn.cursor()
    cursor.execute(sql_statement)
    rv = cursor.fetchall()
    header = ['role', 'movie title', 'actor']
    for line in rv:
        line = list(line)
        line = dict(zip(header, line))
        new_data.append(line)

for role_set in new_data:
    if role_set['actor'] not in all_actors:
        all_actors.append(role_set['actor'])

for actor_name in all_actors:
    summary = {}
    summary['actor'] = actor_name
    all_roles_of_one_actor = []
    for dataset in new_data:
        if dataset['actor'] == actor_name:
            all_roles_of_one_actor.append(dataset)
    number_of_films_acted_in = len(all_roles_of_one_actor)
    summary['movie_count'] = number_of_films_acted_in
    summary['movies'] = []
    for movie_title in all_roles_of_one_actor:
        summary['movies'].append(movie_title['movie title'])
    all_data_to_print.append(summary)

all_data_to_print.sort(key=lambda item: item['movie_count'], reverse=True)

legend = []
y = []
x = []
for actor in all_data_to_print:
    if actor['actor'] == 'Aeryk Egan' or actor['actor'] == 'Adelaide Clemens' or actor['actor'] == 'Angus T. Jones':
        x.append(actor['actor'])
        y.append(actor['movie_count'])
        for movie_title in actor['movies']:
            legend.append(movie_title)
        legend.append('---')

plt.bar(x, y)
for i, text_title in enumerate(legend, start=1):
    plt.plot([], [], ' ', label='{}'.format(str(i)) + '. ' + text_title)
plt.legend()
plt.show()
