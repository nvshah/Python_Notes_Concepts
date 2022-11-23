from collections import defaultdict
import itertools as it
import re

def find_using_rabinKarp(string, sub):
    cnt = 0
    length_string, length_sub = len(string), len(sub) 
    hash_sub = hash(sub)
    for i in range(length_string - length_sub + 1):
        hs = hash(string[i:i+length_sub])
        if hs == hash_sub and string[i:i+length_sub] == sub:
            cnt+=1
    return cnt

#Fast Compare to regex (as C implementation behind)
def findOccurrences_using_find(string, sub):
    count = start = 0
    while True:
        #start = string.find(sub, start) + 1
        start = find_using_rabinKarp(string[start:], sub) + 1
        if start > 0:
            count+=1
        else:
            return count

#slow compare to above implementation
def findOccurrences_using_regex(string, sub):
    pattern_overlapping_count = r'(?={0})'.format(g)
    cnt = len(re.findall(pattern_overlapping_count, d))


def checkIdentical(lst):
    return lst[0] == lst[-1]

#NUMBER_OF_INTEGERS = 2

n = int(input('Number of Inputs :')) #number of genes
elements = input('Elements').split()
values = list(map(int, input('Values:').split()))

#d = defaultdict(int)

dna_strands = []

cases = int(input('cases:'))

for _ in range(cases):
    i = input().split()
    #start, end, d = *map(int, next(zip(*it.repeat(i, 2)))), next(i)  # start & end are integer , d is string
    start = int(i[0])
    end = int(i[1])
    d = i[2]

    # genes = elements[start:end+1]
    # health = values[start:end+1]
    # genes_health_map = defaultdict(int)

    # for k,v in zip(genes, health):
    #     genes_health_map[k] += v
    
    #print(genes_health_map)

    total_health = []

    for j in range(start, end+1):
        #pattern_overlapping_count = r'(?={0})'.format(g)
        #cnt = len(re.findall(pattern_overlapping_count, d))
        #print(cnt, genes_health_map[g])
        #print(g)
        cnt = d.count(elements[j]) if not checkIdentical(elements[j]) else find_using_rabinKarp(d, elements[j])
        total_health.append(cnt * values[j])
    
    dna_strands.append(sum(total_health))
    
    


print(min(dna_strands), max(dna_strands))

    




