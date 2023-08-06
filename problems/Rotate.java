public static void rotate(int[][] matrix){
    int size = matrix.length;
    for(int row = 0; row < size/2; row++){
        for(int col = row; col < size - row-1; col++){
            int nw = matrix[row][col];
            int ne = matrix[col][size-row-1];
            int se = matrix[size-row-1][size-col-1];
            int sw = matrix[size-col-1][row];
            matrix[row][col] = sw;
            matrix[col][size-row-1] = nw;
            matrix[size-row-1][size-col-1] = ne; 
            matrix[size-col-1][row] = se;
        }
    }
}