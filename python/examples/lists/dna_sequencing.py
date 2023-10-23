def get_sequences(dna):
    sequences = dna.split('X')
    sequences.sort(key=len, reverse=True)
    print(sequences)

    return [w for w in sequences if len(w) > 0]


if __name__ == '__main__':
    dna = 'ACCGXXCXXGTTACTGGGCXTTGT'
    short_sequences = get_sequences(dna)
    print(short_sequences)
