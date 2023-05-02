import { swal } from 'components/sweetalert2/instance'
import { isSuccessRequest } from 'store/request/helper';
import { AxiosResponse } from 'axios';

// Set SweetAlert options
export const swalSuccess = (swalTitle:string) => {
	swal.fire({
    icon: 'success',
    title: swalTitle,
    showConfirmButton: false,
    timer: 600,
  });
}

export const swalDeleteSuccess = (swalTitle:string) => {
  swal.fire('Deleted!', `Bạn đã xóa ${swalTitle} thành công`, 'success');
}

export const swalDelete:any = ()  => {
	return swal.fire({
    title: 'Bạn có chắc chắn muốn xóa?',
    text: "Bạn sẽ không thể lấy lại được!",
    icon: 'warning',
    showCancelButton: true,
    confirmButtonColor: '#3085d6',
    cancelButtonColor: '#d33',
    confirmButtonText: 'Xóa',
  })
  .then((result) => {
    return result;
  })
}
// export const swalDelete = (handleDelete: Promise<AxiosResponse<any, any>> ) => {
// 	swal.fire({
//     title: 'Bạn có chắc chắn muốn xóa?',
//     text: "Bạn sẽ không thể lấy lại được!",
//     icon: 'warning',
//     showCancelButton: true,
//     confirmButtonColor: '#3085d6',
//     cancelButtonColor: '#d33',
//     confirmButtonText: 'Xóa',
//   })
//   .then(async (result) => {
//     if (result.isConfirmed) {
//       const res = await handleDelete;
//       if (isSuccessRequest(res)) {
//         swal.fire('Deleted!', `Bạn đã xóa thành công`, 'success');
//       }
//     }
//   })
// }

