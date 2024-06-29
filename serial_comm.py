 import sys
import serial
from cryptography.fernet import Fernet
from infi.devicemanager import DeviceManager
import magic

# key_2 = b"fzzEp2uN2roFOku4UcyTs7gYey5dgjEUAdvCQ1ptBiBM="
key_encrypted = b'gAAAAABkjJtn26tZ5z3op2Uzi5Q1bpdma-YZlk2zqfEj-xyOajzsWklC9X5bPXwMekNAg_9wnGNdMz90X0HkWHJPG2mDor2Mx_G3Oz_87roY9sJQZaBgu4lWtg35Te3eMYvyllRnguQM'


data = [[b'gAAAAABkjLg1rIQhAuQu3IwU0h9mcMIxEISc3tYPVLppwJLj1EftCTvukKRJLlTUvi2drlezHT7uZDZpXZ3l_C1OWRVHMequdg==', 
         b'gAAAAABkjLg15iaF-fDj3FiBcymmmnczS2e4s6LUStWPCab_PoDrt5JRdY64mAf0MyW7b-HV6QS37Cy4qqfdS5DV6ji0Eayo-ksxyvYlVIy6WsBepEwcEPY=', 
         b'gAAAAABkjLg14u_DK_LP6PLN1RAmP-U4HvW9OZ2jHlKbADmWI_qtvyLAJQEk2GVirIfiIgk3F4wbhGP8FDD0uR_9ZrxfafISFQ==', 
         b'gAAAAABkjLg1oHY56kMEF4eksP1OlT_P1jis9YjMWgTNQnLs2cBYE1PNV-wK60I0Fvh35FHDjp-3VZ9FUdAD9b3bTkOpiiFUHOFcrZZqVJqKKK-0m-JKkJc='], 
        [b'gAAAAABkjLg1_gYSAYqxCkGy4V4PMuXrr4Ie1pIdC9A5l88_bhNCBLsfwZjT5HyOjWk5vn2aLsnE8x4MSx070QwYvAu6n-pmpQ==', 
         b'gAAAAABkjLg1tTmLPEXY6euWOMl_HgXyb9pjY48Gia-mCHz4Ek2otDbU9Hm8Pwmv717mLDL9gvmndbQiafHjr-SIJAlvrMm42SPAf3nZ7gUE1E6HIecscR0=', 
         b'gAAAAABkjLg1wiB2JD_P_HDAMwxleU1nUNheR9LOX9f5hnPEFQ3hNNTo-fMWzDsbNNZMIfQbBspW70L6YjXyEuLk9qPuLbzU_g==', 
         b'gAAAAABkjLg1ewTmR41GwbpnORH19gE0yLJBJ_Z7Zfq9T8xdkUesFcRCvgyS9JD02UDAPcvWk9Li-CrcY6GAp8rDdjD_2c_BuUVjoNZN-z8rmQezoO_C5EQ='], 
        [b'gAAAAABkjLg1y4UEPhY0dzD3KFPOm4mJ48Zu_xhoTvY3Cvhb7XNaArgupF047COQzePddf4OjbgYviyzzog9FWA31JIg2rLn4A==', 
         b'gAAAAABkjLg15GelPDSDtZXlPZJBo1bODJj6-FqnJ-NgGJ_5wNSCD0FuQv3Rml73PbSn20cimkoyu4p0KYx-rsrG08XoWMXIA6kIWub9gj7ewx18PH_b5Fs=', 
         b'gAAAAABkjLg1jRBNwZD9pvtUuY1fskbzFLNqeenAn6Eu4Nvq1MxDqa4kV-hU700CD4Y2hhm2jBcaskeVQRqf-wXZZWz8anRq_Q==', 
         b'gAAAAABkjLg15eVy5n32YtdXTAlxJei1s-ro5QOB2LabbUrxYDKoxEbkFHYfyJs5mtH1DJP_CRXy2yjVltp5mrEnFASTDjlYIy6sHfbp6ylOijOuSo49Dqg='], 
        [b'gAAAAABkjLg15DJd6Kup_m6dUGD64GRWrp5u9_aiLh1pFRiK9rSAQ2RNH-gHRi786f3eM8WXqTRTkFtHW1CcLroq-unl8KMOng==', 
         b'gAAAAABkjLg1s9CgTyowKt0c4FanZITXYq0At4xcLdmzNOH1a6H12U0q9i52GRirWVOK_oY_uXTHMNXtGk3LHBtBxxD_mC32lSrh_ASGPK7UQWh2H-887co=', 
         b'gAAAAABkjLg1BX6RHyrLMshZ-AJ5xCPvby4UQS5paI-tdi7LFS8awmK3VsWlrHthy11dxTHAiMbd18PiIfj8TFoy8XIzx1WCHA==', 
         b'gAAAAABkjLg1U-07nYc8PK213hhl8RX8yupBEAMxMNjmjc38bXZHxGdQbj8ETsB6xUseNHYhfT7jM4CPYX2GPWd3pYSlqbtsrG85pwWyLRljGS1e0KEMt1o='], 
        [b'gAAAAABkjLg1UGvfOPOeNIHBixQbGN02x5F1suTbUUaLpkacYYLM6jd_IXT9blqEKYk3oOf2jUMpve89iczNuv21qmdOEvH91w==', 
         b'gAAAAABkjLg1mdbQ61VQYi1PNqVFscjm9SMk1-mq3np8TV5isIeIEbTIZPvrV2RO_1QuMDlKGqu6NnWxoVBuDzRqzOjgbXdXojFEQ1l6LAb0lm_wDKEn6zs=', 
         b'gAAAAABkjLg1_kSLpzTZszgO38SFhdNHHPrzv3Wz46A1hmDN6yp1yA04CpXan33-1NNq2pvIdUBP-8h7wKtAx_-aGh10JlE81g==', 
         b'gAAAAABkjLg1XNAiEWU9E-JSebF5taGWbbRiihSM5Vt9HBxmbJ4ZVX7XhX5WzpyejvvqDspOMjclytRsYr7x43wDMCphuPPnEzhn7zct6hzPXhjWyUS9bPY=']]

class serial_com():
    def __init__(self):
        self.speeds = [9600, 115200, 1000000, 41600]
        self.serial_port = self.find_serial_port()

    def read_data(self,speed):
        ser = serial.Serial(self.serial_port, speed)
        while serial.Serial.in_waiting:
            data = ser.readline()
            if data:
                break
        ser.close()
        data = data.decode('latin-1')
        return data

    def find_serial_port(self):
        dm = DeviceManager()
        dm.root.rescan()
        devices = dm.all_devices
        for device in devices:
            result = None
            if "USB-SERIAL CH340" in device.description:
                z = str(device)
                result = z.split(" ")[-1].split("\\")[0][1:][:-2]
                break
        return result 

    def comunicator(self):
        for i in range(len(self.speeds)):
            try:
                if i != 3:
                    res = self.read_data(self.speeds[i])
                else:
                    res = self.read_data(self.speeds[i])
                    for i in range(20):
                        res = res[1:]
                # print(res.strip())
            except serial.serialutil.SerialException:
                print("Device Unavailable")
                break
        res = res.strip()
        print(res)
        return res
        # return res.strip()
    
# res = serial_com().comunicator()
def test():
    _pass = 0
    _fail = 0
    for i in range(30):
        res = serial_com().comunicator()
        print(res)
    #     if res == "Test 4":
    #         print(res, " PASS")
    #         _pass += 1
    #     else:
    #         print(res, " FAIL")
    #         _fail += 1
    # print("PASS: ", _pass)
    # print("FAIL: ", _fail)
test()       