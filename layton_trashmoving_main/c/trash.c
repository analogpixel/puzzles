
#include <stdio.h>

// cc -std=c99 trash.c

int puz[] = {2,2,1,1,1,1,1,
						 2,2,1,1,1,1,1,
						 3,3,4,4,0,0,1,
						 3,3,4,4,1,1,1,
						 5,5,6,6,1,1,1,
						 7,7,8,8,1,1,1,
						 1,1,0,0,1,1,1,
						 1,1,0,0,1,1,1};

int zeros[] = {0,0,0,0,0,0,0,
						   0,0,0,0,0,0,0,
						   0,0,0,0,1,1,0,
						   0,0,0,0,0,0,0,
						   0,0,0,0,0,0,0,
						   0,0,0,0,0,0,0,
						   0,0,1,1,0,0,0,
						   0,0,1,1,0,0,0};


//                    0             1           2            3              4               5               6               7               8
int loc[][4]   = {   {0,0,0,0}, {0,0,0,0} , {0,1,7,8}, {14,15,21,22}, {16,17,23,24} , {28,29,-1,-1} , {30,31,-1,-1} , {35,36,-1,-1} , {37,38,-1,-1} };
int moves[] = {-7,7,-2,2};

// find valid moves by looking at 0 spaces and what is around them

// Given a part p (2-8)  and a move (0-3) return if that move is valid
int validMoves(int p[], int m) {
	for (int i=0; i < 4; i++) {
		if ( p[i] == -1) return 0;
		if ( zeros[p[i] + m] != 1 ) return 1;
	}
	return 0;
}

void main() {
	printf( "%d", validMoves(loc[4], 2) );
}
