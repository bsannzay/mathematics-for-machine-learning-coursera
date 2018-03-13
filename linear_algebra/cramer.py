def start():
    print('Enter number of unknowns ex: (x, y = 2) (x, y, z = 3)')
    n = int(input())
    return readMatrix(n)

def readMatrix(n):
    print('Sequentially enter the elements of matrix n*(n+1)')
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(n + 1):
            matrix[i].append(float(input()))
    return cramer(matrix)


def det(matrix, mul = 1):
    width = len(matrix)
    if width == 1:
        return mul * matrix[0][0]
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
            total += mul * det(m, sign * matrix[0][i])
        return total


def cramer(matrix):
    n = len(matrix)
    mainMat = []
    solutions = []
    for i in range(n):
        mainMat.append([])
        for j in range(n):
            mainMat[i].append(matrix[i][j])
    mainDet = det(mainMat)

    if mainDet != 0:
        for r in range(n):
            nowMat = []
            for i in range(n):
                nowMat.append([])
                for j in range(n):
                    if j == r:
                        nowMat[i].append(matrix[i][n])
                    else:
                        nowMat[i].append(matrix[i][j])
            print('x', r+1, '=', det(nowMat) / mainDet)
            solutions.append(det(nowMat) / mainDet)
    return solutions


start()
