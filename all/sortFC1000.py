def reorder_train(label):
    new_label=label
    for i in range(10000):
        img=new_label.iloc[i][0]
        # find t, image #
        t=''
        for j in range(len(img)):
            if img[j]=='/':
                if img[j+4]=='.':
                    t+=img[j+1:j+4]
                elif img[j+3]=='.':
                    t+=img[j+1:j+3]
                elif img[j+5]=='.':
                    t+=img[j+1:j+5]
                elif img[j+2]=='.':
                    t+=img[j+1:j+2]
                else:
                    t+=img[j+1]
                
        new_label.set_value(i,0,int(t))
    return new_label.sort_values(by=[0])


# sort train_PooL5
pl5 = pd.DataFrame(pd.read_csv("data/features_train/features_resnet1000intermediate_train.csv", header=-1))
sorted_pl=reorder_train(pl5)
sorted_pl5 = sorted_pl.drop(0, 1).as_matrix()


# sort train_fc1000
fc1 = pd.DataFrame(pd.read_csv("data/features_train/features_resnet1000_train.csv", header=-1))
sorted_fc1=reorder_train(fc1)
sorted_fc1000 = sorted_fc1.drop(0, 1).as_matrix()





