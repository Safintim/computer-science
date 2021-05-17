# import string
# dna.translate(string.maketrans('ATCG', 'TAGC'))

def DNA_strand(dna):
    d = {
        'A': 'T',
        'T': 'A',
        'G': 'C',
        'C': 'G'
    }
    return ''.join(map(lambda x: d.get(x), dna))
