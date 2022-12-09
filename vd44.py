from studert import SinhVien
def main():
    SV = [SinhVien('Lê Anh Duy', 2004, 10), SinhVien('HTNH', 2005, 11)]
    sv= sorted(SV,reverse=True)
    for item in SV:
        print(item)
if __name__=='__main__':
    main()