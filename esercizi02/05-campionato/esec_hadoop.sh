# creare una cartella su HDFS
hdfs dfs -mkdir /data-campionato

# caricare file nella cartella
hdfs dfs -put risultati.txt /data-campionato

hadoop jar $HADOOP_MAPRED_STREAMING \
    -mapper `pwd`/campionato_map.py        \
    -reducer `pwd`/campionato_reduce.py    \
    -input /data-campionato             \
    -output /risultati-campionato

# recupero risultati
hdfs dfs -get /risultati-campionato/part-00000 campionato-finito.txt

# cancellazione cartelle di lavoro
hdfs dfs -rm -r /data-campionato /risultati-campionato
