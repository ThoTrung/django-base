import React from 'react'
import { Row, Col, ListGroup, Button, Modal, Form } from '@blueupcode/components'
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
  ICreateEmail,
  IEmail,
  createEmails,
  updateEmails,
  deleteEmails,
  IEmailSetting
} from 'store/request/email_manager'
import { DATETIME_FORMAT, DATE_FORMAT, TIME_FORMAT, DATE_FORMAT_DISPLAY } from 'constant/const';
import { string } from 'prop-types'



const configData = {
	primary_email: {
		display_name: 'Email *:',
    validate: yup.string().required('Bạn cần nhập email'),
    default_value: '',
    disable_on_edit: true,
    extra_data: {
      type: 'LABLE',
      width: 4,
      data: '',
    }
    // readonly: true,
	},
	password: {
		display_name: 'Password *:',
    validate: yup.string().required('Bạn cần nhập mật khẩu mặc định cho Email này'),
    default_value: '',
	},
	first_name: {
		display_name: 'Họ *:',
    validate: yup.string().required('Bạn cần nhập Họ'),
    default_value: '',
	},
	last_name: {
		display_name: 'Tên *:',
    validate: yup.string().required('Bạn cần nhập Tên'),
    default_value: '',
	},
	phone_number: {
		display_name: 'Tên *:',
    default_value: '',
	},
}

const validateObject:any  = {}

Object.keys(configData).forEach(key => {
  if (configData[key].validate) {
    validateObject[key] = configData[key].validate;
  }
});

const validationSchema = yup.object().shape(validateObject);


type Props = {
  show: boolean;
  selectedEmail: IEmail | null;
  handleShow: (show:boolean) => void;
  refreshData: () => void;
  emailSetting: IEmailSetting;
}


const EmailManagerModal = (props: Props) => {
  const [readOnly, setReadOnly] = React.useState<boolean>(false);
  const [show, setShow] = React.useState<boolean>(props.show);
  const [formTitle, setFormTitle] = React.useState<string>('');
  const [serverErrors, setServerErrors] = React.useState<any>({});
  
  const dispatch = useDispatch();
  const isUpdateMode = props.selectedEmail !== null;
  // const defaultPasswordNotUse = isUpdateMode ? 'defaultPasswordNotUse' : '';

  const defaultValue = {};
  Object.keys(configData).forEach(key => {
    defaultValue[key] = (source === 'auto' && selectedCreateJob && selectedCreateJob[key]) ? selectedCreateJob[key] : (configData[key].default_value ?? '');
  });

	const {control, handleSubmit, setValue, getValues, reset} = useForm<ICreateJob>({
    resolver: yupResolver(validationSchema),
		defaultValues: defaultValue,
  })

  const handleDelete = async() => {
    if (props.selectedEmail !== null) {
      const result = await swalDelete();
      if (result.isConfirmed) {
        dispatch(AShowLoading());
        const res = await deleteEmails(props.selectedEmail.id)
        if (isSuccessRequest(res)) {
          props.refreshData();
          handleHide();
          swalDeleteSuccess('Email');
        }
        dispatch(AHideLoading());
      }
    }
  }

  const onSubmit = async (formData: ICreateEmail) => {
    dispatch(AShowLoading());
    const payload={
      primary_email: formData.primary_email,
      password: formData.password,
      first_name: formData.first_name,
      last_name: formData.last_name,
      phone_number: formData.phone_number,
      // description: formData.description,
    }
    // if (!isUpdateMode || changePassword) {
    // }
    let res = null;
    let swalTitle = '';
    if (props.selectedEmail === null) {
      payload['primary_email'] = `${payload['primary_email']}@${props.emailSetting.domain}`;
      res = await createEmails(payload);
      swalTitle = 'Thêm Email thành công.'
    } else {
      res = await updateEmails(props.selectedEmail.id, payload);
      swalTitle = 'Cập nhật Email thành công.'
    }
    if (isSuccessRequest(res)) {
      props.refreshData();
      handleHide();
      swalSuccess(swalTitle);
    } else { // Error: 4xx
      setServerErrors(res.data);
    }
    dispatch(AHideLoading());
  }

  const handleHide = () => {
    setShow(false);
    setTimeout(() => {
      props.handleShow(false)
    }, 300);
  }

  React.useEffect(() => {
    let readOnlyTemp = false;
    let formTitleTemp = "Thêm Email"
    if (props.selectedEmail !== null) {
      formTitleTemp = "Cập nhật Email"
    }
    setReadOnly(readOnlyTemp);
    setFormTitle(formTitleTemp);
  }, [props.selectedEmail])

	return (
		<>
      <Modal
        show={show}
        onHide={handleHide}
        backdrop="static"
        keyboard={false}
        // size='xl'
        // fullscreen={true}
      >
        <Form onSubmit={handleSubmit(onSubmit)} className="d-grid gap-3">
          <Modal.Header>
            <Modal.Title> {formTitle} </Modal.Title>
            <Button icon variant="label-danger" onClick={handleHide}>
              <FontAwesomeIcon icon={faTimes} />
            </Button>
          </Modal.Header>
          <Modal.Body>

            <Controller
              name="primary_email"
              control={control}
              render={({ field, fieldState: { invalid, error } }) => (
                <Form.Group controlId="primary_email">
                  <Row className='mt-2 align-items-center'>
                    <Col sm={3}>
                      <Form.Label className='mb-0'>Email *:</Form.Label>
                    </Col>
                    <Col sm={props.selectedEmail ? 9 : 5}>
                      <Form.Control
                        disabled={!!props.selectedEmail}
                        isInvalid={invalid || !!serverErrors['primary_email']}
                        {...field}
                      />
                      {invalid && <Form.Control.Feedback type="invalid">{error?.message}</Form.Control.Feedback>}
                      {!!serverErrors['primary_email'] && <Form.Control.Feedback type="invalid">{serverErrors['primary_email']}</Form.Control.Feedback>}
                    </Col>
                    {!props.selectedEmail &&
                      <Col sm={4}>
                        <Form.Label className='mb-0'>@{props.emailSetting?.domain}</Form.Label>
                      </Col>
                    }
                  </Row>
                </Form.Group>
              )}
            />
            
            <Controller
              name="password"
              control={control}
              render={({ field, fieldState: { invalid, error } }) => (
                <Form.Group controlId="password">
                  <Row className='mt-2 align-items-center'>
                    <Col sm={3}>
                      <Form.Label className='mb-0'>Password *:</Form.Label>
                    </Col>
                    <Col sm={5}>
                      <Form.Control
                        disabled={readOnly}
                        isInvalid={invalid || !!serverErrors['password']}
                        {...field}
                      />
                      {invalid && <Form.Control.Feedback type="invalid">{error?.message}</Form.Control.Feedback>}
                      {!!serverErrors['password'] && <Form.Control.Feedback type="invalid">{serverErrors['password']}</Form.Control.Feedback>}
                    </Col>
                  </Row>
                </Form.Group>
              )}
            />
            
            <Controller
              name="first_name"
              control={control}
              render={({ field, fieldState: { invalid, error } }) => (
                <Form.Group controlId="first_name">
                  <Row className='mt-2 align-items-center'>
                    <Col sm={3}>
                      <Form.Label className='mb-0'>Họ *:</Form.Label>
                    </Col>
                    <Col sm={5}>
                      <Form.Control
                        // type='email'
                        disabled={readOnly}
                        isInvalid={invalid || !!serverErrors['first_name']}
                        {...field}
                      />
                      {invalid && <Form.Control.Feedback type="invalid">{error?.message}</Form.Control.Feedback>}
                      {!!serverErrors['first_name'] && <Form.Control.Feedback type="invalid">{serverErrors['first_name']}</Form.Control.Feedback>}
                    </Col>
                  </Row>
                </Form.Group>
              )}
            />
            <Controller
              name="last_name"
              control={control}
              render={({ field, fieldState: { invalid, error } }) => (
                <Form.Group controlId="last_name">
                  <Row className='mt-2 align-items-center'>
                    <Col sm={3}>
                      <Form.Label className='mb-0'>Tên *:</Form.Label>
                    </Col>
                    <Col sm={5}>
                      <Form.Control
                        disabled={readOnly}
                        isInvalid={invalid || !!serverErrors['last_name']}
                        {...field}
                      />
                      {invalid && <Form.Control.Feedback type="invalid">{error?.message}</Form.Control.Feedback>}
                      {!!serverErrors['last_name'] && <Form.Control.Feedback type="invalid">{serverErrors['last_name']}</Form.Control.Feedback>}
                    </Col>
                  </Row>
                </Form.Group>
              )}
            />
            <Controller
              name="phone_number"
              control={control}
              render={({ field, fieldState: { invalid, error } }) => (
                <Form.Group controlId="phone_number">
                  <Row className='mt-2 align-items-center'>
                    <Col sm={3}>
                      <Form.Label className='mb-0'>Số điện thoại :</Form.Label>
                    </Col>
                    <Col sm={5}>
                      <Form.Control
                        disabled={readOnly}
                        isInvalid={invalid || !!serverErrors['phone_number']}
                        {...field}
                      />
                      {invalid && <Form.Control.Feedback type="invalid">{error?.message}</Form.Control.Feedback>}
                      {!!serverErrors['phone_number'] && <Form.Control.Feedback type="invalid">{serverErrors['phone_number']}</Form.Control.Feedback>}
                    </Col>
                  </Row>
                </Form.Group>
              )}
            />
          </Modal.Body>
          <Modal.Footer>
            <Button type="submit" variant="primary">{props.selectedEmail ? 'Cập nhật' : 'Tạo mới'}</Button>
            <Button variant="outline-secondary" onClick={handleHide}>Cancel</Button>
            {props.selectedEmail && <Button variant="outline-danger" onClick={handleDelete}>Xóa</Button>}
          </Modal.Footer>
        </Form>
      </Modal>
			{/* END Modal */}
		</>
	)
}

export default EmailManagerModal;