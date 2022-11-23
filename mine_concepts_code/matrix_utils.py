import itertools as it

def transpose_of_matrix(m):
    return zip(*m)


def get_boundaries(matrix):
    ''' Get All Boundaries Cells Position of {matrix} 
    ie First & last Rows  &
       First & last Cols

    '''
    m, n = len(matrix), len(matrix[0])

    h = it.product((0, m-1), range(n))  # Horizontal - Rows as Boundary
    v = it.product(range(m), (0, n-1))  # Vertical - cols as Boundary

    bounds = it.chain(h, v)

    return bounds