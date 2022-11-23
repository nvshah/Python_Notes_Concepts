import logging

'''
AIM :- LONGEST COMMON SUBSEQUENCE (DP) (MEMOIZING)
NOTE : matrix will hold strings as their character starting at 1...
       1st chr of str will be access via index 1 and so on...
       
       String are matched as case sensitive
'''

### GLOBALS ---------------------------------------
lcs_matrix = []
possible_lcs = set()
string_buffer = []

### FUNCTIONS -------------------------------------
def prepareMatrix(s1: str, s2: str):
    '''
    prepare matrix for memoization
    '''
    global lcs_matrix
    s2_len = len(s2)
    s1_len = len(s1)
    #initalise matrix, initially assume both string have 0 Common Length Substring
    lcs_matrix = [[0]*s2_len for _ in range(s1_len)]
    
    #provide matrix data point for given row & column
    def memberFeeder(*, row: int, col: int) -> int:
        if not (row and col):
            return 0
        elif s1[row] == s2[col]:  #same character
            return lcs_matrix[row-1][col-1] + 1 
        else:
            return max(lcs_matrix[row-1][col], lcs_matrix[row][col-1])
    
    for i in range(1, s1_len):
        for j in range(1, s2_len):
            lcs_matrix[i][j] = memberFeeder(row=i, col=j)

def findStringFrom(r: int,c: int):
    '''
    Help to search characters of longest common substring recursively
    '''
    logging.info(f':== AT position ({r},{c}) <--')
    #string search over
    if not (r and c):
        if string_buffer:
            substr = ''.join(reversed(string_buffer))
            logging.info(f':=========> Found String {substr}')
            possible_lcs.add(substr)
    elif s1[r] == s2[c]:
        logging.info(f':=========> Found Character {s1[r]}')
        string_buffer.append(s1[r])
        findStringFrom(r-1, c-1)
        ch = string_buffer.pop()
        logging.info(f':=========> Removed Character {ch}')
    else:
        cnt = lcs_matrix[r][c]
        #Look at TOP
        if cnt == lcs_matrix[r-1][c]:
            findStringFrom(r-1, c)
        #Look at LEFT
        if cnt == lcs_matrix[r][c-1]:
            findStringFrom(r, c-1)
         
def backtracking():
    '''
    backtracking to find substrings itself
    '''
    last_row = len(s1)-1
    last_col = len(s2)-1
    
    if lcs_matrix[last_row][last_col] == 0:
        return
    else:
        findStringFrom(last_row, last_col)
    
def getLogConsent():
    '''
    permission to show logs or not
    '''
    showLogs = input('\nDo you wanna display logs (for tracking) ?  { y/n } : ')
    while showLogs not in ('y', 'Y', 'n', 'N'):
        showLogs = input('invalid input ! try again : ')
    if showLogs in ('y', 'Y'):
        print('\n------------------------------------------------ Logs -----------------------------------------------------------------')
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.disable(logging.CRITICAL)
    
        
### MAIN CODE -------------------------------------

if __name__ == '__main__':
    
    getLogConsent()
    
    logging.info('***LCS Task Started*** \n')
    logging.info('=> Fetching inputs ... ')
    
    #Fetch inputs
    s1_r, s2_r = input('Enter 2 strings seperated by spaces : ').strip().split()[:2]
    #Fillers for empty string, indexing strats from 1,2,...
    s1, s2 = '#'+s1_r , '*'+s2_r  
    
    #Logic portion
    logging.info('>-------- Calculating ... --------<')
    prepareMatrix(s1, s2)
    
    #Backtracking
    logging.info('>-------- Backtracking Started --------<')
    backtracking()
    logging.info('>-------- Backtracking finished --------<')
    
    print('\n------------------------------------------------ Logs Over -----------------------------------------------------------')
    
    print('\n----------------OUTPUT REsulT-------------------')
    print('\nMATRIX(DP) :')
    for r in lcs_matrix:
        print(r)
    print(f'\nLongest Common Substring length : {lcs_matrix[-1][-1]}')
    print('\nPossible substrings :')
    for s in possible_lcs:
        print(f'-> {s}')