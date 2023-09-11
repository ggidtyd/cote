#include <vector>
#include <iostream>
#define MAT vector<vector<int>>

using namespace std;

void init_result_mat(MAT& mat1, MAT& mat2, MAT& result_mat) {
    vector<int> temp_vec;
    for (int r = 0; r < mat1.size(); r++) {
        for (int c = 0; c < mat2[0].size(); c++) {
            temp_vec.push_back(0);
        }
        result_mat.push_back(temp_vec);
        temp_vec.clear();
    }
}

void mat_mul(MAT& mat1, MAT& mat2, MAT& result_mat) {
    init_result_mat(mat1, mat2, result_mat);
    int temp = 0;
    for (int r = 0; r < mat1.size(); r++) {
        for (int c = 0; c < mat2[0].size(); c++) {
            for (int r2 = 0; r2 < mat2.size(); r2++) {
                temp += mat1[r][r2] * mat2[r2][c];
            }
            result_mat[r][c] = temp;
            temp = 0;
        }
    }
}

MAT solution(MAT mat1, MAT mat2) {
    MAT mat12;
    mat_mul(mat1, mat2, mat12);
    return mat12;
}