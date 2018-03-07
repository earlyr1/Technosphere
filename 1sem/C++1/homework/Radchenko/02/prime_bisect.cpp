#include <numbers.dat>

int mid;

int bisect(int l, int r) {
	while (r - l > 1) {
		mid = (r + l) / 2;
		if (data[mid] >= a) l = mid;
		else r = mid;
	}
	return r;
}

int main(int argc, char ** argv) {
	
}