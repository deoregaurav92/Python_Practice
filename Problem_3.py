# import numpy as np

def main():
    in_weight = [[139,144,144,151],[149,153,153,156],[155,155,159,156],[155,155,156,156],[150,155,159,161],[160,163,162,160],[159,156,160,159],[156,156,159,159],[159,160,161,161],[161,162,161,161],[162,155,160,157],[155,155,157,157],[162,162,162,162],[161,163,161,161],[162,157,163,158],[157,157,158,158]];
    codebook_vec = [[15,15,15,15],[47,47,47,47],[79,79,79,79],[112,112,112,112],[146,146,146,146],[178,178,178,178],[210,210,210,210],[242,242,242,242]];
    # my_list = [[139,144,149,153,155,155,155,155],[144,151,153,156,159,156,156,156],[150,155,160,163,158,156,156,156],[159,161,162,160,160,159,159,159],[159,160,161,162,162,155,155,155],[161,161,161,161,160,157,157,157],[162,162,161,163,162,157,157,157],[162,162,161,161,163,158,158,158]];
    new_sum = 67154;
    c1 = 0;
    final_val = 0;
    
    for i1 in range(0,len(in_weight)):
        temp3 = [];
        min_val = 0;
        for j1 in range(0,len(codebook_vec)):
            temp1 = len(in_weight[i1]);
            temp2 = len(codebook_vec[j1]);
            sum = 0;
            for i2 in range(0,temp1):
                # for j2 in range(0,temp2):
                sum = sum + ((in_weight[i1][i2] - codebook_vec[j1][i2])**2);
                # temp3 = ((sum**0.5)//4);
            if (new_sum >= sum):
                new_sum = sum;
                # print(new_sum);
                min_val = codebook_vec[j1][0];
                min_val1= min_val;
            if min_val == min_val1:
                c1 = c1 + 1;
            if c1 > 2:
                final_val = min_val1;
                        # print(codebook_vec[j1][0]);
            # print(final_val);
            # temp3.append((sum**0.5)//4);
            # min_val = min(temp3);
            # print(sum, end=' ');
        # print(min_val);
                # result.append(temp3);
            # print(result);
            # print('\n');
        # print('\n');
    print('The Compressed Output after Vector Quantization', end= '\n');
    for i in range(0,4):
        for j in range(0,4):
            print(final_val, end=' ');
        print('\n');
    print('***************************************************************** \n');
    print('The updated CodeBook Vector:', end= '\n');
    for i in range(0,8):
        for j in range(0,4):
            if ( i == 4):
                for k in range(1):
                    print(final_val, end= ' ');
            else:
                    print(codebook_vec[i][j], end= ' ');
            # print(final_val, end=' ');
        print('\n');
            
    # count1 = 0;
    # for i in range(0,len(codebook_vec)):
        # temp = len(codebook_vec[i]);
        # for j in range(0,temp):
            # count1 = count1 + 1;
            # print(codebook_vec[i][j], end=' ');
        # print('\n');
    # print((in_weight[0][0]-codebook_vec[0][0])**2);
    
if __name__ == '__main__': main();