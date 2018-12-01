from mrjob.job import MRJob

class Conteggio(MRJob):

    def mapper(self, _, nome):
        nome=nome.strip()
        yield (nome, 1)
    
    def reducer(self, nome, voti):
        yield (nome, sum(voti))

if __name__ == '__main__':
    Conteggio.run()
