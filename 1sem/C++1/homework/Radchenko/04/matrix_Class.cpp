#include <vector>
#include <stdexcept>
#include <iostream>

using std::size_t;
using std::vector;

class Row {
	vector<int> vec;
public:
	Row(vector<int> &vect): vec(vect) {};
	Row(int m, int init): vec(m, init) {};
	int& operator [](size_t ind) {
		if (ind >= vec.size()) throw std::out_of_range("Out of column index");
		return vec[ind];
	}
	const int& operator [](size_t ind) const {
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
	size_t getRows() const {
		return n;
	}
	size_t getColumns() const {
		return m;
	}
	Row& operator[] (size_t i) {
		if (i >= n) throw std::out_of_range("Out of row index");
		return matr[i];
	}
	const Row& operator[] (size_t i) const {
		if (i >= n) throw std::out_of_range("Out of row index");
		return matr[i];
	}
	Matrix& operator *=(int C) {
		for (size_t i = 0; i < n; i++) {
			for(size_t j = 0; j < m; j++) {
				matr[i][j] *= C;
			}
		}
		return *this;
	}
	bool operator ==(const Matrix &other) const {
		if ((*this).getRows() != other.getRows()) return false;
		if ((*this).getColumns() != other.getColumns()) return false;
		for (size_t i = 0; i < (*this).getRows(); i++) {
			for(size_t j = 0; j < (*this).getColumns(); j++) {
				if ((*this)[i][j] != other[i][j]) return false;
			}
		}
		return true;
	}

	bool operator !=(const Matrix &other) const {
		return !((*this) == other);
	}
};

