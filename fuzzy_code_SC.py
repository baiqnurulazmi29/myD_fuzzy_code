ulang=1
# miu ipk kurang & sedang
def n_ipk_KS(ipk):
    miu_ipk[0]=float((2.4-ipk)/0.9)
    miu_ipk[1]=float((ipk-1.5)/0.9)

# miu ipk Sedang & Tinggi
def n_ipk_ST(ipk):
    miu_ipk[1]=float((3.5-ipk)/1.1)
    miu_ipk[2]=float((ipk-2.4)/1.1)

# miu toefl kecil & sedang
def n_toefl_KS(toefl):
    miu_toefl[0]=float((500-toefl)/105)
    miu_toefl[1]=float((toefl-395)/105)

# miu toefl sedang & besar
def n_toefl_SB(toefl):
    miu_toefl[1]=float((600-toefl)/100)
    miu_toefl[2]=float((toefl-500)/100)

# miu tpa Kurang & Normal
def n_tpa_KN(tpa):
    miu_tpa[0]=float((500-tpa)/250)
    miu_tpa[1]=float((tpa-250)/250)

# miu tpa Normal & Cerdas
def n_tpa_NC(tpa):
    miu_tpa[1]=float((750-tpa)/250)
    miu_tpa[2]=float((tpa-500)/250)

# tabel inferensi
def inferensi():
    miu = []
    if (miu_ipk[0]>0 and miu_toefl[0]>0 and miu_tpa[0]>0):
        miu.append(miu_ipk[0]);  miu.append(miu_toefl[0]);  miu.append(miu_tpa[0])
        miu = sorted(miu)
        skor_tidak_layak.append(miu[0])
        miu.clear()
    if (miu_ipk[0]>0 and miu_toefl[0]>0 and miu_tpa[1]>0):
        miu.append(miu_ipk[0]);  miu.append(miu_toefl[0]);  miu.append(miu_tpa[1])
        miu = sorted(miu)
        skor_tidak_layak.append(miu[0])
        miu.clear()
    if (miu_ipk[0]>0 and miu_toefl[0]>0 and miu_tpa[2]>0):
        miu.append(miu_ipk[0]);  miu.append(miu_toefl[0]);  miu.append(miu_tpa[2])
        miu = sorted(miu)
        skor_tidak_layak.append(miu[0])
        miu.clear()
    if (miu_ipk[0]>0 and miu_toefl[1]>0 and miu_tpa[0]>0):
        miu.append(miu_ipk[0]);  miu.append(miu_toefl[1]);  miu.append(miu_tpa[0])
        miu = sorted(miu)
        skor_tidak_layak.append(miu[0])
        miu.clear()
    if (miu_ipk[0]>0 and miu_toefl[1]>0 and miu_tpa[1]>0):
        miu.append(miu_ipk[0]);  miu.append(miu_toefl[1]);  miu.append(miu_tpa[1])
        miu = sorted(miu)
        skor_layak.append(miu[0])
        miu.clear()
    if (miu_ipk[0]>0 and miu_toefl[1]>0 and miu_tpa[2]>0):
        miu.append(miu_ipk[0]);  miu.append(miu_toefl[1]);  miu.append(miu_tpa[2])
        miu = sorted(miu)
        skor_layak.append(miu[0])
        miu.clear()
    if (miu_ipk[0]>0 and miu_toefl[2]>0 and miu_tpa[0]>0):
        miu.append(miu_ipk[0]);  miu.append(miu_toefl[2]);  miu.append(miu_tpa[0])
        miu = sorted(miu)
        skor_tidak_layak.append(miu[0])
        miu.clear
    if (miu_ipk[0]>0 and miu_toefl[2]>0 and miu_tpa[1]>0):
        miu.append(miu_ipk[0]);  miu.append(miu_toefl[2]);  miu.append(miu_tpa[1])
        miu = sorted(miu)
        skor_layak.append(miu[0])
        miu.clear()
    if (miu_ipk[0]>0 and miu_toefl[2]>0 and miu_tpa[2]>0):
        miu.append(miu_ipk[0]);  miu.append(miu_toefl[2]);  miu.append(miu_tpa[2])
        miu = sorted(miu)
        skor_layak.append(miu[0])
        miu.clear()
    if (miu_ipk[1]>0 and miu_toefl[0]>0 and miu_tpa[0]>0):
        miu.append(miu_ipk[1]);  miu.append(miu_toefl[0]);  miu.append(miu_tpa[0])
        miu = sorted(miu)
        skor_tidak_layak.append(miu[0])
        miu.clear()
    if (miu_ipk[1]>0 and miu_toefl[0]>0 and miu_tpa[1]>0):
        miu.append(miu_ipk[1]);  miu.append(miu_toefl[0]);  miu.append(miu_tpa[1])
        miu = sorted(miu)
        skor_layak.append(miu[0])
        miu.clear()
    if (miu_ipk[1]>0 and miu_toefl[0]>0 and miu_tpa[2]>0):
        miu.append(miu_ipk[1]);  miu.append(miu_toefl[0]);  miu.append(miu_tpa[2])
        miu = sorted(miu)
        skor_layak.append(miu[0])
        miu.clear()
    if (miu_ipk[1]>0 and miu_toefl[1]>0 and miu_tpa[0]>0):
        miu.append(miu_ipk[1]);  miu.append(miu_toefl[1]);  miu.append(miu_tpa[0])
        miu = sorted(miu)
        skor_tidak_layak.append(miu[0])
        miu.clear()
    if (miu_ipk[1]>0 and miu_toefl[1]>0 and miu_tpa[1]>0):
        miu.append(miu_ipk[1]);  miu.append(miu_toefl[1]);  miu.append(miu_tpa[1])
        miu = sorted(miu)
        skor_layak.append(miu[0])
        miu.clear()
    if (miu_ipk[1]>0 and miu_toefl[1]>0 and miu_tpa[2]>0):
        miu.append(miu_ipk[1]);  miu.append(miu_toefl[1]);  miu.append(miu_tpa[2])
        miu = sorted(miu)
        skor_layak.append(miu[0])
        miu.clear()
    if (miu_ipk[1]>0 and miu_toefl[2]>0 and miu_tpa[0]>0):
        miu.append(miu_ipk[1]);  miu.append(miu_toefl[2]);  miu.append(miu_tpa[0])
        miu = sorted(miu)
        skor_layak.append(miu[0])
        miu.clear()
    if (miu_ipk[1]>0 and miu_toefl[2]>0 and miu_tpa[1]>0):
        miu.append(miu_ipk[1]);  miu.append(miu_toefl[2]);  miu.append(miu_tpa[1])
        miu = sorted(miu)
        skor_sangat_layak.append(miu[0])
        miu.clear()
    if (miu_ipk[1]>0 and miu_toefl[2]>0 and miu_tpa[2]>0):
        miu.append(miu_ipk[1]);  miu.append(miu_toefl[2]);  miu.append(miu_tpa[2])
        miu = sorted(miu)
        skor_sangat_layak.append(miu[0])
        miu.clear()
    if (miu_ipk[2]>0 and miu_toefl[0]>0 and miu_tpa[0]>0):
        miu.append(miu_ipk[2]);  miu.append(miu_toefl[0]);  miu.append(miu_tpa[0])
        miu = sorted(miu)
        skor_tidak_layak.append(miu[0])
        miu.clear()
    if (miu_ipk[2]>0 and miu_toefl[0]>0 and miu_tpa[1]>0):
        miu.append(miu_ipk[2]);  miu.append(miu_toefl[0]);  miu.append(miu_tpa[1])
        miu = sorted(miu)
        skor_layak.append(miu[0])
        miu.clear()
    if (miu_ipk[2]>0 and miu_toefl[0]>0 and miu_tpa[2]>0):
        miu.append(miu_ipk[2]);  miu.append(miu_toefl[0]);  miu.append(miu_tpa[2])
        miu = sorted(miu)
        skor_sangat_layak.append(miu[0])
        miu.clear()
    if (miu_ipk[2]>0 and miu_toefl[1]>0 and miu_tpa[0]>0):
        miu.append(miu_ipk[2]);  miu.append(miu_toefl[1]);  miu.append(miu_tpa[0])
        miu = sorted(miu)
        skor_layak.append(miu[0])
        miu.clear()
    if (miu_ipk[2]>0 and miu_toefl[1]>0 and miu_tpa[1]>0):
        miu.append(miu_ipk[2]);  miu.append(miu_toefl[1]);  miu.append(miu_tpa[1])
        miu = sorted(miu)
        skor_sangat_layak.append(miu[0])
        miu.clear()
    if (miu_ipk[2]>0 and miu_toefl[1]>0 and miu_tpa[2]>0):
        miu.append(miu_ipk[2]);  miu.append(miu_toefl[1]);  miu.append(miu_tpa[2])
        miu = sorted(miu)
        skor_sangat_layak.append(miu[0])
        miu.clear()
    if (miu_ipk[2]>0 and miu_toefl[2]>0 and miu_tpa[0]>0):
        miu.append(miu_ipk[2]);  miu.append(miu_toefl[2]);  miu.append(miu_tpa[0])
        miu = sorted(miu)
        skor_layak.append(miu[0])
        miu.clear()
    if (miu_ipk[2]>0 and miu_toefl[2]>0 and miu_tpa[1]>0):
        miu.append(miu_ipk[2]);  miu.append(miu_toefl[2]);  miu.append(miu_tpa[1])
        miu = sorted(miu)
        skor_sangat_layak.append(miu[0])
        miu.clear()
    if (miu_ipk[2]>0 and miu_toefl[2]>0 and miu_tpa[2]>0):
        miu.append(miu_ipk[2]);  miu.append(miu_toefl[2]);  miu.append(miu_tpa[2])
        miu = sorted(miu)
        skor_sangat_layak.append(miu[0])
        miu.clear()
    
    # urutkan dr paling besar
    skor_tidak_layak.sort(reverse=True)
    skor_layak.sort(reverse=True)
    skor_sangat_layak.sort(reverse=True)
    
    
#defuzzyfication

    

while ulang!=0:
    # miu_x[0] = rendah, [1] = sedang, [2] = tinggi
    miu_ipk=[0,0,0]
    miu_toefl=[0,0,0]
    miu_tpa=[0,0,0]

    
    
    # skor kelayakan, rendah sedang tinggi
    skor_tidak_layak=[]
     
    skor_layak=[]
    
    skor_sangat_layak=[]
    
    
    print("Exit, inputkan 0")
    try:
        ipk = float(input("Masukkan ipk: "))
        if(ipk==0):
            break
        toefl = float(input("Masukkan toefl: "))
        if(toefl==0):
            break
        tpa = float(input("Masukkan tpa: "))
        if(tpa==0):
            break
    except ValueError:
        print("\nError : Input harus angka!")
        print("---------------------------------------------------")
        continue
    
    if ipk >=0 and ipk <=4 and toefl >= 0 and toefl <= 630 and tpa >= 0 and tpa <= 750:
        # itung miu ipk
        if ipk >=0 and ipk <= 1.5:
            miu_ipk[0]=1
        elif ipk > 1.5 and ipk < 2.4:
            n_ipk_KS(ipk)
        elif ipk == 2.4 :
            miu_ipk[1]=1
        elif ipk > 2.4  and ipk < 3.5:
            n_ipk_ST(ipk)
        else:
            miu_ipk[2]=1

        # itung miu toefl
        if toefl >=0 and toefl <= 395:
            miu_toefl[0]=1
        elif toefl > 395 and toefl < 500:
            n_toefl_KS(toefl)
        elif toefl == 500:
            miu_toefl[1] = 1
        elif toefl > 500 and toefl < 600:
            n_toefl_SB(toefl)
        else:
            miu_toefl[2] = 1

        # itung miu tpa
        if tpa >=0 and tpa <= 250:
            miu_tpa[0]=1
        elif tpa > 250 and tpa < 500:
            n_tpa_KN(tpa)
        elif tpa ==500:
            miu_tpa[1] = 1
        elif tpa > 500 and tpa < 750:
            n_tpa_NC(tpa)
        else:
            miu_tpa[2] = 1
        
        
        
        inferensi()
        print("nilai linguistik skor kelayakan :" )

        print("\n---------------------------------------- ----------------------------------------\n")
        print("miu ipk =", miu_ipk)
        print("miu toefl =", miu_toefl)
        print("miu tpa =", miu_tpa)
        print("\n--------------------------------------------------------------------------------\n")
        print("tidak layak =", skor_tidak_layak)
        print("layak =", skor_layak[0])
        print("sangat layak  =", skor_sangat_layak[0])
        print("\n--------------------------------------------------------------------------------\n")
        
        tsukamoto=0.0
        mamdani = 0.0
        
        #y1 = (50-(skor_tidak_layak * (50-25)))
        y2 = (25+(skor_layak[0] *( 50-25)))
        y3 = (75-(skor_layak[0] * (75-50)))
        y4 = (50+(skor_sangat_layak[0] * (75-50)))
        
        atas = ((y2*skor_layak[0])+(y3*skor_layak[0])+(y4*skor_sangat_layak[0]))
        bawah = (skor_layak[0]*2) + skor_sangat_layak[0]
    
        atasM = (10+20+(y2*skor_layak[0])+50+(y3*skor_layak[0])+(y4*skor_sangat_layak[0]+80))
        bawahM = skor_layak[0]*2 + skor_sangat_layak[0]+1+1+1+1
        
        tsukamoto = atas/bawah
        mamdani =  (atasM/bawahM)
        
        #print("y1 : ", y1)
        print("y2 : ", y2)
        print("y3 : ", y3)
        print("y4 : ", y4)
        
        print("Tsukamoto : " ,tsukamoto)
        print("Mamdani : " ,mamdani)
        
    else:
        print("\nError : Nilai yang anda masukkan salah!")
        print("---------------------------------------------------")
