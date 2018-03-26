#include <vector>
#include <stdexcept>
#include <iostream>

using std::size_t;
using std::vector;

class Row {
	vector<int> vec;
public:
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
		matr = vector<Row>(n, Row(m, init));
	};
	size_t getRows() {
		return n;
	}
	size_t getColumns() {
		return m;
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
	friend bool operator== (Matrix &first, Matrix &other);
	friend bool operator!= (Matrix &first, Matrix &other);
};

bool operator ==(Matrix &first, Matrix &other) {
	if (first.getRows() != other.getRows()) return false;
	if (first.getColumns() != other.getColumns()) return false;
	for (size_t i = 0; i < first.getRows(); i++) {
		for(size_t j = 0; j < first.getColumns(); j++) {
			if (first[i][j] != other[i][j]) return false;
		}
	}
	return true;
	
}

bool operator !=(Matrix &first, Matrix &other)  {
	return !(first == other);
}

int main() {
	Matrix m1 = Matrix(3, 4);
	Matrix m2 = Matrix(3, 4);
	Matrix m3 = Matrix(4, 5, 1);
	std::cout << (m1 == m2) << " " << (m2 == m3) << std::endl;
	m3 *= 4;
	m3[0][0] = 6;
	std::cout << m3[0][1] << " " << m3[0][0] << std::endl;

}