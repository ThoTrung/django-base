from django.core.management.base import BaseCommand
from myapp.models import MyModel1, MyModel2
from otherapp.models import OtherModel

class Command(BaseCommand):
    help = 'Moves data from one database to another'

    def handle(self, *args, **options):
        # Retrieve data from the source database
        source_data = MyModel1.objects.using('source_db').all()

        # Map the data to the target models and save to the target database
        target_data = [MyModel2(field1=item.field1, field2=item.field2) for item in source_data]
        MyModel2.objects.using('target_db').bulk_create(target_data)

        # You can repeat the above process for other models as needed
        # If you need to access data from another app, import its models and use them like so:
        other_data = OtherModel.objects.using('source_db').all()
        # ...

from himalaya import models
# DmNhomdoituong
# DmDoituong

srcDmNhomdoituongs = models.DmNhomdoituong.objects.using('himalaya').all()
desDmNhomdoituongsData = [models.DmNhomdoituong(
    id=item.id,
    loaidoituong=item.loaidoituong,
    manhom=item.manhom,
    tennhom=item.tennhom,
    ghichu=item.ghichu,
    usertao=item.usertao,
    ngaytao=item.ngaytao,
    usersuacuoi=item.usersuacuoi,
    ngaysuacuoi=item.ngaysuacuoi,
) for item in srcDmNhomdoituongs]
models.DmNhomdoituong.objects.using('default').bulk_create(desDmNhomdoituongsData)


srcDmDoituongs = models.DmDoituong.objects.using('himalaya').all()
desDmDoituongsData = [models.DmDoituong(
    id=item.id,
    loaidoituong=item.loaidoituong,
    lacanhan=item.lacanhan,
    id_nhomdoituong_id=item.id_nhomdoituong_id,
    madoituong=item.madoituong,
    tendoituong=item.tendoituong,
    dienthoai=item.dienthoai,
    fax=item.fax,
    email=item.email,
    website=item.website,
    anh=item.anh,
    masothue=item.masothue,
    taikhoannganhang=item.taikhoannganhang,
    gioihancongno=item.gioihancongno,
    ghichu=item.ghichu,
    id_tinhthanh=item.id_tinhthanh,
    ngaysinh_ngaytlap=item.ngaysinh_ngaytlap,
    chiase=item.chiase,
    theodoi=item.theodoi,
    usertao=item.usertao,
    ngaynhap=item.ngaynhap,
    usersuacuoi=item.usersuacuoi,
    ngaysuacuoi=item.ngaysuacuoi,
    id_index=item.id_index,
    theodoivantay=item.theodoivantay,
    id_quanhuyen=item.id_quanhuyen,
    id_nhanvienphutrach=item.id_nhanvienphutrach,
    ngaydoinhom=item.ngaydoinhom,
    diemkhoitao=item.diemkhoitao,
    doanhsokhoitao=item.doanhsokhoitao,
    id_nguoigioithieu=item.id_nguoigioithieu,
    id_nguonkhach=item.id_nguonkhach,
    captai_dkkd=item.captai_dkkd,
    diachi=item.diachi,
    gioitinhnam=item.gioitinhnam,
    nganhang=item.nganhang,
    ngaycapcmtnd_dkkd=item.ngaycapcmtnd_dkkd,
    noicapcmtnd_dkkd=item.noicapcmtnd_dkkd,
    sdt_coquan=item.sdt_coquan,
    sdt_nharieng=item.sdt_nharieng,
    socmtnd_dkkd=item.socmtnd_dkkd,
    thuongtru=item.thuongtru,
    xungho=item.xungho,
    id_quocgia=item.id_quocgia,
    ngaygiaodichgannhat=item.ngaygiaodichgannhat,
    id_nhomcu=item.id_nhomcu,
    tennguonkhach=item.tennguonkhach,
    tennhom=item.tennhom,
    id_donvi=item.id_donvi,
    chucvu=item.chucvu,
    linhvuc=item.linhvuc,
    nghenghiep=item.nghenghiep,
    tenkhac=item.tenkhac,
    diachikhac=item.diachikhac,
    id_trangthai=item.id_trangthai,
    ngaysuatrangthai=item.ngaysuatrangthai,
) for item in srcDmDoituongs]
models.DmDoituong.objects.using('default').bulk_create(desDmDoituongsData)