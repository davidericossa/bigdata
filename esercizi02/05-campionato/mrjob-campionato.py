from mrjob.job import MRJob

class ElaboraRisultati(MRJob):

    def mapper(self, _, riga):
        riga=riga.strip()
        if len(riga)==0:
            return
        partita, risultato = riga.split()
        squadre=partita.split('-')
        goal=risultato.split('-')
        if int(goal[0])==int(goal[1]):
           yield (squadre[0], 1)
           yield (squadre[1], 1)
        elif int(goal[0])>int(goal[1]):
           yield (squadre[0], 3)
        else:
           yield (squadre[1], 3)
    
    def reducer(self, squadra, punti):
        yield (squadra, sum(punti))

if __name__ == '__main__':
    ElaboraRisultati.run()
