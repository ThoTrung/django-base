import { Row, Col, ListGroup, Button, Modal, Form } from '@blueupcode/components'
import React, { useEffect } from 'react';
import type { ExtendedNextPage } from '@blueupcode/components/types'
import withAuth from 'components/auth/withAuth'
import { useDispatch, useSelector } from "react-redux";
import { useRouter } from 'next/router';
import { AShowLoading, AHideLoading } from 'store/common/actions'
import { useForm, Controller } from 'react-hook-form'
import DateTimePicker from 'react-datetime'
import * as yup from 'yup'
import Uppy from '@uppy/core';
import Tus from "@uppy/tus";
import { Dashboard } from '@uppy/react';

// Don't forget the CSS: core and the UI components + plugins you are using.
import '@uppy/core/dist/style.min.css';
import '@uppy/dashboard/dist/style.min.css';
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
import { DATETIME_FORMAT, DATE_FORMAT, TIME_FORMAT, NUMBER_ARRAY_10, ALLOW_FILE_TYPES } from 'constant/const';
import { getSCreateJob } from 'store/c2c/selectors';
import { swal } from 'components/sweetalert2/instance';
import { InputForm1 } from 'components/input_form/input_form1';


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

const validateObject:any  = {}

Object.keys(configData).forEach(key => {
  if (configData[key].validate) {
    validateObject[key] = configData[key].validate;
  }
});

const validationSchema = yup.object().shape(validateObject);

export type ICreateJobProps = {
  data: {
    customers: {[key: string]: ICustomer},
    users: {[key: string]: ICUser},
  }
}

const CreateJobPage: ExtendedNextPage<ICreateJobProps> = (props) => {
  const [serverErrors, setServerErrors] = React.useState<any>({});
  const [fileGUIDs, setFileGUIDs] = React.useState<string[]>([]);
  const [isRetry, setIsRetry] = React.useState<boolean>(false);

  const uppyTmp = new Uppy({
    id: 'create_job_uppy',
    meta: { type: "avatar" },
    autoProceed: false
  });
  uppyTmp.use(Tus, {
    endpoint: `/api/files/`,
    chunkSize: 52428800,
  });
  const [uppy, setUppy] = React.useState<Uppy>(uppyTmp);
  // const [selectedCreateJob, setSelectedCreaetJob] = React.useState<string[]>([]);
  
  
  const router = useRouter();
  const dispatch = useDispatch();
  const source = router.query?.source ?? 'manual';
  const selectedCreateJob = useSelector(getSCreateJob);

  React.useEffect(() => {
    return () => uppy.close();
  }, []);

  // useEffect(() => {
  //   const handleRouteChange = (url: string, { shallow }) => {
  //     console.log(uppy.close());
  //     console.log(
  //       `App is changing to ${url} ${
  //         shallow ? 'with' : 'without'
  //       } shallow routing`
  //     )
  //   }
 
  //   router.events.on('routeChangeStart', handleRouteChange)
 
  //   // If the component is unmounted, unsubscribe
  //   // from the event with the `off` method:
  //   return () => {
  //     router.events.off('routeChangeStart', handleRouteChange)
  //   }
  // }, [router])

  const defaultValue = {};
  Object.keys(configData).forEach(key => {
    defaultValue[key] = (source === 'auto' && selectedCreateJob && selectedCreateJob[key]) ? selectedCreateJob[key] : (configData[key].default_value ?? '');
  });

	const {control, handleSubmit, setValue, getValues, reset} = useForm<ICreateJob>({
    resolver: yupResolver(validationSchema),
		defaultValues: defaultValue,
  })

  const onChangeSelect = (id: string, key: string) => {
    console.log('onChangeSelect', id, key);
    switch(key) {
      case 'customer':
        if (id) {
          const customer = props.data.customers[id];
          setValue('expose', customer.expose);
          setValue('style', customer.style);
          setValue('customer_price', customer.customer_price);
          setValue('editor_price', customer.editor_price);
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
    try {
      dispatch(AShowLoading());
      const payload={}
      Object.keys(configData).forEach(key => {
        payload[key] = formData[key];
      });
      payload['source'] = source;

      if (source === 'auto') {
        payload['files'] = selectedCreateJob['files'] ?? [];
      } else {
        // Upload file and handle resume
        let resFiles = null;
        if (!isRetry) {
          resFiles = await uppy.upload();
        } else {
          resFiles = await uppy.retryAll();
        }
        let fileGUIDsTemp = fileGUIDs;
    
        if (resFiles.successful.length > 0) {
          resFiles.successful.forEach(item => {
            const urlElements = item.uploadURL.split('/').filter(n => n);
            fileGUIDsTemp.push(urlElements.pop());
          })
          setFileGUIDs(fileGUIDsTemp);
        }
        
        if (resFiles.failed.length === 0) {
          payload['files'] = fileGUIDsTemp;
          setIsRetry(false);
        } else {
          // Need to retry.
          setIsRetry(true);
          dispatch(AHideLoading());
          swal.fire('Upload files không thành công!', '', 'error');
          return;
        }
      }

      const res = await createJob(payload as ICreateJob);
      const swalTitle = 'Tạo Job thành công'
      if (isSuccessRequest(res)) {
        swalSuccess(swalTitle);
      } else { // Error: 4xx
        setServerErrors(res.data);
      }
    } catch(e) {
    } finally {
      dispatch(AHideLoading());
    }
  }

  const handleCancel = () => {
    console.log('handle cancel')
  }

  const handleFolderSelection = (event: React.ChangeEvent<HTMLInputElement>, key: string) => {
    const files = event.target.files;
    const acceptedFiles = [];
    uppy.cancelAll();
    let fileGeneratedIDsTmp:string[] = [];
    if (files && files.length > 0) {
      // Filter file
      for (let i = 0; i < files.length; ++i) {
        const file = files[i];
        // if (ALLOW_FILE_TYPES.includes(file.type)) {
          acceptedFiles.push(file);
          uppy.addFile({
            source: 'Manual',
            name: file.name,
            type: file.type,
            data: file,
          });
        // }
      }
      console.log('3333');
      setValue('folder_path', files[0].webkitRelativePath.split('/')[0]);
    }
    if (acceptedFiles.length > 0) {
      console.log('4444');
      setValue('file_number', acceptedFiles.length);
      delete serverErrors['folder_path'];
      setServerErrors({...serverErrors});
    } else {
      console.log('555');
      setValue('file_number', 0);
      setServerErrors({...serverErrors, folder_path: 'Thư mục không có file thỏa mãn, hãy chắc chắn rằng thư mục bạn đang chọn có các file .jpg, .png'})
    }
  };

	return (
    <>
    {Object.keys(props).length !== 0 && 
      <div className='d-flex'>
        <div className='w-xlg'>
          <Form onSubmit={handleSubmit(onSubmit, onErrors)} className="d-grid gap-3">
            <InputForm1
              configData={configData}
              control={control}
              handleFolderSelection={handleFolderSelection}
              onChangeSelect={onChangeSelect}
              data={props.data}
            />
            <div className="d-flex justify-content-end">
              <Button type="submit" variant="primary">{isRetry ? 'Tạo lại' : 'Tạo'}</Button>
              <Button variant="outline-secondary" onClick={handleCancel} className='ms-2'>Cancel</Button>
            </div>
          </Form>
        </div>
        {source !== 'auto' &&
          <div className='fr-1 maw-750 ms-3'>
            <Dashboard
              uppy={uppy}
              hideUploadButton={true}
              plugins={["DragDrop"]}
              width='100%'
              {...props}
            />
          </div>
        }
      </div>
    }
    </>
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
  return {
    props: {}
  }
}

CreateJobPage.pageTitle = 'Tạo job'
CreateJobPage.activeLink = 'create_job'
CreateJobPage.breadcrumb = [
	{ text: "Tạo job", link: "/create_job" },
]

export default withAuth(CreateJobPage)
