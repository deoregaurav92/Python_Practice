import math

def main():
    my_list = [139,144,149,153,155,155,155,155,144,151,153,156,159,156,156,156,150,155,160,163,158,156,156,156,159,161,162,160,160,159,159,159,159,160,161,162,162,155,155,155,161,161,161,161,160,157,157,157,162,162,161,163,162,157,157,157,162,162,161,161,163,158,158,158];
    new_list = sorted(my_list);
    unique_list = [];
    c1 = 0; c2 = 0; c3 = 0; c4 = 0; c5 = 0; c6 = 0;c7 = 0; c8 = 0; 
    c9 = 0; c10 = 0; c11 = 0; c12 = 0; c13 = 0; c14=0; c15 = 0;

    for i in new_list:
        if i not in unique_list:
            unique_list.append(i);
            
    for i in new_list:
        if i == 139:
            c1 = c1 + 1;
        elif i == 144:
            c2 = c2 + 1;
        elif i == 149:
            c3 = c3 + 1;
        elif i == 150:
            c4 = c4 + 1;
        elif i == 151:
            c5 = c5 + 1;
        elif i == 153:
            c6 = c6 + 1;
        elif i == 155:
            c7 = c7 + 1;
        elif i == 156:
            c8 = c8+ 1;
        elif i == 157:
            c9 = c9 + 1;
        elif i == 158:
            c10 = c10 + 1;
        elif i == 159:
            c11 = c11 + 1;
        elif i == 160:
            c12 = c12 + 1;
        elif i == 161:
            c13 = c13 + 1;
        elif i == 162:
            c14 = c14 + 1;
        elif i == 163:
            c15 = c15 + 1;
    c1 =c1/64;    c2 =c2/64;    c3 =c3/64;    c4 =c4/64;    c5 =c5/64;    c6 =c6/64;    c7 =c7/64;    c8 =c8/64;
    c9 =c9/64;    c10 =c10/64;    c11 =c11/64;    c12 =c12/64;    c13 =c13/64;    c14 =c14/64;    c15 =c15/64;
    
    c1 = c1*(math.log2(c1));        c2 = c2*(math.log2(c2));
    c3 = c3*(math.log2(c3));        c4 = c4*(math.log2(c4));
    c5 = c5*(math.log2(c5));        c6 = c6*(math.log2(c6));
    c7 = c7*(math.log2(c7));        c8 = c8*(math.log2(c8));
    c9 = c9*(math.log2(c9));        c10 = c10*(math.log2(c10));
    c11 = c11*(math.log2(c11));     c12 = c12*(math.log2(c12));
    c13 = c13*(math.log2(c13));     c14 = c14*(math.log2(c14));
    c15 = c15*(math.log2(c15));
    
    sum = c1+ c2 + c3 + c4 + c5 + c6 + c7 + c8 + c9 + c10 + c11 + c12 + c13 + c14+ c15;
    print(f'The Entropy for 8x8 image is: {abs(sum)}');
            
if __name__ == '__main__': main();
