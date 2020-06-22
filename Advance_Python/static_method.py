class Mobile:
    fp= 'hyy madhu'
    @staticmethod
    def show_model(m,p):
        model = m
        price = p
        print(Mobile.fp, model, price)

realme  = Mobile()
Mobile.show_model('realme', 200)    #calling argument    