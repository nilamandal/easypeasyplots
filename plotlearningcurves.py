import matplotlib.pyplot as plt
import numpy as np

files=['lr1e-2/lr1e-2.txt','lr1e-3/lr1e-3.txt','lr1e-4/lr1e-4.txt','lr1e-5/lr1e-5.txt','lr1e-6/lr1e-6.txt','lr1e-7/lr1e-7.txt','lr1e-8/lr1e-8.txt']
path='./results19/spk10-spenalty/'
for file in files:
    #figtitle=file.split('.')[0]+'.png'
    figtitle=path+file.split('.')[0]+'.png'
    f= open(path+file)
    f= f.readlines()
    #lr=f[0].split(',')
    #lr=lr[7]
    plt.figure(figsize=(18, 16))
    plt.rc('font', size=40)
    #print(temp[7])
    #plt.ylim([0,10])
    train_mse=[]
    val_mse=[]
    temp_train=[]
    for line_num in range(len(f)):
        if 'val loss and acc' in f[line_num]:
            loss= float(f[line_num+1].split(' ')[1])
            #print(loss)
            val_mse.append(loss)
        if 'train accuracy' in f[line_num]:
            train_mse.append(float(f[line_num].split('(')[1].split(',')[0]))
            #print()

            #temp_train.append(float(f[line_num+3].split(',')[0].split('(')[1]))
            #print(temp_train)
        #if len(temp_train)==703:
        #    train_mse.append(np.mean(temp_train))
        #    temp_train=[]
    print(train_mse)
    print(len(train_mse))
    print(len(val_mse))
        # if 'mse' in line:
        #     mse=float(line.split(':')[-1].strip()[:-1])
        #     #print(mse)
        #     if "Train" in line:
        #         train_mse.append(mse)
        #     elif "Validation" in line:
        #         val_mse.append(mse)
    epochs=list(range(len(train_mse)))
    plt.plot(epochs, train_mse, label='training accuracy')
    plt.plot(epochs, val_mse, label='val accuracy')
    plt.title('learning curves')
    plt.xlabel('epochs')
    plt.legend()
    plt.ylabel('accuracy (range [0,1])')
    plt.savefig(figtitle)
