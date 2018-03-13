
def inputMatrix():
    nn_matrix = raw_input().split()
    total_cells =  len(nn_matrix)
    row_cells = int(total_cells**0.5)
    matrix = [nn_matrix[i:i+row_cells] for i in xrange(0, total_cells, row_cells)]
    return matrixToInt(matrix)

def matrixToInt(matrix):
    m3 = matrix
    h, w = calculate_dimensions(matrix)
    for i in range(0,h):
        for j in range(0,w):
            m3[i][j] = int(matrix[i][j])
    return m3

def calculate_dimensions(matrix):
    height = len(matrix)
    width = 1
    for item in matrix:
        width = len(item)
        break
    return height, width

def calculate_Dx(matrix):
    return

def determinat(matrix):
    heigth, width = calculate_dimensions(matrix)
  
    if heigth != width:
        print('-------')
        print(matrix)
        print(heigth)
        print(width)
        print('-------')
        return -666
    else:
        sign = -1
        total = 0
        for i in range(width):
            m = []
            for j in range(1, width):
                buff = []
                for k in range(width):
                    if k != i:
                        buff.append(matrix[j][k])
                m.append(buff)
            sign *= -1
            total += 1 * determinat(m, sign * matrix[0][i])
        return total

 