def seq_sum(sequence):
    sum = 0
    for i in sequence:
        sum+=seq_sum(i)
    return sum


sequence = [1, 2, 3, [4, 5, (6, 7)]]

print(seq_sum(sequence))