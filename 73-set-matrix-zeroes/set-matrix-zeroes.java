class Solution {
    public void setZeroes(int[][] matrix) {
        
        
        int row = matrix.length;
        int col = matrix[0].length;

        boolean firstRowZero = false;
        boolean firstColZero = false;
        
        // first row has any zeroes?
        for(int i=0; i<col; i++){
            if(matrix[0][i] == 0){
                firstRowZero = true;
            }
        }

        //first col has any zeroes?

        for(int j=0; j<row; j++){
            if(matrix[j][0] == 0){
                firstColZero = true;
            }
        }

        //other than first row and column checking if any other rows or cols have zeros mark zero for the for the first row and column

        for(int i=1; i<row; i++){
            for(int j=1; j<col; j++){
                if(matrix[i][j] == 0){
                    matrix[0][j] = 0;
                    matrix[i][0] = 0;
                }
            }
        }


        // set those rows and cols to zeroes
        for(int i=1; i<row; i++){
            for(int j=1; j<col; j++){
                if(matrix[0][j] == 0 || matrix[i][0] == 0){
                    matrix[i][j] = 0;
                }

                }
            }
        


        //set the first rows and cols to zero if the variables are flagged true
        if(firstRowZero == true){
            for(int i=0; i<col; i++){
                matrix[0][i] = 0;
            }
        }

        if(firstColZero == true){
            for(int i=0; i<row; i++){
                matrix[i][0] = 0;
            }
        }




    }
}