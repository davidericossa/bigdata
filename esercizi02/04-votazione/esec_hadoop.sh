# creare una cartella su HDFS
hdfs dfs -mkdir /data-votazione

# caricare file nella cartella
hdfs dfs -put voti.txt /data-votazione

hadoop jar $HADOOP_MAPRED_STREAMING \
    -mapper `pwd`/votazione_map.py        \
    -reducer `pwd`/votazione_reduce.py    \
    -input /data-votazione             \
    -output /risultati-votazione

# recupero risultati
hdfs dfs -get /risultati-votazione/part-00000 risultati-votazione.txt

# cancellazione cartelle di lavoro
hdfs dfs -rm -r /data-votazione /risultati-votazione
