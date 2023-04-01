# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class BhDonbanhang(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    id_donvi = models.ForeignKey('DmDonvi', models.DO_NOTHING, db_column='ID_DonVi')  # Field name made lowercase.
    sodonhang = models.CharField(db_column='SoDonHang', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaydonhang = models.DateTimeField(db_column='NgayDonHang')  # Field name made lowercase.
    id_doituong = models.ForeignKey('DmDoituong', models.DO_NOTHING, db_column='ID_DoiTuong', blank=True, null=True)  # Field name made lowercase.
    ngaygiaohang = models.DateTimeField(db_column='NgayGiaoHang', blank=True, null=True)  # Field name made lowercase.
    diachigiaohang = models.CharField(db_column='DiaChiGiaoHang', max_length=255, blank=True, null=True)  # Field name made lowercase.
    id_lienhe = models.ForeignKey('DmLienhe', models.DO_NOTHING, db_column='ID_LienHe', blank=True, null=True)  # Field name made lowercase.
    id_vanchuyen = models.ForeignKey('DmHinhthucvanchuyen', models.DO_NOTHING, db_column='ID_VanChuyen', blank=True, null=True)  # Field name made lowercase.
    id_hinhthucthanhtoan = models.ForeignKey('DmHinhthucthanhtoan', models.DO_NOTHING, db_column='ID_HinhThucThanhToan', blank=True, null=True)  # Field name made lowercase.
    id_ngoaite = models.ForeignKey('DmTiente', models.DO_NOTHING, db_column='ID_NgoaiTe', blank=True, null=True)  # Field name made lowercase.
    tygia = models.FloatField(db_column='TyGia')  # Field name made lowercase.
    tongtienhang = models.FloatField(db_column='TongTienHang')  # Field name made lowercase.
    tongchietkhau = models.FloatField(db_column='TongChietKhau')  # Field name made lowercase.
    tongtienthue = models.FloatField(db_column='TongTienThue')  # Field name made lowercase.
    tongchiphi = models.FloatField(db_column='TongChiPhi')  # Field name made lowercase.
    tongphaitra = models.FloatField(db_column='TongPhaiTra')  # Field name made lowercase.
    diengiai = models.CharField(db_column='DienGiai', max_length=500, blank=True, null=True)  # Field name made lowercase.
    usertao = models.CharField(db_column='UserTao', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaytao = models.DateTimeField(db_column='NgayTao', blank=True, null=True)  # Field name made lowercase.
    usersuacuoi = models.CharField(db_column='UserSuaCuoi', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaysuacuoi = models.DateTimeField(db_column='NgaySuaCuoi', blank=True, null=True)  # Field name made lowercase.
    id_nhanvien = models.ForeignKey('DmNhanvien', models.DO_NOTHING, db_column='ID_NhanVien', blank=True, null=True)  # Field name made lowercase.
    chuaduyet_duyet_huy = models.IntegerField(db_column='ChuaDuyet_Duyet_Huy', blank=True, null=True)  # Field name made lowercase.
    id_quatrinh = models.CharField(db_column='ID_QuaTrinh', max_length=36, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BH_DonBanHang'


class BhDonbanhangChitiet(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    id_donbanhang = models.ForeignKey(BhDonbanhang, models.DO_NOTHING, db_column='ID_DonBanHang')  # Field name made lowercase.
    sothutu = models.IntegerField(db_column='SoThuTu', blank=True, null=True)  # Field name made lowercase.
    id_kho = models.ForeignKey('DmKho', models.DO_NOTHING, db_column='ID_Kho', blank=True, null=True)  # Field name made lowercase.
    id_hanghoa = models.ForeignKey('DmHanghoa', models.DO_NOTHING, db_column='ID_HangHoa')  # Field name made lowercase.
    id_mavach = models.CharField(db_column='ID_MaVach', max_length=36, blank=True, null=True)  # Field name made lowercase.
    mavach = models.CharField(db_column='MaVach', max_length=50, blank=True, null=True)  # Field name made lowercase.
    id_lohang = models.ForeignKey('DmLohang', models.DO_NOTHING, db_column='ID_LoHang', blank=True, null=True)  # Field name made lowercase.
    id_donvitinh = models.ForeignKey('DmDonvitinh', models.DO_NOTHING, db_column='ID_DonViTinh')  # Field name made lowercase.
    soluong = models.FloatField(db_column='SoLuong')  # Field name made lowercase.
    dongia = models.FloatField(db_column='DonGia')  # Field name made lowercase.
    thanhtien = models.FloatField(db_column='ThanhTien')  # Field name made lowercase.
    ptchietkhau = models.FloatField(db_column='PTChietKhau')  # Field name made lowercase.
    tienchietkhau = models.FloatField(db_column='TienChietKhau')  # Field name made lowercase.
    ptthue = models.FloatField(db_column='PTThue')  # Field name made lowercase.
    tienthuesuat = models.FloatField(db_column='TienThueSuat')  # Field name made lowercase.
    tienphaitra = models.FloatField(db_column='TienPhaiTra')  # Field name made lowercase.
    tralaivattuthaythe = models.BooleanField(db_column='TraLaiVatTuThayThe', blank=True, null=True)  # Field name made lowercase.
    ghichu = models.TextField(db_column='GhiChu', blank=True, null=True)  # Field name made lowercase.
    soluong_yeucau = models.FloatField(db_column='SoLuong_YeuCau', blank=True, null=True)  # Field name made lowercase.
    tenhanghoathaythe = models.TextField(db_column='TenHangHoaThayThe', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BH_DonBanHang_ChiTiet'


class BhDonmuahang(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    id_donvi = models.ForeignKey('DmDonvi', models.DO_NOTHING, db_column='ID_DonVi')  # Field name made lowercase.
    sodonhang = models.CharField(db_column='SoDonHang', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaydonhang = models.DateTimeField(db_column='NgayDonHang')  # Field name made lowercase.
    ngaygiaohang = models.DateTimeField(db_column='NgayGiaoHang', blank=True, null=True)  # Field name made lowercase.
    id_doituong = models.ForeignKey('DmDoituong', models.DO_NOTHING, db_column='ID_DoiTuong', blank=True, null=True)  # Field name made lowercase.
    id_lienhe = models.ForeignKey('DmLienhe', models.DO_NOTHING, db_column='ID_LienHe', blank=True, null=True)  # Field name made lowercase.
    id_vanchuyen = models.ForeignKey('DmHinhthucvanchuyen', models.DO_NOTHING, db_column='ID_VanChuyen', blank=True, null=True)  # Field name made lowercase.
    diachigiaohang = models.CharField(db_column='DiaChiGiaoHang', max_length=255, blank=True, null=True)  # Field name made lowercase.
    id_hinhthucthanhtoan = models.ForeignKey('DmHinhthucthanhtoan', models.DO_NOTHING, db_column='ID_HinhThucThanhToan', blank=True, null=True)  # Field name made lowercase.
    id_ngoaite = models.ForeignKey('DmTiente', models.DO_NOTHING, db_column='ID_NgoaiTe', blank=True, null=True)  # Field name made lowercase.
    tygia = models.FloatField(db_column='TyGia')  # Field name made lowercase.
    tongtienhang = models.FloatField(db_column='TongTienHang')  # Field name made lowercase.
    tongchietkhau = models.FloatField(db_column='TongChietKhau')  # Field name made lowercase.
    tongtienthue = models.FloatField(db_column='TongTienThue')  # Field name made lowercase.
    tongchiphi = models.FloatField(db_column='TongChiPhi')  # Field name made lowercase.
    tongphaitra = models.FloatField(db_column='TongPhaiTra')  # Field name made lowercase.
    diengiai = models.CharField(db_column='DienGiai', max_length=500, blank=True, null=True)  # Field name made lowercase.
    usertao = models.CharField(db_column='UserTao', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngayvaoso = models.DateTimeField(db_column='NgayVaoSo', blank=True, null=True)  # Field name made lowercase.
    usersuacuoi = models.CharField(db_column='UserSuaCuoi', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaysuacuoi = models.DateTimeField(db_column='NgaySuaCuoi', blank=True, null=True)  # Field name made lowercase.
    id_nhanvien = models.ForeignKey('DmNhanvien', models.DO_NOTHING, db_column='ID_NhanVien', blank=True, null=True)  # Field name made lowercase.
    chuaduyet_duyet_huy = models.IntegerField(db_column='ChuaDuyet_Duyet_Huy', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BH_DonMuaHang'


class BhDonmuahangChitiet(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    id_donmuahang = models.ForeignKey(BhDonmuahang, models.DO_NOTHING, db_column='ID_DonMuaHang')  # Field name made lowercase.
    sothutu = models.IntegerField(db_column='SoThuTu', blank=True, null=True)  # Field name made lowercase.
    id_hanghoa = models.ForeignKey('DmHanghoa', models.DO_NOTHING, db_column='ID_HangHoa')  # Field name made lowercase.
    id_mavach = models.CharField(db_column='ID_MaVach', max_length=36, blank=True, null=True)  # Field name made lowercase.
    mavach = models.CharField(db_column='MaVach', max_length=50, blank=True, null=True)  # Field name made lowercase.
    theolo = models.BooleanField(db_column='TheoLo')  # Field name made lowercase.
    id_lohang = models.ForeignKey('DmLohang', models.DO_NOTHING, db_column='ID_LoHang', blank=True, null=True)  # Field name made lowercase.
    id_kho = models.ForeignKey('DmKho', models.DO_NOTHING, db_column='ID_Kho', blank=True, null=True)  # Field name made lowercase.
    id_donvitinh = models.ForeignKey('DmDonvitinh', models.DO_NOTHING, db_column='ID_DonViTinh')  # Field name made lowercase.
    soluong = models.FloatField(db_column='SoLuong')  # Field name made lowercase.
    dongia = models.FloatField(db_column='DonGia')  # Field name made lowercase.
    thanhtien = models.FloatField(db_column='ThanhTien')  # Field name made lowercase.
    ptchietkhau = models.FloatField(db_column='PTChietKhau')  # Field name made lowercase.
    tienchietkhau = models.FloatField(db_column='TienChietKhau')  # Field name made lowercase.
    id_thuesuat = models.ForeignKey('DmThuesuat', models.DO_NOTHING, db_column='ID_ThueSuat', blank=True, null=True)  # Field name made lowercase.
    tienthuesuat = models.FloatField(db_column='TienThueSuat')  # Field name made lowercase.
    tienphaitra = models.FloatField(db_column='TienPhaiTra')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BH_DonMuaHang_ChiTiet'


class BhMuahang(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    id_donvi = models.ForeignKey('DmDonvi', models.DO_NOTHING, db_column='ID_DonVi', blank=True, null=True)  # Field name made lowercase.
    sochungtu = models.CharField(db_column='SoChungTu', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaychungtu = models.DateTimeField(db_column='NgayChungTu')  # Field name made lowercase.
    id_doituong = models.ForeignKey('DmDoituong', models.DO_NOTHING, db_column='ID_DoiTuong', blank=True, null=True)  # Field name made lowercase.
    id_ngoaite = models.ForeignKey('DmTiente', models.DO_NOTHING, db_column='ID_NgoaiTe', blank=True, null=True)  # Field name made lowercase.
    id_donmuahang = models.ForeignKey(BhDonmuahang, models.DO_NOTHING, db_column='ID_DonMuaHang', blank=True, null=True)  # Field name made lowercase.
    id_nhanvien = models.ForeignKey('DmNhanvien', models.DO_NOTHING, db_column='ID_NhanVien', blank=True, null=True)  # Field name made lowercase.
    nguoigiao = models.CharField(db_column='NguoiGiao', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tygia = models.FloatField(db_column='TyGia')  # Field name made lowercase.
    tongtienhang = models.FloatField(db_column='TongTienHang')  # Field name made lowercase.
    tongchietkhau = models.FloatField(db_column='TongChietKhau')  # Field name made lowercase.
    tongtienthue = models.FloatField(db_column='TongTienThue')  # Field name made lowercase.
    tongchiphi = models.FloatField(db_column='TongChiPhi')  # Field name made lowercase.
    tongphaitra = models.FloatField(db_column='TongPhaiTra')  # Field name made lowercase.
    diengiai = models.CharField(db_column='DienGiai', max_length=500, blank=True, null=True)  # Field name made lowercase.
    userlap = models.CharField(db_column='UserLap', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngayvaoso = models.DateTimeField(db_column='NgayVaoSo', blank=True, null=True)  # Field name made lowercase.
    usersuacuoi = models.CharField(db_column='UserSuaCuoi', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaysuacuoi = models.DateTimeField(db_column='NgaySuaCuoi', blank=True, null=True)  # Field name made lowercase.
    duocphepsua = models.IntegerField(db_column='DuocPhepSua', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BH_MuaHang'


class BhMuahangChitiet(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    id_muahang = models.ForeignKey(BhMuahang, models.DO_NOTHING, db_column='ID_MuaHang')  # Field name made lowercase.
    sothutu = models.IntegerField(db_column='SoThuTu', blank=True, null=True)  # Field name made lowercase.
    id_hanghoa = models.ForeignKey('DmHanghoa', models.DO_NOTHING, db_column='ID_HangHoa')  # Field name made lowercase.
    id_mavach = models.CharField(db_column='ID_MaVach', max_length=36, blank=True, null=True)  # Field name made lowercase.
    mavach = models.CharField(db_column='MaVach', max_length=50, blank=True, null=True)  # Field name made lowercase.
    id_lohang = models.ForeignKey('DmLohang', models.DO_NOTHING, db_column='ID_LoHang', blank=True, null=True)  # Field name made lowercase.
    id_kho = models.ForeignKey('DmKho', models.DO_NOTHING, db_column='ID_Kho', blank=True, null=True)  # Field name made lowercase.
    id_donvitinh = models.ForeignKey('DmDonvitinh', models.DO_NOTHING, db_column='ID_DonViTinh')  # Field name made lowercase.
    soluong = models.FloatField(db_column='SoLuong')  # Field name made lowercase.
    dongia = models.FloatField(db_column='DonGia')  # Field name made lowercase.
    thanhtien = models.FloatField(db_column='ThanhTien')  # Field name made lowercase.
    ptchietkhau = models.FloatField(db_column='PTChietKhau')  # Field name made lowercase.
    tienchietkhau = models.FloatField(db_column='TienChietKhau')  # Field name made lowercase.
    id_thuesuat = models.ForeignKey('DmThuesuat', models.DO_NOTHING, db_column='ID_ThueSuat', blank=True, null=True)  # Field name made lowercase.
    tienthuesuat = models.FloatField(db_column='TienThueSuat')  # Field name made lowercase.
    tienchiphi = models.FloatField(db_column='TienChiPhi')  # Field name made lowercase.
    tienphaitra = models.FloatField(db_column='TienPhaiTra')  # Field name made lowercase.
    ghichu = models.TextField(db_column='GhiChu', blank=True, null=True)  # Field name made lowercase.
    ghichu2 = models.TextField(db_column='GhiChu2', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BH_MuaHang_ChiTiet'


class Bangluong(models.Model):
    id_nhanvien = models.CharField(db_column='ID_NhanVien', max_length=36, blank=True, null=True)  # Field name made lowercase.
    luongtuvan = models.FloatField(db_column='LuongTuVan', blank=True, null=True)  # Field name made lowercase.
    luongdoanhso = models.FloatField(db_column='LuongDoanhSo', blank=True, null=True)  # Field name made lowercase.
    khoancong = models.FloatField(db_column='KhoanCong', blank=True, null=True)  # Field name made lowercase.
    khoantru = models.FloatField(db_column='KhoanTru', blank=True, null=True)  # Field name made lowercase.
    thang = models.DecimalField(db_column='Thang', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    nam = models.DecimalField(db_column='Nam', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BangLuong'


class Baocaoquyca(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    id_nhanvien = models.CharField(db_column='ID_NhanVien', max_length=36, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=50)  # Field name made lowercase.
    thoigianbatdau = models.DateTimeField(db_column='ThoiGianBatDau')  # Field name made lowercase.
    thoigianketthuc = models.DateTimeField(db_column='ThoiGianKetThuc', blank=True, null=True)  # Field name made lowercase.
    id_donvi = models.CharField(db_column='ID_DonVi', max_length=36)  # Field name made lowercase.
    tienmat_dauca = models.FloatField(db_column='TienMat_DauCa')  # Field name made lowercase.
    tienthutrongca = models.FloatField(db_column='TienThuTrongCa')  # Field name made lowercase.
    tienbangiaolai = models.FloatField(db_column='TienBanGiaoLai')  # Field name made lowercase.
    tienmat_cuoica = models.FloatField(db_column='TienMat_CuoiCa')  # Field name made lowercase.
    tongtienhang = models.FloatField(db_column='TongTienHang')  # Field name made lowercase.
    tongtienck = models.FloatField(db_column='TongTienCK')  # Field name made lowercase.
    tongtienthue = models.FloatField(db_column='TongTienThue')  # Field name made lowercase.
    tongtiencktoanhd = models.FloatField(db_column='TongTienCKToanHD')  # Field name made lowercase.
    tongtienphaithanhtoan = models.FloatField(db_column='TongTienPhaiThanhToan')  # Field name made lowercase.
    tongtiendathu = models.FloatField(db_column='TongTienDaThu')  # Field name made lowercase.
    dathu_tienmat = models.FloatField(db_column='DaThu_TienMat')  # Field name made lowercase.
    dathu_tiengui = models.FloatField(db_column='DaThu_TienGui')  # Field name made lowercase.
    dathu_thegiamgia = models.FloatField(db_column='DaThu_TheGiamGia')  # Field name made lowercase.
    dathu_thegiatri = models.FloatField(db_column='DaThu_TheGiaTri')  # Field name made lowercase.
    dathu_diemtichluy = models.FloatField(db_column='DaThu_DiemTichLuy')  # Field name made lowercase.
    tongtiendoitralai = models.FloatField(db_column='TongTienDoiTraLai')  # Field name made lowercase.
    tongtienthucte = models.FloatField(db_column='TongTienThucTe')  # Field name made lowercase.
    conthieu = models.FloatField(db_column='ConThieu')  # Field name made lowercase.
    daketthucca = models.BooleanField(db_column='DaKetThucCa')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BaoCaoQuyCa'


class Chbangluongtheomucdoanhthu(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    bophan = models.CharField(db_column='BoPhan', max_length=36, blank=True, null=True)  # Field name made lowercase.
    doanhso_min = models.FloatField(db_column='DoanhSo_Min')  # Field name made lowercase.
    doanhso_max = models.FloatField(db_column='DoanhSo_Max', blank=True, null=True)  # Field name made lowercase.
    lathochinh = models.BooleanField(db_column='LaThoChinh')  # Field name made lowercase.
    luongduocnhan = models.FloatField(db_column='LuongDuocNhan')  # Field name made lowercase.
    luongtheopt = models.BooleanField(db_column='LuongTheoPT')  # Field name made lowercase.
    tungay = models.DateTimeField(db_column='TuNgay')  # Field name made lowercase.
    denngay = models.DateTimeField(db_column='DenNgay', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CHBangLuongTheoMucDoanhThu'


class Chgiamtrubangluong(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    id_bophantra = models.CharField(db_column='ID_BoPhanTra', max_length=36)  # Field name made lowercase.
    lathochinh = models.BooleanField(db_column='LaThoChinh')  # Field name made lowercase.
    id_bophannhan = models.CharField(db_column='ID_BoPhanNhan', max_length=36)  # Field name made lowercase.
    luonggiamtru = models.FloatField(db_column='LuongGiamTru')  # Field name made lowercase.
    laphantram = models.BooleanField(db_column='LaPhanTram')  # Field name made lowercase.
    tungay = models.DateTimeField(db_column='TuNgay')  # Field name made lowercase.
    denngay = models.DateTimeField(db_column='DenNgay', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CHGiamTruBangLuong'


class Cauhinhbangluong(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    id_donvi = models.CharField(db_column='ID_DonVi', max_length=36)  # Field name made lowercase.
    songaycongmd_thang = models.FloatField(db_column='SoNgayCongMD_Thang')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CauHinhBangLuong'


class Cauhinhhomthu(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    diachiemail = models.TextField(db_column='DiaChiEmail')  # Field name made lowercase.
    matkhau = models.TextField(db_column='MatKhau', blank=True, null=True)  # Field name made lowercase.
    usersohuu = models.CharField(db_column='UserSoHuu', max_length=50)  # Field name made lowercase.
    maychu_gui = models.TextField(db_column='MayChu_Gui', blank=True, null=True)  # Field name made lowercase.
    cong_gui = models.IntegerField(db_column='Cong_Gui', blank=True, null=True)  # Field name made lowercase.
    ssl_gui = models.BooleanField(db_column='SSL_Gui', blank=True, null=True)  # Field name made lowercase.
    maychu_nhan = models.TextField(db_column='MayChu_Nhan', blank=True, null=True)  # Field name made lowercase.
    cong_nhan = models.IntegerField(db_column='Cong_Nhan', blank=True, null=True)  # Field name made lowercase.
    ssl_nhan = models.BooleanField(db_column='SSL_Nhan', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CauHinhHomThu'


class ChietkhaumacdinhNhanvien(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    id_sanpham = models.ForeignKey('DmHanghoa', models.DO_NOTHING, db_column='ID_SanPham', blank=True, null=True)  # Field name made lowercase.
    nhanvien = models.ForeignKey('DmNhanvien', models.DO_NOTHING, db_column='NhanVien', blank=True, null=True)  # Field name made lowercase.
    chietkhau = models.FloatField(db_column='ChietKhau')  # Field name made lowercase.
    laphantram = models.BooleanField(db_column='LaPhanTram')  # Field name made lowercase.
    id_nhomnhanvien = models.ForeignKey('DmDonvi', models.DO_NOTHING, db_column='ID_NhomNhanVien', blank=True, null=True)  # Field name made lowercase.
    theonhomnhanvien = models.BooleanField(db_column='TheoNhomNhanVien')  # Field name made lowercase.
    id_nhomhanghoa = models.ForeignKey('DmNhomhanghoa', models.DO_NOTHING, db_column='ID_NhomHangHoa', blank=True, null=True)  # Field name made lowercase.
    theonhomhanghoa = models.BooleanField(db_column='TheoNhomHangHoa')  # Field name made lowercase.
    chietkhau_yeucau = models.FloatField(db_column='ChietKhau_YeuCau', blank=True, null=True)  # Field name made lowercase.
    laphantram_yeucau = models.BooleanField(db_column='LaPhanTram_YeuCau', blank=True, null=True)  # Field name made lowercase.
    chietkhautuvan = models.BooleanField(db_column='ChietKhauTuVan', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ChietKhauMacDinh_NhanVien'


class CongdoanDichvu(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    id_dichvu = models.CharField(db_column='ID_DichVu', max_length=36)  # Field name made lowercase.
    stt = models.IntegerField(db_column='STT')  # Field name made lowercase.
    id_congdoan = models.CharField(db_column='ID_CongDoan', max_length=36)  # Field name made lowercase.
    thoigian = models.TextField(db_column='ThoiGian', blank=True, null=True)  # Field name made lowercase.
    sophutthuchien = models.FloatField(db_column='SoPhutThucHien', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CongDoan_DichVu'


class Congnodauki(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    id_donvi = models.CharField(db_column='ID_DonVi', max_length=36)  # Field name made lowercase.
    id_doituong = models.ForeignKey('DmDoituong', models.DO_NOTHING, db_column='ID_DoiTuong')  # Field name made lowercase.
    namhachtoan = models.IntegerField(db_column='NamHachToan')  # Field name made lowercase.
    laphaithu = models.BooleanField(db_column='LaPhaiThu')  # Field name made lowercase.
    sotien = models.FloatField(db_column='SoTien')  # Field name made lowercase.
    id_tiente = models.CharField(db_column='ID_TienTe', max_length=36, blank=True, null=True)  # Field name made lowercase.
    tygia = models.FloatField(db_column='TyGia')  # Field name made lowercase.
    usertao = models.CharField(db_column='UserTao', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngayvaoso = models.DateTimeField(db_column='NgayVaoSo', blank=True, null=True)  # Field name made lowercase.
    usersuacuoi = models.CharField(db_column='UserSuaCuoi', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaysuacuoi = models.DateTimeField(db_column='NgaySuaCuoi', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CongNoDauKi'


class Conversation(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    username = models.TextField(db_column='Username')  # Field name made lowercase.
    postdatetime = models.DateTimeField(db_column='PostDateTime')  # Field name made lowercase.
    messagebody = models.TextField(db_column='MessageBody')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Conversation'


class DmChucvu(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    machucvu = models.CharField(db_column='MaChucVu', max_length=50)  # Field name made lowercase.
    tenchucvu = models.CharField(db_column='TenChucVu', max_length=255)  # Field name made lowercase.
    ghichu = models.CharField(db_column='GhiChu', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DM_ChucVu'


class DmDacdiemkhachhang(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    madacdiem = models.CharField(db_column='MaDacDiem', max_length=50)  # Field name made lowercase.
    tendacdiem = models.TextField(db_column='TenDacDiem')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DM_DacDiemKhachHang'


class DmDoituong(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    loaidoituong = models.IntegerField(db_column='LoaiDoiTuong')  # Field name made lowercase.
    lacanhan = models.BooleanField(db_column='LaCaNhan')  # Field name made lowercase.
    id_nhomdoituong = models.ForeignKey('DmNhomdoituong', models.DO_NOTHING, db_column='ID_NhomDoiTuong', blank=True, null=True)  # Field name made lowercase.
    madoituong = models.CharField(db_column='MaDoiTuong', max_length=50)  # Field name made lowercase.
    tendoituong = models.TextField(db_column='TenDoiTuong')  # Field name made lowercase.
    dienthoai = models.TextField(db_column='DienThoai', blank=True, null=True)  # Field name made lowercase.
    fax = models.TextField(db_column='Fax', blank=True, null=True)  # Field name made lowercase.
    email = models.TextField(db_column='Email', blank=True, null=True)  # Field name made lowercase.
    website = models.TextField(db_column='Website', blank=True, null=True)  # Field name made lowercase.
    anh = models.BinaryField(db_column='Anh', blank=True, null=True)  # Field name made lowercase.
    masothue = models.TextField(db_column='MaSoThue', blank=True, null=True)  # Field name made lowercase.
    taikhoannganhang = models.TextField(db_column='TaiKhoanNganHang', blank=True, null=True)  # Field name made lowercase.
    gioihancongno = models.FloatField(db_column='GioiHanCongNo', blank=True, null=True)  # Field name made lowercase.
    ghichu = models.TextField(db_column='GhiChu', blank=True, null=True)  # Field name made lowercase.
    id_tinhthanh = models.CharField(db_column='ID_TinhThanh', max_length=36, blank=True, null=True)  # Field name made lowercase.
    ngaysinh_ngaytlap = models.DateTimeField(db_column='NgaySinh_NgayTLap', blank=True, null=True)  # Field name made lowercase.
    chiase = models.BooleanField(db_column='ChiaSe')  # Field name made lowercase.
    theodoi = models.BooleanField(db_column='TheoDoi')  # Field name made lowercase.
    usertao = models.CharField(db_column='UserTao', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaynhap = models.DateTimeField(db_column='NgayNhap', blank=True, null=True)  # Field name made lowercase.
    usersuacuoi = models.CharField(db_column='UserSuaCuoi', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaysuacuoi = models.DateTimeField(db_column='NgaySuaCuoi', blank=True, null=True)  # Field name made lowercase.
    id_index = models.IntegerField(db_column='ID_Index', blank=True, null=True)  # Field name made lowercase.
    theodoivantay = models.BooleanField(db_column='TheoDoiVanTay', blank=True, null=True)  # Field name made lowercase.
    id_quanhuyen = models.CharField(db_column='ID_QuanHuyen', max_length=36, blank=True, null=True)  # Field name made lowercase.
    id_nhanvienphutrach = models.CharField(db_column='ID_NhanVienPhuTrach', max_length=36, blank=True, null=True)  # Field name made lowercase.
    ngaydoinhom = models.DateTimeField(db_column='NgayDoiNhom', blank=True, null=True)  # Field name made lowercase.
    diemkhoitao = models.FloatField(db_column='DiemKhoiTao', blank=True, null=True)  # Field name made lowercase.
    doanhsokhoitao = models.FloatField(db_column='DoanhSoKhoiTao', blank=True, null=True)  # Field name made lowercase.
    id_nguoigioithieu = models.CharField(db_column='ID_NguoiGioiThieu', max_length=36, blank=True, null=True)  # Field name made lowercase.
    id_nguonkhach = models.CharField(db_column='ID_NguonKhach', max_length=36, blank=True, null=True)  # Field name made lowercase.
    captai_dkkd = models.TextField(db_column='CapTai_DKKD', blank=True, null=True)  # Field name made lowercase.
    diachi = models.TextField(db_column='DiaChi', blank=True, null=True)  # Field name made lowercase.
    gioitinhnam = models.BooleanField(db_column='GioiTinhNam', blank=True, null=True)  # Field name made lowercase.
    nganhang = models.TextField(db_column='NganHang', blank=True, null=True)  # Field name made lowercase.
    ngaycapcmtnd_dkkd = models.DateTimeField(db_column='NgayCapCMTND_DKKD', blank=True, null=True)  # Field name made lowercase.
    noicapcmtnd_dkkd = models.TextField(db_column='NoiCapCMTND_DKKD', blank=True, null=True)  # Field name made lowercase.
    sdt_coquan = models.CharField(db_column='SDT_CoQuan', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sdt_nharieng = models.CharField(db_column='SDT_NhaRieng', max_length=255, blank=True, null=True)  # Field name made lowercase.
    socmtnd_dkkd = models.CharField(db_column='SoCMTND_DKKD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    thuongtru = models.TextField(db_column='ThuongTru', blank=True, null=True)  # Field name made lowercase.
    xungho = models.CharField(db_column='XungHo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    id_quocgia = models.CharField(db_column='ID_QuocGia', max_length=36, blank=True, null=True)  # Field name made lowercase.
    ngaygiaodichgannhat = models.DateTimeField(db_column='NgayGiaoDichGanNhat', blank=True, null=True)  # Field name made lowercase.
    id_nhomcu = models.CharField(db_column='ID_NhomCu', max_length=36, blank=True, null=True)  # Field name made lowercase.
    tennguonkhach = models.TextField(db_column='TenNguonKhach', blank=True, null=True)  # Field name made lowercase.
    tennhom = models.TextField(db_column='TenNhom', blank=True, null=True)  # Field name made lowercase.
    id_donvi = models.CharField(db_column='ID_DonVi', max_length=36, blank=True, null=True)  # Field name made lowercase.
    chucvu = models.CharField(db_column='ChucVu', max_length=255, blank=True, null=True)  # Field name made lowercase.
    linhvuc = models.CharField(db_column='LinhVuc', max_length=255, blank=True, null=True)  # Field name made lowercase.
    nghenghiep = models.CharField(db_column='NgheNghiep', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tenkhac = models.TextField(db_column='TenKhac', blank=True, null=True)  # Field name made lowercase.
    diachikhac = models.TextField(db_column='DiaChiKhac', blank=True, null=True)  # Field name made lowercase.
    id_trangthai = models.IntegerField(db_column='ID_TrangThai', blank=True, null=True)  # Field name made lowercase.
    ngaysuatrangthai = models.DateTimeField(db_column='NgaySuaTrangThai', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DM_DoiTuong'


class DmDonvi(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    madonvi = models.CharField(db_column='MaDonVi', max_length=50)  # Field name made lowercase.
    tendonvi = models.CharField(db_column='TenDonVi', max_length=255)  # Field name made lowercase.
    id_parent = models.CharField(db_column='ID_Parent', max_length=36, blank=True, null=True)  # Field name made lowercase.
    diachi = models.CharField(db_column='DiaChi', max_length=255, blank=True, null=True)  # Field name made lowercase.
    website = models.CharField(db_column='Website', max_length=50, blank=True, null=True)  # Field name made lowercase.
    masothue = models.CharField(db_column='MaSoThue', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sotaikhoan = models.CharField(db_column='SoTaiKhoan', max_length=50, blank=True, null=True)  # Field name made lowercase.
    id_nganhang = models.CharField(db_column='ID_NganHang', max_length=36, blank=True, null=True)  # Field name made lowercase.
    sodienthoai = models.CharField(db_column='SoDienThoai', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sofax = models.CharField(db_column='SoFax', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kitudanhma = models.CharField(db_column='KiTuDanhMa', max_length=50, blank=True, null=True)  # Field name made lowercase.
    usertao = models.CharField(db_column='UserTao', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaytao = models.DateTimeField(db_column='NgayTao', blank=True, null=True)  # Field name made lowercase.
    usersuacuoi = models.CharField(db_column='UserSuaCuoi', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaysuacuoi = models.DateTimeField(db_column='NgaySuaCuoi', blank=True, null=True)  # Field name made lowercase.
    hienthi_chinh = models.BooleanField(db_column='HienThi_Chinh', blank=True, null=True)  # Field name made lowercase.
    hienthi_phu = models.BooleanField(db_column='HienThi_Phu', blank=True, null=True)  # Field name made lowercase.
    nhapchiphi = models.IntegerField(db_column='NhapChiPhi', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DM_DonVi'


class DmDonvitinh(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    madonvitinh = models.CharField(db_column='MaDonViTinh', max_length=50)  # Field name made lowercase.
    tendonvitinh = models.CharField(db_column='TenDonViTinh', max_length=255)  # Field name made lowercase.
    ghichu = models.CharField(db_column='GhiChu', max_length=255, blank=True, null=True)  # Field name made lowercase.
    usertao = models.CharField(db_column='UserTao', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaytao = models.DateTimeField(db_column='NgayTao', blank=True, null=True)  # Field name made lowercase.
    usersuacuoi = models.CharField(db_column='UserSuaCuoi', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaysuacuoi = models.DateTimeField(db_column='NgaySuaCuoi', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DM_DonViTinh'


class DmGiaban(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    magiaban = models.CharField(db_column='MaGiaBan', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tengiaban = models.CharField(db_column='TenGiaBan', max_length=250, blank=True, null=True)  # Field name made lowercase.
    apdung = models.BooleanField(db_column='ApDung')  # Field name made lowercase.
    tungay = models.DateTimeField(db_column='TuNgay', blank=True, null=True)  # Field name made lowercase.
    denngay = models.DateTimeField(db_column='DenNgay', blank=True, null=True)  # Field name made lowercase.
    ngaytrongtuan = models.CharField(db_column='NgayTrongTuan', max_length=50, blank=True, null=True)  # Field name made lowercase.
    apdungkhunggio = models.BooleanField(db_column='ApDungKhungGio')  # Field name made lowercase.
    tugio = models.DateTimeField(db_column='TuGio', blank=True, null=True)  # Field name made lowercase.
    dengio = models.DateTimeField(db_column='DenGio', blank=True, null=True)  # Field name made lowercase.
    chungtu = models.TextField(db_column='ChungTu', blank=True, null=True)  # Field name made lowercase.
    giamgiatheonhomdoituong = models.BooleanField(db_column='GiamGiaTheoNhomDoiTuong', blank=True, null=True)  # Field name made lowercase.
    id_nhomdoituongs = models.CharField(db_column='ID_NhomDoiTuongs', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    giamgiatatcadoituong = models.BooleanField(db_column='GiamGiaTatCaDoiTuong', blank=True, null=True)  # Field name made lowercase.
    id_doituongs = models.CharField(db_column='ID_DoiTuongs', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    ghichu = models.TextField(db_column='GhiChu', blank=True, null=True)  # Field name made lowercase.
    id_donvi = models.ForeignKey(DmDonvi, models.DO_NOTHING, db_column='ID_DonVi', blank=True, null=True)  # Field name made lowercase.
    userlap = models.CharField(db_column='UserLap', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaylap = models.DateTimeField(db_column='NgayLap', blank=True, null=True)  # Field name made lowercase.
    usersua = models.CharField(db_column='UserSua', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaysuacuoi = models.DateTimeField(db_column='NgaySuaCuoi', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DM_GiaBan'


class DmGiabanChitiet(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    id_giaban = models.ForeignKey(DmGiaban, models.DO_NOTHING, db_column='ID_GiaBan')  # Field name made lowercase.
    id_hanghoa = models.ForeignKey('DmHanghoa', models.DO_NOTHING, db_column='ID_HangHoa')  # Field name made lowercase.
    id_donvitinh = models.CharField(db_column='ID_DonViTinh', max_length=36)  # Field name made lowercase.
    id_khohang = models.ForeignKey('DmKho', models.DO_NOTHING, db_column='ID_KhoHang')  # Field name made lowercase.
    giaban = models.FloatField(db_column='GiaBan')  # Field name made lowercase.
    id_ngoaite = models.CharField(db_column='ID_NgoaiTe', max_length=36, blank=True, null=True)  # Field name made lowercase.
    tygia = models.FloatField(db_column='TyGia')  # Field name made lowercase.
    phuongthuctinhgiaban = models.IntegerField(db_column='PhuongThucTinhGiaBan', blank=True, null=True)  # Field name made lowercase.
    theopt = models.BooleanField(db_column='TheoPT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DM_GiaBan_ChiTiet'


class DmHanghoa(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    anh = models.BinaryField(db_column='Anh', blank=True, null=True)  # Field name made lowercase.
    mahanghoa = models.CharField(db_column='MaHangHoa', max_length=50)  # Field name made lowercase.
    tenhanghoa = models.TextField(db_column='TenHangHoa')  # Field name made lowercase.
    lahanghoa = models.BooleanField(db_column='LaHangHoa')  # Field name made lowercase.
    id_nhomhang = models.ForeignKey('DmNhomhanghoa', models.DO_NOTHING, db_column='ID_NhomHang', blank=True, null=True)  # Field name made lowercase.
    id_phanloai = models.CharField(db_column='ID_PhanLoai', max_length=36, blank=True, null=True)  # Field name made lowercase.
    id_donvitinh = models.ForeignKey(DmDonvitinh, models.DO_NOTHING, db_column='ID_DonViTinh')  # Field name made lowercase.
    id_quocgia = models.ForeignKey('DmQuocgia', models.DO_NOTHING, db_column='ID_QuocGia', blank=True, null=True)  # Field name made lowercase.
    id_doituong = models.ForeignKey(DmDoituong, models.DO_NOTHING, db_column='ID_DoiTuong', blank=True, null=True)  # Field name made lowercase.
    giabanle = models.FloatField(db_column='GiaBanLe')  # Field name made lowercase.
    id_thuesuatban = models.ForeignKey('DmThuesuat', models.DO_NOTHING, db_column='ID_ThueSuatBan', related_name='HangHoaBan', blank=True, null=True)  # Field name made lowercase.
    tisuatbanle = models.FloatField(db_column='TiSuatBanLe', blank=True, null=True)  # Field name made lowercase.
    gianhap = models.FloatField(db_column='GiaNhap')  # Field name made lowercase.
    id_thuesuatnhap = models.ForeignKey('DmThuesuat', models.DO_NOTHING, db_column='ID_ThueSuatNhap', related_name='HangHoaNhap', blank=True, null=True)  # Field name made lowercase.
    giaban1 = models.FloatField(db_column='GiaBan1', blank=True, null=True)  # Field name made lowercase.
    tisuattheogiaban1 = models.IntegerField(db_column='TiSuatTheoGiaBan1', blank=True, null=True)  # Field name made lowercase.
    giaban2 = models.FloatField(db_column='GiaBan2', blank=True, null=True)  # Field name made lowercase.
    tisuattheogiaban2 = models.IntegerField(db_column='TiSuatTheoGiaBan2', blank=True, null=True)  # Field name made lowercase.
    giaban3 = models.FloatField(db_column='GiaBan3', blank=True, null=True)  # Field name made lowercase.
    tisuattheogiaban3 = models.IntegerField(db_column='TiSuatTheoGiaBan3', blank=True, null=True)  # Field name made lowercase.
    ids_nhomkh1 = models.TextField(db_column='IDs_NhomKH1', blank=True, null=True)  # Field name made lowercase.
    ids_nhomkh2 = models.TextField(db_column='IDs_NhomKH2', blank=True, null=True)  # Field name made lowercase.
    ids_nhomkh3 = models.TextField(db_column='IDs_NhomKH3', blank=True, null=True)  # Field name made lowercase.
    mavach = models.CharField(db_column='MaVach', max_length=50, blank=True, null=True)  # Field name made lowercase.
    quycach = models.FloatField(db_column='QuyCach', blank=True, null=True)  # Field name made lowercase.
    id_dvtquycach = models.CharField(db_column='ID_DVTQuyCach', max_length=36, blank=True, null=True)  # Field name made lowercase.
    loaibaohanh = models.IntegerField(db_column='LoaiBaoHanh', blank=True, null=True)  # Field name made lowercase.
    thoigianbaohanh = models.IntegerField(db_column='ThoiGianBaoHanh', blank=True, null=True)  # Field name made lowercase.
    tentgbaohanh = models.TextField(db_column='TenTGBaoHanh', blank=True, null=True)  # Field name made lowercase.
    chiphithuchien = models.FloatField(db_column='ChiPhiThucHien')  # Field name made lowercase.
    chiphitinhtheopt = models.BooleanField(db_column='ChiPhiTinhTheoPT')  # Field name made lowercase.
    tinhcpsauchietkhau = models.BooleanField(db_column='TinhCPSauChietKhau', blank=True, null=True)  # Field name made lowercase.
    ghichu = models.TextField(db_column='GhiChu', blank=True, null=True)  # Field name made lowercase.
    sophutthuchien = models.IntegerField(db_column='SoPhutThucHien', blank=True, null=True)  # Field name made lowercase.
    chietkhaumd_nv = models.FloatField(db_column='ChietKhauMD_NV', blank=True, null=True)  # Field name made lowercase.
    chietkhaumd_nvtheopt = models.BooleanField(db_column='ChietKhauMD_NVTheoPT', blank=True, null=True)  # Field name made lowercase.
    id_donvitinhphu1 = models.CharField(db_column='ID_DonViTinhPhu1', max_length=36, blank=True, null=True)  # Field name made lowercase.
    tylechuyendoi1 = models.FloatField(db_column='TyLeChuyenDoi1', blank=True, null=True)  # Field name made lowercase.
    id_donvitinhphu2 = models.CharField(db_column='ID_DonViTinhPhu2', max_length=36, blank=True, null=True)  # Field name made lowercase.
    tylechuyendoi2 = models.FloatField(db_column='TyLeChuyenDoi2', blank=True, null=True)  # Field name made lowercase.
    id_donvitinhphu3 = models.CharField(db_column='ID_DonViTinhPhu3', max_length=36, blank=True, null=True)  # Field name made lowercase.
    tylechuyendoi3 = models.FloatField(db_column='TyLeChuyenDoi3', blank=True, null=True)  # Field name made lowercase.
    tinhgiavon = models.IntegerField(db_column='TinhGiaVon', blank=True, null=True)  # Field name made lowercase.
    theodoi = models.BooleanField(db_column='TheoDoi')  # Field name made lowercase.
    usertao = models.CharField(db_column='UserTao', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaytao = models.DateTimeField(db_column='NgayTao', blank=True, null=True)  # Field name made lowercase.
    usersuacuoi = models.CharField(db_column='UserSuaCuoi', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaysuacuoi = models.DateTimeField(db_column='NgaySuaCuoi', blank=True, null=True)  # Field name made lowercase.
    tenkhac = models.TextField(db_column='TenKhac', blank=True, null=True)  # Field name made lowercase.
    chatlieu = models.CharField(db_column='ChatLieu', max_length=255, blank=True, null=True)  # Field name made lowercase.
    kichco = models.CharField(db_column='KichCo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mausac = models.CharField(db_column='MauSac', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tisuat1 = models.FloatField(db_column='TiSuat1', blank=True, null=True)  # Field name made lowercase.
    tisuat2 = models.FloatField(db_column='TiSuat2', blank=True, null=True)  # Field name made lowercase.
    tisuat3 = models.FloatField(db_column='TiSuat3', blank=True, null=True)  # Field name made lowercase.
    trangthai = models.IntegerField(db_column='TrangThai', blank=True, null=True)  # Field name made lowercase.
    sokmbaoduong = models.FloatField(db_column='SoKmBaoDuong', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DM_HangHoa'


class DmHinhthucthanhtoan(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    mahinhthuc = models.CharField(db_column='MaHinhThuc', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tenhinhthuc = models.CharField(db_column='TenHinhThuc', max_length=255)  # Field name made lowercase.
    ghichu = models.CharField(db_column='GhiChu', max_length=255, blank=True, null=True)  # Field name made lowercase.
    usertao = models.CharField(db_column='UserTao', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaytao = models.DateTimeField(db_column='NgayTao', blank=True, null=True)  # Field name made lowercase.
    usersuacuoi = models.CharField(db_column='UserSuaCuoi', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaysuacuoi = models.DateTimeField(db_column='NgaySuaCuoi', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DM_HinhThucThanhToan'


class DmHinhthucvanchuyen(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    mahinhthuc = models.CharField(db_column='MaHinhThuc', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tenhinhthuc = models.CharField(db_column='TenHinhThuc', max_length=255)  # Field name made lowercase.
    ghichu = models.CharField(db_column='GhiChu', max_length=255, blank=True, null=True)  # Field name made lowercase.
    usertao = models.CharField(db_column='UserTao', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaytao = models.DateTimeField(db_column='NgayTao', blank=True, null=True)  # Field name made lowercase.
    usersuacuoi = models.CharField(db_column='UserSuaCuoi', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaysuacuoi = models.DateTimeField(db_column='NgaySuaCuoi', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DM_HinhThucVanChuyen'


class DmKho(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    makho = models.CharField(db_column='MaKho', max_length=50)  # Field name made lowercase.
    tenkho = models.CharField(db_column='TenKho', max_length=255)  # Field name made lowercase.
    diadiem = models.CharField(db_column='DiaDiem', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ghichu = models.CharField(db_column='GhiChu', max_length=255, blank=True, null=True)  # Field name made lowercase.
    usertao = models.CharField(db_column='UserTao', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaytao = models.DateTimeField(db_column='NgayTao', blank=True, null=True)  # Field name made lowercase.
    usersuacuoi = models.CharField(db_column='UserSuaCuoi', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaysuacuoi = models.DateTimeField(db_column='NgaySuaCuoi', blank=True, null=True)  # Field name made lowercase.
    id_donvis = models.TextField(db_column='ID_DonVis', blank=True, null=True)  # Field name made lowercase.
    tendonvis = models.TextField(db_column='TenDonVis', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DM_Kho'


class DmKhoanphucap(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    makhoanphucap = models.CharField(db_column='MaKhoanPhuCap', max_length=50)  # Field name made lowercase.
    tenkhoanphucap = models.TextField(db_column='TenKhoanPhuCap')  # Field name made lowercase.
    ghichu = models.TextField(db_column='GhiChu', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DM_KhoanPhuCap'


class DmKhuvuc(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    makhuvuc = models.CharField(db_column='MaKhuVuc', max_length=50)  # Field name made lowercase.
    tenkhuvuc = models.CharField(db_column='TenKhuVuc', max_length=250)  # Field name made lowercase.
    ghichu = models.CharField(db_column='GhiChu', max_length=500, blank=True, null=True)  # Field name made lowercase.
    tang = models.IntegerField(db_column='Tang', blank=True, null=True)  # Field name made lowercase.
    usertao = models.CharField(db_column='UserTao', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaytao = models.DateTimeField(db_column='NgayTao', blank=True, null=True)  # Field name made lowercase.
    usersuacuoi = models.CharField(db_column='UserSuaCuoi', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaysuacuoi = models.DateTimeField(db_column='NgaySuaCuoi', blank=True, null=True)  # Field name made lowercase.
    sodokhuvuc = models.BinaryField(db_column='SoDoKhuVuc', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DM_KhuVuc'


class DmKhuyenmai(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    id_donvi = models.ForeignKey(DmDonvi, models.DO_NOTHING, db_column='ID_DonVi', blank=True, null=True)  # Field name made lowercase.
    giamgiatheonhomdoituong = models.BooleanField(db_column='GiamGiaTheoNhomDoiTuong', blank=True, null=True)  # Field name made lowercase.
    ghichu = models.TextField(db_column='GhiChu', blank=True, null=True)  # Field name made lowercase.
    tungay = models.DateTimeField(db_column='TuNgay', blank=True, null=True)  # Field name made lowercase.
    denngay = models.DateTimeField(db_column='DenNgay', blank=True, null=True)  # Field name made lowercase.
    ngaytrongtuan = models.CharField(db_column='NgayTrongTuan', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chungtu = models.CharField(db_column='ChungTu', max_length=500, blank=True, null=True)  # Field name made lowercase.
    dengio = models.DateTimeField(db_column='DenGio', blank=True, null=True)  # Field name made lowercase.
    giamgiatatcadoituong = models.BooleanField(db_column='GiamGiaTatCaDoiTuong', blank=True, null=True)  # Field name made lowercase.
    id_doituongs = models.CharField(db_column='ID_DoiTuongs', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    id_nhomdoituongs = models.CharField(db_column='ID_NhomDoiTuongs', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    makhuyenmai = models.CharField(db_column='MaKhuyenMai', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tenkhuyenmai = models.CharField(db_column='TenKhuyenMai', max_length=250)  # Field name made lowercase.
    tugio = models.DateTimeField(db_column='TuGio', blank=True, null=True)  # Field name made lowercase.
    apdung = models.BooleanField(db_column='ApDung')  # Field name made lowercase.
    apdungkhunggio = models.BooleanField(db_column='ApDungKhungGio')  # Field name made lowercase.
    usertao = models.CharField(db_column='UserTao', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaytao = models.DateTimeField(db_column='NgayTao', blank=True, null=True)  # Field name made lowercase.
    usersuacuoi = models.CharField(db_column='UserSuaCuoi', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaysuacuoi = models.DateTimeField(db_column='NgaySuaCuoi', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DM_KhuyenMai'


class DmKhuyenmaiChitiet(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    id_khuyenmai = models.ForeignKey(DmKhuyenmai, models.DO_NOTHING, db_column='ID_KhuyenMai')  # Field name made lowercase.
    idnhomhang_idhanghoa = models.CharField(db_column='IDNhomHang_IDHangHoa', max_length=36)  # Field name made lowercase.
    soluong = models.FloatField(db_column='SoLuong')  # Field name made lowercase.
    tile = models.FloatField(db_column='TiLe')  # Field name made lowercase.
    tiengiam = models.FloatField(db_column='TienGiam')  # Field name made lowercase.
    giacu = models.FloatField(db_column='GiaCu')  # Field name made lowercase.
    id_donvitinh = models.CharField(db_column='ID_DonViTinh', max_length=36, blank=True, null=True)  # Field name made lowercase.
    lanhomhang = models.BooleanField(db_column='LaNhomHang')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DM_KhuyenMai_ChiTiet'


class DmLienhe(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    id_doituong = models.ForeignKey(DmDoituong, models.DO_NOTHING, db_column='ID_DoiTuong')  # Field name made lowercase.
    malienhe = models.CharField(db_column='MaLienHe', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tenlienhe = models.CharField(db_column='TenLienHe', max_length=255)  # Field name made lowercase.
    chucvu = models.CharField(db_column='ChucVu', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sodienthoai = models.CharField(db_column='SoDienThoai', max_length=50, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ghichu = models.CharField(db_column='GhiChu', max_length=255, blank=True, null=True)  # Field name made lowercase.
    usertao = models.CharField(db_column='UserTao', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaytao = models.DateTimeField(db_column='NgayTao', blank=True, null=True)  # Field name made lowercase.
    usersuacuoi = models.CharField(db_column='UserSuaCuoi', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaysuacuoi = models.DateTimeField(db_column='NgaySuaCuoi', blank=True, null=True)  # Field name made lowercase.
    diachi = models.TextField(db_column='DiaChi', blank=True, null=True)  # Field name made lowercase.
    ngaysinh = models.DateTimeField(db_column='NgaySinh', blank=True, null=True)  # Field name made lowercase.
    cannang = models.CharField(db_column='CanNang', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chieucao = models.CharField(db_column='ChieuCao', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DM_LienHe'


class DmLohang(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    id_hanghoa = models.ForeignKey(DmHanghoa, models.DO_NOTHING, db_column='ID_HangHoa')  # Field name made lowercase.
    solo = models.CharField(db_column='SoLo', max_length=50)  # Field name made lowercase.
    ngaysanxuat = models.DateTimeField(db_column='NgaySanXuat', blank=True, null=True)  # Field name made lowercase.
    ngayhethan = models.DateTimeField(db_column='NgayHetHan', blank=True, null=True)  # Field name made lowercase.
    usertao = models.CharField(db_column='UserTao', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaytao = models.DateTimeField(db_column='NgayTao', blank=True, null=True)  # Field name made lowercase.
    usersuacuoi = models.CharField(db_column='UserSuaCuoi', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaysuacuoi = models.DateTimeField(db_column='NgaySuaCuoi', blank=True, null=True)  # Field name made lowercase.
    tenlo = models.TextField(db_column='TenLo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DM_LoHang'


class DmLoaichungtu(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    loaichungtu = models.TextField(db_column='LoaiChungTu')  # Field name made lowercase.
    ghichu = models.TextField(db_column='GhiChu', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DM_LoaiChungTu'


class DmLoaigiaphong(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    maloai = models.CharField(db_column='MaLoai', max_length=50)  # Field name made lowercase.
    tenloai = models.CharField(db_column='TenLoai', max_length=50)  # Field name made lowercase.
    lagiangay = models.BooleanField(db_column='LaGiaNgay')  # Field name made lowercase.
    thoigian_min = models.FloatField(db_column='ThoiGian_Min', blank=True, null=True)  # Field name made lowercase.
    thoigian_max = models.FloatField(db_column='ThoiGian_Max', blank=True, null=True)  # Field name made lowercase.
    ghichu = models.TextField(db_column='GhiChu', blank=True, null=True)  # Field name made lowercase.
    sogiotoithieu = models.FloatField(db_column='SoGioToiThieu', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DM_LoaiGiaPhong'


class DmLoainhapxuat(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    maloai = models.CharField(db_column='MaLoai', max_length=50)  # Field name made lowercase.
    tenloai = models.TextField(db_column='TenLoai')  # Field name made lowercase.
    ghichu = models.TextField(db_column='GhiChu', blank=True, null=True)  # Field name made lowercase.
    nhap_xuat_dieuchuyen = models.IntegerField(db_column='Nhap_Xuat_DieuChuyen')  # Field name made lowercase.
    sudung = models.BooleanField(db_column='SuDung')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DM_LoaiNhapXuat'


class DmLoaiphieuthanhtoan(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    maloai = models.CharField(db_column='MaLoai', max_length=50)  # Field name made lowercase.
    tenloai = models.TextField(db_column='TenLoai')  # Field name made lowercase.
    solansudung = models.FloatField(db_column='SoLanSuDung', blank=True, null=True)  # Field name made lowercase.
    thanhtoantheophantram = models.BooleanField(db_column='ThanhToanTheoPhanTram')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DM_LoaiPhieuThanhToan'


class DmLoaiphong(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    maloai = models.CharField(db_column='MaLoai', max_length=50)  # Field name made lowercase.
    tenloai = models.TextField(db_column='TenLoai')  # Field name made lowercase.
    songuoi_min = models.IntegerField(db_column='SoNguoi_Min', blank=True, null=True)  # Field name made lowercase.
    songuoi_max = models.IntegerField(db_column='SoNguoi_Max', blank=True, null=True)  # Field name made lowercase.
    sudung = models.BooleanField(db_column='SuDung')  # Field name made lowercase.
    mausac = models.IntegerField(db_column='MauSac', blank=True, null=True)  # Field name made lowercase.
    usernhap = models.CharField(db_column='UserNhap', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaynhap = models.DateTimeField(db_column='NgayNhap', blank=True, null=True)  # Field name made lowercase.
    usersua = models.CharField(db_column='UserSua', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaysuacuoi = models.DateTimeField(db_column='NgaySuaCuoi', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DM_LoaiPhong'


class DmLophoc(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    malop = models.CharField(db_column='MaLop', max_length=50)  # Field name made lowercase.
    tenlop = models.TextField(db_column='TenLop')  # Field name made lowercase.
    ngaybd = models.DateTimeField(db_column='NgayBD', blank=True, null=True)  # Field name made lowercase.
    ngaykt = models.DateTimeField(db_column='NgayKT', blank=True, null=True)  # Field name made lowercase.
    giobd = models.DateTimeField(db_column='GioBD', blank=True, null=True)  # Field name made lowercase.
    giokt = models.DateTimeField(db_column='GioKT', blank=True, null=True)  # Field name made lowercase.
    ngaytrongtuan = models.TextField(db_column='NgayTrongTuan', blank=True, null=True)  # Field name made lowercase.
    giaovienphutrach = models.CharField(db_column='GiaoVienPhuTrach', max_length=36, blank=True, null=True)  # Field name made lowercase.
    id_donvi = models.CharField(db_column='ID_DonVi', max_length=36)  # Field name made lowercase.
    ghichu = models.TextField(db_column='GhiChu', blank=True, null=True)  # Field name made lowercase.
    userlap = models.CharField(db_column='UserLap', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaylap = models.DateTimeField(db_column='NgayLap', blank=True, null=True)  # Field name made lowercase.
    usersuacuoi = models.CharField(db_column='UserSuaCuoi', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaysuacuoi = models.DateTimeField(db_column='NgaySuaCuoi', blank=True, null=True)  # Field name made lowercase.
    chietkhau_giaovienphutrach = models.FloatField(db_column='ChietKhau_GiaoVienPhuTrach', blank=True, null=True)  # Field name made lowercase.
    laphantram_ckgv = models.BooleanField(db_column='LaPhanTram_CKGV', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DM_LopHoc'


class DmLydohuylichhen(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    lydohuylichhen = models.TextField(db_column='LyDoHuyLichHen')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DM_LyDoHuyLichHen'


class DmMavach(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    id_hanghoa = models.ForeignKey(DmHanghoa, models.DO_NOTHING, db_column='ID_HangHoa')  # Field name made lowercase.
    mavach = models.CharField(db_column='MaVach', max_length=50)  # Field name made lowercase.
    lahientai = models.BooleanField(db_column='LaHienTai')  # Field name made lowercase.
    sudung = models.BooleanField(db_column='SuDung', blank=True, null=True)  # Field name made lowercase.
    usertao = models.CharField(db_column='UserTao', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaytao = models.DateTimeField(db_column='NgayTao', blank=True, null=True)  # Field name made lowercase.
    usersuacuoi = models.CharField(db_column='UserSuaCuoi', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaysuacuoi = models.DateTimeField(db_column='NgaySuaCuoi', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DM_MaVach'


class DmMaychamcong(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    mamay = models.IntegerField(db_column='MaMay')  # Field name made lowercase.
    tenmaychamcong = models.TextField(db_column='TenMayChamCong', blank=True, null=True)  # Field name made lowercase.
    ip = models.CharField(db_column='IP', max_length=15, blank=True, null=True)  # Field name made lowercase.
    port = models.IntegerField(db_column='Port', blank=True, null=True)  # Field name made lowercase.
    tenmien = models.TextField(db_column='TenMien', blank=True, null=True)  # Field name made lowercase.
    comport = models.IntegerField(db_column='COMPort', blank=True, null=True)  # Field name made lowercase.
    kieuketnoi = models.IntegerField(db_column='KieuKetNoi', blank=True, null=True)  # Field name made lowercase.
    baudrate = models.IntegerField(db_column='BaudRate', blank=True, null=True)  # Field name made lowercase.
    sudungtenmien = models.BooleanField(db_column='SuDungTenMien', blank=True, null=True)  # Field name made lowercase.
    sudung = models.BooleanField(db_column='SuDung')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DM_MayChamCong'


class DmNganhang(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    manganhang = models.CharField(db_column='MaNganHang', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tennganhang = models.TextField(db_column='TenNganHang')  # Field name made lowercase.
    chinhanh = models.TextField(db_column='ChiNhanh', blank=True, null=True)  # Field name made lowercase.
    ghichu = models.TextField(db_column='GhiChu', blank=True, null=True)  # Field name made lowercase.
    usertao = models.CharField(db_column='UserTao', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaytao = models.DateTimeField(db_column='NgayTao', blank=True, null=True)  # Field name made lowercase.
    usersuacuoi = models.CharField(db_column='UserSuaCuoi', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaysuacuoi = models.DateTimeField(db_column='NgaySuaCuoi', blank=True, null=True)  # Field name made lowercase.
    chiphithanhtoan = models.FloatField(db_column='ChiPhiThanhToan', blank=True, null=True)  # Field name made lowercase.
    theophantram = models.BooleanField(db_column='TheoPhanTram', blank=True, null=True)  # Field name made lowercase.
    macdinh = models.BooleanField(db_column='MacDinh', blank=True, null=True)  # Field name made lowercase.
    thuphithanhtoan = models.BooleanField(db_column='ThuPhiThanhToan', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DM_NganHang'


class DmNhanvien(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    manhanvien = models.CharField(db_column='MaNhanVien', max_length=50)  # Field name made lowercase.
    tennhanvien = models.TextField(db_column='TenNhanVien')  # Field name made lowercase.
    ngaysinh = models.DateTimeField(db_column='NgaySinh', blank=True, null=True)  # Field name made lowercase.
    gioitinh = models.BooleanField(db_column='GioiTinh')  # Field name made lowercase.
    noisinh = models.TextField(db_column='NoiSinh', blank=True, null=True)  # Field name made lowercase.
    nguyenquan = models.TextField(db_column='NguyenQuan', blank=True, null=True)  # Field name made lowercase.
    thuongtru = models.TextField(db_column='ThuongTru', blank=True, null=True)  # Field name made lowercase.
    tamtru = models.TextField(db_column='TamTru', blank=True, null=True)  # Field name made lowercase.
    dienthoaicoquan = models.CharField(db_column='DienThoaiCoQuan', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dienthoainharieng = models.CharField(db_column='DienThoaiNhaRieng', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dienthoaididong = models.CharField(db_column='DienThoaiDiDong', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sofax = models.CharField(db_column='SoFax', max_length=50, blank=True, null=True)  # Field name made lowercase.
    diachicoquan = models.TextField(db_column='DiaChiCoQuan', blank=True, null=True)  # Field name made lowercase.
    socmnd = models.CharField(db_column='SoCMND', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sobhxh = models.CharField(db_column='SoBHXH', max_length=50, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=50, blank=True, null=True)  # Field name made lowercase.
    website = models.CharField(db_column='Website', max_length=50, blank=True, null=True)  # Field name made lowercase.
    anh = models.BinaryField(db_column='Anh', blank=True, null=True)  # Field name made lowercase.
    captaikhoan = models.BooleanField(db_column='CapTaiKhoan', blank=True, null=True)  # Field name made lowercase.
    ghichu = models.TextField(db_column='GhiChu', blank=True, null=True)  # Field name made lowercase.
    danghiviec = models.BooleanField(db_column='DaNghiViec')  # Field name made lowercase.
    usertao = models.CharField(db_column='UserTao', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaytao = models.DateTimeField(db_column='NgayTao', blank=True, null=True)  # Field name made lowercase.
    usersuacuoi = models.CharField(db_column='UserSuaCuoi', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaysuacuoi = models.DateTimeField(db_column='NgaySuaCuoi', blank=True, null=True)  # Field name made lowercase.
    laptck_the = models.BooleanField(db_column='LaPTCK_The', blank=True, null=True)  # Field name made lowercase.
    pt_tienckbanthe = models.FloatField(db_column='PT_TienCKBanThe', blank=True, null=True)  # Field name made lowercase.
    lathochinh = models.BooleanField(db_column='LaThoChinh', blank=True, null=True)  # Field name made lowercase.
    ngaycap = models.DateTimeField(db_column='NgayCap', blank=True, null=True)  # Field name made lowercase.
    noicap = models.TextField(db_column='NoiCap', blank=True, null=True)  # Field name made lowercase.
    luongtuvantheodoanhthu = models.BooleanField(db_column='LuongTuVanTheoDoanhThu', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DM_NhanVien'


class DmNhomdoituong(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    loaidoituong = models.IntegerField(db_column='LoaiDoiTuong')  # Field name made lowercase.
    manhom = models.CharField(db_column='MaNhom', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tennhom = models.CharField(db_column='TenNhom', max_length=255)  # Field name made lowercase.
    ghichu = models.TextField(db_column='GhiChu', blank=True, null=True)  # Field name made lowercase.
    usertao = models.CharField(db_column='UserTao', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaytao = models.DateTimeField(db_column='NgayTao', blank=True, null=True)  # Field name made lowercase.
    usersuacuoi = models.CharField(db_column='UserSuaCuoi', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaysuacuoi = models.DateTimeField(db_column='NgaySuaCuoi', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DM_NhomDoiTuong'


class DmNhomhanghoa(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    manhom = models.CharField(db_column='MaNhom', max_length=50)  # Field name made lowercase.
    tennhom = models.CharField(db_column='TenNhom', max_length=255)  # Field name made lowercase.
    ghichu = models.TextField(db_column='GhiChu', blank=True, null=True)  # Field name made lowercase.
    id_parent = models.CharField(db_column='ID_Parent', max_length=36, blank=True, null=True)  # Field name made lowercase.
    lanhomhanghoa = models.BooleanField(db_column='LaNhomHangHoa')  # Field name made lowercase.
    usertao = models.CharField(db_column='UserTao', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaytao = models.DateTimeField(db_column='NgayTao', blank=True, null=True)  # Field name made lowercase.
    usersuacuoi = models.CharField(db_column='UserSuaCuoi', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaysuacuoi = models.DateTimeField(db_column='NgaySuaCuoi', blank=True, null=True)  # Field name made lowercase.
    hienthi_chinh = models.BooleanField(db_column='HienThi_Chinh', blank=True, null=True)  # Field name made lowercase.
    hienthi_phu = models.BooleanField(db_column='HienThi_Phu', blank=True, null=True)  # Field name made lowercase.
    mayin = models.TextField(db_column='MayIn', blank=True, null=True)  # Field name made lowercase.
    id_kho = models.CharField(db_column='ID_Kho', max_length=36, blank=True, null=True)  # Field name made lowercase.
    hienthi_banthe = models.BooleanField(db_column='HienThi_BanThe', blank=True, null=True)  # Field name made lowercase.
    mauhienthi = models.IntegerField(db_column='MauHienThi', blank=True, null=True)  # Field name made lowercase.
    id_donvis = models.TextField(db_column='ID_DonVis', blank=True, null=True)  # Field name made lowercase.
    tendonvis = models.TextField(db_column='TenDonVis', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DM_NhomHangHoa'


class DmNhomthe(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    manhomthe = models.CharField(db_column='MaNhomThe', max_length=50)  # Field name made lowercase.
    tennhomthe = models.TextField(db_column='TenNhomThe')  # Field name made lowercase.
    ghichu = models.TextField(db_column='GhiChu', blank=True, null=True)  # Field name made lowercase.
    usertao = models.CharField(db_column='UserTao', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaytao = models.DateTimeField(db_column='NgayTao', blank=True, null=True)  # Field name made lowercase.
    usersuacuoi = models.CharField(db_column='UserSuaCuoi', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaysuacuoi = models.DateTimeField(db_column='NgaySuaCuoi', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DM_NhomThe'


class DmNoidungquantam(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    manoidung = models.CharField(db_column='MaNoiDung', max_length=50)  # Field name made lowercase.
    tennoidung = models.TextField(db_column='TenNoiDung')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DM_NoiDungQuanTam'


class DmPhanloaihanghoadichvu(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    maphanloai = models.CharField(db_column='MaPhanLoai', max_length=50)  # Field name made lowercase.
    tenphanloai = models.TextField(db_column='TenPhanLoai')  # Field name made lowercase.
    ghichu = models.TextField(db_column='GhiChu', blank=True, null=True)  # Field name made lowercase.
    thoigianbaohanh = models.IntegerField(db_column='ThoiGianBaoHanh', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DM_PhanLoaiHangHoaDichVu'


class DmQuanhuyen(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    maquanhuyen = models.CharField(db_column='MaQuanHuyen', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tenquanhuyen = models.TextField(db_column='TenQuanHuyen')  # Field name made lowercase.
    id_tinhthanh = models.ForeignKey('DmTinhthanh', models.DO_NOTHING, db_column='ID_TinhThanh')  # Field name made lowercase.
    ghichu = models.CharField(db_column='GhiChu', max_length=255, blank=True, null=True)  # Field name made lowercase.
    usertao = models.CharField(db_column='UserTao', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaytao = models.DateTimeField(db_column='NgayTao', blank=True, null=True)  # Field name made lowercase.
    usersuacuoi = models.CharField(db_column='UserSuaCuoi', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaysuacuoi = models.DateTimeField(db_column='NgaySuaCuoi', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DM_QuanHuyen'


class DmQuocgia(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    manuoc = models.CharField(db_column='MaNuoc', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tennuoc = models.CharField(db_column='TenNuoc', max_length=255)  # Field name made lowercase.
    ghichu = models.CharField(db_column='GhiChu', max_length=255, blank=True, null=True)  # Field name made lowercase.
    usertao = models.CharField(db_column='UserTao', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaytao = models.DateTimeField(db_column='NgayTao', blank=True, null=True)  # Field name made lowercase.
    usersuacuoi = models.CharField(db_column='UserSuaCuoi', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaysuacuoi = models.DateTimeField(db_column='NgaySuaCuoi', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DM_QuocGia'


class DmThuesuat(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    mathuesuat = models.CharField(db_column='MaThueSuat', max_length=50)  # Field name made lowercase.
    thuesuat = models.IntegerField(db_column='ThueSuat')  # Field name made lowercase.
    ghichu = models.CharField(db_column='GhiChu', max_length=255, blank=True, null=True)  # Field name made lowercase.
    usertao = models.CharField(db_column='UserTao', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaytao = models.DateTimeField(db_column='NgayTao', blank=True, null=True)  # Field name made lowercase.
    usersuacuoi = models.CharField(db_column='UserSuaCuoi', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaysuacuoi = models.DateTimeField(db_column='NgaySuaCuoi', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DM_ThueSuat'


class DmTichdiem(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    matichdiem = models.CharField(db_column='MaTichDiem', max_length=50)  # Field name made lowercase.
    ngaybatdauapdung = models.DateTimeField(db_column='NgayBatDauApDung')  # Field name made lowercase.
    tienthuve_min = models.FloatField(db_column='TienThuVe_Min')  # Field name made lowercase.
    tienthuve_max = models.FloatField(db_column='TienThuVe_Max', blank=True, null=True)  # Field name made lowercase.
    diemquydoi = models.FloatField(db_column='DiemQuyDoi')  # Field name made lowercase.
    mucdiem = models.FloatField(db_column='MucDiem')  # Field name made lowercase.
    tienthanhtoanquydoi = models.FloatField(db_column='TienThanhToanQuyDoi')  # Field name made lowercase.
    diemtoithieu = models.FloatField(db_column='DiemToiThieu')  # Field name made lowercase.
    tientoithieu = models.FloatField(db_column='TienToiThieu')  # Field name made lowercase.
    id_donvi = models.TextField(db_column='ID_DonVi')  # Field name made lowercase.
    nhomkhachhang = models.TextField(db_column='NhomKhachHang', blank=True, null=True)  # Field name made lowercase.
    chungtu = models.TextField(db_column='ChungTu', blank=True, null=True)  # Field name made lowercase.
    thutrongtuan = models.CharField(db_column='ThuTrongTuan', max_length=255, blank=True, null=True)  # Field name made lowercase.
    apdung = models.BooleanField(db_column='ApDung')  # Field name made lowercase.
    ngaybatdau = models.DateTimeField(db_column='NgayBatDau')  # Field name made lowercase.
    ngayketthuc = models.DateTimeField(db_column='NgayKetThuc', blank=True, null=True)  # Field name made lowercase.
    ngaylap = models.DateTimeField(db_column='NgayLap', blank=True, null=True)  # Field name made lowercase.
    userlap = models.CharField(db_column='UserLap', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaysuacuoi = models.DateTimeField(db_column='NgaySuaCuoi', blank=True, null=True)  # Field name made lowercase.
    usersuacuoi = models.CharField(db_column='UserSuaCuoi', max_length=50, blank=True, null=True)  # Field name made lowercase.
    apdung_nguoigioithieu = models.BooleanField(db_column='ApDung_NguoiGioiThieu', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DM_TichDiem'


class DmTiente(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    mangoaite = models.CharField(db_column='MaNgoaiTe', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tenngoaite = models.CharField(db_column='TenNgoaiTe', max_length=100)  # Field name made lowercase.
    ghichu = models.CharField(db_column='GhiChu', max_length=255, blank=True, null=True)  # Field name made lowercase.
    id_quocgia = models.ForeignKey(DmQuocgia, models.DO_NOTHING, db_column='ID_QuocGia')  # Field name made lowercase.
    lanoite = models.BooleanField(db_column='LaNoiTe')  # Field name made lowercase.
    usertao = models.CharField(db_column='UserTao', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaytao = models.DateTimeField(db_column='NgayTao', blank=True, null=True)  # Field name made lowercase.
    usersuacuoi = models.CharField(db_column='UserSuaCuoi', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaysuacuoi = models.DateTimeField(db_column='NgaySuaCuoi', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DM_TienTe'


class DmTinhthanh(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    matinhthanh = models.CharField(db_column='MaTinhThanh', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tentinhthanh = models.CharField(db_column='TenTinhThanh', max_length=255)  # Field name made lowercase.
    id_quocgia = models.ForeignKey(DmQuocgia, models.DO_NOTHING, db_column='ID_QuocGia', blank=True, null=True)  # Field name made lowercase.
    id_vungmien = models.ForeignKey('DmVungmien', models.DO_NOTHING, db_column='ID_VungMien', blank=True, null=True)  # Field name made lowercase.
    ghichu = models.CharField(db_column='GhiChu', max_length=255, blank=True, null=True)  # Field name made lowercase.
    usertao = models.CharField(db_column='UserTao', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaytao = models.DateTimeField(db_column='NgayTao', blank=True, null=True)  # Field name made lowercase.
    usersuacuoi = models.CharField(db_column='UserSuaCuoi', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaysuacuoi = models.DateTimeField(db_column='NgaySuaCuoi', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DM_TinhThanh'


class DmTrangthai(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tentrangthai = models.TextField(db_column='TenTrangThai', blank=True, null=True)  # Field name made lowercase.
    usertao = models.CharField(db_column='UserTao', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ngaytao = models.DateTimeField(db_column='NgayTao', blank=True, null=True)  # Field name made lowercase.
    usersuacuoi = models.CharField(db_column='UserSuaCuoi', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ngaysuacuoi = models.DateTimeField(db_column='NgaySuaCuoi', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DM_TrangThai'


class DmTygia(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    id_ngoaite = models.ForeignKey(DmTiente, models.DO_NOTHING, db_column='ID_NgoaiTe')  # Field name made lowercase.
    tygia = models.FloatField(db_column='TyGia')  # Field name made lowercase.
    ngaytygia = models.DateTimeField(db_column='NgayTyGia')  # Field name made lowercase.
    ghichu = models.CharField(db_column='GhiChu', max_length=255, blank=True, null=True)  # Field name made lowercase.
    usertao = models.CharField(db_column='UserTao', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaytao = models.DateTimeField(db_column='NgayTao', blank=True, null=True)  # Field name made lowercase.
    usersuacuoi = models.CharField(db_column='UserSuaCuoi', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaysuacuoi = models.DateTimeField(db_column='NgaySuaCuoi', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DM_TyGia'


class DmVitri(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    mavitri = models.CharField(db_column='MaViTri', max_length=50)  # Field name made lowercase.
    id_khuvuc = models.ForeignKey(DmKhuvuc, models.DO_NOTHING, db_column='ID_KhuVuc')  # Field name made lowercase.
    tinhtrang = models.BooleanField(db_column='TinhTrang', blank=True, null=True)  # Field name made lowercase.
    ghichu = models.CharField(db_column='GhiChu', max_length=500, blank=True, null=True)  # Field name made lowercase.
    usertao = models.CharField(db_column='UserTao', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaytao = models.DateTimeField(db_column='NgayTao', blank=True, null=True)  # Field name made lowercase.
    usersuacuoi = models.CharField(db_column='UserSuaCuoi', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaysuacuoi = models.DateTimeField(db_column='NgaySuaCuoi', blank=True, null=True)  # Field name made lowercase.
    dongiagio = models.FloatField(db_column='DonGiaGio', blank=True, null=True)  # Field name made lowercase.
    anh = models.BinaryField(db_column='Anh', blank=True, null=True)  # Field name made lowercase.
    dongiangay = models.FloatField(db_column='DonGiaNgay', blank=True, null=True)  # Field name made lowercase.
    id_loaiphong = models.CharField(db_column='ID_LoaiPhong', max_length=36, blank=True, null=True)  # Field name made lowercase.
    tang = models.IntegerField(db_column='Tang', blank=True, null=True)  # Field name made lowercase.
    tenvitri = models.TextField(db_column='TenViTri', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DM_ViTri'


class DmVungmien(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    mavung = models.CharField(db_column='MaVung', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tenvung = models.TextField(db_column='TenVung')  # Field name made lowercase.
    ghichu = models.TextField(db_column='GhiChu', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DM_VungMien'


class Danhsachthi(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    ma = models.CharField(db_column='Ma', max_length=50)  # Field name made lowercase.
    ten = models.TextField(db_column='Ten')  # Field name made lowercase.
    id_donvi = models.CharField(db_column='ID_DonVi', max_length=36)  # Field name made lowercase.
    id_monthi = models.CharField(db_column='ID_MonThi', max_length=36)  # Field name made lowercase.
    id_giaovien = models.CharField(db_column='ID_GiaoVien', max_length=36, blank=True, null=True)  # Field name made lowercase.
    id_trongtai = models.CharField(db_column='ID_TrongTai', max_length=36, blank=True, null=True)  # Field name made lowercase.
    thoigianbatdau = models.DateTimeField(db_column='ThoiGianBatDau', blank=True, null=True)  # Field name made lowercase.
    thoigianketthuc = models.DateTimeField(db_column='ThoiGianKetThuc', blank=True, null=True)  # Field name made lowercase.
    usertao = models.CharField(db_column='UserTao', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaytao = models.DateTimeField(db_column='NgayTao', blank=True, null=True)  # Field name made lowercase.
    usersua = models.CharField(db_column='UserSua', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaysua = models.DateTimeField(db_column='NgaySua', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DanhSachThi'


class DanhsachthiChitiet(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    id_danhsachthi = models.CharField(db_column='ID_DanhSachThi', max_length=36)  # Field name made lowercase.
    id_thisinh = models.CharField(db_column='ID_ThiSinh', max_length=36)  # Field name made lowercase.
    maduthi = models.TextField(db_column='MaDuThi', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DanhSachThi_ChiTiet'


class Dieuchuyenkho(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    id_donvi = models.ForeignKey(DmDonvi, models.DO_NOTHING, db_column='ID_DonVi')  # Field name made lowercase.
    machungtu = models.CharField(db_column='MaChungTu', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaydieuchuyen = models.DateTimeField(db_column='NgayDieuChuyen')  # Field name made lowercase.
    id_nhanvien = models.CharField(db_column='ID_NhanVien', max_length=36, blank=True, null=True)  # Field name made lowercase.
    id_ngoaite = models.ForeignKey(DmTiente, models.DO_NOTHING, db_column='ID_NgoaiTe', blank=True, null=True)  # Field name made lowercase.
    tygia = models.FloatField(db_column='TyGia')  # Field name made lowercase.
    tongtien = models.FloatField(db_column='TongTien')  # Field name made lowercase.
    ghichu = models.CharField(db_column='GhiChu', max_length=500, blank=True, null=True)  # Field name made lowercase.
    userlap = models.CharField(db_column='UserLap', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngayvaoso = models.DateTimeField(db_column='NgayVaoSo', blank=True, null=True)  # Field name made lowercase.
    usersuacuoi = models.CharField(db_column='UserSuaCuoi', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaysuacuoi = models.DateTimeField(db_column='NgaySuaCuoi', blank=True, null=True)  # Field name made lowercase.
    id_loaidieuchuyen = models.CharField(db_column='ID_LoaiDieuChuyen', max_length=36, blank=True, null=True)  # Field name made lowercase.
    daduyet = models.BooleanField(db_column='DaDuyet', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DieuChuyenKho'


class DieuchuyenkhoChitiet(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    id_dieuchuyen = models.ForeignKey(Dieuchuyenkho, models.DO_NOTHING, db_column='ID_DieuChuyen', blank=True, null=True)  # Field name made lowercase.
    sothutu = models.IntegerField(db_column='SoThuTu', blank=True, null=True)  # Field name made lowercase.
    id_khotu = models.ForeignKey(DmKho, models.DO_NOTHING, db_column='ID_KhoTu', related_name='DieuChuyenKhoChiTietTu')  # Field name made lowercase.
    id_khoden = models.ForeignKey(DmKho, models.DO_NOTHING, db_column='ID_KhoDen', related_name='DieuChuyenKhoChiTietDen')  # Field name made lowercase.
    id_hanghoa = models.ForeignKey(DmHanghoa, models.DO_NOTHING, db_column='ID_HangHoa')  # Field name made lowercase.
    id_mavach = models.CharField(db_column='ID_MaVach', max_length=36, blank=True, null=True)  # Field name made lowercase.
    id_lohang = models.ForeignKey(DmLohang, models.DO_NOTHING, db_column='ID_LoHang', blank=True, null=True)  # Field name made lowercase.
    id_donvitinh = models.ForeignKey(DmDonvitinh, models.DO_NOTHING, db_column='ID_DonViTinh')  # Field name made lowercase.
    soluong = models.FloatField(db_column='SoLuong')  # Field name made lowercase.
    dongia = models.FloatField(db_column='DonGia')  # Field name made lowercase.
    thanhtien = models.FloatField(db_column='ThanhTien')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DieuChuyenKho_ChiTiet'


class Dieukienchuyennhom(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    id_nhommoi = models.CharField(db_column='ID_NhomMoi', max_length=36)  # Field name made lowercase.
    id_nhomht = models.CharField(db_column='ID_NhomHT', max_length=36)  # Field name made lowercase.
    diem_min = models.FloatField(db_column='Diem_Min')  # Field name made lowercase.
    diem_max = models.FloatField(db_column='Diem_Max', blank=True, null=True)  # Field name made lowercase.
    congdondiem = models.BooleanField(db_column='CongDonDiem')  # Field name made lowercase.
    doanhthu_min = models.FloatField(db_column='DoanhThu_Min')  # Field name made lowercase.
    doanhthu_max = models.FloatField(db_column='DoanhThu_Max', blank=True, null=True)  # Field name made lowercase.
    congdondoanhthu = models.BooleanField(db_column='CongDonDoanhThu')  # Field name made lowercase.
    thoigiantinhdoanhso = models.FloatField(db_column='ThoiGianTinhDoanhSo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DieuKienChuyenNhom'


class Dinhluongdichvu(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    id_dichvu = models.CharField(db_column='ID_DichVu', max_length=36)  # Field name made lowercase.
    id_nguyenlieu = models.CharField(db_column='ID_NguyenLieu', max_length=36)  # Field name made lowercase.
    soluong = models.FloatField(db_column='SoLuong')  # Field name made lowercase.
    id_donvitinh = models.ForeignKey(DmDonvitinh, models.DO_NOTHING, db_column='ID_DonViTinh')  # Field name made lowercase.
    ghichu = models.TextField(db_column='GhiChu', blank=True, null=True)  # Field name made lowercase.
    soluongdinhluong = models.FloatField(db_column='SoLuongDinhLuong', blank=True, null=True)  # Field name made lowercase.
    stt = models.IntegerField(db_column='STT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DinhLuongDichVu'


class Dinhmuchanghoaxuatkhochodichvu(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    id_hanghoa = models.CharField(db_column='ID_HangHoa', max_length=36)  # Field name made lowercase.
    id_donvitinh_hanghoa = models.CharField(db_column='ID_DonViTinh_HangHoa', max_length=36)  # Field name made lowercase.
    soluong_hanghoa = models.FloatField(db_column='SoLuong_HangHoa')  # Field name made lowercase.
    id_dichvusudung = models.CharField(db_column='ID_DichVuSuDung', max_length=36)  # Field name made lowercase.
    soluong_dichvusudung = models.FloatField(db_column='SoLuong_DichVuSuDung')  # Field name made lowercase.
    id_donvitinh_dichvusudung = models.CharField(db_column='ID_DonViTinh_DichVuSuDung', max_length=36)  # Field name made lowercase.
    ghichu = models.TextField(db_column='GhiChu', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DinhMucHangHoaXuatKhoChoDichVu'


class DoituongDacdiem(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    id_doituong = models.CharField(db_column='ID_DoiTuong', max_length=36, blank=True, null=True)  # Field name made lowercase.
    id_dacdiem = models.CharField(db_column='ID_DacDiem', max_length=36, blank=True, null=True)  # Field name made lowercase.
    ladoituong = models.BooleanField(db_column='LaDoiTuong', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DoiTuong_DacDiem'


class Donviquidoi(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    id_hanghoa = models.ForeignKey(DmHanghoa, models.DO_NOTHING, db_column='ID_HangHoa')  # Field name made lowercase.
    id_donvitinh = models.ForeignKey(DmDonvitinh, models.DO_NOTHING, db_column='ID_DonViTinh')  # Field name made lowercase.
    tylechuyendoi = models.FloatField(db_column='TyLeChuyenDoi')  # Field name made lowercase.
    ladonvichuan = models.BooleanField(db_column='LaDonViChuan')  # Field name made lowercase.
    gianhap = models.FloatField(db_column='GiaNhap')  # Field name made lowercase.
    giaban = models.FloatField(db_column='GiaBan')  # Field name made lowercase.
    ghichu = models.TextField(db_column='GhiChu', blank=True, null=True)  # Field name made lowercase.
    usertao = models.CharField(db_column='UserTao', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaytao = models.DateTimeField(db_column='NgayTao', blank=True, null=True)  # Field name made lowercase.
    usersuacuoi = models.CharField(db_column='UserSuaCuoi', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaysuacuoi = models.DateTimeField(db_column='NgaySuaCuoi', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DonViQuiDoi'


class GaraAnhQtsuachua(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    id_quatrinhsuachua = models.CharField(db_column='ID_QuaTrinhSuaChua', max_length=36)  # Field name made lowercase.
    anh = models.BinaryField(db_column='Anh')  # Field name made lowercase.
    stt = models.IntegerField(db_column='STT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Gara_Anh_QTSuaChua'


class GaraChietkhausuachua(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    id_quatrinh = models.CharField(db_column='ID_QuaTrinh', max_length=36)  # Field name made lowercase.
    id_khachhang = models.CharField(db_column='ID_KhachHang', max_length=36)  # Field name made lowercase.
    chiphikhac = models.FloatField(db_column='ChiPhiKhac')  # Field name made lowercase.
    chietkhau_hopdonggoc = models.FloatField(db_column='ChietKhau_HopDongGoc')  # Field name made lowercase.
    lapt_hopdonggoc = models.BooleanField(db_column='LaPT_HopDongGoc')  # Field name made lowercase.
    chietkhauguithem = models.FloatField(db_column='ChietKhauGuiThem')  # Field name made lowercase.
    chietkhau_guithem = models.FloatField(db_column='ChietKhau_GuiThem')  # Field name made lowercase.
    lapt_guithem = models.BooleanField(db_column='LaPT_GuiThem')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Gara_ChietKhauSuaChua'


class GaraHangxe(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    tenhangxe = models.TextField(db_column='TenHangXe')  # Field name made lowercase.
    ghichu = models.TextField(db_column='GhiChu', blank=True, null=True)  # Field name made lowercase.
    logo = models.BinaryField(db_column='Logo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Gara_HangXe'


class GaraHinhthucsuachua(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    mahinhthuc = models.CharField(db_column='MaHinhThuc', max_length=50)  # Field name made lowercase.
    tenhinhthuc = models.TextField(db_column='TenHinhThuc')  # Field name made lowercase.
    ghichu = models.TextField(db_column='GhiChu', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Gara_HinhThucSuaChua'


class GaraLoaixe(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    tenloaixe = models.TextField(db_column='TenLoaiXe')  # Field name made lowercase.
    id_hangxe = models.CharField(db_column='ID_HangXe', max_length=36)  # Field name made lowercase.
    ghichu = models.TextField(db_column='GhiChu', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Gara_LoaiXe'


class GaraQuatrinhsuachua(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    masuachua = models.CharField(db_column='MaSuaChua', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngayvaoxuong = models.DateTimeField(db_column='NgayVaoXuong')  # Field name made lowercase.
    id_xe = models.CharField(db_column='ID_Xe', max_length=36)  # Field name made lowercase.
    id_khachhang = models.CharField(db_column='ID_KhachHang', max_length=36)  # Field name made lowercase.
    id_lienhechuxe = models.CharField(db_column='ID_LienHeChuXe', max_length=36, blank=True, null=True)  # Field name made lowercase.
    kmvaoxuong = models.FloatField(db_column='KMVaoXuong', blank=True, null=True)  # Field name made lowercase.
    kmxuatxuong = models.FloatField(db_column='KMXuatXuong', blank=True, null=True)  # Field name made lowercase.
    ngayxuatxuong = models.DateTimeField(db_column='NgayXuatXuong', blank=True, null=True)  # Field name made lowercase.
    id_donvi = models.CharField(db_column='ID_DonVi', max_length=36)  # Field name made lowercase.
    ghichu = models.TextField(db_column='GhiChu', blank=True, null=True)  # Field name made lowercase.
    theodoi = models.BooleanField(db_column='TheoDoi')  # Field name made lowercase.
    id_covandichvu = models.CharField(db_column='ID_CoVanDichVu', max_length=36, blank=True, null=True)  # Field name made lowercase.
    daxuatxuong = models.BooleanField(db_column='DaXuatXuong')  # Field name made lowercase.
    id_baohiem = models.CharField(db_column='ID_BaoHiem', max_length=36, blank=True, null=True)  # Field name made lowercase.
    id_lienhebaohiem = models.CharField(db_column='ID_LienHeBaoHiem', max_length=36, blank=True, null=True)  # Field name made lowercase.
    id_nhanvien = models.CharField(db_column='ID_NhanVien', max_length=36, blank=True, null=True)  # Field name made lowercase.
    id_nvtiepnhanxe = models.CharField(db_column='ID_NVTiepNhanXe', max_length=36, blank=True, null=True)  # Field name made lowercase.
    ngaysua = models.DateTimeField(db_column='NgaySua', blank=True, null=True)  # Field name made lowercase.
    ngaytao = models.DateTimeField(db_column='NgayTao', blank=True, null=True)  # Field name made lowercase.
    usersuacuoi = models.CharField(db_column='UserSuaCuoi', max_length=50, blank=True, null=True)  # Field name made lowercase.
    usertao = models.CharField(db_column='UserTao', max_length=50, blank=True, null=True)  # Field name made lowercase.
    listid_covandichvu = models.TextField(db_column='ListID_CoVanDichVu', blank=True, null=True)  # Field name made lowercase.
    ngayradukien = models.DateTimeField(db_column='NgayRaDuKien', blank=True, null=True)  # Field name made lowercase.
    listid_nhanvienkinhdoanh = models.TextField(db_column='ListID_NhanVienKinhDoanh', blank=True, null=True)  # Field name made lowercase.
    ngaydukienketthuc = models.DateTimeField(db_column='NgayDuKienKetThuc', blank=True, null=True)  # Field name made lowercase.
    ngaydukiensua = models.DateTimeField(db_column='NgayDuKienSua', blank=True, null=True)  # Field name made lowercase.
    yeucausuachua = models.TextField(db_column='YeuCauSuaChua', blank=True, null=True)  # Field name made lowercase.
    id_hinhthucsuachua = models.CharField(db_column='ID_HinhThucSuaChua', max_length=36, blank=True, null=True)  # Field name made lowercase.
    ghichuxuatxuong = models.TextField(db_column='GhiChuXuatXuong', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Gara_QuaTrinhSuaChua'


class GaraTinhtrangxeQtsuachua(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    id_quatrinhsuachua = models.CharField(db_column='ID_QuaTrinhSuaChua', max_length=36)  # Field name made lowercase.
    id_phanloai = models.CharField(db_column='ID_PhanLoai', max_length=36, blank=True, null=True)  # Field name made lowercase.
    tinhtrang = models.TextField(db_column='TinhTrang')  # Field name made lowercase.
    phuongan = models.TextField(db_column='PhuongAn', blank=True, null=True)  # Field name made lowercase.
    soluong = models.FloatField(db_column='SoLuong')  # Field name made lowercase.
    ghichu = models.TextField(db_column='GhiChu', blank=True, null=True)  # Field name made lowercase.
    id_dichvuhanghoa = models.CharField(db_column='ID_DichVuHangHoa', max_length=36, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Gara_TinhTrangXe_QTSuaChua'


class GaraVatdunggiaytoQtsuachua(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    id_quatrinhsuachua = models.CharField(db_column='ID_QuaTrinhSuaChua', max_length=36)  # Field name made lowercase.
    tenvatdung = models.TextField(db_column='TenVatDung')  # Field name made lowercase.
    linktailieu = models.TextField(db_column='LinkTaiLieu', blank=True, null=True)  # Field name made lowercase.
    anh = models.BinaryField(db_column='Anh', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Gara_VatDungGiayTo_QTSuaChua'


class GaraXe(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    bienso = models.CharField(db_column='BienSo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sokhung = models.CharField(db_column='SoKhung', max_length=50, blank=True, null=True)  # Field name made lowercase.
    somay = models.CharField(db_column='SoMay', max_length=50, blank=True, null=True)  # Field name made lowercase.
    doixe = models.CharField(db_column='DoiXe', max_length=50, blank=True, null=True)  # Field name made lowercase.
    id_loaixe = models.CharField(db_column='ID_LoaiXe', max_length=36, blank=True, null=True)  # Field name made lowercase.
    mauson = models.CharField(db_column='MauSon', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dungtich = models.CharField(db_column='DungTich', max_length=50, blank=True, null=True)  # Field name made lowercase.
    hopso = models.CharField(db_column='HopSo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    manoithat = models.CharField(db_column='MaNoiThat', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sodangky = models.CharField(db_column='SoDangKy', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaydangky = models.DateTimeField(db_column='NgayDangKy', blank=True, null=True)  # Field name made lowercase.
    noidangky = models.TextField(db_column='NoiDangKy', blank=True, null=True)  # Field name made lowercase.
    id_chuxe = models.CharField(db_column='ID_ChuXe', max_length=36, blank=True, null=True)  # Field name made lowercase.
    id_lienhe = models.CharField(db_column='ID_LienHe', max_length=36, blank=True, null=True)  # Field name made lowercase.
    id_baohiem = models.CharField(db_column='ID_BaoHiem', max_length=36, blank=True, null=True)  # Field name made lowercase.
    id_lienhebaohiem = models.CharField(db_column='ID_LienHeBaoHiem', max_length=36, blank=True, null=True)  # Field name made lowercase.
    ghichu = models.TextField(db_column='GhiChu', blank=True, null=True)  # Field name made lowercase.
    userlap = models.CharField(db_column='UserLap', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaynhap = models.DateTimeField(db_column='NgayNhap', blank=True, null=True)  # Field name made lowercase.
    usersuacuoi = models.CharField(db_column='UserSuaCuoi', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaysuacuoi = models.DateTimeField(db_column='NgaySuaCuoi', blank=True, null=True)  # Field name made lowercase.
    anh = models.BinaryField(db_column='Anh', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Gara_Xe'


class Giaocalamviec(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    ngaybatdau = models.DateTimeField(db_column='NgayBatDau', blank=True, null=True)  # Field name made lowercase.
    id_nhanviengiaoca = models.CharField(db_column='ID_NhanVienGiaoCa', max_length=36, blank=True, null=True)  # Field name made lowercase.
    id_nhanvien = models.CharField(db_column='ID_NhanVien', max_length=36, blank=True, null=True)  # Field name made lowercase.
    ngaygioketthuc = models.DateTimeField(db_column='NgayGioKetThuc', blank=True, null=True)  # Field name made lowercase.
    id_nhanvienketthuc = models.CharField(db_column='ID_NhanVienKetThuc', max_length=36, blank=True, null=True)  # Field name made lowercase.
    sotiengiaoca = models.FloatField(db_column='SoTienGiaoCa', blank=True, null=True)  # Field name made lowercase.
    sotienhoadon = models.FloatField(db_column='SoTienHoaDon', blank=True, null=True)  # Field name made lowercase.
    sotienketthucca = models.FloatField(db_column='SoTienKetThucCa', blank=True, null=True)  # Field name made lowercase.
    ketthucca = models.BooleanField(db_column='KetThucCa', blank=True, null=True)  # Field name made lowercase.
    usertao = models.CharField(db_column='UserTao', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaytao = models.DateTimeField(db_column='NgayTao', blank=True, null=True)  # Field name made lowercase.
    usersuacuoi = models.CharField(db_column='UserSuaCuoi', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaysuacuoi = models.DateTimeField(db_column='NgaySuaCuoi', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GiaoCaLamViec'


class HrsDongiavitri(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    id_nhomdoituong = models.CharField(db_column='ID_NhomDoiTuong', max_length=36)  # Field name made lowercase.
    id_vitri = models.CharField(db_column='ID_ViTri', max_length=36)  # Field name made lowercase.
    thoigian_bd = models.DateTimeField(db_column='ThoiGian_BD')  # Field name made lowercase.
    thoigian_kt = models.DateTimeField(db_column='ThoiGian_KT')  # Field name made lowercase.
    dongia = models.FloatField(db_column='DonGia')  # Field name made lowercase.
    ghichu = models.TextField(db_column='GhiChu', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HRS_DonGiaViTri'


class Hangdoitralai(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    mahoadon = models.CharField(db_column='MaHoaDon', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaylaphoadon = models.DateTimeField(db_column='NgayLapHoaDon')  # Field name made lowercase.
    id_donvi = models.ForeignKey(DmDonvi, models.DO_NOTHING, db_column='ID_DonVi', blank=True, null=True)  # Field name made lowercase.
    id_nhanvien = models.ForeignKey(DmNhanvien, models.DO_NOTHING, db_column='ID_NhanVien', blank=True, null=True)  # Field name made lowercase.
    id_khachhang = models.ForeignKey(DmDoituong, models.DO_NOTHING, db_column='ID_KhachHang', blank=True, null=True)  # Field name made lowercase.
    id_ngoaite = models.ForeignKey(DmTiente, models.DO_NOTHING, db_column='ID_NgoaiTe', blank=True, null=True)  # Field name made lowercase.
    tygia = models.FloatField(db_column='TyGia')  # Field name made lowercase.
    tongtienhangdoi = models.FloatField(db_column='TongTienHangDoi')  # Field name made lowercase.
    tongtienchietkhaudoi = models.FloatField(db_column='TongTienChietKhauDoi')  # Field name made lowercase.
    tongtienthuedoi = models.FloatField(db_column='TongTienThueDoi')  # Field name made lowercase.
    tongthanhtoandoi = models.FloatField(db_column='TongThanhToanDoi')  # Field name made lowercase.
    tongtienhangtralai = models.FloatField(db_column='TongTienHangTraLai')  # Field name made lowercase.
    tongtienchietkhautralai = models.FloatField(db_column='TongTienChietKhauTraLai')  # Field name made lowercase.
    tongtienthuetralai = models.FloatField(db_column='TongTienThueTraLai')  # Field name made lowercase.
    tongthanhtoantralai = models.FloatField(db_column='TongThanhToanTraLai')  # Field name made lowercase.
    tongtienbuchenhlech = models.FloatField(db_column='TongTienBuChenhLech', blank=True, null=True)  # Field name made lowercase.
    daidienkhachhang = models.CharField(db_column='DaiDienKhachHang', max_length=250, blank=True, null=True)  # Field name made lowercase.
    diengiai = models.CharField(db_column='DienGiai', max_length=500, blank=True, null=True)  # Field name made lowercase.
    userlap = models.CharField(db_column='UserLap', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngayvaoso = models.DateTimeField(db_column='NgayVaoSo', blank=True, null=True)  # Field name made lowercase.
    usersuacuoi = models.CharField(db_column='UserSuaCuoi', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaysuacuoi = models.DateTimeField(db_column='NgaySuaCuoi', blank=True, null=True)  # Field name made lowercase.
    banle_hdban = models.IntegerField(db_column='BanLe_HDBan', blank=True, null=True)  # Field name made lowercase.
    id_ctlienquan = models.CharField(db_column='ID_CTLienQuan', max_length=36, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HangDoiTraLai'


class Hangdoitralaichitiet(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    sothutu = models.IntegerField(db_column='SoThuTu', blank=True, null=True)  # Field name made lowercase.
    id_doitralai = models.ForeignKey(Hangdoitralai, models.DO_NOTHING, db_column='ID_DoiTraLai')  # Field name made lowercase.
    id_hanghoa = models.ForeignKey(DmHanghoa, models.DO_NOTHING, db_column='ID_HangHoa')  # Field name made lowercase.
    id_mavach = models.CharField(db_column='ID_MaVach', max_length=36, blank=True, null=True)  # Field name made lowercase.
    id_lohang = models.ForeignKey(DmLohang, models.DO_NOTHING, db_column='ID_LoHang', blank=True, null=True)  # Field name made lowercase.
    id_kho = models.ForeignKey(DmKho, models.DO_NOTHING, db_column='ID_Kho')  # Field name made lowercase.
    id_donvitinh = models.ForeignKey(DmDonvitinh, models.DO_NOTHING, db_column='ID_DonViTinh')  # Field name made lowercase.
    soluong = models.FloatField(db_column='SoLuong')  # Field name made lowercase.
    dongia = models.FloatField(db_column='DonGia')  # Field name made lowercase.
    thanhtien = models.FloatField(db_column='ThanhTien')  # Field name made lowercase.
    tylechietkhau = models.FloatField(db_column='TyLeChietKhau')  # Field name made lowercase.
    tienchietkhau = models.FloatField(db_column='TienChietKhau')  # Field name made lowercase.
    id_thuesuat = models.ForeignKey(DmThuesuat, models.DO_NOTHING, db_column='ID_ThueSuat', blank=True, null=True)  # Field name made lowercase.
    tienthue = models.FloatField(db_column='TienThue')  # Field name made lowercase.
    thanhtoan = models.FloatField(db_column='ThanhToan')  # Field name made lowercase.
    latralai = models.BooleanField(db_column='LaTraLai')  # Field name made lowercase.
    ghichu = models.TextField(db_column='GhiChu', blank=True, null=True)  # Field name made lowercase.
    giavon = models.FloatField(db_column='GiaVon', blank=True, null=True)  # Field name made lowercase.
    thoigianbaohanh = models.FloatField(db_column='ThoiGianBaoHanh', blank=True, null=True)  # Field name made lowercase.
    loaithoigianbh = models.IntegerField(db_column='LoaiThoiGianBH', blank=True, null=True)  # Field name made lowercase.
    id_tangkem = models.CharField(db_column='ID_TangKem', max_length=36, blank=True, null=True)  # Field name made lowercase.
    tangkem = models.BooleanField(db_column='TangKem', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HangDoiTraLaiChiTiet'


class Hangtralainccchitiet(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    id_tralai = models.ForeignKey('Hangtralainhacungcap', models.DO_NOTHING, db_column='ID_TraLai')  # Field name made lowercase.
    sothutu = models.IntegerField(db_column='SoThuTu', blank=True, null=True)  # Field name made lowercase.
    id_hanghoa = models.ForeignKey(DmHanghoa, models.DO_NOTHING, db_column='ID_HangHoa')  # Field name made lowercase.
    id_donvitinh = models.ForeignKey(DmDonvitinh, models.DO_NOTHING, db_column='ID_DonViTinh')  # Field name made lowercase.
    id_mavach = models.CharField(db_column='ID_MaVach', max_length=36, blank=True, null=True)  # Field name made lowercase.
    mavach = models.CharField(db_column='MaVach', max_length=50, blank=True, null=True)  # Field name made lowercase.
    id_kho = models.ForeignKey(DmKho, models.DO_NOTHING, db_column='ID_Kho', blank=True, null=True)  # Field name made lowercase.
    id_lohang = models.ForeignKey(DmLohang, models.DO_NOTHING, db_column='ID_LoHang', blank=True, null=True)  # Field name made lowercase.
    soluong = models.FloatField(db_column='SoLuong')  # Field name made lowercase.
    dongia = models.FloatField(db_column='DonGia')  # Field name made lowercase.
    thanhtien = models.FloatField(db_column='ThanhTien')  # Field name made lowercase.
    ptchietkhau = models.FloatField(db_column='PTChietKhau')  # Field name made lowercase.
    tienchietkhau = models.FloatField(db_column='TienChietKhau', blank=True, null=True)  # Field name made lowercase.
    id_thuesuat = models.ForeignKey(DmThuesuat, models.DO_NOTHING, db_column='ID_ThueSuat', blank=True, null=True)  # Field name made lowercase.
    tienthue = models.FloatField(db_column='TienThue')  # Field name made lowercase.
    thanhtoan = models.FloatField(db_column='ThanhToan')  # Field name made lowercase.
    giavon = models.FloatField(db_column='GiaVon', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HangTraLaiNCCChiTiet'


class Hangtralainhacungcap(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    id_donvi = models.ForeignKey(DmDonvi, models.DO_NOTHING, db_column='ID_DonVi')  # Field name made lowercase.
    mahoadon = models.CharField(db_column='MaHoaDon', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaylaphoadon = models.DateTimeField(db_column='NgayLapHoaDon')  # Field name made lowercase.
    id_nhanvien = models.ForeignKey(DmNhanvien, models.DO_NOTHING, db_column='ID_NhanVien', blank=True, null=True)  # Field name made lowercase.
    id_doituong = models.ForeignKey(DmDoituong, models.DO_NOTHING, db_column='ID_DoiTuong', blank=True, null=True)  # Field name made lowercase.
    id_lienhe = models.ForeignKey(DmLienhe, models.DO_NOTHING, db_column='ID_LienHe', blank=True, null=True)  # Field name made lowercase.
    id_ngoaite = models.ForeignKey(DmTiente, models.DO_NOTHING, db_column='ID_NgoaiTe', blank=True, null=True)  # Field name made lowercase.
    tygia = models.FloatField(db_column='TyGia')  # Field name made lowercase.
    tongtienhang = models.FloatField(db_column='TongTienHang')  # Field name made lowercase.
    tongtienthue = models.FloatField(db_column='TongTienThue')  # Field name made lowercase.
    tongchietkhau = models.FloatField(db_column='TongChietKhau')  # Field name made lowercase.
    tongthanhtoan = models.FloatField(db_column='TongThanhToan')  # Field name made lowercase.
    diengiai = models.TextField(db_column='DienGiai', blank=True, null=True)  # Field name made lowercase.
    usertao = models.CharField(db_column='UserTao', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaytao = models.DateTimeField(db_column='NgayTao', blank=True, null=True)  # Field name made lowercase.
    usersuacuoi = models.CharField(db_column='UserSuaCuoi', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaysuacuoi = models.DateTimeField(db_column='NgaySuaCuoi', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HangTraLaiNhaCungCap'


class Hoadonban(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    mahoadon = models.CharField(db_column='MaHoaDon', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaylaphoadon = models.DateTimeField(db_column='NgayLapHoaDon')  # Field name made lowercase.
    ngayvaoso = models.DateTimeField(db_column='NgayVaoSo', blank=True, null=True)  # Field name made lowercase.
    id_dondathangban = models.ForeignKey(BhDonbanhang, models.DO_NOTHING, db_column='ID_DonDatHangBan', blank=True, null=True)  # Field name made lowercase.
    id_khachhang = models.ForeignKey(DmDoituong, models.DO_NOTHING, db_column='ID_KhachHang', blank=True, null=True)  # Field name made lowercase.
    diachi_khachhang = models.TextField(db_column='DiaChi_KhachHang', blank=True, null=True)  # Field name made lowercase.
    dienthoai_khachhang = models.TextField(db_column='DienThoai_KhachHang', blank=True, null=True)  # Field name made lowercase.
    fax_khachhang = models.TextField(db_column='Fax_KhachHang', blank=True, null=True)  # Field name made lowercase.
    id_lienhe = models.ForeignKey(DmLienhe, models.DO_NOTHING, db_column='ID_LienHe', blank=True, null=True)  # Field name made lowercase.
    id_nhanvien = models.ForeignKey(DmNhanvien, models.DO_NOTHING, db_column='ID_NhanVien', blank=True, null=True)  # Field name made lowercase.
    id_ngoaite = models.ForeignKey(DmTiente, models.DO_NOTHING, db_column='ID_NgoaiTe', blank=True, null=True)  # Field name made lowercase.
    tygia = models.FloatField(db_column='TyGia')  # Field name made lowercase.
    tongtienhang = models.FloatField(db_column='TongTienHang')  # Field name made lowercase.
    tienchietkhau = models.FloatField(db_column='TienChietKhau')  # Field name made lowercase.
    tongtienthue = models.FloatField(db_column='TongTienThue')  # Field name made lowercase.
    tongchiphi = models.FloatField(db_column='TongChiPhi')  # Field name made lowercase.
    tiengiamgia = models.FloatField(db_column='TienGiamGia')  # Field name made lowercase.
    trututhetichdiem = models.FloatField(db_column='TruTuTheTichDiem')  # Field name made lowercase.
    tongthanhtoan = models.FloatField(db_column='TongThanhToan')  # Field name made lowercase.
    id_htthanhtoan = models.CharField(db_column='ID_HTThanhToan', max_length=36, blank=True, null=True)  # Field name made lowercase.
    id_donvi = models.ForeignKey(DmDonvi, models.DO_NOTHING, db_column='ID_DonVi', blank=True, null=True)  # Field name made lowercase.
    userlap = models.CharField(db_column='UserLap', max_length=50, blank=True, null=True)  # Field name made lowercase.
    usersuacuoi = models.CharField(db_column='UserSuaCuoi', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaysuacuoi = models.DateTimeField(db_column='NgaySuaCuoi', blank=True, null=True)  # Field name made lowercase.
    diengiai = models.TextField(db_column='DienGiai', blank=True, null=True)  # Field name made lowercase.
    noidungchiphi = models.TextField(db_column='NoiDungChiPhi', blank=True, null=True)  # Field name made lowercase.
    id_quatrinh = models.CharField(db_column='ID_QuaTrinh', max_length=36, blank=True, null=True)  # Field name made lowercase.
    xuatkhotoanbo = models.BooleanField(db_column='XuatKhoToanBo', blank=True, null=True)  # Field name made lowercase.
    duocphepsua = models.IntegerField(db_column='DuocPhepSua', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HoaDonBan'


class Hoadonbanchitiet(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    id_hoadon = models.ForeignKey(Hoadonban, models.DO_NOTHING, db_column='ID_HoaDon')  # Field name made lowercase.
    sothutu = models.IntegerField(db_column='SoThuTu', blank=True, null=True)  # Field name made lowercase.
    id_hanghoa = models.ForeignKey(DmHanghoa, models.DO_NOTHING, db_column='ID_HangHoa')  # Field name made lowercase.
    id_mavach = models.CharField(db_column='ID_MaVach', max_length=36, blank=True, null=True)  # Field name made lowercase.
    id_donvitinh = models.ForeignKey(DmDonvitinh, models.DO_NOTHING, db_column='ID_DonViTinh')  # Field name made lowercase.
    thoigianbaohanh = models.FloatField(db_column='ThoiGianBaoHanh', blank=True, null=True)  # Field name made lowercase.
    loaithoigianbh = models.IntegerField(db_column='LoaiThoiGianBH', blank=True, null=True)  # Field name made lowercase.
    id_lohang = models.ForeignKey(DmLohang, models.DO_NOTHING, db_column='ID_LoHang', blank=True, null=True)  # Field name made lowercase.
    id_kho = models.ForeignKey(DmKho, models.DO_NOTHING, db_column='ID_Kho', blank=True, null=True)  # Field name made lowercase.
    soluong = models.FloatField(db_column='SoLuong')  # Field name made lowercase.
    dongia = models.FloatField(db_column='DonGia')  # Field name made lowercase.
    thanhtien = models.FloatField(db_column='ThanhTien')  # Field name made lowercase.
    tilechietkhau = models.FloatField(db_column='TiLeChietKhau')  # Field name made lowercase.
    tienchietkhau = models.FloatField(db_column='TienChietKhau')  # Field name made lowercase.
    ptthuesuat = models.FloatField(db_column='PTThueSuat')  # Field name made lowercase.
    tienthue = models.FloatField(db_column='TienThue')  # Field name made lowercase.
    ptchiphi = models.FloatField(db_column='PTChiPhi')  # Field name made lowercase.
    tienchiphi = models.FloatField(db_column='TienChiPhi')  # Field name made lowercase.
    giamgia = models.FloatField(db_column='GiamGia')  # Field name made lowercase.
    thanhtoan = models.FloatField(db_column='ThanhToan')  # Field name made lowercase.
    ghichu = models.TextField(db_column='GhiChu', blank=True, null=True)  # Field name made lowercase.
    giavon = models.FloatField(db_column='GiaVon', blank=True, null=True)  # Field name made lowercase.
    slhaohut = models.FloatField(db_column='SLHaoHut', blank=True, null=True)  # Field name made lowercase.
    thoigian = models.DateTimeField(db_column='ThoiGian', blank=True, null=True)  # Field name made lowercase.
    thoigianthuchien = models.FloatField(db_column='ThoiGianThucHien', blank=True, null=True)  # Field name made lowercase.
    tralaivattuthaythe = models.BooleanField(db_column='TraLaiVatTuThayThe', blank=True, null=True)  # Field name made lowercase.
    id_tangkem = models.CharField(db_column='ID_TangKem', max_length=36, blank=True, null=True)  # Field name made lowercase.
    tangkem = models.BooleanField(db_column='TangKem', blank=True, null=True)  # Field name made lowercase.
    tenhanghoathaythe = models.TextField(db_column='TenHangHoaThayThe', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HoaDonBanChiTiet'


class Hoadonbanle(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    mahoadon = models.CharField(db_column='MaHoaDon', max_length=50)  # Field name made lowercase.
    ngaylaphoadon = models.DateTimeField(db_column='NgayLapHoaDon')  # Field name made lowercase.
    giovao = models.DateTimeField(db_column='GioVao', blank=True, null=True)  # Field name made lowercase.
    giora = models.DateTimeField(db_column='GioRa', blank=True, null=True)  # Field name made lowercase.
    id_vitri = models.CharField(db_column='ID_ViTri', max_length=36, blank=True, null=True)  # Field name made lowercase.
    id_checkin = models.CharField(db_column='ID_CheckIn', max_length=36, blank=True, null=True)  # Field name made lowercase.
    id_doituong = models.ForeignKey(DmDoituong, models.DO_NOTHING, db_column='ID_DoiTuong')  # Field name made lowercase.
    diachi_khachhang = models.TextField(db_column='DiaChi_KhachHang', blank=True, null=True)  # Field name made lowercase.
    dienthoai_khachhang = models.TextField(db_column='DienThoai_KhachHang', blank=True, null=True)  # Field name made lowercase.
    fax_khachhang = models.TextField(db_column='Fax_KhachHang', blank=True, null=True)  # Field name made lowercase.
    id_ngoaite = models.ForeignKey(DmTiente, models.DO_NOTHING, db_column='ID_NgoaiTe', blank=True, null=True)  # Field name made lowercase.
    tygia = models.FloatField(db_column='TyGia')  # Field name made lowercase.
    id_nhanvien = models.ForeignKey(DmNhanvien, models.DO_NOTHING, db_column='ID_NhanVien', blank=True, null=True)  # Field name made lowercase.
    loaihoadon = models.IntegerField(db_column='LoaiHoaDon')  # Field name made lowercase.
    chothanhtoan = models.BooleanField(db_column='ChoThanhToan')  # Field name made lowercase.
    tongtienhang = models.FloatField(db_column='TongTienHang')  # Field name made lowercase.
    tongchietkhau = models.FloatField(db_column='TongChietKhau')  # Field name made lowercase.
    tongtienthue = models.FloatField(db_column='TongTienThue')  # Field name made lowercase.
    tonggiamgia = models.FloatField(db_column='TongGiamGia')  # Field name made lowercase.
    tongchiphi = models.FloatField(db_column='TongChiPhi')  # Field name made lowercase.
    phaithanhtoan = models.FloatField(db_column='PhaiThanhToan')  # Field name made lowercase.
    diengiai = models.TextField(db_column='DienGiai', blank=True, null=True)  # Field name made lowercase.
    solanin = models.IntegerField(db_column='SoLanIn', blank=True, null=True)  # Field name made lowercase.
    userlap = models.CharField(db_column='UserLap', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngayvaoso = models.DateTimeField(db_column='NgayVaoSo', blank=True, null=True)  # Field name made lowercase.
    ngaysuacuoi = models.DateTimeField(db_column='NgaySuaCuoi', blank=True, null=True)  # Field name made lowercase.
    usersuacuoi = models.CharField(db_column='UserSuaCuoi', max_length=50, blank=True, null=True)  # Field name made lowercase.
    id_donvi = models.ForeignKey(DmDonvi, models.DO_NOTHING, db_column='ID_DonVi')  # Field name made lowercase.
    yeucau = models.TextField(db_column='YeuCau', blank=True, null=True)  # Field name made lowercase.
    id_dacdiemkhachhang = models.CharField(db_column='ID_DacDiemKhachHang', max_length=36, blank=True, null=True)  # Field name made lowercase.
    loaichungtu = models.IntegerField(db_column='LoaiChungTu', blank=True, null=True)  # Field name made lowercase.
    manhanvienthuchien = models.CharField(db_column='MaNhanVienThucHien', max_length=50, blank=True, null=True)  # Field name made lowercase.
    manhanvientuvan = models.CharField(db_column='MaNhanVienTuVan', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mathegiatri = models.TextField(db_column='MaTheGiaTri', blank=True, null=True)  # Field name made lowercase.
    mathelan = models.TextField(db_column='MaTheLan', blank=True, null=True)  # Field name made lowercase.
    tennhanvienthuchien = models.TextField(db_column='TenNhanVienThucHien', blank=True, null=True)  # Field name made lowercase.
    tennhanvientuvan = models.TextField(db_column='TenNhanVienTuVan', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HoaDonBanLe'


class Hoadonbanlechitiet(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    id_hoadon = models.ForeignKey(Hoadonbanle, models.DO_NOTHING, db_column='ID_HoaDon')  # Field name made lowercase.
    sothutu = models.IntegerField(db_column='SoThuTu')  # Field name made lowercase.
    thoigian = models.DateTimeField(db_column='ThoiGian', blank=True, null=True)  # Field name made lowercase.
    id_hanghoa = models.ForeignKey(DmHanghoa, models.DO_NOTHING, db_column='ID_HangHoa')  # Field name made lowercase.
    thoigianbaohanh = models.FloatField(db_column='ThoiGianBaoHanh', blank=True, null=True)  # Field name made lowercase.
    loaithoigianbh = models.IntegerField(db_column='LoaiThoiGianBH', blank=True, null=True)  # Field name made lowercase.
    id_khohang = models.ForeignKey(DmKho, models.DO_NOTHING, db_column='ID_KhoHang', blank=True, null=True)  # Field name made lowercase.
    id_donvitinh = models.ForeignKey(DmDonvitinh, models.DO_NOTHING, db_column='ID_DonViTinh')  # Field name made lowercase.
    id_lohang = models.ForeignKey(DmLohang, models.DO_NOTHING, db_column='ID_LoHang', blank=True, null=True)  # Field name made lowercase.
    id_mavach = models.CharField(db_column='ID_MaVach', max_length=36, blank=True, null=True)  # Field name made lowercase.
    chatlieu = models.CharField(db_column='ChatLieu', max_length=250, blank=True, null=True)  # Field name made lowercase.
    mausac = models.CharField(db_column='MauSac', max_length=250, blank=True, null=True)  # Field name made lowercase.
    kichco = models.CharField(db_column='KichCo', max_length=250, blank=True, null=True)  # Field name made lowercase.
    soluong = models.FloatField(db_column='SoLuong')  # Field name made lowercase.
    dongia = models.FloatField(db_column='DonGia')  # Field name made lowercase.
    thanhtien = models.FloatField(db_column='ThanhTien')  # Field name made lowercase.
    ptchietkhau = models.FloatField(db_column='PTChietKhau')  # Field name made lowercase.
    tienchietkhau = models.FloatField(db_column='TienChietKhau')  # Field name made lowercase.
    id_thuesuat = models.CharField(db_column='ID_ThueSuat', max_length=36, blank=True, null=True)  # Field name made lowercase.
    tienthue = models.FloatField(db_column='TienThue')  # Field name made lowercase.
    ptchiphi = models.FloatField(db_column='PTChiPhi')  # Field name made lowercase.
    tienchiphi = models.FloatField(db_column='TienChiPhi')  # Field name made lowercase.
    thanhtoan = models.FloatField(db_column='ThanhToan')  # Field name made lowercase.
    giavon = models.FloatField(db_column='GiaVon', blank=True, null=True)  # Field name made lowercase.
    ghichu = models.TextField(db_column='GhiChu', blank=True, null=True)  # Field name made lowercase.
    usernhap = models.CharField(db_column='UserNhap', max_length=50, blank=True, null=True)  # Field name made lowercase.
    solandain = models.FloatField(db_column='SoLanDaIn', blank=True, null=True)  # Field name made lowercase.
    id_tangkem = models.CharField(db_column='ID_TangKem', max_length=36, blank=True, null=True)  # Field name made lowercase.
    tangkem = models.BooleanField(db_column='TangKem', blank=True, null=True)  # Field name made lowercase.
    thoigianthuchien = models.FloatField(db_column='ThoiGianThucHien', blank=True, null=True)  # Field name made lowercase.
    soluong_tl = models.FloatField(db_column='SoLuong_TL', blank=True, null=True)  # Field name made lowercase.
    soluong_yc = models.FloatField(db_column='SoLuong_YC', blank=True, null=True)  # Field name made lowercase.
    chieu = models.BooleanField(db_column='Chieu', blank=True, null=True)  # Field name made lowercase.
    sang = models.BooleanField(db_column='Sang', blank=True, null=True)  # Field name made lowercase.
    ptthue = models.FloatField(db_column='PTThue', blank=True, null=True)  # Field name made lowercase.
    manhanvienthuchien = models.CharField(db_column='MaNhanVienThucHien', max_length=50, blank=True, null=True)  # Field name made lowercase.
    manhanvientuvan = models.CharField(db_column='MaNhanVienTuVan', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mathegiatri = models.TextField(db_column='MaTheGiaTri', blank=True, null=True)  # Field name made lowercase.
    mathelan = models.TextField(db_column='MaTheLan', blank=True, null=True)  # Field name made lowercase.
    tennhanvienthuchien = models.TextField(db_column='TenNhanVienThucHien', blank=True, null=True)  # Field name made lowercase.
    tennhanvientuvan = models.TextField(db_column='TenNhanVienTuVan', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HoaDonBanLeChiTiet'


class HoadonbanleDacdiemkhachhang(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    id_hoadonbanle = models.CharField(db_column='ID_HoaDonBanLe', max_length=36)  # Field name made lowercase.
    id_dacdiemkhachhang = models.CharField(db_column='ID_DacDiemKhachHang', max_length=36)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HoaDonBanLe_DacDiemKhachHang'


class HoadonbanChietkhauthanhtoan(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    sophieu = models.CharField(db_column='SoPhieu', max_length=50)  # Field name made lowercase.
    ngay = models.DateTimeField(db_column='Ngay')  # Field name made lowercase.
    id_hoadon = models.CharField(db_column='ID_HoaDon', max_length=36)  # Field name made lowercase.
    chietkhauthanhtoan = models.FloatField(db_column='ChietKhauThanhToan')  # Field name made lowercase.
    laphantram = models.BooleanField(db_column='LaPhanTram')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HoaDonBan_ChietKhauThanhToan'


class Hoadondichvu(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    id_hoadon = models.CharField(db_column='ID_HoaDon', max_length=36)  # Field name made lowercase.
    bddichvu = models.DateTimeField(db_column='BDDichVu')  # Field name made lowercase.
    ktdichvu = models.DateTimeField(db_column='KTDichVu')  # Field name made lowercase.
    tongthoigian = models.FloatField(db_column='TongThoiGian')  # Field name made lowercase.
    dongiadichvu = models.FloatField(db_column='DonGiaDichVu')  # Field name made lowercase.
    tongtiendichvu = models.FloatField(db_column='TongTienDichVu')  # Field name made lowercase.
    chietkhau = models.FloatField(db_column='ChietKhau')  # Field name made lowercase.
    laptchietkhau = models.BooleanField(db_column='LaPTChietKhau')  # Field name made lowercase.
    ptthue = models.FloatField(db_column='PTThue')  # Field name made lowercase.
    tienthue = models.FloatField(db_column='TienThue')  # Field name made lowercase.
    tongthanhtoan = models.FloatField(db_column='TongThanhToan')  # Field name made lowercase.
    dangtinhgio = models.BooleanField(db_column='DangTinhGio')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HoaDonDichVu'


class HotelCheckin(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    sophieu = models.CharField(db_column='SoPhieu', max_length=50)  # Field name made lowercase.
    ngaycheckin = models.DateTimeField(db_column='NgayCheckIn')  # Field name made lowercase.
    id_khachhang = models.CharField(db_column='ID_KhachHang', max_length=36)  # Field name made lowercase.
    id_nhanvien = models.CharField(db_column='ID_NhanVien', max_length=36, blank=True, null=True)  # Field name made lowercase.
    id_donvi = models.CharField(db_column='ID_DonVi', max_length=36)  # Field name made lowercase.
    ghichu = models.TextField(db_column='GhiChu', blank=True, null=True)  # Field name made lowercase.
    id_tiente = models.CharField(db_column='ID_TienTe', max_length=36, blank=True, null=True)  # Field name made lowercase.
    tygia = models.FloatField(db_column='TyGia', blank=True, null=True)  # Field name made lowercase.
    userlap = models.CharField(db_column='UserLap', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaynhap = models.DateTimeField(db_column='NgayNhap', blank=True, null=True)  # Field name made lowercase.
    usersua = models.CharField(db_column='UserSua', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaysuacuoi = models.DateTimeField(db_column='NgaySuaCuoi', blank=True, null=True)  # Field name made lowercase.
    id_booking = models.CharField(db_column='ID_Booking', max_length=36, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Hotel_CheckIn'


class HotelCheckinChitiet(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    id_checkin = models.CharField(db_column='ID_CheckIn', max_length=36)  # Field name made lowercase.
    id_phong = models.CharField(db_column='ID_Phong', max_length=36, blank=True, null=True)  # Field name made lowercase.
    thoigianden = models.DateTimeField(db_column='ThoiGianDen')  # Field name made lowercase.
    thoigiandi = models.DateTimeField(db_column='ThoiGianDi', blank=True, null=True)  # Field name made lowercase.
    id_loaigia = models.CharField(db_column='ID_LoaiGia', max_length=36, blank=True, null=True)  # Field name made lowercase.
    dongiangay = models.FloatField(db_column='DonGiaNgay')  # Field name made lowercase.
    dongiagio = models.FloatField(db_column='DonGiaGio')  # Field name made lowercase.
    soluong_ngay = models.FloatField(db_column='SoLuong_Ngay')  # Field name made lowercase.
    soluong_gio = models.FloatField(db_column='SoLuong_Gio')  # Field name made lowercase.
    soluong_nguoi = models.IntegerField(db_column='SoLuong_Nguoi')  # Field name made lowercase.
    chietkhau = models.FloatField(db_column='ChietKhau')  # Field name made lowercase.
    ptchietkhau = models.FloatField(db_column='PTChietKhau')  # Field name made lowercase.
    theongay = models.BooleanField(db_column='TheoNgay', blank=True, null=True)  # Field name made lowercase.
    thanhtoan = models.FloatField(db_column='ThanhToan', blank=True, null=True)  # Field name made lowercase.
    ghichu = models.TextField(db_column='GhiChu', blank=True, null=True)  # Field name made lowercase.
    ngaycheck_out = models.DateTimeField(db_column='NgayCheck_Out', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Hotel_CheckIn_ChiTiet'


class HotelDatphong(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    sophieu = models.CharField(db_column='SoPhieu', max_length=50)  # Field name made lowercase.
    ngaydat = models.DateTimeField(db_column='NgayDat')  # Field name made lowercase.
    id_khachhang = models.CharField(db_column='ID_KhachHang', max_length=36, blank=True, null=True)  # Field name made lowercase.
    id_nhanvien = models.CharField(db_column='ID_NhanVien', max_length=36, blank=True, null=True)  # Field name made lowercase.
    id_donvi = models.CharField(db_column='ID_DonVi', max_length=36)  # Field name made lowercase.
    ghichu = models.TextField(db_column='GhiChu', blank=True, null=True)  # Field name made lowercase.
    id_tiente = models.CharField(db_column='ID_TienTe', max_length=36, blank=True, null=True)  # Field name made lowercase.
    tygia = models.FloatField(db_column='TyGia', blank=True, null=True)  # Field name made lowercase.
    userlap = models.CharField(db_column='UserLap', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaynhap = models.DateTimeField(db_column='NgayNhap', blank=True, null=True)  # Field name made lowercase.
    usersua = models.CharField(db_column='UserSua', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaysuacuoi = models.DateTimeField(db_column='NgaySuaCuoi', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Hotel_DatPhong'


class HotelDatphongChitiet(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    id_datphong = models.CharField(db_column='ID_DatPhong', max_length=36)  # Field name made lowercase.
    id_loaiphong = models.CharField(db_column='ID_LoaiPhong', max_length=36, blank=True, null=True)  # Field name made lowercase.
    thoigianden = models.DateTimeField(db_column='ThoiGianDen')  # Field name made lowercase.
    thoigiandi = models.DateTimeField(db_column='ThoiGianDi', blank=True, null=True)  # Field name made lowercase.
    id_loaigia = models.CharField(db_column='ID_LoaiGia', max_length=36, blank=True, null=True)  # Field name made lowercase.
    dongia = models.FloatField(db_column='DonGia')  # Field name made lowercase.
    soluong_nguoi = models.IntegerField(db_column='SoLuong_Nguoi')  # Field name made lowercase.
    chietkhau = models.FloatField(db_column='ChietKhau')  # Field name made lowercase.
    ptchietkhau = models.FloatField(db_column='PTChietKhau')  # Field name made lowercase.
    thanhtoan = models.FloatField(db_column='ThanhToan')  # Field name made lowercase.
    ghichu = models.TextField(db_column='GhiChu', blank=True, null=True)  # Field name made lowercase.
    theongay = models.BooleanField(db_column='TheoNgay', blank=True, null=True)  # Field name made lowercase.
    id_phong = models.CharField(db_column='ID_Phong', max_length=36, blank=True, null=True)  # Field name made lowercase.
    theodoi = models.BooleanField(db_column='TheoDoi', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Hotel_DatPhong_ChiTiet'


class HotelDongiaphong(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    id_loaiphong = models.CharField(db_column='ID_LoaiPhong', max_length=36)  # Field name made lowercase.
    id_loaigia = models.CharField(db_column='ID_LoaiGia', max_length=36)  # Field name made lowercase.
    dongia = models.FloatField(db_column='DonGia')  # Field name made lowercase.
    tungay = models.DateTimeField(db_column='TuNgay', blank=True, null=True)  # Field name made lowercase.
    denngay = models.DateTimeField(db_column='DenNgay', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Hotel_DonGiaPhong'


class HotelHoadonsudungdichvu(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    loaict = models.IntegerField(db_column='LoaiCT')  # Field name made lowercase.
    idchungtu = models.CharField(db_column='IDChungTu', max_length=36)  # Field name made lowercase.
    idcheckin = models.CharField(db_column='IDCheckIn', max_length=36)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Hotel_HoaDonSuDungDichVu'


class KhAnh(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    id_khachhang = models.ForeignKey(DmDoituong, models.DO_NOTHING, db_column='ID_KhachHang')  # Field name made lowercase.
    anh = models.BinaryField(db_column='Anh')  # Field name made lowercase.
    ghichu = models.TextField(db_column='GhiChu', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'KH_Anh'


class KhKiemke(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    sochungtu = models.CharField(db_column='SoChungTu', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaychungtu = models.DateTimeField(db_column='NgayChungTu')  # Field name made lowercase.
    id_nhanvien = models.ForeignKey(DmNhanvien, models.DO_NOTHING, db_column='ID_NhanVien', blank=True, null=True)  # Field name made lowercase.
    diengiai = models.CharField(db_column='DienGiai', max_length=500, blank=True, null=True)  # Field name made lowercase.
    id_donvi = models.ForeignKey(DmDonvi, models.DO_NOTHING, db_column='ID_DonVi')  # Field name made lowercase.
    ngayvaoso = models.DateTimeField(db_column='NgayVaoSo', blank=True, null=True)  # Field name made lowercase.
    userlap = models.CharField(db_column='UserLap', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaysuacuoi = models.DateTimeField(db_column='NgaySuaCuoi', blank=True, null=True)  # Field name made lowercase.
    usersuacuoi = models.CharField(db_column='UserSuaCuoi', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'KH_KiemKe'


class KhKiemkechitiet(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    id_kiemke = models.ForeignKey(KhKiemke, models.DO_NOTHING, db_column='ID_KiemKe')  # Field name made lowercase.
    id_kho = models.ForeignKey(DmKho, models.DO_NOTHING, db_column='ID_Kho', blank=True, null=True)  # Field name made lowercase.
    id_hanghoa = models.ForeignKey(DmHanghoa, models.DO_NOTHING, db_column='ID_HangHoa')  # Field name made lowercase.
    id_mavach = models.CharField(db_column='ID_MaVach', max_length=36, blank=True, null=True)  # Field name made lowercase.
    id_nhacc = models.CharField(db_column='ID_NhaCC', max_length=36, blank=True, null=True)  # Field name made lowercase.
    id_donvitinh = models.ForeignKey(DmDonvitinh, models.DO_NOTHING, db_column='ID_DonViTinh')  # Field name made lowercase.
    id_lohang = models.ForeignKey(DmLohang, models.DO_NOTHING, db_column='ID_LoHang', blank=True, null=True)  # Field name made lowercase.
    soluongton = models.FloatField(db_column='SoLuongTon')  # Field name made lowercase.
    theolo = models.BooleanField(db_column='TheoLo')  # Field name made lowercase.
    soluongkiemke = models.FloatField(db_column='SoLuongKiemKe')  # Field name made lowercase.
    dongia = models.FloatField(db_column='DonGia', blank=True, null=True)  # Field name made lowercase.
    giatri = models.FloatField(db_column='GiaTri', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'KH_KiemKeChiTiet'


class KhNhapkho(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    id_donvi = models.ForeignKey(DmDonvi, models.DO_NOTHING, db_column='ID_DonVi', blank=True, null=True)  # Field name made lowercase.
    sochungtu = models.CharField(db_column='SoChungTu', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaychungtu = models.DateTimeField(db_column='NgayChungTu')  # Field name made lowercase.
    ngayvaoso = models.DateTimeField(db_column='NgayVaoSo', blank=True, null=True)  # Field name made lowercase.
    userlap = models.CharField(db_column='UserLap', max_length=50, blank=True, null=True)  # Field name made lowercase.
    id_doituong = models.ForeignKey(DmDoituong, models.DO_NOTHING, db_column='ID_DoiTuong', blank=True, null=True)  # Field name made lowercase.
    id_nhanvien = models.ForeignKey(DmNhanvien, models.DO_NOTHING, db_column='ID_NhanVien', blank=True, null=True)  # Field name made lowercase.
    id_ngoaite = models.ForeignKey(DmTiente, models.DO_NOTHING, db_column='ID_NgoaiTe', blank=True, null=True)  # Field name made lowercase.
    tygia = models.FloatField(db_column='TyGia')  # Field name made lowercase.
    nguoigiao = models.TextField(db_column='NguoiGiao', blank=True, null=True)  # Field name made lowercase.
    tongthanhtien = models.FloatField(db_column='TongThanhTien', blank=True, null=True)  # Field name made lowercase.
    id_chungtulienquan = models.CharField(db_column='ID_ChungTuLienQuan', max_length=36, blank=True, null=True)  # Field name made lowercase.
    loaichungtulienquan = models.IntegerField(db_column='LoaiChungTuLienQuan', blank=True, null=True)  # Field name made lowercase.
    diengiai = models.TextField(db_column='DienGiai', blank=True, null=True)  # Field name made lowercase.
    ngaysuacuoi = models.DateTimeField(db_column='NgaySuaCuoi', blank=True, null=True)  # Field name made lowercase.
    usersuacuoi = models.CharField(db_column='UserSuaCuoi', max_length=50, blank=True, null=True)  # Field name made lowercase.
    id_loainhapkho = models.CharField(db_column='ID_LoaiNhapKho', max_length=36, blank=True, null=True)  # Field name made lowercase.
    id_phieusuachua = models.CharField(db_column='ID_PhieuSuaChua', max_length=36, blank=True, null=True)  # Field name made lowercase.
    id_xe = models.ForeignKey(GaraXe, models.DO_NOTHING, db_column='ID_Xe', blank=True, null=True)  # Field name made lowercase.
    duocphepsua = models.IntegerField(db_column='DuocPhepSua', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'KH_NhapKho'


class KhNhapkhoChitiet(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    sothutu = models.IntegerField(db_column='SoThuTu', blank=True, null=True)  # Field name made lowercase.
    id_nhapkho = models.ForeignKey(KhNhapkho, models.DO_NOTHING, db_column='ID_NhapKho')  # Field name made lowercase.
    id_kho = models.ForeignKey(DmKho, models.DO_NOTHING, db_column='ID_Kho')  # Field name made lowercase.
    id_hanghoa = models.ForeignKey(DmHanghoa, models.DO_NOTHING, db_column='ID_HangHoa')  # Field name made lowercase.
    id_mavach = models.CharField(db_column='ID_MaVach', max_length=36, blank=True, null=True)  # Field name made lowercase.
    id_donvitinh = models.ForeignKey(DmDonvitinh, models.DO_NOTHING, db_column='ID_DonViTinh')  # Field name made lowercase.
    id_lohang = models.ForeignKey(DmLohang, models.DO_NOTHING, db_column='ID_LoHang', blank=True, null=True)  # Field name made lowercase.
    soluong = models.FloatField(db_column='SoLuong')  # Field name made lowercase.
    dongia = models.FloatField(db_column='DonGia')  # Field name made lowercase.
    thanhtien = models.FloatField(db_column='ThanhTien')  # Field name made lowercase.
    ghichu = models.TextField(db_column='GhiChu', blank=True, null=True)  # Field name made lowercase.
    id_ctchungtulienquan = models.CharField(db_column='ID_CTChungTuLienQuan', max_length=36, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'KH_NhapKho_ChiTiet'


class KhXuatkho(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    sochungtu = models.CharField(db_column='SoChungTu', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaychungtu = models.DateTimeField(db_column='NgayChungTu')  # Field name made lowercase.
    id_donvi = models.ForeignKey(DmDonvi, models.DO_NOTHING, db_column='ID_DonVi', blank=True, null=True)  # Field name made lowercase.
    ngayvaoso = models.DateTimeField(db_column='NgayVaoSo')  # Field name made lowercase.
    userlap = models.CharField(db_column='UserLap', max_length=50)  # Field name made lowercase.
    id_doituong = models.ForeignKey(DmDoituong, models.DO_NOTHING, db_column='ID_DoiTuong', blank=True, null=True)  # Field name made lowercase.
    id_nhanvien = models.ForeignKey(DmNhanvien, models.DO_NOTHING, db_column='ID_NhanVien', blank=True, null=True)  # Field name made lowercase.
    id_ngoaite = models.ForeignKey(DmTiente, models.DO_NOTHING, db_column='ID_NgoaiTe', blank=True, null=True)  # Field name made lowercase.
    tygia = models.FloatField(db_column='TyGia')  # Field name made lowercase.
    nguoinhan = models.CharField(db_column='NguoiNhan', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tongtienhang = models.FloatField(db_column='TongTienHang')  # Field name made lowercase.
    diengiai = models.CharField(db_column='DienGiai', max_length=500, blank=True, null=True)  # Field name made lowercase.
    ngaysuacuoi = models.DateTimeField(db_column='NgaySuaCuoi', blank=True, null=True)  # Field name made lowercase.
    usersuacuoi = models.CharField(db_column='UserSuaCuoi', max_length=50, blank=True, null=True)  # Field name made lowercase.
    id_chungtulienquan = models.CharField(db_column='ID_ChungTuLienQuan', max_length=36, blank=True, null=True)  # Field name made lowercase.
    loaichungtulienquan = models.IntegerField(db_column='LoaiChungTuLienQuan', blank=True, null=True)  # Field name made lowercase.
    id_loaixuatkho = models.CharField(db_column='ID_LoaiXuatKho', max_length=36, blank=True, null=True)  # Field name made lowercase.
    id_phieusuachua = models.CharField(db_column='ID_PhieuSuaChua', max_length=36, blank=True, null=True)  # Field name made lowercase.
    id_nhanviennhan = models.CharField(db_column='ID_NhanVienNhan', max_length=36, blank=True, null=True)  # Field name made lowercase.
    phieuxuatnoibo = models.BooleanField(db_column='PhieuXuatNoiBo', blank=True, null=True)  # Field name made lowercase.
    id_xe = models.ForeignKey(GaraXe, models.DO_NOTHING, db_column='ID_Xe', blank=True, null=True)  # Field name made lowercase.
    duocphepsua = models.IntegerField(db_column='DuocPhepSua', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'KH_XuatKho'


class KhXuatkhoChitiet(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    id_xuatkho = models.ForeignKey(KhXuatkho, models.DO_NOTHING, db_column='ID_XuatKho')  # Field name made lowercase.
    sothutu = models.IntegerField(db_column='SoThuTu', blank=True, null=True)  # Field name made lowercase.
    id_kho = models.ForeignKey(DmKho, models.DO_NOTHING, db_column='ID_Kho')  # Field name made lowercase.
    id_hanghoa = models.ForeignKey(DmHanghoa, models.DO_NOTHING, db_column='ID_HangHoa')  # Field name made lowercase.
    id_donvitinh = models.ForeignKey(DmDonvitinh, models.DO_NOTHING, db_column='ID_DonViTinh')  # Field name made lowercase.
    id_mavach = models.CharField(db_column='ID_MaVach', max_length=36, blank=True, null=True)  # Field name made lowercase.
    id_lohang = models.ForeignKey(DmLohang, models.DO_NOTHING, db_column='ID_LoHang', blank=True, null=True)  # Field name made lowercase.
    soluong = models.FloatField(db_column='SoLuong')  # Field name made lowercase.
    dongia = models.FloatField(db_column='DonGia')  # Field name made lowercase.
    thanhtien = models.FloatField(db_column='ThanhTien')  # Field name made lowercase.
    id_ctchungtulienquan = models.CharField(db_column='ID_CTChungTuLienQuan', max_length=36, blank=True, null=True)  # Field name made lowercase.
    giavon = models.FloatField(db_column='GiaVon', blank=True, null=True)  # Field name made lowercase.
    tienvon = models.FloatField(db_column='TienVon', blank=True, null=True)  # Field name made lowercase.
    ghichu = models.TextField(db_column='GhiChu', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'KH_XuatKho_ChiTiet'


class KhoDonvi(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    id_kho = models.CharField(db_column='ID_Kho', max_length=36)  # Field name made lowercase.
    id_donvi = models.CharField(db_column='ID_DonVi', max_length=36)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Kho_DonVi'


class KhoKhuyenmai(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    id_kho = models.CharField(db_column='ID_Kho', max_length=36)  # Field name made lowercase.
    id_khuyenmai = models.CharField(db_column='ID_KhuyenMai', max_length=36)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Kho_KhuyenMai'


class Khoasolieu(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    denngay = models.DateTimeField(db_column='DenNgay')  # Field name made lowercase.
    id_donvi = models.CharField(db_column='ID_DonVi', max_length=36, blank=True, null=True)  # Field name made lowercase.
    ngayvaoso = models.DateTimeField(db_column='NgayVaoSo', blank=True, null=True)  # Field name made lowercase.
    userlap = models.CharField(db_column='UserLap', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaysuacuoi = models.DateTimeField(db_column='NgaySuaCuoi', blank=True, null=True)  # Field name made lowercase.
    usersuacuoi = models.CharField(db_column='UserSuaCuoi', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ghichu = models.TextField(db_column='GhiChu', blank=True, null=True)  # Field name made lowercase.
    xemdulieudakhoa = models.BooleanField(db_column='XemDuLieuDaKhoa', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'KhoaSoLieu'


class KhoanchiphiDoanhthu(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    ma = models.CharField(db_column='Ma', max_length=150, blank=True, null=True)  # Field name made lowercase.
    ten = models.CharField(db_column='Ten', max_length=255)  # Field name made lowercase.
    ghichu = models.TextField(db_column='GhiChu', blank=True, null=True)  # Field name made lowercase.
    lachiphi = models.BooleanField(db_column='LaChiPhi')  # Field name made lowercase.
    sudung = models.BooleanField(db_column='SuDung')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'KhoanChiPhi_DoanhThu'


class Khoanthuchi(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    makhoanthuchi = models.CharField(db_column='MaKhoanThuChi', max_length=50)  # Field name made lowercase.
    noidungthuchi = models.CharField(db_column='NoiDungThuChi', max_length=500, blank=True, null=True)  # Field name made lowercase.
    ghichu = models.CharField(db_column='GhiChu', max_length=500, blank=True, null=True)  # Field name made lowercase.
    lakhoanthu = models.BooleanField(db_column='LaKhoanThu')  # Field name made lowercase.
    butrucongno = models.BooleanField(db_column='BuTruCongNo')  # Field name made lowercase.
    usertao = models.CharField(db_column='UserTao', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaytao = models.DateTimeField(db_column='NgayTao', blank=True, null=True)  # Field name made lowercase.
    usersuacuoi = models.CharField(db_column='UserSuaCuoi', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaysuacuoi = models.DateTimeField(db_column='NgaySuaCuoi', blank=True, null=True)  # Field name made lowercase.
    tinhluong = models.BooleanField(db_column='TinhLuong', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'KhoanThuChi'


class KhoanthuchiChiphidoanhthu(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    id_khoancpdt = models.CharField(db_column='ID_KhoanCPDT', max_length=36)  # Field name made lowercase.
    id_khoanthuchi = models.CharField(db_column='ID_KhoanThuChi', max_length=36)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'KhoanThuChi_ChiPhiDoanhThu'


class KhuvucDonvi(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    id_khuvuc = models.CharField(db_column='ID_KhuVuc', max_length=36)  # Field name made lowercase.
    id_donvi = models.CharField(db_column='ID_DonVi', max_length=36)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'KhuVuc_DonVi'


class Khuyenmaitangkem(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    id_kho = models.CharField(db_column='ID_Kho', max_length=36, blank=True, null=True)  # Field name made lowercase.
    tungay = models.DateTimeField(db_column='TuNgay')  # Field name made lowercase.
    denngay = models.DateTimeField(db_column='DenNgay', blank=True, null=True)  # Field name made lowercase.
    usertao = models.CharField(db_column='UserTao', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaytao = models.DateTimeField(db_column='NgayTao', blank=True, null=True)  # Field name made lowercase.
    usersuacuoi = models.CharField(db_column='UserSuaCuoi', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaysuacuoi = models.DateTimeField(db_column='NgaySuaCuoi', blank=True, null=True)  # Field name made lowercase.
    apdung = models.BooleanField(db_column='ApDung')  # Field name made lowercase.
    lakhuyenmaithe = models.BooleanField(db_column='LaKhuyenMaiThe', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'KhuyenMaiTangKem'


class Lichhenkhachhang(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    tieude = models.TextField(db_column='TieuDe', blank=True, null=True)  # Field name made lowercase.
    ngaydatlich = models.DateTimeField(db_column='NgayDatLich')  # Field name made lowercase.
    ngayhen = models.DateTimeField(db_column='NgayHen')  # Field name made lowercase.
    cangay = models.BooleanField(db_column='CaNgay')  # Field name made lowercase.
    thoigiantu = models.DateTimeField(db_column='ThoiGianTu')  # Field name made lowercase.
    thoigianden = models.DateTimeField(db_column='ThoiGianDen')  # Field name made lowercase.
    id_khachhang = models.CharField(db_column='ID_KhachHang', max_length=36, blank=True, null=True)  # Field name made lowercase.
    id_nhanvien = models.CharField(db_column='ID_NhanVien', max_length=36, blank=True, null=True)  # Field name made lowercase.
    ghichu = models.TextField(db_column='GhiChu', blank=True, null=True)  # Field name made lowercase.
    usertao = models.CharField(db_column='UserTao', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaytao = models.DateTimeField(db_column='NgayTao', blank=True, null=True)  # Field name made lowercase.
    usersuacuoi = models.CharField(db_column='UserSuaCuoi', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaysuacuoi = models.DateTimeField(db_column='NgaySuaCuoi', blank=True, null=True)  # Field name made lowercase.
    nhacnho = models.BooleanField(db_column='NhacNho')  # Field name made lowercase.
    nhacnhotruoc = models.FloatField(db_column='NhacNhoTruoc')  # Field name made lowercase.
    nhacngay = models.BooleanField(db_column='NhacNgay')  # Field name made lowercase.
    id_donvi = models.CharField(db_column='ID_DonVi', max_length=36, blank=True, null=True)  # Field name made lowercase.
    trangthai = models.IntegerField(db_column='TrangThai', blank=True, null=True)  # Field name made lowercase.
    id_phanloai = models.CharField(db_column='ID_PhanLoai', max_length=36, blank=True, null=True)  # Field name made lowercase.
    id_vitri = models.CharField(db_column='ID_ViTri', max_length=36, blank=True, null=True)  # Field name made lowercase.
    lydohuy = models.TextField(db_column='LyDoHuy', blank=True, null=True)  # Field name made lowercase.
    id_tuvan = models.CharField(db_column='ID_TuVan', max_length=36, blank=True, null=True)  # Field name made lowercase.
    id_noidungquantam = models.CharField(db_column='ID_NoiDungQuanTam', max_length=36, blank=True, null=True)  # Field name made lowercase.
    id_loailydohuy = models.CharField(db_column='ID_LoaiLyDoHuy', max_length=36, blank=True, null=True)  # Field name made lowercase.
    lydohuylichhen = models.TextField(db_column='LyDoHuyLichHen', blank=True, null=True)  # Field name made lowercase.
    nguonkhach = models.TextField(db_column='NguonKhach', blank=True, null=True)  # Field name made lowercase.
    nhanvienlienquan = models.TextField(db_column='NhanVienLienQuan', blank=True, null=True)  # Field name made lowercase.
    noidungquantam = models.TextField(db_column='NoiDungQuanTam', blank=True, null=True)  # Field name made lowercase.
    theodoi = models.BooleanField(db_column='TheoDoi', blank=True, null=True)  # Field name made lowercase.
    congviec = models.TextField(db_column='CongViec', blank=True, null=True)  # Field name made lowercase.
    diachi = models.TextField(db_column='DiaChi', blank=True, null=True)  # Field name made lowercase.
    dienthoai = models.CharField(db_column='DienThoai', max_length=20, blank=True, null=True)  # Field name made lowercase.
    email = models.TextField(db_column='Email', blank=True, null=True)  # Field name made lowercase.
    id_dichvu = models.CharField(db_column='ID_DichVu', max_length=36, blank=True, null=True)  # Field name made lowercase.
    id_lienhe = models.CharField(db_column='ID_LienHe', max_length=36, blank=True, null=True)  # Field name made lowercase.
    lalichhen = models.BooleanField(db_column='LaLichHen', blank=True, null=True)  # Field name made lowercase.
    loailichhen = models.IntegerField(db_column='LoaiLichHen', blank=True, null=True)  # Field name made lowercase.
    ngaysinh = models.DateTimeField(db_column='NgaySinh', blank=True, null=True)  # Field name made lowercase.
    tenkhachhang = models.TextField(db_column='TenKhachHang', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LichHenKhachHang'


class LichnhacbaohanhXeban(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    apdung = models.BooleanField(db_column='ApDung')  # Field name made lowercase.
    mabaohanh = models.CharField(db_column='MaBaoHanh', max_length=50)  # Field name made lowercase.
    nhomhanghoa = models.CharField(db_column='NhomHangHoa', max_length=36, blank=True, null=True)  # Field name made lowercase.
    userlap = models.CharField(db_column='UserLap', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaylap = models.DateTimeField(db_column='NgayLap', blank=True, null=True)  # Field name made lowercase.
    usersuacuoi = models.CharField(db_column='UserSuaCuoi', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaysuacuoi = models.DateTimeField(db_column='NgaySuaCuoi', blank=True, null=True)  # Field name made lowercase.
    id_hanghoa = models.CharField(db_column='ID_HangHoa', max_length=36, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LichNhacBaoHanh_XeBan'


class LichnhacbaohanhXebanChitiet(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    id_lichnhacbaohanh = models.CharField(db_column='ID_LichNhacBaoHanh', max_length=36)  # Field name made lowercase.
    sothutu = models.IntegerField(db_column='SoThuTu')  # Field name made lowercase.
    thoigian_min = models.FloatField(db_column='ThoiGian_Min')  # Field name made lowercase.
    thoigian_max = models.FloatField(db_column='ThoiGian_Max', blank=True, null=True)  # Field name made lowercase.
    donvithoigian = models.IntegerField(db_column='DonViThoiGian')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LichNhacBaoHanh_XeBan_ChiTiet'


class LichnhacbaohanhXesuachua(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    apdung = models.BooleanField(db_column='ApDung')  # Field name made lowercase.
    mabaohanh = models.CharField(db_column='MaBaoHanh', max_length=50)  # Field name made lowercase.
    id_hangxe = models.CharField(db_column='ID_HangXe', max_length=36, blank=True, null=True)  # Field name made lowercase.
    userlap = models.CharField(db_column='UserLap', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaylap = models.DateTimeField(db_column='NgayLap', blank=True, null=True)  # Field name made lowercase.
    usersuacuoi = models.CharField(db_column='UserSuaCuoi', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaysuacuoi = models.DateTimeField(db_column='NgaySuaCuoi', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LichNhacBaoHanh_XeSuaChua'


class LichnhacbaohanhXesuachuaChitiet(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    id_lichnhacbaohanh = models.CharField(db_column='ID_LichNhacBaoHanh', max_length=36)  # Field name made lowercase.
    sothutu = models.IntegerField(db_column='SoThuTu')  # Field name made lowercase.
    thoigian_min = models.FloatField(db_column='ThoiGian_Min')  # Field name made lowercase.
    thoigian_max = models.FloatField(db_column='ThoiGian_Max', blank=True, null=True)  # Field name made lowercase.
    donvithoigian = models.IntegerField(db_column='DonViThoiGian')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LichNhacBaoHanh_XeSuaChua_ChiTiet'


class Machungtu(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    id_donvi = models.CharField(db_column='ID_DonVi', max_length=36)  # Field name made lowercase.
    loaichungtu = models.CharField(db_column='LoaiChungTu', max_length=50)  # Field name made lowercase.
    tiento = models.CharField(db_column='TienTo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngancach1 = models.CharField(db_column='NganCach1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaythangnam = models.CharField(db_column='NgayThangNam', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngancach2 = models.CharField(db_column='NganCach2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dodaistt = models.IntegerField(db_column='DoDaiSTT')  # Field name made lowercase.
    sudungusername = models.BooleanField(db_column='SuDungUserName', blank=True, null=True)  # Field name made lowercase.
    sudungmadonvi = models.BooleanField(db_column='SuDungMaDonVi', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MaChungTu'


class Mohinhkhuvuc(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    tenmohinh = models.TextField(db_column='TenMoHinh', blank=True, null=True)  # Field name made lowercase.
    x = models.IntegerField(db_column='X')  # Field name made lowercase.
    y = models.IntegerField(db_column='Y')  # Field name made lowercase.
    tylechieucao = models.FloatField(db_column='TyLeChieuCao')  # Field name made lowercase.
    tylechieurong = models.FloatField(db_column='TyLeChieuRong')  # Field name made lowercase.
    lagroup = models.BooleanField(db_column='LaGroup')  # Field name made lowercase.
    id_parent = models.CharField(db_column='ID_Parent', max_length=36, blank=True, null=True)  # Field name made lowercase.
    idkhuvuc = models.CharField(db_column='IDKhuVuc', max_length=36)  # Field name made lowercase.
    id_tag = models.CharField(db_column='ID_Tag', max_length=36, blank=True, null=True)  # Field name made lowercase.
    anh = models.BinaryField(db_column='Anh', blank=True, null=True)  # Field name made lowercase.
    tylex = models.FloatField(db_column='TyLeX')  # Field name made lowercase.
    tyley = models.FloatField(db_column='TyLeY')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MoHinhKhuVuc'


class Monanchothuchien(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    monan = models.CharField(db_column='MonAn', max_length=36)  # Field name made lowercase.
    banan = models.CharField(db_column='BanAn', max_length=36, blank=True, null=True)  # Field name made lowercase.
    soluong = models.IntegerField(db_column='SoLuong')  # Field name made lowercase.
    cthd = models.CharField(db_column='CTHD', max_length=36)  # Field name made lowercase.
    hd = models.CharField(db_column='HD', max_length=36, blank=True, null=True)  # Field name made lowercase.
    thoigian = models.DateTimeField(db_column='ThoiGian', blank=True, null=True)  # Field name made lowercase.
    daxong = models.BooleanField(db_column='DaXong', blank=True, null=True)  # Field name made lowercase.
    danglam = models.BooleanField(db_column='DangLam', blank=True, null=True)  # Field name made lowercase.
    huy = models.BooleanField(db_column='Huy', blank=True, null=True)  # Field name made lowercase.
    ghichu = models.TextField(db_column='GhiChu', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MonAnChoThucHien'


class NsChamcongChitiet(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    id_nhanvien = models.ForeignKey(DmNhanvien, models.DO_NOTHING, db_column='ID_NhanVien')  # Field name made lowercase.
    thang = models.IntegerField(db_column='Thang')  # Field name made lowercase.
    nam = models.IntegerField(db_column='Nam')  # Field name made lowercase.
    ngay1 = models.CharField(db_column='Ngay1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ngay2 = models.CharField(db_column='Ngay2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ngay3 = models.CharField(db_column='Ngay3', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ngay4 = models.CharField(db_column='Ngay4', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ngay5 = models.CharField(db_column='Ngay5', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ngay6 = models.CharField(db_column='Ngay6', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ngay7 = models.CharField(db_column='Ngay7', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ngay8 = models.CharField(db_column='Ngay8', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ngay9 = models.CharField(db_column='Ngay9', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ngay10 = models.CharField(db_column='Ngay10', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ngay11 = models.CharField(db_column='Ngay11', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ngay12 = models.CharField(db_column='Ngay12', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ngay13 = models.CharField(db_column='Ngay13', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ngay14 = models.CharField(db_column='Ngay14', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ngay15 = models.CharField(db_column='Ngay15', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ngay16 = models.CharField(db_column='Ngay16', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ngay17 = models.CharField(db_column='Ngay17', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ngay18 = models.CharField(db_column='Ngay18', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ngay19 = models.CharField(db_column='Ngay19', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ngay20 = models.CharField(db_column='Ngay20', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ngay21 = models.CharField(db_column='Ngay21', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ngay22 = models.CharField(db_column='Ngay22', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ngay23 = models.CharField(db_column='Ngay23', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ngay24 = models.CharField(db_column='Ngay24', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ngay25 = models.CharField(db_column='Ngay25', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ngay26 = models.CharField(db_column='Ngay26', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ngay27 = models.CharField(db_column='Ngay27', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ngay28 = models.CharField(db_column='Ngay28', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ngay29 = models.CharField(db_column='Ngay29', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ngay30 = models.CharField(db_column='Ngay30', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ngay31 = models.CharField(db_column='Ngay31', max_length=100, blank=True, null=True)  # Field name made lowercase.
    songaynghi = models.FloatField(db_column='SoNgayNghi')  # Field name made lowercase.
    tongcong = models.FloatField(db_column='TongCong')  # Field name made lowercase.
    ngaylap = models.DateTimeField(db_column='NgayLap', blank=True, null=True)  # Field name made lowercase.
    usertao = models.CharField(db_column='UserTao', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaytao = models.DateTimeField(db_column='NgayTao', blank=True, null=True)  # Field name made lowercase.
    usersuacuoi = models.CharField(db_column='UserSuaCuoi', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaysuacuoi = models.DateTimeField(db_column='NgaySuaCuoi', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NS_ChamCong_ChiTiet'


class NsHosoluong(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    id_nhanvien = models.CharField(db_column='ID_NhanVien', max_length=36)  # Field name made lowercase.
    ngaybd = models.DateTimeField(db_column='NgayBD')  # Field name made lowercase.
    ngaykt = models.DateTimeField(db_column='NgayKT', blank=True, null=True)  # Field name made lowercase.
    mucluongcb = models.FloatField(db_column='MucLuongCB')  # Field name made lowercase.
    ghichu = models.TextField(db_column='GhiChu', blank=True, null=True)  # Field name made lowercase.
    usertao = models.CharField(db_column='UserTao', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaytao = models.DateTimeField(db_column='NgayTao', blank=True, null=True)  # Field name made lowercase.
    usersuacuoi = models.CharField(db_column='UserSuaCuoi', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaysuacuoi = models.DateTimeField(db_column='NgaySuaCuoi', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NS_HoSoLuong'


class NsHosoluongdoanhthu(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    id_nhanvien = models.CharField(db_column='ID_NhanVien', max_length=36)  # Field name made lowercase.
    ngaybd = models.DateTimeField(db_column='NgayBD')  # Field name made lowercase.
    ngaykt = models.DateTimeField(db_column='NgayKT', blank=True, null=True)  # Field name made lowercase.
    id_luongdoanhthu = models.CharField(db_column='ID_LuongDoanhThu', max_length=36)  # Field name made lowercase.
    ghichu = models.TextField(db_column='GhiChu', blank=True, null=True)  # Field name made lowercase.
    usertao = models.CharField(db_column='UserTao', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaytao = models.DateTimeField(db_column='NgayTao', blank=True, null=True)  # Field name made lowercase.
    usersuacuoi = models.CharField(db_column='UserSuaCuoi', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaysuacuoi = models.DateTimeField(db_column='NgaySuaCuoi', blank=True, null=True)  # Field name made lowercase.
    luongtuvan = models.BooleanField(db_column='LuongTuVan', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NS_HoSoLuongDoanhThu'


class NsKyhieuchamcong(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    makyhieu = models.CharField(db_column='MaKyHieu', max_length=50)  # Field name made lowercase.
    tenkyhieu = models.CharField(db_column='TenKyHieu', max_length=100)  # Field name made lowercase.
    tylehuongluong = models.FloatField(db_column='TyLeHuongLuong')  # Field name made lowercase.
    lacongnghi = models.BooleanField(db_column='LaCongNghi')  # Field name made lowercase.
    usertao = models.CharField(db_column='UserTao', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaytao = models.DateTimeField(db_column='NgayTao', blank=True, null=True)  # Field name made lowercase.
    usersuacuoi = models.CharField(db_column='UserSuaCuoi', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaysuacuoi = models.DateTimeField(db_column='NgaySuaCuoi', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NS_KyHieuChamCong'


class NsLuongdoanhthu(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    ma = models.CharField(db_column='Ma', max_length=50)  # Field name made lowercase.
    ten = models.TextField(db_column='Ten')  # Field name made lowercase.
    ghichu = models.TextField(db_column='GhiChu', blank=True, null=True)  # Field name made lowercase.
    usertao = models.CharField(db_column='UserTao', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaytao = models.DateTimeField(db_column='NgayTao', blank=True, null=True)  # Field name made lowercase.
    usersua = models.CharField(db_column='UserSua', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaysua = models.DateTimeField(db_column='NgaySua', blank=True, null=True)  # Field name made lowercase.
    apdung_hanghoadichvu = models.IntegerField(db_column='ApDung_HangHoaDichVu', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NS_LuongDoanhThu'


class NsLuongdoanhthuChitiet(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    id_luongdoanhthu = models.CharField(db_column='ID_LuongDoanhThu', max_length=36)  # Field name made lowercase.
    doanhthu_min = models.FloatField(db_column='DoanhThu_Min')  # Field name made lowercase.
    doanhthu_max = models.FloatField(db_column='DoanhThu_Max', blank=True, null=True)  # Field name made lowercase.
    luongduocnhan = models.FloatField(db_column='LuongDuocNhan')  # Field name made lowercase.
    theopt = models.BooleanField(db_column='TheoPT')  # Field name made lowercase.
    lathochinh = models.BooleanField(db_column='LaThoChinh')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NS_LuongDoanhThu_ChiTiet'


class NsPhucapnhanvien(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    id_nhanvien = models.CharField(db_column='ID_NhanVien', max_length=36)  # Field name made lowercase.
    id_khoanphucap = models.CharField(db_column='ID_KhoanPhuCap', max_length=36)  # Field name made lowercase.
    phucap = models.FloatField(db_column='PhuCap')  # Field name made lowercase.
    lapt = models.BooleanField(db_column='LaPT')  # Field name made lowercase.
    ngayapdung = models.DateTimeField(db_column='NgayApDung')  # Field name made lowercase.
    ngayketthuc = models.DateTimeField(db_column='NgayKetThuc', blank=True, null=True)  # Field name made lowercase.
    ghichu = models.TextField(db_column='GhiChu', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NS_PhuCapNhanVien'


class NsQuatrinhcongtac(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    id_nhanvien = models.ForeignKey(DmNhanvien, models.DO_NOTHING, db_column='ID_NhanVien')  # Field name made lowercase.
    id_donvi = models.ForeignKey(DmDonvi, models.DO_NOTHING, db_column='ID_DonVi')  # Field name made lowercase.
    id_chucvu = models.ForeignKey(DmChucvu, models.DO_NOTHING, db_column='ID_ChucVu', blank=True, null=True)  # Field name made lowercase.
    ngayapdung = models.DateTimeField(db_column='NgayApDung')  # Field name made lowercase.
    ngayhethan = models.DateTimeField(db_column='NgayHetHan', blank=True, null=True)  # Field name made lowercase.
    lachucvuhienthoi = models.BooleanField(db_column='LaChucVuHienThoi')  # Field name made lowercase.
    ladonvihienthoi = models.BooleanField(db_column='LaDonViHienThoi')  # Field name made lowercase.
    ngaylap = models.DateTimeField(db_column='NgayLap', blank=True, null=True)  # Field name made lowercase.
    userlap = models.CharField(db_column='UserLap', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaysuacuoi = models.DateTimeField(db_column='NgaySuaCuoi', blank=True, null=True)  # Field name made lowercase.
    usersuacuoi = models.CharField(db_column='UserSuaCuoi', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NS_QuaTrinhCongTac'


class Nguonkhachhang(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    tennguonkhach = models.TextField(db_column='TenNguonKhach')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NguonKhachHang'


class NguyenlieuChungtuchitiet(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    id_chungtu = models.CharField(db_column='ID_ChungTu', max_length=36)  # Field name made lowercase.
    id_chungtuchitiet = models.CharField(db_column='ID_ChungTuChiTiet', max_length=36)  # Field name made lowercase.
    loaichungtu = models.IntegerField(db_column='LoaiChungTu')  # Field name made lowercase.
    id_hanghoadichvu = models.CharField(db_column='ID_HangHoaDichVu', max_length=36)  # Field name made lowercase.
    soluong = models.FloatField(db_column='SoLuong')  # Field name made lowercase.
    id_donvitinh = models.CharField(db_column='ID_DonViTinh', max_length=36)  # Field name made lowercase.
    id_kho = models.CharField(db_column='ID_Kho', max_length=36)  # Field name made lowercase.
    id_lohang = models.CharField(db_column='ID_LoHang', max_length=36, blank=True, null=True)  # Field name made lowercase.
    mavach = models.CharField(db_column='MaVach', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ghichu = models.TextField(db_column='GhiChu', blank=True, null=True)  # Field name made lowercase.
    id_khonhap = models.CharField(db_column='ID_KhoNhap', max_length=36, blank=True, null=True)  # Field name made lowercase.
    dongia = models.FloatField(db_column='DonGia', blank=True, null=True)  # Field name made lowercase.
    nguyenlieuchinh = models.BooleanField(db_column='NguyenLieuChinh', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NguyenLieu_ChungTuChiTiet'


class Nhanvienthuchien(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    loaichungtu = models.IntegerField(db_column='LoaiChungTu')  # Field name made lowercase.
    machungtu = models.CharField(db_column='MaChungTu', max_length=36)  # Field name made lowercase.
    nhanvien = models.ForeignKey(DmNhanvien, models.DO_NOTHING, db_column='NhanVien')  # Field name made lowercase.
    id_chitietchungtu = models.CharField(db_column='ID_ChiTietChungTu', max_length=36, blank=True, null=True)  # Field name made lowercase.
    id_congviec = models.ForeignKey(DmHanghoa, models.DO_NOTHING, db_column='ID_CongViec', blank=True, null=True)  # Field name made lowercase.
    tienchietkhau = models.FloatField(db_column='TienChietKhau')  # Field name made lowercase.
    laphantram = models.BooleanField(db_column='LaPhanTram')  # Field name made lowercase.
    lanhanvienchinh = models.BooleanField(db_column='LaNhanVienChinh')  # Field name made lowercase.
    diengiai = models.TextField(db_column='DienGiai', blank=True, null=True)  # Field name made lowercase.
    id_nhanvienchinh = models.CharField(db_column='ID_NhanVienChinh', max_length=36, blank=True, null=True)  # Field name made lowercase.
    chietkhautheothucthu = models.BooleanField(db_column='ChietKhauTheoThucThu', blank=True, null=True)  # Field name made lowercase.
    ptdoanhthuduochuong = models.FloatField(db_column='PTDoanhThuDuocHuong', blank=True, null=True)  # Field name made lowercase.
    duocyeucau = models.BooleanField(db_column='DuocYeuCau', blank=True, null=True)  # Field name made lowercase.
    chiphithuchien = models.FloatField(db_column='ChiPhiThucHien', blank=True, null=True)  # Field name made lowercase.
    laptchiphithuchien = models.BooleanField(db_column='LaPTChiPhiThucHien', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NhanVienThucHien'


class Nhanvientuvan(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    id_nhanvien = models.ForeignKey(DmNhanvien, models.DO_NOTHING, db_column='ID_NhanVien')  # Field name made lowercase.
    loaichungtu = models.IntegerField(db_column='LoaiChungTu')  # Field name made lowercase.
    id_chungtu = models.CharField(db_column='ID_ChungTu', max_length=36)  # Field name made lowercase.
    id_chungtuchitiet = models.CharField(db_column='ID_ChungTuChiTiet', max_length=36, blank=True, null=True)  # Field name made lowercase.
    tienchietkhau = models.FloatField(db_column='TienChietKhau')  # Field name made lowercase.
    laphantram = models.BooleanField(db_column='LaPhanTram')  # Field name made lowercase.
    chietkhautheothucthu = models.BooleanField(db_column='ChietKhauTheoThucThu', blank=True, null=True)  # Field name made lowercase.
    ptdoanhthuduochuong = models.FloatField(db_column='PTDoanhThuDuocHuong', blank=True, null=True)  # Field name made lowercase.
    diengiai = models.TextField(db_column='DienGiai', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NhanVienTuVan'


class NhanvienLichhenkhachhang(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    id_lichhen = models.CharField(db_column='ID_LichHen', max_length=36)  # Field name made lowercase.
    id_nhanvien = models.CharField(db_column='ID_NhanVien', max_length=36)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NhanVien_LichHenKhachHang'


class NhanLichhenkhachhang(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    id_lichhen = models.CharField(db_column='ID_LichHen', max_length=36)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Nhan_LichHenKhachHang'


class NhatkybaohanhNhomhhHanghoa(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    id_hanghoa = models.CharField(db_column='ID_HangHoa', max_length=36)  # Field name made lowercase.
    thoigianbaohanh = models.DateTimeField(db_column='ThoiGianBaoHanh')  # Field name made lowercase.
    id_nhanvienbaohanh = models.CharField(db_column='ID_NhanVienBaoHanh', max_length=36, blank=True, null=True)  # Field name made lowercase.
    ghichu = models.TextField(db_column='GhiChu', blank=True, null=True)  # Field name made lowercase.
    id_donvi = models.CharField(db_column='ID_DonVi', max_length=36)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NhatKyBaoHanh_NhomHH_HangHoa'


class NhatkyhoatdongNhomhanghoa(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    sophieu = models.CharField(db_column='SoPhieu', max_length=150)  # Field name made lowercase.
    ngaylapphieu = models.DateTimeField(db_column='NgayLapPhieu')  # Field name made lowercase.
    id_donvi = models.CharField(db_column='ID_DonVi', max_length=36)  # Field name made lowercase.
    id_nhomhang = models.CharField(db_column='ID_NhomHang', max_length=36)  # Field name made lowercase.
    id_nhanvien = models.CharField(db_column='ID_NhanVien', max_length=36, blank=True, null=True)  # Field name made lowercase.
    sogiohoatdong = models.FloatField(db_column='SoGioHoatDong')  # Field name made lowercase.
    ghichu = models.TextField(db_column='GhiChu', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NhatKyHoatDong_NhomHangHoa'


class Nhatkysudungthe(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    id_thekhachhang = models.ForeignKey('Thekhachhang', models.DO_NOTHING, db_column='ID_TheKhachHang')  # Field name made lowercase.
    loaichungtu = models.IntegerField(db_column='LoaiChungTu')  # Field name made lowercase.
    id_chungtu = models.CharField(db_column='ID_ChungTu', max_length=36)  # Field name made lowercase.
    id_chitietchungtu = models.CharField(db_column='ID_ChiTietChungTu', max_length=36)  # Field name made lowercase.
    soluong = models.FloatField(db_column='SoLuong', blank=True, null=True)  # Field name made lowercase.
    sotien = models.FloatField(db_column='SoTien', blank=True, null=True)  # Field name made lowercase.
    id_nhanvien = models.CharField(db_column='ID_NhanVien', max_length=36, blank=True, null=True)  # Field name made lowercase.
    ngay = models.DateTimeField(db_column='Ngay', blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lasoluongduoctang = models.BooleanField(db_column='LaSoLuongDuocTang', blank=True, null=True)  # Field name made lowercase.
    id_hanghoadichvu = models.CharField(db_column='ID_HangHoaDichVu', max_length=36, blank=True, null=True)  # Field name made lowercase.
    tonluyke = models.FloatField(db_column='TonLuyKe', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NhatKySuDungThe'


class NhatkysudungPhieuthanhtoan(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    id_phieuthanhtoan = models.CharField(db_column='ID_PhieuThanhToan', max_length=36)  # Field name made lowercase.
    loaichungtu = models.IntegerField(db_column='LoaiChungTu')  # Field name made lowercase.
    id_chungtu = models.CharField(db_column='ID_ChungTu', max_length=36)  # Field name made lowercase.
    sotienthanhtoan = models.FloatField(db_column='SoTienThanhToan')  # Field name made lowercase.
    ngaysudung = models.DateTimeField(db_column='NgaySuDung')  # Field name made lowercase.
    id_nhanvien = models.CharField(db_column='ID_NhanVien', max_length=36, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NhatKySuDung_PhieuThanhToan'


class Nhatkythaydoinhomkhachhang(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    id_khachhang = models.CharField(db_column='ID_KhachHang', max_length=36)  # Field name made lowercase.
    ngaythaydoinhom = models.DateTimeField(db_column='NgayThayDoiNhom')  # Field name made lowercase.
    id_nhomcu = models.CharField(db_column='ID_NhomCu', max_length=36, blank=True, null=True)  # Field name made lowercase.
    id_nhommoi = models.CharField(db_column='ID_NhomMoi', max_length=36)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NhatKyThayDoiNhomKhachHang'


class NhomdoituongDonvi(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    id_nhomdoituong = models.CharField(db_column='ID_NhomDoiTuong', max_length=36)  # Field name made lowercase.
    id_donvi = models.CharField(db_column='ID_DonVi', max_length=36)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NhomDoiTuong_DonVi'


class NhomhanghoaDonvi(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    id_nhomhanghoa = models.CharField(db_column='ID_NhomHangHoa', max_length=36)  # Field name made lowercase.
    id_donvi = models.CharField(db_column='ID_DonVi', max_length=36)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NhomHangHoa_DonVi'


class Phanhoikhachhang(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    id_khachhang = models.CharField(db_column='ID_KhachHang', max_length=36)  # Field name made lowercase.
    ngaylienhe = models.DateTimeField(db_column='NgayLienHe', blank=True, null=True)  # Field name made lowercase.
    id_lienhe = models.CharField(db_column='ID_LienHe', max_length=36, blank=True, null=True)  # Field name made lowercase.
    id_xe = models.CharField(db_column='ID_Xe', max_length=36, blank=True, null=True)  # Field name made lowercase.
    id_nhanviennhan = models.CharField(db_column='ID_NhanVienNhan', max_length=36, blank=True, null=True)  # Field name made lowercase.
    id_nhanvientraloi = models.CharField(db_column='ID_NhanVienTraLoi', max_length=36, blank=True, null=True)  # Field name made lowercase.
    id_phanloai = models.CharField(db_column='ID_PhanLoai', max_length=36, blank=True, null=True)  # Field name made lowercase.
    tieude = models.TextField(db_column='TieuDe')  # Field name made lowercase.
    noidung = models.TextField(db_column='NoiDung')  # Field name made lowercase.
    noidungtraloi = models.TextField(db_column='NoiDungTraLoi', blank=True, null=True)  # Field name made lowercase.
    userlap = models.CharField(db_column='UserLap', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaylap = models.DateTimeField(db_column='NgayLap', blank=True, null=True)  # Field name made lowercase.
    usersua = models.CharField(db_column='UserSua', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaysua = models.DateTimeField(db_column='NgaySua', blank=True, null=True)  # Field name made lowercase.
    id_donvis = models.TextField(db_column='ID_DonVis', blank=True, null=True)  # Field name made lowercase.
    id_nhanviens = models.TextField(db_column='ID_NhanViens', blank=True, null=True)  # Field name made lowercase.
    ketqua = models.TextField(db_column='KetQua', blank=True, null=True)  # Field name made lowercase.
    mucdodanhgia = models.IntegerField(db_column='MucDoDanhGia', blank=True, null=True)  # Field name made lowercase.
    mucdophanhoi = models.IntegerField(db_column='MucDoPhanHoi', blank=True, null=True)  # Field name made lowercase.
    id_dichvu = models.CharField(db_column='ID_DichVu', max_length=36, blank=True, null=True)  # Field name made lowercase.
    trangthai = models.IntegerField(db_column='TrangThai', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PhanHoiKhachHang'


class Phanloaichamsockhachhang(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    maphanloai = models.CharField(db_column='MaPhanLoai', max_length=50)  # Field name made lowercase.
    tenphanloai = models.TextField(db_column='TenPhanLoai')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PhanLoaiChamSocKhachHang'


class Phanloailichhen(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    maloailichhen = models.CharField(db_column='MaLoaiLichHen', max_length=50)  # Field name made lowercase.
    tenloailichhen = models.TextField(db_column='TenLoaiLichHen')  # Field name made lowercase.
    ghichu = models.TextField(db_column='GhiChu', blank=True, null=True)  # Field name made lowercase.
    sudung = models.BooleanField(db_column='SuDung')  # Field name made lowercase.
    usertao = models.CharField(db_column='UserTao', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaytao = models.DateTimeField(db_column='NgayTao', blank=True, null=True)  # Field name made lowercase.
    usersuacuoi = models.CharField(db_column='UserSuaCuoi', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaysuacuoi = models.DateTimeField(db_column='NgaySuaCuoi', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PhanLoaiLichHen'


class Phieuchi(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    maphieuchi = models.CharField(db_column='MaPhieuChi', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaylapphieu = models.DateTimeField(db_column='NgayLapPhieu')  # Field name made lowercase.
    ngayvaoso = models.DateTimeField(db_column='NgayVaoSo', blank=True, null=True)  # Field name made lowercase.
    id_nhanvien = models.ForeignKey(DmNhanvien, models.DO_NOTHING, db_column='ID_NhanVien', blank=True, null=True)  # Field name made lowercase.
    id_ngoaite = models.ForeignKey(DmTiente, models.DO_NOTHING, db_column='ID_NgoaiTe', blank=True, null=True)  # Field name made lowercase.
    tygia = models.FloatField(db_column='TyGia')  # Field name made lowercase.
    nguoinhan = models.CharField(db_column='NguoiNhan', max_length=250, blank=True, null=True)  # Field name made lowercase.
    noidungchi = models.TextField(db_column='NoiDungChi', blank=True, null=True)  # Field name made lowercase.
    tongtienchi = models.FloatField(db_column='TongTienChi')  # Field name made lowercase.
    chichonhieudoituong = models.BooleanField(db_column='ChiChoNhieuDoiTuong')  # Field name made lowercase.
    id_donvi = models.ForeignKey(DmDonvi, models.DO_NOTHING, db_column='ID_DonVi', blank=True, null=True)  # Field name made lowercase.
    userlap = models.CharField(db_column='UserLap', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaysuacuoi = models.DateTimeField(db_column='NgaySuaCuoi', blank=True, null=True)  # Field name made lowercase.
    usersuacuoi = models.CharField(db_column='UserSuaCuoi', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PhieuChi'


class Phieuchichitiet(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    id_phieuchi = models.ForeignKey(Phieuchi, models.DO_NOTHING, db_column='ID_PhieuChi')  # Field name made lowercase.
    id_khoanthuchi = models.ForeignKey(Khoanthuchi, models.DO_NOTHING, db_column='ID_KhoanThuChi', blank=True, null=True)  # Field name made lowercase.
    id_doituong = models.ForeignKey(DmDoituong, models.DO_NOTHING, db_column='ID_DoiTuong', blank=True, null=True)  # Field name made lowercase.
    ghichu = models.TextField(db_column='GhiChu', blank=True, null=True)  # Field name made lowercase.
    tienchi = models.FloatField(db_column='TienChi')  # Field name made lowercase.
    loaict = models.IntegerField(db_column='LoaiCT', blank=True, null=True)  # Field name made lowercase.
    id_chungtu = models.CharField(db_column='ID_ChungTu', max_length=36, blank=True, null=True)  # Field name made lowercase.
    tiengui = models.FloatField(db_column='TienGui')  # Field name made lowercase.
    tienmat = models.FloatField(db_column='TienMat')  # Field name made lowercase.
    diachi_doituong = models.TextField(db_column='DiaChi_DoiTuong', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PhieuChiChiTiet'


class Phieuthanhtoan(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    mathe = models.CharField(db_column='MaThe', max_length=50)  # Field name made lowercase.
    tenthe = models.TextField(db_column='TenThe', blank=True, null=True)  # Field name made lowercase.
    ngaysudung = models.DateTimeField(db_column='NgaySuDung')  # Field name made lowercase.
    ngayhethan = models.DateTimeField(db_column='NgayHetHan', blank=True, null=True)  # Field name made lowercase.
    menhgia = models.FloatField(db_column='MenhGia')  # Field name made lowercase.
    id_tiente = models.CharField(db_column='ID_TienTe', max_length=36)  # Field name made lowercase.
    ghichu = models.TextField(db_column='GhiChu', blank=True, null=True)  # Field name made lowercase.
    id_loaiphieu = models.CharField(db_column='ID_LoaiPhieu', max_length=36, blank=True, null=True)  # Field name made lowercase.
    solansudung = models.FloatField(db_column='SoLanSuDung', blank=True, null=True)  # Field name made lowercase.
    id_khachhang = models.CharField(db_column='ID_KhachHang', max_length=36, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PhieuThanhToan'


class Phieuthu(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    maphieuthu = models.CharField(db_column='MaPhieuThu', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaylapphieu = models.DateTimeField(db_column='NgayLapPhieu')  # Field name made lowercase.
    ngayvaoso = models.DateTimeField(db_column='NgayVaoSo', blank=True, null=True)  # Field name made lowercase.
    id_nhanvien = models.ForeignKey(DmNhanvien, models.DO_NOTHING, db_column='ID_NhanVien', blank=True, null=True)  # Field name made lowercase.
    id_ngoaite = models.ForeignKey(DmTiente, models.DO_NOTHING, db_column='ID_NgoaiTe', blank=True, null=True)  # Field name made lowercase.
    tygia = models.FloatField(db_column='TyGia')  # Field name made lowercase.
    nguoinoptien = models.CharField(db_column='NguoiNopTien', max_length=250, blank=True, null=True)  # Field name made lowercase.
    noidungthu = models.CharField(db_column='NoiDungThu', max_length=500, blank=True, null=True)  # Field name made lowercase.
    tongtienthu = models.FloatField(db_column='TongTienThu')  # Field name made lowercase.
    thucuanhieudoituong = models.BooleanField(db_column='ThuCuaNhieuDoiTuong')  # Field name made lowercase.
    userlap = models.CharField(db_column='UserLap', max_length=50, blank=True, null=True)  # Field name made lowercase.
    id_donvi = models.ForeignKey(DmDonvi, models.DO_NOTHING, db_column='ID_DonVi', blank=True, null=True)  # Field name made lowercase.
    ngaysuacuoi = models.DateTimeField(db_column='NgaySuaCuoi', blank=True, null=True)  # Field name made lowercase.
    usersuacuoi = models.CharField(db_column='UserSuaCuoi', max_length=50, blank=True, null=True)  # Field name made lowercase.
    id_doituong = models.ForeignKey(DmDoituong, models.DO_NOTHING, db_column='ID_DoiTuong', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PhieuThu'


class Phieuthuchitiet(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    id_phieuthu = models.ForeignKey(Phieuthu, models.DO_NOTHING, db_column='ID_PhieuThu')  # Field name made lowercase.
    id_khoanthu = models.ForeignKey(Khoanthuchi, models.DO_NOTHING, db_column='ID_KhoanThu')  # Field name made lowercase.
    id_khachhang = models.ForeignKey(DmDoituong, models.DO_NOTHING, db_column='ID_KhachHang', blank=True, null=True)  # Field name made lowercase.
    id_thethoanhtoan = models.CharField(db_column='ID_TheThoanhToan', max_length=36, blank=True, null=True)  # Field name made lowercase.
    thututhe = models.FloatField(db_column='ThuTuThe')  # Field name made lowercase.
    tienmat = models.FloatField(db_column='TienMat')  # Field name made lowercase.
    tiengui = models.FloatField(db_column='TienGui')  # Field name made lowercase.
    tienthu = models.FloatField(db_column='TienThu')  # Field name made lowercase.
    ghichu = models.TextField(db_column='GhiChu', blank=True, null=True)  # Field name made lowercase.
    id_chungtu = models.CharField(db_column='ID_ChungTu', max_length=36, blank=True, null=True)  # Field name made lowercase.
    loaict = models.IntegerField(db_column='LoaiCT', blank=True, null=True)  # Field name made lowercase.
    chiphinganhang = models.FloatField(db_column='ChiPhiNganHang', blank=True, null=True)  # Field name made lowercase.
    id_nganhang = models.CharField(db_column='ID_NganHang', max_length=36, blank=True, null=True)  # Field name made lowercase.
    laptchiphinganhang = models.BooleanField(db_column='LaPTChiPhiNganHang', blank=True, null=True)  # Field name made lowercase.
    diachi_khachhang = models.TextField(db_column='DiaChi_KhachHang', blank=True, null=True)  # Field name made lowercase.
    thuphitiengui = models.BooleanField(db_column='ThuPhiTienGui', blank=True, null=True)  # Field name made lowercase.
    id_nhanvien = models.ForeignKey(DmNhanvien, models.DO_NOTHING, db_column='ID_NhanVien', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PhieuThuChiTiet'


class Quyenmacdinh(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    userid = models.ForeignKey('SysNguoidung', models.DO_NOTHING, db_column='UserID')  # Field name made lowercase.
    nhapgiaban = models.BooleanField(db_column='NhapGiaBan', blank=True, null=True)  # Field name made lowercase.
    nhapchietkhau = models.BooleanField(db_column='NhapChietKhau', blank=True, null=True)  # Field name made lowercase.
    iddoituong_hdb = models.CharField(db_column='IDDoiTuong_HDB', max_length=36, blank=True, null=True)  # Field name made lowercase.
    idkho_hdb = models.CharField(db_column='IDKho_HDB', max_length=36, blank=True, null=True)  # Field name made lowercase.
    iddoituong_hdbl = models.CharField(db_column='IDDoiTuong_HDBL', max_length=36, blank=True, null=True)  # Field name made lowercase.
    idkho_hdbl = models.CharField(db_column='IDKho_HDBL', max_length=36, blank=True, null=True)  # Field name made lowercase.
    idkho_nhapkho = models.CharField(db_column='IDKho_NhapKho', max_length=36, blank=True, null=True)  # Field name made lowercase.
    iddoituong_nhapkho = models.CharField(db_column='IDDoiTuong_NhapKho', max_length=36, blank=True, null=True)  # Field name made lowercase.
    idkho_xuatkho = models.CharField(db_column='IDKho_XuatKho', max_length=36, blank=True, null=True)  # Field name made lowercase.
    iddoituong_xuatkho = models.CharField(db_column='IDDoiTuong_XuatKho', max_length=36, blank=True, null=True)  # Field name made lowercase.
    iddoituong_muahang = models.CharField(db_column='IDDoiTuong_MuaHang', max_length=36, blank=True, null=True)  # Field name made lowercase.
    idkho_muahang = models.CharField(db_column='IDKho_MuaHang', max_length=36, blank=True, null=True)  # Field name made lowercase.
    iddoituong_hbtl = models.CharField(db_column='IDDoiTuong_HBTL', max_length=36, blank=True, null=True)  # Field name made lowercase.
    idkho_hbtl = models.CharField(db_column='IDKho_HBTL', max_length=36, blank=True, null=True)  # Field name made lowercase.
    iddoituong_tralaincc = models.CharField(db_column='IDDoiTuong_TraLaiNCC', max_length=36, blank=True, null=True)  # Field name made lowercase.
    idkho_tralaincc = models.CharField(db_column='IDKho_TraLaiNCC', max_length=36, blank=True, null=True)  # Field name made lowercase.
    iddoituong_phieuthu = models.CharField(db_column='IDDoiTuong_PhieuThu', max_length=36, blank=True, null=True)  # Field name made lowercase.
    iddoituong_phieuchi = models.CharField(db_column='IDDoiTuong_PhieuChi', max_length=36, blank=True, null=True)  # Field name made lowercase.
    idkho_dieuchuyen = models.CharField(db_column='IDKho_DieuChuyen', max_length=36, blank=True, null=True)  # Field name made lowercase.
    suangaychungtu = models.BooleanField(db_column='SuaNgayChungTu', blank=True, null=True)  # Field name made lowercase.
    suasochungtu = models.BooleanField(db_column='SuaSoChungTu', blank=True, null=True)  # Field name made lowercase.
    thaydoinhanvien = models.BooleanField(db_column='ThayDoiNhanVien', blank=True, null=True)  # Field name made lowercase.
    id_nhomdichvu = models.CharField(db_column='ID_NhomDichVu', max_length=36, blank=True, null=True)  # Field name made lowercase.
    id_nhomdoituong = models.CharField(db_column='ID_NhomDoiTuong', max_length=36, blank=True, null=True)  # Field name made lowercase.
    id_nhomhanghoa = models.CharField(db_column='ID_NhomHangHoa', max_length=36, blank=True, null=True)  # Field name made lowercase.
    nhapchietkhauchung = models.BooleanField(db_column='NhapChietKhauChung', blank=True, null=True)  # Field name made lowercase.
    nhapgiamgia = models.BooleanField(db_column='NhapGiamGia', blank=True, null=True)  # Field name made lowercase.
    iddoituong_baogia = models.CharField(db_column='IDDoiTuong_BaoGia', max_length=36, blank=True, null=True)  # Field name made lowercase.
    iddoituong_dondatmua = models.CharField(db_column='IDDoiTuong_DonDatMua', max_length=36, blank=True, null=True)  # Field name made lowercase.
    idkho_baogia = models.CharField(db_column='IDKho_BaoGia', max_length=36, blank=True, null=True)  # Field name made lowercase.
    idkho_dondatmua = models.CharField(db_column='IDKho_DonDatMua', max_length=36, blank=True, null=True)  # Field name made lowercase.
    nhapchietkhaunvth = models.BooleanField(db_column='NhapChietKhauNVTH', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'QuyenMacDinh'


class Sanphamchinh(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    id_tangkem = models.CharField(db_column='ID_TangKem', max_length=36)  # Field name made lowercase.
    id_hanghoa = models.CharField(db_column='ID_HangHoa', max_length=36)  # Field name made lowercase.
    soluong = models.FloatField(db_column='SoLuong')  # Field name made lowercase.
    id_donvitinh = models.CharField(db_column='ID_DonViTinh', max_length=36)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SanPhamChinh'


class Sanphamtangkem(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    id_tangkem = models.CharField(db_column='ID_TangKem', max_length=36)  # Field name made lowercase.
    id_hanghoa = models.CharField(db_column='ID_HangHoa', max_length=36)  # Field name made lowercase.
    soluong = models.FloatField(db_column='SoLuong')  # Field name made lowercase.
    id_donvitinh = models.CharField(db_column='ID_DonViTinh', max_length=36)  # Field name made lowercase.
    ghichu = models.TextField(db_column='GhiChu', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SanPhamTangKem'


class Sodukhoitao(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    ngaynhap = models.DateTimeField(db_column='NgayNhap')  # Field name made lowercase.
    namhachtoan = models.IntegerField(db_column='NamHachToan')  # Field name made lowercase.
    soduno = models.FloatField(db_column='SoDuNo')  # Field name made lowercase.
    soduco = models.FloatField(db_column='SoDuCo')  # Field name made lowercase.
    id_tiente = models.CharField(db_column='ID_TienTe', max_length=36, blank=True, null=True)  # Field name made lowercase.
    tygia = models.FloatField(db_column='TyGia')  # Field name made lowercase.
    usertao = models.CharField(db_column='UserTao', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaytao = models.DateTimeField(db_column='NgayTao', blank=True, null=True)  # Field name made lowercase.
    usersuacuoi = models.CharField(db_column='UserSuaCuoi', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaysuacuoi = models.DateTimeField(db_column='NgaySuaCuoi', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SoDuKhoiTao'


class Sotichdiem(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    id_khachhang = models.CharField(db_column='ID_KhachHang', max_length=36)  # Field name made lowercase.
    loaichungtu = models.IntegerField(db_column='LoaiChungTu', blank=True, null=True)  # Field name made lowercase.
    id_chungtu = models.CharField(db_column='ID_ChungTu', max_length=36, blank=True, null=True)  # Field name made lowercase.
    id_phieuthu = models.CharField(db_column='ID_PhieuThu', max_length=36)  # Field name made lowercase.
    id_phieuthuchitiet = models.CharField(db_column='ID_PhieuThuChiTiet', max_length=36)  # Field name made lowercase.
    ngayphieuthu = models.DateTimeField(db_column='NgayPhieuThu')  # Field name made lowercase.
    sotienphieuthu = models.FloatField(db_column='SoTienPhieuThu')  # Field name made lowercase.
    sodiemtuongung = models.FloatField(db_column='SoDiemTuongUng', blank=True, null=True)  # Field name made lowercase.
    sotienquydoi = models.FloatField(db_column='SoTienQuyDoi')  # Field name made lowercase.
    id_tichdiem = models.CharField(db_column='ID_TichDiem', max_length=36, blank=True, null=True)  # Field name made lowercase.
    usertao = models.CharField(db_column='UserTao', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaytao = models.DateTimeField(db_column='NgayTao', blank=True, null=True)  # Field name made lowercase.
    usersuacuoi = models.CharField(db_column='UserSuaCuoi', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaysuacuoi = models.DateTimeField(db_column='NgaySuaCuoi', blank=True, null=True)  # Field name made lowercase.
    languoigioithieu = models.BooleanField(db_column='LaNguoiGioiThieu', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SoTichDiem'


class Sudungdiemtich(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    loaichungtu = models.IntegerField(db_column='LoaiChungTu', blank=True, null=True)  # Field name made lowercase.
    id_chungtu = models.CharField(db_column='ID_ChungTu', max_length=36)  # Field name made lowercase.
    ngaychungtu = models.DateTimeField(db_column='NgayChungTu')  # Field name made lowercase.
    id_khachhang = models.CharField(db_column='ID_KhachHang', max_length=36)  # Field name made lowercase.
    sotiensudung = models.FloatField(db_column='SoTienSuDung')  # Field name made lowercase.
    sodiemsudung = models.FloatField(db_column='SoDiemSuDung')  # Field name made lowercase.
    usertao = models.CharField(db_column='UserTao', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaytao = models.DateTimeField(db_column='NgayTao', blank=True, null=True)  # Field name made lowercase.
    usersuacuoi = models.CharField(db_column='UserSuaCuoi', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaysuacuoi = models.DateTimeField(db_column='NgaySuaCuoi', blank=True, null=True)  # Field name made lowercase.
    id_nhanvien = models.CharField(db_column='ID_NhanVien', max_length=36, blank=True, null=True)  # Field name made lowercase.
    id_phieuthu = models.CharField(db_column='ID_PhieuThu', max_length=36, blank=True, null=True)  # Field name made lowercase.
    id_phieuthuchitiet = models.CharField(db_column='ID_PhieuThuChiTiet', max_length=36, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SuDungDiemTich'


class Taikhoannhantin(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    id_nguoidung = models.ForeignKey('SysNguoidung', models.DO_NOTHING, db_column='ID_NguoiDung')  # Field name made lowercase.
    sotiennap = models.FloatField(db_column='SoTienNap')  # Field name made lowercase.
    ngaynap = models.DateTimeField(db_column='NgayNap')  # Field name made lowercase.
    nguoinap = models.TextField(db_column='NguoiNap')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TaiKhoanNhanTin'


class Tailieu(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    id_doituong = models.CharField(db_column='ID_DoiTuong', max_length=36, blank=True, null=True)  # Field name made lowercase.
    tieude = models.TextField(db_column='TieuDe', blank=True, null=True)  # Field name made lowercase.
    id_phanloai = models.CharField(db_column='ID_PhanLoai', max_length=36)  # Field name made lowercase.
    tailieuden = models.BooleanField(db_column='TaiLieuDen')  # Field name made lowercase.
    mota = models.TextField(db_column='MoTa', blank=True, null=True)  # Field name made lowercase.
    filepath = models.TextField(db_column='FilePath')  # Field name made lowercase.
    nguoitao = models.CharField(db_column='NguoiTao', max_length=50)  # Field name made lowercase.
    ngaytao = models.DateTimeField(db_column='NgayTao')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TaiLieu'


class TailieuPhanloai(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    tenphanloai = models.TextField(db_column='TenPhanLoai', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TaiLieu_PhanLoai'


class Tanggiatrithe(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    id_thekh = models.CharField(db_column='ID_TheKH', max_length=36)  # Field name made lowercase.
    ngaytanggt = models.DateTimeField(db_column='NgayTangGT')  # Field name made lowercase.
    id_donvi = models.CharField(db_column='ID_DonVi', max_length=36, blank=True, null=True)  # Field name made lowercase.
    id_khachhang = models.CharField(db_column='ID_KhachHang', max_length=36)  # Field name made lowercase.
    id_nvlap = models.CharField(db_column='ID_NVLap', max_length=36, blank=True, null=True)  # Field name made lowercase.
    matanggt = models.CharField(db_column='MaTangGT', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dongia = models.FloatField(db_column='DonGia')  # Field name made lowercase.
    pttangthem = models.FloatField(db_column='PTTangThem', blank=True, null=True)  # Field name made lowercase.
    tientangthem = models.FloatField(db_column='TienTangThem', blank=True, null=True)  # Field name made lowercase.
    lapt = models.BooleanField(db_column='LaPT')  # Field name made lowercase.
    chietkhau = models.FloatField(db_column='ChietKhau')  # Field name made lowercase.
    phaithanhtoan = models.FloatField(db_column='PhaiThanhToan')  # Field name made lowercase.
    id_tiente = models.CharField(db_column='ID_TienTe', max_length=36, blank=True, null=True)  # Field name made lowercase.
    tygia = models.FloatField(db_column='TyGia', blank=True, null=True)  # Field name made lowercase.
    ghichu = models.TextField(db_column='GhiChu', blank=True, null=True)  # Field name made lowercase.
    usertao = models.CharField(db_column='UserTao', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaytao = models.DateTimeField(db_column='NgayTao', blank=True, null=True)  # Field name made lowercase.
    usersua = models.CharField(db_column='UserSua', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaysua = models.DateTimeField(db_column='NgaySua', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TangGiaTriThe'


class Thekhachhang(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    mathe = models.CharField(db_column='MaThe', max_length=50)  # Field name made lowercase.
    id_nhomthe = models.ForeignKey(DmNhomthe, models.DO_NOTHING, db_column='ID_NhomThe')  # Field name made lowercase.
    ngaymua = models.DateTimeField(db_column='NgayMua')  # Field name made lowercase.
    ngayapdung = models.DateTimeField(db_column='NgayApDung')  # Field name made lowercase.
    ngayhethan = models.DateTimeField(db_column='NgayHetHan', blank=True, null=True)  # Field name made lowercase.
    id_khachhang = models.ForeignKey(DmDoituong, models.DO_NOTHING, db_column='ID_KhachHang')  # Field name made lowercase.
    menhgiathe = models.FloatField(db_column='MenhGiaThe')  # Field name made lowercase.
    ptchietkhau = models.FloatField(db_column='PTChietKhau', blank=True, null=True)  # Field name made lowercase.
    tienchietkhau = models.FloatField(db_column='TienChietKhau', blank=True, null=True)  # Field name made lowercase.
    phaithanhtoan = models.FloatField(db_column='PhaiThanhToan')  # Field name made lowercase.
    id_tiente = models.ForeignKey(DmTiente, models.DO_NOTHING, db_column='ID_TienTe', blank=True, null=True)  # Field name made lowercase.
    tygia = models.FloatField(db_column='TyGia', blank=True, null=True)  # Field name made lowercase.
    id_nhanvienlap = models.CharField(db_column='ID_NhanVienLap', max_length=36, blank=True, null=True)  # Field name made lowercase.
    apdungtatcasanpham = models.BooleanField(db_column='ApDungTatCaSanPham')  # Field name made lowercase.
    duocchomuon = models.BooleanField(db_column='DuocChoMuon')  # Field name made lowercase.
    thegiatri_solan_giamgia = models.IntegerField(db_column='TheGiaTri_SoLan_GiamGia')  # Field name made lowercase.
    usertao = models.CharField(db_column='UserTao', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngayvaoso = models.DateTimeField(db_column='NgayVaoSo', blank=True, null=True)  # Field name made lowercase.
    usersuacuoi = models.CharField(db_column='UserSuaCuoi', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaysuacuoi = models.DateTimeField(db_column='NgaySuaCuoi', blank=True, null=True)  # Field name made lowercase.
    ghichu = models.TextField(db_column='GhiChu', blank=True, null=True)  # Field name made lowercase.
    id_donvi = models.CharField(db_column='ID_DonVi', max_length=36, blank=True, null=True)  # Field name made lowercase.
    pttangthem = models.FloatField(db_column='PTTangThem', blank=True, null=True)  # Field name made lowercase.
    tientangthem = models.FloatField(db_column='TienTangThem', blank=True, null=True)  # Field name made lowercase.
    id_lienhe = models.CharField(db_column='ID_LienHe', max_length=36, blank=True, null=True)  # Field name made lowercase.
    huythe = models.BooleanField(db_column='HuyThe', blank=True, null=True)  # Field name made lowercase.
    ngayhuy = models.DateTimeField(db_column='NgayHuy', blank=True, null=True)  # Field name made lowercase.
    solanduocsudung = models.IntegerField(db_column='SoLanDuocSuDung', blank=True, null=True)  # Field name made lowercase.
    id_dacdiemkhachhang = models.CharField(db_column='ID_DacDiemKhachHang', max_length=36, blank=True, null=True)  # Field name made lowercase.
    manhanvientuvan = models.CharField(db_column='MaNhanVienTuVan', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tennhanvientuvan = models.TextField(db_column='TenNhanVienTuVan', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TheKhachHang'


class Thekhachhangchitiet(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    id_thekhachhang = models.ForeignKey(Thekhachhang, models.DO_NOTHING, db_column='ID_TheKhachHang')  # Field name made lowercase.
    id_hanghoa = models.CharField(db_column='ID_HangHoa', max_length=36)  # Field name made lowercase.
    soluong = models.FloatField(db_column='SoLuong', blank=True, null=True)  # Field name made lowercase.
    dongia = models.FloatField(db_column='DonGia', blank=True, null=True)  # Field name made lowercase.
    ptchietkhau = models.FloatField(db_column='PTChietKhau', blank=True, null=True)  # Field name made lowercase.
    tienchietkhau = models.FloatField(db_column='TienChietKhau', blank=True, null=True)  # Field name made lowercase.
    thanhtoan = models.FloatField(db_column='ThanhToan', blank=True, null=True)  # Field name made lowercase.
    id_lophoc = models.CharField(db_column='ID_LopHoc', max_length=36, blank=True, null=True)  # Field name made lowercase.
    ghichu = models.TextField(db_column='GhiChu', blank=True, null=True)  # Field name made lowercase.
    soluongtang = models.FloatField(db_column='SoLuongTang', blank=True, null=True)  # Field name made lowercase.
    ngaytralai = models.DateTimeField(db_column='NgayTraLai', blank=True, null=True)  # Field name made lowercase.
    soluongtralai = models.FloatField(db_column='SoLuongTraLai', blank=True, null=True)  # Field name made lowercase.
    tiendasudung = models.FloatField(db_column='TienDaSuDung', blank=True, null=True)  # Field name made lowercase.
    tralaihhdv = models.BooleanField(db_column='TraLaiHHDV', blank=True, null=True)  # Field name made lowercase.
    id_sanphamchinh = models.CharField(db_column='ID_SanPhamChinh', max_length=36, blank=True, null=True)  # Field name made lowercase.
    latangkem = models.BooleanField(db_column='LaTangKem', blank=True, null=True)  # Field name made lowercase.
    soluongdasudung = models.FloatField(db_column='SoLuongDaSuDung', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TheKhachHangChiTiet'


class ThekhachhangDonvisudung(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    id_thekhachhang = models.CharField(db_column='ID_TheKhachHang', max_length=36)  # Field name made lowercase.
    id_donvisudung = models.CharField(db_column='ID_DonViSuDung', max_length=36)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TheKhachHang_DonViSuDung'


class Theodoilophoc(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    sophieu = models.CharField(db_column='SoPhieu', max_length=50)  # Field name made lowercase.
    ngaytap = models.DateTimeField(db_column='NgayTap')  # Field name made lowercase.
    id_khachhang = models.CharField(db_column='ID_KhachHang', max_length=36)  # Field name made lowercase.
    id_thekh = models.CharField(db_column='ID_TheKH', max_length=36, blank=True, null=True)  # Field name made lowercase.
    id_lophoc = models.CharField(db_column='ID_LopHoc', max_length=36, blank=True, null=True)  # Field name made lowercase.
    giovao = models.DateTimeField(db_column='GioVao', blank=True, null=True)  # Field name made lowercase.
    giora = models.DateTimeField(db_column='GioRa', blank=True, null=True)  # Field name made lowercase.
    cannanght = models.FloatField(db_column='CanNangHT', blank=True, null=True)  # Field name made lowercase.
    cannangtruoc = models.FloatField(db_column='CanNangTruoc', blank=True, null=True)  # Field name made lowercase.
    ghichu = models.TextField(db_column='GhiChu', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TheoDoiLopHoc'


class Theodoilophocchitiet(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    id_theodoilophoc = models.CharField(db_column='ID_TheoDoiLopHoc', max_length=36)  # Field name made lowercase.
    id_dichvu = models.CharField(db_column='ID_DichVu', max_length=36)  # Field name made lowercase.
    ghichu = models.TextField(db_column='GhiChu', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TheoDoiLopHocChiTiet'


class Thudientu(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    diachigui = models.TextField(db_column='DiaChiGui', blank=True, null=True)  # Field name made lowercase.
    diachinhan = models.TextField(db_column='DiaChiNhan', blank=True, null=True)  # Field name made lowercase.
    thoigian = models.DateTimeField(db_column='ThoiGian')  # Field name made lowercase.
    tieude = models.TextField(db_column='TieuDe', blank=True, null=True)  # Field name made lowercase.
    noidung = models.TextField(db_column='NoiDung', blank=True, null=True)  # Field name made lowercase.
    dadoc = models.BooleanField(db_column='DaDoc', blank=True, null=True)  # Field name made lowercase.
    quantrong = models.BooleanField(db_column='QuanTrong', blank=True, null=True)  # Field name made lowercase.
    filedinhkem = models.BooleanField(db_column='FileDinhKem', blank=True, null=True)  # Field name made lowercase.
    userlap = models.CharField(db_column='UserLap', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaytao = models.DateTimeField(db_column='NgayTao', blank=True, null=True)  # Field name made lowercase.
    usersua = models.CharField(db_column='UserSua', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaysua = models.DateTimeField(db_column='NgaySua', blank=True, null=True)  # Field name made lowercase.
    loaithu = models.IntegerField(db_column='LoaiThu')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ThuDienTu'


class Tinnhan(models.Model):
    id = models.OneToOneField('self', models.DO_NOTHING, db_column='ID', primary_key=True)  # Field name made lowercase.
    id_nguoidung = models.ForeignKey('SysNguoidung', models.DO_NOTHING, db_column='ID_NguoiDung')  # Field name made lowercase.
    id_chungtu = models.CharField(db_column='ID_ChungTu', max_length=36, blank=True, null=True)  # Field name made lowercase.
    id_khachhang = models.ForeignKey(DmDoituong, models.DO_NOTHING, db_column='ID_KhachHang', blank=True, null=True)  # Field name made lowercase.
    sodienthoai = models.CharField(db_column='SoDienThoai', max_length=16, blank=True, null=True)  # Field name made lowercase.
    noidungtin = models.TextField(db_column='NoiDungTin', blank=True, null=True)  # Field name made lowercase.
    trangthai = models.IntegerField(db_column='TrangThai', blank=True, null=True)  # Field name made lowercase.
    thoigiangui = models.DateTimeField(db_column='ThoiGianGui', blank=True, null=True)  # Field name made lowercase.
    loaitinnhan = models.IntegerField(db_column='LoaiTinNhan', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TinNhan'


class Tonkhokhoitao(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    ngaychungtu = models.DateTimeField(db_column='NgayChungTu')  # Field name made lowercase.
    namhachtoan = models.IntegerField(db_column='NamHachToan')  # Field name made lowercase.
    id_hanghoa = models.ForeignKey(DmHanghoa, models.DO_NOTHING, db_column='ID_HangHoa')  # Field name made lowercase.
    id_kho = models.ForeignKey(DmKho, models.DO_NOTHING, db_column='ID_Kho')  # Field name made lowercase.
    id_lohang = models.ForeignKey(DmLohang, models.DO_NOTHING, db_column='ID_LoHang', blank=True, null=True)  # Field name made lowercase.
    id_donvitinh = models.ForeignKey(DmDonvitinh, models.DO_NOTHING, db_column='ID_DonViTinh')  # Field name made lowercase.
    soluong = models.FloatField(db_column='SoLuong')  # Field name made lowercase.
    dongia = models.FloatField(db_column='DonGia')  # Field name made lowercase.
    thanhtien = models.FloatField(db_column='ThanhTien')  # Field name made lowercase.
    id_donvi = models.CharField(db_column='ID_DonVi', max_length=36, blank=True, null=True)  # Field name made lowercase.
    usertao = models.CharField(db_column='UserTao', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngayvaoso = models.DateTimeField(db_column='NgayVaoSo', blank=True, null=True)  # Field name made lowercase.
    usersuacuoi = models.CharField(db_column='UserSuaCuoi', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaysuacuoi = models.DateTimeField(db_column='NgaySuaCuoi', blank=True, null=True)  # Field name made lowercase.
    id_mavach = models.CharField(db_column='ID_MaVach', max_length=36, blank=True, null=True)  # Field name made lowercase.
    soluongchuan = models.FloatField(db_column='SoLuongChuan', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TonKhoKhoiTao'


class TonquychitietDonvi(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    tienmat = models.FloatField(db_column='TienMat')  # Field name made lowercase.
    tiengui = models.FloatField(db_column='TienGui')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TonQuyChiTiet_DonVi'


class Tonquykhoitao(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    ngaychungtu = models.DateTimeField(db_column='NgayChungTu')  # Field name made lowercase.
    namhachtoan = models.IntegerField(db_column='NamHachToan')  # Field name made lowercase.
    tonquy = models.FloatField(db_column='TonQuy')  # Field name made lowercase.
    id_donvi = models.ForeignKey(DmDonvi, models.DO_NOTHING, db_column='ID_DonVi', blank=True, null=True)  # Field name made lowercase.
    id_tiente = models.ForeignKey(DmTiente, models.DO_NOTHING, db_column='ID_TienTe')  # Field name made lowercase.
    tygia = models.FloatField(db_column='TyGia')  # Field name made lowercase.
    latienmat = models.BooleanField(db_column='LaTienMat', blank=True, null=True)  # Field name made lowercase.
    usertao = models.CharField(db_column='UserTao', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngayvaoso = models.DateTimeField(db_column='NgayVaoSo', blank=True, null=True)  # Field name made lowercase.
    usersuacuoi = models.CharField(db_column='UserSuaCuoi', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaysuacuoi = models.DateTimeField(db_column='NgaySuaCuoi', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TonQuyKhoiTao'


class Tontoithieu(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    id_hanghoa = models.ForeignKey(DmHanghoa, models.DO_NOTHING, db_column='ID_HangHoa')  # Field name made lowercase.
    id_kho = models.ForeignKey(DmKho, models.DO_NOTHING, db_column='ID_Kho')  # Field name made lowercase.
    soluongtontoithieu = models.FloatField(db_column='SoLuongTonToiThieu', blank=True, null=True)  # Field name made lowercase.
    tontoida = models.FloatField(db_column='TonToiDa', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TonToiThieu'


class Tonghopnhapxuat(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    id_donvi = models.CharField(db_column='ID_DonVi', max_length=36, blank=True, null=True)  # Field name made lowercase.
    loaichungtu = models.IntegerField(db_column='LoaiChungTu')  # Field name made lowercase.
    id_chungtu = models.CharField(db_column='ID_ChungTu', max_length=36)  # Field name made lowercase.
    machungtu = models.CharField(db_column='MaChungTu', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaychungtu = models.DateTimeField(db_column='NgayChungTu')  # Field name made lowercase.
    id_nhanvien = models.CharField(db_column='ID_NhanVien', max_length=36, blank=True, null=True)  # Field name made lowercase.
    id_chitiet_chungtu = models.CharField(db_column='ID_ChiTiet_ChungTu', max_length=36)  # Field name made lowercase.
    id_doituong = models.CharField(db_column='ID_DoiTuong', max_length=36, blank=True, null=True)  # Field name made lowercase.
    id_hanghoa = models.CharField(db_column='ID_HangHoa', max_length=36)  # Field name made lowercase.
    id_mavach = models.CharField(db_column='ID_MaVach', max_length=36, blank=True, null=True)  # Field name made lowercase.
    id_donvitinh = models.CharField(db_column='ID_DonViTinh', max_length=36)  # Field name made lowercase.
    id_kho = models.CharField(db_column='ID_Kho', max_length=36)  # Field name made lowercase.
    id_lohang = models.CharField(db_column='ID_LoHang', max_length=36, blank=True, null=True)  # Field name made lowercase.
    soluongnhap = models.FloatField(db_column='SoLuongNhap', blank=True, null=True)  # Field name made lowercase.
    gianhap = models.FloatField(db_column='GiaNhap', blank=True, null=True)  # Field name made lowercase.
    tiennhap = models.FloatField(db_column='TienNhap', blank=True, null=True)  # Field name made lowercase.
    soluongxuat = models.FloatField(db_column='SoLuongXuat', blank=True, null=True)  # Field name made lowercase.
    giaban = models.FloatField(db_column='GiaBan', blank=True, null=True)  # Field name made lowercase.
    tienban = models.FloatField(db_column='TienBan', blank=True, null=True)  # Field name made lowercase.
    tienchietkhau = models.FloatField(db_column='TienChietKhau', blank=True, null=True)  # Field name made lowercase.
    tienthue = models.FloatField(db_column='TienThue', blank=True, null=True)  # Field name made lowercase.
    thanhtoan = models.FloatField(db_column='ThanhToan', blank=True, null=True)  # Field name made lowercase.
    giaxuat = models.FloatField(db_column='GiaXuat', blank=True, null=True)  # Field name made lowercase.
    tienxuat = models.FloatField(db_column='TienXuat', blank=True, null=True)  # Field name made lowercase.
    lanhap = models.BooleanField(db_column='LaNhap', blank=True, null=True)  # Field name made lowercase.
    chiphi = models.FloatField(db_column='ChiPhi', blank=True, null=True)  # Field name made lowercase.
    giamgia = models.FloatField(db_column='GiamGia', blank=True, null=True)  # Field name made lowercase.
    diengiaichungtu = models.TextField(db_column='DienGiaiChungTu', blank=True, null=True)  # Field name made lowercase.
    ghichuchitiet = models.TextField(db_column='GhiChuChiTiet', blank=True, null=True)  # Field name made lowercase.
    soluongchuan = models.FloatField(db_column='SoLuongChuan', blank=True, null=True)  # Field name made lowercase.
    manhanvienthuchien = models.CharField(db_column='MaNhanVienThucHien', max_length=50, blank=True, null=True)  # Field name made lowercase.
    manhanvientuvan = models.CharField(db_column='MaNhanVienTuVan', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mathegiatri = models.TextField(db_column='MaTheGiaTri', blank=True, null=True)  # Field name made lowercase.
    mathelan = models.TextField(db_column='MaTheLan', blank=True, null=True)  # Field name made lowercase.
    tennhanvienthuchien = models.TextField(db_column='TenNhanVienThucHien', blank=True, null=True)  # Field name made lowercase.
    tennhanvientuvan = models.TextField(db_column='TenNhanVienTuVan', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TongHopNhapXuat'


class Tuvankhachhang(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    id_donvi = models.CharField(db_column='ID_DonVi', max_length=36)  # Field name made lowercase.
    id_nhanvien = models.CharField(db_column='ID_NhanVien', max_length=36)  # Field name made lowercase.
    sophieu = models.CharField(db_column='SoPhieu', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaytuvan = models.DateTimeField(db_column='NgayTuVan')  # Field name made lowercase.
    id_khachhang = models.CharField(db_column='ID_KhachHang', max_length=36)  # Field name made lowercase.
    id_dichvu = models.CharField(db_column='ID_DichVu', max_length=36, blank=True, null=True)  # Field name made lowercase.
    ykienkhachhang = models.TextField(db_column='YKienKhachHang', blank=True, null=True)  # Field name made lowercase.
    noidungtuvan = models.TextField(db_column='NoiDungTuVan', blank=True, null=True)  # Field name made lowercase.
    trangthaisautuvan = models.IntegerField(db_column='TrangThaiSauTuVan')  # Field name made lowercase.
    userlap = models.CharField(db_column='UserLap', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaytao = models.DateTimeField(db_column='NgayTao', blank=True, null=True)  # Field name made lowercase.
    usersuacuoi = models.CharField(db_column='UserSuaCuoi', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaysuacuoi = models.DateTimeField(db_column='NgaySuaCuoi', blank=True, null=True)  # Field name made lowercase.
    id_noidungquantam2 = models.CharField(db_column='ID_NoiDungQuanTam2', max_length=36, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TuVanKhachHang'


class Vitrihangtrongkho(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    id_kho = models.ForeignKey(DmKho, models.DO_NOTHING, db_column='ID_Kho')  # Field name made lowercase.
    id_hanghoa = models.ForeignKey(DmHanghoa, models.DO_NOTHING, db_column='ID_HangHoa')  # Field name made lowercase.
    id_mavach = models.CharField(db_column='ID_MaVach', max_length=36, blank=True, null=True)  # Field name made lowercase.
    vitri = models.CharField(db_column='ViTri', max_length=250)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ViTriHangTrongKho'


class SysApi(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    nhacungcap = models.TextField(db_column='NhaCungCap')  # Field name made lowercase.
    taikhoan = models.TextField(db_column='TaiKhoan')  # Field name made lowercase.
    matkhau = models.TextField(db_column='MatKhau')  # Field name made lowercase.
    apikey = models.TextField(db_column='APIKey')  # Field name made lowercase.
    ghichu = models.TextField(db_column='GhiChu')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sys_API'


class SysCauhinhphanmem(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    macauhinh = models.CharField(db_column='MaCauHinh', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tencauhinh = models.CharField(db_column='TenCauHinh', max_length=255, blank=True, null=True)  # Field name made lowercase.
    giatricauhinh = models.TextField(db_column='GiaTriCauHinh', blank=True, null=True)  # Field name made lowercase.
    ghichu = models.TextField(db_column='GhiChu', blank=True, null=True)  # Field name made lowercase.
    chungtu = models.TextField(db_column='ChungTu', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sys_CauHinhPhanMem'


class SysCompany(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    tencongty = models.CharField(db_column='TenCongTy', max_length=250)  # Field name made lowercase.
    diachi = models.CharField(db_column='DiaChi', max_length=500, blank=True, null=True)  # Field name made lowercase.
    sodienthoai = models.CharField(db_column='SoDienThoai', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sofax = models.CharField(db_column='SoFax', max_length=50, blank=True, null=True)  # Field name made lowercase.
    masothue = models.CharField(db_column='MaSoThue', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mail = models.CharField(db_column='Mail', max_length=50, blank=True, null=True)  # Field name made lowercase.
    website = models.CharField(db_column='Website', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tengiamdoc = models.CharField(db_column='TenGiamDoc', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tenketoantruong = models.CharField(db_column='TenKeToanTruong', max_length=50, blank=True, null=True)  # Field name made lowercase.
    logo = models.BinaryField(db_column='Logo', blank=True, null=True)  # Field name made lowercase.
    ghichu = models.CharField(db_column='GhiChu', max_length=500, blank=True, null=True)  # Field name made lowercase.
    taikhoannganhang = models.CharField(db_column='TaiKhoanNganHang', max_length=50, blank=True, null=True)  # Field name made lowercase.
    diachinganhang = models.CharField(db_column='DiaChiNganHang', max_length=500, blank=True, null=True)  # Field name made lowercase.
    tenvt = models.CharField(db_column='TenVT', max_length=250, blank=True, null=True)  # Field name made lowercase.
    diachivt = models.CharField(db_column='DiaChiVT', max_length=500, blank=True, null=True)  # Field name made lowercase.
    danghoatdong = models.BooleanField(db_column='DangHoatDong', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sys_Company'


class SysNguoidung(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    id_nhanvien = models.ForeignKey(DmNhanvien, models.DO_NOTHING, db_column='ID_NhanVien', blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=50)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=150)  # Field name made lowercase.
    hoten = models.CharField(db_column='HoTen', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ngaysinh = models.DateTimeField(db_column='NgaySinh', blank=True, null=True)  # Field name made lowercase.
    mota = models.CharField(db_column='MoTa', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sochungminh = models.CharField(db_column='SoChungMinh', max_length=50, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=250, blank=True, null=True)  # Field name made lowercase.
    website = models.CharField(db_column='Website', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dienthoainoilamviec = models.CharField(db_column='DienThoaiNoiLamViec', max_length=20, blank=True, null=True)  # Field name made lowercase.
    dienthoainharieng = models.CharField(db_column='DienThoaiNhaRieng', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dienthoaididong = models.CharField(db_column='DienThoaiDiDong', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fax = models.CharField(db_column='Fax', max_length=50, blank=True, null=True)  # Field name made lowercase.
    diachilamviec = models.CharField(db_column='DiaChiLamViec', max_length=255, blank=True, null=True)  # Field name made lowercase.
    nguyenquan = models.CharField(db_column='NguyenQuan', max_length=255, blank=True, null=True)  # Field name made lowercase.
    thuongtru = models.CharField(db_column='ThuongTru', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tamtru = models.CharField(db_column='TamTru', max_length=255, blank=True, null=True)  # Field name made lowercase.
    anh = models.BinaryField(db_column='Anh', blank=True, null=True)  # Field name made lowercase.
    lanhanvien = models.BooleanField(db_column='LaNhanVien')  # Field name made lowercase.
    laadmin = models.BooleanField(db_column='LaAdmin')  # Field name made lowercase.
    inactive = models.BooleanField(db_column='Inactive')  # Field name made lowercase.
    issystem = models.BooleanField(db_column='IsSystem')  # Field name made lowercase.
    usertao = models.CharField(db_column='UserTao', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaytao = models.DateTimeField(db_column='NgayTao', blank=True, null=True)  # Field name made lowercase.
    usersuacuoi = models.CharField(db_column='UserSuaCuoi', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaysuacuoi = models.DateTimeField(db_column='NgaySuaCuoi', blank=True, null=True)  # Field name made lowercase.
    id_donvi = models.CharField(db_column='ID_DonVi', max_length=36, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sys_NguoiDung'


class SysNguoidungnhom(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    idnhom = models.ForeignKey('SysNhomnguoidung', models.DO_NOTHING, db_column='IDNhom')  # Field name made lowercase.
    iduser = models.ForeignKey(SysNguoidung, models.DO_NOTHING, db_column='IDUser')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sys_NguoiDungNhom'


class SysNhatkynguoidung(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    userid = models.ForeignKey(SysNguoidung, models.DO_NOTHING, db_column='UserID')  # Field name made lowercase.
    sukien = models.CharField(db_column='SuKien', max_length=255, blank=True, null=True)  # Field name made lowercase.
    chucnang = models.CharField(db_column='ChucNang', max_length=255, blank=True, null=True)  # Field name made lowercase.
    idbanghi = models.CharField(db_column='IDBanGhi', max_length=36, blank=True, null=True)  # Field name made lowercase.
    mabanghi = models.CharField(db_column='MaBanGhi', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tenbanghi = models.CharField(db_column='TenBanGhi', max_length=500, blank=True, null=True)  # Field name made lowercase.
    ngaygio = models.DateTimeField(db_column='NgayGio', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sys_NhatKyNguoiDung'


class SysNhomnguoidung(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    manhom = models.CharField(db_column='MaNhom', max_length=50)  # Field name made lowercase.
    tennhom = models.CharField(db_column='TenNhom', max_length=100)  # Field name made lowercase.
    mota = models.CharField(db_column='MoTa', max_length=255, blank=True, null=True)  # Field name made lowercase.
    usertao = models.CharField(db_column='UserTao', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaytao = models.DateTimeField(db_column='NgayTao', blank=True, null=True)  # Field name made lowercase.
    usersuacuoi = models.CharField(db_column='UserSuaCuoi', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaysuacuoi = models.DateTimeField(db_column='NgaySuaCuoi', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sys_NhomNguoiDung'


class SysPhimtat(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    maphim = models.CharField(db_column='MaPhim', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tenphim = models.CharField(db_column='TenPhim', max_length=255, blank=True, null=True)  # Field name made lowercase.
    keyfn = models.IntegerField(db_column='KeyFn', blank=True, null=True)  # Field name made lowercase.
    keycode = models.IntegerField(db_column='KeyCode', blank=True, null=True)  # Field name made lowercase.
    diengiai = models.CharField(db_column='DienGiai', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sys_PhimTat'


class SysQuyen(models.Model):
    maquyen = models.CharField(db_column='MaQuyen', primary_key=True, max_length=100)  # Field name made lowercase.
    tenquyen = models.TextField(db_column='TenQuyen', blank=True, null=True)  # Field name made lowercase.
    mota = models.TextField(db_column='MoTa')  # Field name made lowercase.
    quyencha = models.CharField(db_column='QuyenCha', max_length=100, blank=True, null=True)  # Field name made lowercase.
    duocsudung = models.BooleanField(db_column='DuocSuDung', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sys_Quyen'


class SysQuyennhom(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    idnhom = models.ForeignKey(SysNhomnguoidung, models.DO_NOTHING, db_column='IDNhom')  # Field name made lowercase.
    maquyen = models.ForeignKey(SysQuyen, models.DO_NOTHING, db_column='MaQuyen')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sys_QuyenNhom'


class Sysdiagrams(models.Model):
    name = models.CharField(max_length=128)
    principal_id = models.IntegerField()
    diagram_id = models.AutoField(primary_key=True)
    version = models.IntegerField(blank=True, null=True)
    definition = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sysdiagrams'
        unique_together = (('principal_id', 'name'),)


class Tbltinnhansms(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    thuebaonhan = models.TextField(db_column='ThueBaoNhan', blank=True, null=True)  # Field name made lowercase.
    tbnhantc = models.TextField(db_column='TBNhanTC', blank=True, null=True)  # Field name made lowercase.
    tbnhanktc = models.TextField(db_column='TBNhanKTC', blank=True, null=True)  # Field name made lowercase.
    noidungtn = models.TextField(db_column='NoiDungTN', blank=True, null=True)  # Field name made lowercase.
    thoigian = models.DateTimeField(db_column='ThoiGian', blank=True, null=True)  # Field name made lowercase.
    latinguidi = models.BooleanField(db_column='LaTinGuiDi')  # Field name made lowercase.
    latinnhap = models.BooleanField(db_column='LaTinNhap')  # Field name made lowercase.
    danhdauchuadoc = models.BooleanField(db_column='DanhDauChuaDoc', blank=True, null=True)  # Field name made lowercase.
    sothuebaoguidi = models.CharField(db_column='SoThueBaoGuiDi', max_length=20, blank=True, null=True)  # Field name made lowercase.
    sothuebaoguiden = models.CharField(db_column='SoThueBaoGuiDen', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ghichu = models.TextField(db_column='GhiChu', blank=True, null=True)  # Field name made lowercase.
    matn = models.CharField(db_column='MaTN', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblTinNhanSMS'
