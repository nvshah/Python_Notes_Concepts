from collections import defaultdict
import itertools as it
import re

#Fast Compare to regex (as C implementation behind)
def findOccurrences_using_find(string, sub):
    count = start = 0
    while True:
        start = string.find(sub, start) + 1
        if start > 0:
            count+=1
        else:
            return count

#slow compare to above implementation
def findOccurrences_using_regex(string, sub):
    pattern_overlapping_count = r'(?={0})'.format(g)
    cnt = len(re.findall(pattern_overlapping_count, d))


def checkIdentical(lst):
    lst[0] == lst[-1]
    #return lst.count(lst[0]) == len(lst)    #more efficient
    #return len(set(lst)) == 1


NUMBER_OF_INTEGERS = 2

n = int(input()) #number of genes
elements = input().split()                  #genes
values = list(map(int, input().split()))    #healths

#d = defaultdict(int)

dna_strands = []

cases = int(input())

for _ in range(cases):
    i = iter(input().split())
    start, end, d = *map(int, next(zip(*it.repeat(i, 2)))), next(i)  # start & end are integer , d is string

    genes = elements[start:end+1]
    health = values[start:end+1]
    genes_health_map = defaultdict(int)

    #individual_check = [gene for gene in genes if checkIdentical(gene)]

    for k,v in zip(genes, health):
        genes_health_map[k] += v
    
    #print(genes_health_map)

    total_health = 0
    
    for gene in genes_health_map:
        cnt = d.count(gene) if not checkIdentical(gene) else findOccurrences_using_find(d, gene)
        total_health += cnt * genes_health_map[g]

    # for g in genes_health_map:
    #     pattern_overlapping_count = r'(?={0})'.format(g)
    #     cnt = len(re.findall(pattern_overlapping_count, d))
    #     #print(cnt, genes_health_map[g])
    #     total_health += cnt * genes_health_map[g]

    dna_strands.append(total_health)

print(min(dna_strands), max(dna_strands))

def getCount(string, sub):
    if len(set(string)) == 1:
        return findOccurrences_using_find(string, sub)
    else:
        return string.count(sub)




    




