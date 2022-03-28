class Matrix() :

    @staticmethod
    def createMatrix(rows,coloumn) :
        resultMatrix = []
        print("\n")

        for i in range(rows) :
            row = [] 
            print("\nBaris ",i)
            for j in range(coloumn) :
                row.append(int(input("=> Matrix [%d,%d] = " % (i,j) )))
            resultMatrix.append(row)


        return resultMatrix


    @staticmethod
    def addMatrix(matrix1,matrix2) :
        checkSize    = len(matrix1) == len(matrix2) and len(matrix1[0]) == len(matrix2[0])
        resultMatrix = []

        if checkSize :
            for i in range(len(matrix1)) :
                row = []
                for j in range(len(matrix1[0])) :
                    row.append(matrix1[i][j]+matrix2[i][j])
                resultMatrix.append(row)

            return resultMatrix

        else :
            return "Ukuran matrix tidak sama"


    @staticmethod
    def mulMatrix(matrix1,matrix2) :
        checkSize    = len(matrix1[0]) == len(matrix2) 
        resultMatrix = [] 

        if checkSize :
            for i in range(len(matrix1)) :
                tmpResult = []
                for j in range(len(matrix2[0])) :
                    total = 0
                    for k in range(len(matrix1)) :
                        total+= matrix1[i][k]*matrix2[k][j]
                    tmpResult.append(total)
                resultMatrix.append(tmpResult)
            return resultMatrix

        else :
            return "Tidak Memenuhi"        
       

