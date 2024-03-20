# Trainning Data
x1 = [1.0,2.0,4.0]
x2 = [1.0,3.0,2.0]
y = [2.0,4.0,6.0]

# Initail weight
w1 = 0.0
w2 = 0.0
alpha = 0.05
b = 0.0

def gradient(w1,w2,b,x1,y):
    n=len(x1)
    del_w1 = 0.0
    del_w2 = 0.0
    del_b = 0.0
    for i in range(n):
        del_w1 += (w1*x1[i]+w2*x2[i]+b-y[i])*x1[i]
        del_w2 += (w1*x1[i]+w2*x2[i]+b-y[i])*x2[i]
        del_b += (w1*x1[i]+w2*x2[i]+b-y[i])

    del_w1 =(2/n) * del_w1
    del_w2 = (2/n) * del_w2
    del_b = (2/2)* del_b

    return del_w1,del_w2,del_b

del_w1,del_w2,del_b = gradient(w1,w2,b,x1,y)



while ((abs(del_w1) > 0.00001) and (abs(del_b) > 0.00001) and (abs(del_w2) > 0.00001)):
    w1_new = w1 - alpha * del_w1
    w2_new = w2 - alpha * del_w2
    b_new = b - alpha * del_b
    print("w1_new =" ,format(w1_new,'.6f'),",w2new =",format(w2_new,'.6f'),",b_new =",format(b_new,'.6f'))

del_w1,del_w2,del_b = gradient(w1,w2,b,x1,y)

