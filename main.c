#include<stdio.h>
void main()
{
    int a=10;
    int b=20;
    while( a > b ){ //L0 declared on time
        a = a+1;
    }
    if( b <= a ){ //L1 forward declared, never declared on time
        a = 10;
    }
    else{ // L2 forward declared, declared on time
        a = 20;
    }
    a = 100; // L3 forward declared, declared on time
    for(i=0;i<10; // L4 declared on time
    i = i+1) // L7 declared on time
    {
        a = a+1; // L6 forward declared, declared on time
    }
    printf(a);// L5 forward declared, declared on time
    printf(b);
    printf(i);
}


// a = 10
// b = 20
// L0
// T0 = a > b
// T1 = !(T0)
// if T1 goto L1
// T2 = a + 1
// a = T2
// goto L0
// L1 (implicit)
// T3 = b <= c
// T4 = !(T3)
// if T4 goto L2
// a = 10
// goto L3
// L2
// a = 20
// L3
// a = 100
// i = 0
// L4
// T5 = i < 10
// T6 = !(T5)
// if T6 goto L5
// goto L6
// L7
// T7 = i + 1
// i = T7
// goto L4
// L6
// T8 = a + 1
// a = T8
// goto L7
// L5
// T9 = x < b
// T10 = !(T9)
