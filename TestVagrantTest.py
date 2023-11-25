products =[['Leather Wallet',1100,18,1],
           ['Umbrella',900,12,4],
           ['Ciggarate',200,28,3],
           ['Honey',1000,0,2]
           ]
##########gst paid for each product#####################
gst_paid=[3,2,1,0]
for x in range(3):
    gst_paid[x]=products[x][1]*products[x][2]*products[x][3]/100


###### max gst product ################
index=0
max_paid=max(gst_paid)
for i in range(4):
    if(gst_paid[i]==max_paid):
        index=i
max_gst_product=products[index][0]
print(max_gst_product)



############price of each product #######################
price_paid=[0,1,2,3]
for i in range(4):
    if(products[i][1]<500):
        price_paid[i]=products[i][1]*products[i][3]+gst_paid[i]
    else:
        price_paid[i]=(products[i][1]*products[i][3]+gst_paid[i])*0.95

price_paid[3]=200

##########total price to be paid#####################
total_paid=0
for i in range(3):
    total_paid+=price_paid[i]

print(total_paid)