#include <vector>
#include <stdexcept>
#include <iostream>

using std::size_t;
using std::vector;

class Row {
    
public:
    vector<int> vec;
    Row(vector<int> vect) {
        vec = vect;
    }
    Row(int m, int init) {
        vec = vector<int>(m, init);
    }
    int& operator [](size_t ind) {
        if (ind >= vec.size()) throw std::out_of_range("Out of column index");
        return vec[ind];
    }

};
class Matrix {
    vector<Row> matr;
    size_t n;
    size_t m;
public:
    Matrix(size_t N, size_t M, int init = 0) {
        n = N;
        m = M;
        matr = vector<Row> (n, Row(m, init));
    };
    size_t getRows() const {
        return m;
    }
    size_t getColumns() const {
        return n;
    }
    Row& operator[] (size_t i) {
        if (i >= n) throw std::out_of_range("Out of row index");
        return matr[i];
    }
    void operator *=(int C) {
        for (size_t i = 0; i < n; i++) {
            for(size_t j = 0; j < m; j++) {
                matr[i][j] *= C;
            }
        }
    }
    int getval(int i, int j) const {
        if (i >= n || j >= m) throw std::out_of_range("Out of row index");
        return matr[i].vec[j];
    }
    friend bool operator== (const Matrix &first, const Matrix &other);
    friend bool operator!= (const Matrix &first, const Matrix &other);
};
 
bool operator ==(const Matrix &first, const Matrix &other) {
    if (first.getRows() != other.getRows()) return false;
    if (first.getColumns() != other.getColumns()) return false;
    for (size_t i = 0; i < first.getColumns(); i++) {
        for(size_t j = 0; j < first.getRows(); j++) {
            if (first.getval(i, j) != other.getval(i, j)) return false;
        }
    }
    return true;
}

bool operator !=(const Matrix &first, const Matrix &other)  {
    return !(first == other);
}

