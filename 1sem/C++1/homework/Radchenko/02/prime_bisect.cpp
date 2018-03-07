#include "numbers.dat"
#include <vector>
#include <iostream>

int LbinSearch(int key) { 
    int l = -1;                      
    int r = Size;   
    int m;
    while (l < r - 1) {              
        m = (l + r) / 2;         
        if (Data[m] < key) l = m;
        else r = m;         
    }        
    return r;
}

int RbinSearch(int key) { 
    int l = -1;                      
    int r = Size;   
    int m;
    while (l < r - 1) {              
        m = (l + r) / 2;            
        if (Data[m] <= key) l = m;
        else r = m;         
    }        
    return r;
}

void Erato(std::vector<bool> &isprime) {
	isprime[1] = false;
	for(int i = 2; i < isprime.size(); i++) {
		if (isprime[i]) {
			int k = 2;
			while (k * i < isprime.size()) {
				isprime[i * (k++)] = false;
			}
		}
	}
}

int main(int argc, char ** argv) {

	if (argc == 1 || argc % 2 == 0) return -1;
	int vec_sz = Data[Size - 1];
	std::vector<bool> isprime(vec_sz, true);
	Erato(isprime);

	for(int i = 1; i < argc; i += 2) {
		int L = std::atoi(argv[i]);
		int R = std::atoi(argv[i + 1]);
		int l = LbinSearch(L);
		int r = RbinSearch(R);
		if (Data[l] != L || r == 0 || Data[r - 1] != R) {
			std::cout << 0;
			continue;
		}
		int cnt = 0;
		while (l < r - 1) {  
			if (isprime[Data[l]]) cnt++;
			l++;
		}
		std::cout << cnt << std::endl;
	}
	return 0;
}