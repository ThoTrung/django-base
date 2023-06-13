<<<<<<< HEAD
import React from 'react'
import { Row, Col, ListGroup, Button, Modal, Form } from '@blueupcode/components'
=======
import React, { useEffect } from 'react';
import withAuth from 'components/auth/withAuth'
>>>>>>> 3aa7f2d (test)
import type { ExtendedNextPage } from '@blueupcode/components/types'
import withAuth from 'components/auth/withAuth'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faTimes } from '@fortawesome/free-solid-svg-icons'
import { modalType, newType, updateType, detailType } from 'constant/type'
import { useDispatch } from "react-redux";
import { AShowLoading, AHideLoading } from 'store/common/actions'
import { useForm, Controller } from 'react-hook-form'
import DateTimePicker from 'react-datetime'
import * as yup from 'yup'
import { yupResolver } from '@hookform/resolvers/yup'
import { isSuccessRequest } from 'store/request/helper'
import { swalSuccess, swalDelete, swalDeleteSuccess } from 'components/swals/swals'
import {
  ICreateJob,
  createJob,
  updateJob,
} from 'store/request/job'
import {
	ICustomer,
	listCustomers,
} from 'store/request/customer_manager';
import {
  ICUser,
  listCUsers
} from 'store/request/user_manager'
import { DATETIME_FORMAT, DATE_FORMAT, TIME_FORMAT, DATE_FORMAT_DISPLAY, NUMBER_ARRAY_10, ALLOW_FILE_TYPES } from 'constant/const';
import { string } from 'prop-types'

const configData = {
	folder_path: {
    type: 'file',
		display_name: 'Đường dẫn *:',
    validate: yup.string().required('Bạn cần chọn đường thư mục để upload ảnh'),
    default_value: '',
    readonly: true,
    allow_file_type: ".jpg, .png, .psd",
    version: 1,
	},
	name: {
		display_name: 'Tên Job *:',
    validate: yup.string().required('Bạn cần nhập tên job'),
    default_value: '',
	},
	customer: {
    type: 'select',
    selected_list: 'customers',
		display_name: 'Tên KH *:',
    validate: yup.string().required('Bạn cần chọn khách hàng'),
    default_value: '',
	},
	file_number: {
    type: 'number',
		display_name: 'Số lượng file *:',
    validate: yup.number().required('Bạn cần chọn số lượng file'),
    default_value: 0,
    readonly: true,
	},
	expose: {
		display_name: 'Số expose *:',
    validate: yup.string().required('Bạn cần nhập số expose'),
    default_value: '',
	},
	style: {
    type: 'textarea',
		display_name: 'Style cố định *:',
    validate: yup.string().required('Bạn cần nhập style cố định'),
    default_value: '',
	},
	note: {
    type: 'textarea',
		display_name: 'Chú ý:',
    default_value: '',
	},
	deadline: {
    type: 'timepicker',
		display_name: 'Deadline:',
    default_value: '',
    classNames: 'w-md',
	},
	number_sub_job: {
    type: 'select',
    selected_list: 'number_sub_job',
    default_value: 1,
		display_name: 'Số Job chia:',
    classNames: 'w-md',
	},
	editor: {
    type: 'select',
    selected_list: 'users',
		display_name: 'Editor:',
    default_value: '',
	},
	customer_price: {
    type: 'number',
		display_name: 'Giá KH:',
    default_value: 0,
    classNames: 'w-md',
    post_display: 'USD',
	},
	editor_price: {
    type: 'number',
		display_name: 'Giá editor:',
    default_value: 0,
    classNames: 'w-md',
    post_display: 'VNĐ',
	},
}

export type ICreateJobProps = {
  data: {
    customers: {[key: string]: ICustomer},
    users: {[key: string]: ICUser},
  }
}

const validateObject:any  = {}

Object.keys(configData).forEach(key => {
  if (configData[key].validate) {
    validateObject[key] = configData[key].validate;
  }
});

const validationSchema = yup.object().shape(validateObject);

const CreateJobPage: ExtendedNextPage<ICreateJobProps> = (props) => {
  const [serverErrors, setServerErrors] = React.useState<any>({});
  const [selectedFiles, setSelectedFiles] = React.useState<any>([]);

  const dispatch = useDispatch();

  const defaultValue = {};
  Object.keys(configData).forEach(key => {
    defaultValue[key] = configData[key].default_value ?? '';
  });

	const {control, handleSubmit, setValue, getValues, reset} = useForm<ICreateJob>({
    resolver: yupResolver(validationSchema),
		defaultValues: defaultValue,
  })

  const onChangeSelect = (id, key) => {
    console.log('onChangeSelect', id, key);
    switch(key) {
      case 'customer':
        if (id) {
          const customer = props.data.customers[id];
          setValue('expose', customer.expose);
          setValue('style', customer.style);
          setValue('deadline', customer.deadline ? customer.deadline.substring(0, 5) : '');
          console.log('customer.deadline', customer.deadline);
        }
        break;
      case 'number_sub_job':
        if (id && id > 0) {
          let jobName = getValues('name');
          console.log('jobName', jobName);
          if (jobName) {
            jobName = jobName.split("__")[0];
            let jobNames = id > 1 ? `${jobName}__1` : jobName;
            for (let i = 2; i <= id; i ++) {
              jobNames = `${jobNames}, ${jobName}__${i}`;
            }
            setValue('name', jobNames);
          }
        }
      default:
        break;
    }
  }

  const onErrors = (error) => {
    console.log('onErrors....', error);
  }

	const onSubmit = async (formData: any) => {
    dispatch(AShowLoading());
    const payload={}
    Object.keys(configData).forEach(key => {
      payload[key] = formData[key];
    });
    console.log('payload', payload);
    // if (!isUpdateMode || changePassword) {
    // }
    let res = null;
    let swalTitle = '';
    res = await createJob(payload as ICreateJob);

    // Now it time for upload file
    

    swalTitle = 'Tạo Job thành công'
    if (isSuccessRequest(res)) {
      swalSuccess(swalTitle);
    } else { // Error: 4xx
      setServerErrors(res.data);
    }
    dispatch(AHideLoading());
  }

  const handleCancel = () => {
    console.log('handle cancel')
  }

  const handleFolderSelection = (event: React.ChangeEvent<HTMLInputElement>) => {
    const files = event.target.files;
    const acceptedFiles = [];
    console.log('1111');
    if (files && files.length > 0) {
      // Filter file
      console.log('2222');
      for (let i = 0; i < files.length; ++i) {
        const file = files[i];
        if (ALLOW_FILE_TYPES.includes(file.type)) {
          acceptedFiles.push(file);
        }
      }
      console.log('3333');
      setValue('folder_path', files[0].webkitRelativePath.split('/')[0]);
    }
    if (acceptedFiles.length > 0) {
      console.log('4444');
      setValue('file_number', acceptedFiles.length);
      setSelectedFiles(acceptedFiles);
      delete serverErrors['folder_path'];
      setServerErrors({...serverErrors});
    } else {
      console.log('555');
      setValue('file_number', 0);
      setServerErrors({...serverErrors, folder_path: 'Thư mục không có file thỏa mãn, hãy chắc chắn rằng thư mục bạn đang chọn có các file .jpg, .png'})
    }
    console.log('---------------------', files, acceptedFiles);
  };

	return (
		<div className='w-xlg'>
			<Form onSubmit={handleSubmit(onSubmit, onErrors)} className="d-grid gap-3">
        {Object.keys(configData).map(key => {

          switch(configData[key].type) {
            case 'file':
              return (
                <Controller
                  key={key}
                  name={key}
                  control={control}
                  render={({ field, fieldState: { invalid, error } }) => (
                    <Form.Group controlId={key}>
                      <Row className='mt-2'>
                        <Col sm={12}>
                          <div className='d-flex align-items-center'>
                            <Form.Label className='w-sm mb-0'>{configData[key].display_name}</Form.Label>
                            <div className={configData[key].classNames ?? 'fr-1'}>
                              <Form.Control
                                disabled={configData[key].readonly ?? false}
                                type='text'
                                // disabled={readOnly}
                                isInvalid={invalid || !!serverErrors[key]}
                                {...field}
                              />
                              {invalid && <Form.Control.Feedback type="invalid">{error?.message}</Form.Control.Feedback>}
                              {!!serverErrors[key] && <Form.Control.Feedback type="invalid">{serverErrors[key]}</Form.Control.Feedback>}
                            </div>
                            <div className='align-self-start'>
                              <label htmlFor="forderInput" className='btn btn-success ms-2'>Duyệt thư mục</label>
                              <input
                                type="file"
                                id="forderInput"
                                onChange={(e) => {
                                  handleFolderSelection(e, key);
                                }}
                                accept={configData[key].allow_file_type ?? null}
                                hidden
                                webkitdirectory="true"
                                directory
                                multiple
                              />
                            </div>
                          </div>
                        </Col>
                      </Row>
                    </Form.Group>
                  )}
                />
              );
            case 'select':
              const selected_list = props.data[configData[key].selected_list];
              return (
                <Controller
                  key={key}
                  name={key}
                  control={control}
                  render={({ field, fieldState: { invalid, error } }) => (
                    <Form.Group controlId={key}>
                      <Row className='mt-2'>
                        <Col sm={12}>
                          <div className='d-flex align-items-center'>
                          <Form.Label className='w-sm mb-0'>{configData[key].display_name}</Form.Label>
                          <div className={configData[key].classNames ?? 'fr-1'}>
                              <Form.Select
                                disabled={configData[key].readonly ?? false}
                                defaultValue=""
                                {...field}
                                onChange={(e) => {
                                  console.log('on change 111')
                                  field.onChange(e);
                                  onChangeSelect(e.target.value, key);
                                }}
                              >
                                <option value=""></option>
                                {Object.keys(selected_list).map((k: string) => (
                                  <option key={k} value={k} selected={configData[key].default_value && k==configData[key].default_value}>{selected_list[k].name}</option>
                                ))}
                              </Form.Select>
                              {invalid && <Form.Control.Feedback type="invalid">{error?.message}</Form.Control.Feedback>}
                              {!!serverErrors[key] && <Form.Control.Feedback type="invalid">{serverErrors[key]}</Form.Control.Feedback>}
                            </div>
                          </div>
                        </Col>
                      </Row>
                    </Form.Group>
                  )}
                />
              )
            case 'textarea':
              return (
                <Controller
                  key={key}
                  name={key}
                  control={control}
                  render={({ field, fieldState: { invalid, error } }) => (
                    <Form.Group controlId={key}>
                      <Row className='mt-2'>
                        <Col sm={12}>
                          <div className='d-flex align-items-center'>
                            <Form.Label className='w-sm mb-0'>{configData[key].display_name}</Form.Label>
                            <div className={configData[key].classNames ?? 'fr-1'}>
                              <Form.Control
                                disabled={configData[key].readonly ?? false}
                                as="textarea"
                                // type={configData[key].type ?? 'text'}
                                isInvalid={invalid || !!serverErrors[key]}
                                {...field}
                              />
                              {invalid && <Form.Control.Feedback type="invalid">{error?.message}</Form.Control.Feedback>}
                              {!!serverErrors[key] && <Form.Control.Feedback type="invalid">{serverErrors[key]}</Form.Control.Feedback>}
                            </div>
                          </div>
                        </Col>
                      </Row>
                    </Form.Group>
                  )}
                />
              )
            case 'timepicker':
              return (
                <Controller
                  key={key}
                  name={key}
                  control={control}
                  render={({ field, fieldState: { invalid, error } }) => (
                    <Form.Group controlId={key}>
                      <Row className='mt-2'>
                        <Col sm={12}>
                          <div className='d-flex align-items-center'>
                            <Form.Label className='w-sm mb-0'>{configData[key].display_name}</Form.Label>
                            <div className={configData[key].classNames ?? 'fr-1'}>
                            <DateTimePicker
                              closeOnSelect
                              dateFormat={false}
                              timeFormat={TIME_FORMAT}
                              onChange={(date) => field.onChange(date)}
                              value={field.value}
                              initialViewMode={'time'}
                            />
                            {invalid && <Form.Control.Feedback type="invalid">{error?.message}</Form.Control.Feedback>}
                            {!!serverErrors[key] && <Form.Control.Feedback type="invalid">{serverErrors[key]}</Form.Control.Feedback>}
                            </div>
                          </div>
                        </Col>
                      </Row>
                    </Form.Group>
                  )}
                />
              )
            case 'number':
              return (
                <Controller
                  key={key}
                  name={key}
                  control={control}
                  render={({ field, fieldState: { invalid, error } }) => (
                    <Form.Group controlId={key}>
                      <Row className='mt-2'>
                        <Col sm={12}>
                          <div className='d-flex align-items-center'>
                            <Form.Label className='w-sm mb-0'>{configData[key].display_name}</Form.Label>
                            <div className={configData[key].classNames ?? 'fr-1'}>
                              <Form.Control
                                disabled={configData[key].readonly ?? false}
                                type='number'
                                isInvalid={invalid || !!serverErrors[key]}
                                min={configData[key].min}
                                max={configData[key].max}
                                {...field}
                              />
                              {invalid && <Form.Control.Feedback type="invalid">{error?.message}</Form.Control.Feedback>}
                              {!!serverErrors[key] && <Form.Control.Feedback type="invalid">{serverErrors[key]}</Form.Control.Feedback>}
                            </div>
                            {configData[key].post_display && (
                              <div className='ms-2'>{configData[key].post_display}</div>
                            )}
                          </div>
                        </Col>
                      </Row>
                    </Form.Group>
                  )}
                />
              )
            default:
              return (
                <Controller
                  key={key}
                  name={key}
                  control={control}
                  render={({ field, fieldState: { invalid, error } }) => (
                    <Form.Group controlId={key}>
                      <Row className='mt-2'>
                        <Col sm={12}>
                          <div className='d-flex align-items-center'>
                            <Form.Label className='w-sm mb-0'>{configData[key].display_name}</Form.Label>
                            <div className={configData[key].classNames ?? 'fr-1'}>
                              <Form.Control
                                disabled={configData[key].readonly ?? false}
                                type={configData[key].type ?? 'text'}
                                isInvalid={invalid || !!serverErrors[key]}
                                {...field}
                              />
                              {invalid && <Form.Control.Feedback type="invalid">{error?.message}</Form.Control.Feedback>}
                              {!!serverErrors[key] && <Form.Control.Feedback type="invalid">{serverErrors[key]}</Form.Control.Feedback>}
                            </div>
                            {configData[key].post_display && (
                              <div className='ms-2'>{configData[key].post_display}</div>
                            )}
                          </div>
                        </Col>
                      </Row>
                    </Form.Group>
                  )}
                />
              )
          }
        }
        )}
        <div className="d-flex justify-content-end">
          <Button type="submit" variant="primary">Tạo</Button>
          <Button variant="outline-secondary" onClick={handleCancel} className='ms-2'>Cancel</Button>
        </div>
      </Form>
		</div>
import Uppy from '@uppy/core';
import Tus from "@uppy/tus";
import { Dashboard } from '@uppy/react';

// Don't forget the CSS: core and the UI components + plugins you are using.
import '@uppy/core/dist/style.min.css';
import '@uppy/dashboard/dist/style.min.css';

const uppy = new Uppy({
  meta: { type: "avatar" },
  restrictions: {
    allowedFileTypes: ['.jpg', '.png'],
  },
  autoProceed: false
});
uppy.use(Tus, {
  endpoint: "http://localhost:8880/api/files/",
  chunkSize: 52428800,
});

uppy.on("complete", (result) => {
  const url = result.successful[0].uploadURL;
  // store.dispatch({
  //   type: 'SET_USER_AVATAR_URL',
  //   payload: { url },
  // })
  console.log(url);
});


const CreateJobPage: ExtendedNextPage = (props) => {
  React.useEffect(() => {
    return () => uppy.close();
  }, []);
	return (
		<div>
      <Dashboard uppy={uppy} hideUploadButton={true} plugins={["DragDrop"]} {...props} />
    </div>
	)
}

export async function getServerSideProps() {
	const	[resCustomer, resUser] = await Promise.all([listCustomers(), listCUsers()])
	if (isSuccessRequest(resCustomer) && isSuccessRequest(resUser)) {
    const customers = resCustomer.data.reduce((acc, obj) => {
      acc[obj.id] = obj;
      return acc;
    }, {});
    const users = resUser.data.reduce((acc, obj) => {
      acc[obj.id] = obj;
      return acc;
    }, {});
		const data = {
			customers,
      users,
      number_sub_job: NUMBER_ARRAY_10,
    }
		return {
			props: {
				data
			}
		}
	}
}

CreateJobPage.pageTitle = 'Tạo job'
CreateJobPage.activeLink = 'create_job'
CreateJobPage.breadcrumb = [
	{ text: "Tạo job", link: "/create_job" },
]

export default withAuth(CreateJobPage)
