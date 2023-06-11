// import React from 'react'
// import { Row, Col, ListGroup, Button, Modal, Form } from '@blueupcode/components'
// import type { ExtendedNextPage } from '@blueupcode/components/types'
// import withAuth from 'components/auth/withAuth'
// import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
// import { faTimes } from '@fortawesome/free-solid-svg-icons'
// import { modalType, newType, updateType, detailType } from 'constant/type'
// import { useDispatch } from "react-redux";
// import { AShowLoading, AHideLoading } from 'store/common/actions'
// import { useForm, Controller } from 'react-hook-form'
// import DateTimePicker from 'react-datetime'
// import * as yup from 'yup'
// import { yupResolver } from '@hookform/resolvers/yup'
// import { isSuccessRequest } from 'store/request/helper'
// import { swalSuccess, swalDelete, swalDeleteSuccess } from 'components/swals/swals'
// import {
//   ICreateJob,
//   createJob,
//   updateJob,
// } from 'store/request/job'
// import { DATETIME_FORMAT, DATE_FORMAT, TIME_FORMAT, DATE_FORMAT_DISPLAY } from 'constant/const';
// import { string } from 'prop-types'

// const configData = {
// 	folder_path: {
// 		display_name: 'Đường dẫn *',
//     validate: yup.string().required('Bạn cần chọn đường thư mục để upload ảnh'),
//     default_value: '11111',
// 	},
// 	name: {
// 		display_name: 'Tên Job *',
//     validate: yup.string().required('Bạn cần nhập tên job'),
//     default_value: '',
// 	},
// 	customer: {
//     type: 'select',
// 		display_name: 'Tên KH *',
//     validate: yup.string().required('Bạn cần chọn khách hàng'),
//     default_value: '',
// 	},
// 	file_number: {
// 		display_name: 'Số lượng file *',
//     validate: yup.number().required('Bạn cần chọn số lượng file'),
//     default_value: 0,
// 	},
// 	expose: {
// 		display_name: 'Số expose *',
//     validate: yup.string().required('Bạn cần nhập số expose'),
//     default_value: '',
// 	},
// 	style: {
// 		display_name: 'Style cố định',
//     validate: yup.string().required('Bạn cần nhập style cố định'),
//     default_value: '',
// 	},
// 	note: {
// 		display_name: 'Chú ý',
//     default_value: '',
// 	},
// 	deadline: {
// 		display_name: 'Deadline',
//     default_value: '',
// 	},
// 	number_sub_job: {
// 		display_name: 'Số Job chia',
//     default_value: '',
// 	},
// 	editor: {
// 		display_name: 'Editor',
//     default_value: '',
// 	},
// 	customer_price: {
// 		display_name: 'Giá KH',
//     default_value: '',
//     post_display: 'USD'
// 	},
// 	editor_price: {
// 		display_name: 'Giá editor',
//     default_value: '',
//     post_display: 'VNĐ',
// 	},
// }


// export type ICreateJobProps = {
//   data: {

//   }
// }

// const validateObject:any  = {}

// Object.keys(configData).forEach(key => {
//   if (configData[key].validate) {
//     validateObject[key] = configData[key].validate;
//   }
// });

// const validationSchema = yup.object().shape(validateObject);

// const CreateJobPage: ExtendedNextPage<ICreateJob> = (props) => {
//   const [serverErrors, setServerErrors] = React.useState<any>({});

//   const dispatch = useDispatch();

//   const defaultValue = {};
//   Object.keys(configData).forEach(key => {
//     defaultValue[key] = configData[key].default_value ?? '';
//   });

// 	const {control, handleSubmit} = useForm<ICreateJob>({
//     resolver: yupResolver(validationSchema),
// 		defaultValues: defaultValue,
//   })

//   const onErrors = (error) => {
//     // console.log('onErrors....', error);
//   }

// 	const onSubmit = async (formData: any) => {
//     dispatch(AShowLoading());
//     const payload={}
//     Object.keys(configData).forEach(key => {
//       payload[key] = formData[key];
//     });
//     console.log('payload', payload);
//     // if (!isUpdateMode || changePassword) {
//     // }
//     let res = null;
//     let swalTitle = '';
//     res = await createJob(payload as ICreateJob);
//     swalTitle = 'Tạo Job thành công'
//     if (isSuccessRequest(res)) {
//       swalSuccess(swalTitle);
//     } else { // Error: 4xx
//       setServerErrors(res.data);
//     }
//     dispatch(AHideLoading());
//   }

//   const handleCancel = () => {
//     console.log('handle cancel')
//   }

// 	return (
// 		<div className='w-xlg'>
// 			<Form onSubmit={handleSubmit(onSubmit, onErrors)} className="d-grid gap-3">
//         {Object.keys(configData).map(key => (
//             <Controller
//               key={key}
//               name={key}
//               control={control}
//               render={({ field, fieldState: { invalid, error } }) => (
//                 <Form.Group controlId={key}>
//                   <Row className='mt-2'>
//                     <Col sm={12}>
//                       <div className='d-flex'>
//                         <Form.Label className='w-sm'>{configData[key].display_name}</Form.Label>
//                         <div className='fr-1'>
//                           <Form.Control
//                             // type='email'
//                             // disabled={readOnly}
//                             isInvalid={invalid || !!serverErrors[key]}
//                             {...field}
//                           />
//                           {invalid && <Form.Control.Feedback type="invalid">{error?.message}</Form.Control.Feedback>}
//                           {!!serverErrors[key] && <Form.Control.Feedback type="invalid">{serverErrors[key]}</Form.Control.Feedback>}
//                         </div>
//                       </div>
//                     </Col>
//                   </Row>
//                 </Form.Group>
//               )}
//             />
//           )
//         )}
//         <div className="d-flex justify-content-end">
//           <Button type="submit" variant="primary">Tạo</Button>
//           <Button variant="outline-secondary" onClick={handleCancel} className='ms-2'>Cancel</Button>
//         </div>
//       </Form>
// 		</div>
// 	)
// }

// CreateJobPage.pageTitle = 'Tạo job'
// CreateJobPage.activeLink = 'create_job'
// CreateJobPage.breadcrumb = [
// 	{ text: "Tạo job", link: "/create_job" },
// ]

// export default withAuth(CreateJobPage)
