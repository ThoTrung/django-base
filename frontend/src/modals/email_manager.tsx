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
  deleteEmails
} from 'store/request/email_manager'
import { DATETIME_FORMAT, DATE_FORMAT, TIME_FORMAT, DATE_FORMAT_DISPLAY } from 'constant/const';
import { string } from 'prop-types'

type Props = {
  show: boolean;
  selectedEmail: IEmail | null;
  handleShow: (show:boolean) => void;
  refreshData: () => void;
}

const validationSchema = yup.object().shape({
	primary_email: yup.string().required('Bạn cần nhập email'),
	password: yup.string().required('Bạn cần password'),
  first_name: yup.string().required('Bạn cần nhập họ'),
  last_name: yup.string().required('Bạn cần nhập tên'),
  // phone_number: yup.string().required('Bạn cần nhập style cố định'),
  // pay_name: yup.string().required('Bạn cần nhập tên thanh toán'),
  // phone_number
  // contact_channel
})

const EmailManagerModal = (props: Props) => {
  const [readOnly, setReadOnly] = React.useState<boolean>(false);
  const [show, setShow] = React.useState<boolean>(props.show);
  const [formTitle, setFormTitle] = React.useState<string>('');
  const [serverErrors, setServerErrors] = React.useState<any>({});
  
  const dispatch = useDispatch();
  const isUpdateMode = props.selectedEmail !== null;
  // const defaultPasswordNotUse = isUpdateMode ? 'defaultPasswordNotUse' : '';

  const {control, handleSubmit} = useForm<ICreateEmail>({
    resolver: yupResolver(validationSchema),
		defaultValues: {
      primary_email: (props.selectedEmail ? props.selectedEmail.primary_email : ''),
			password: (props.selectedEmail ? props.selectedEmail.password : ''),
      first_name: (props.selectedEmail ? props.selectedEmail.first_name : ''),
      last_name: (props.selectedEmail ? props.selectedEmail.last_name : ''),
      phone_number: (props.selectedEmail ? props.selectedEmail.phone_number : ''),
      // description: (props.selectedEmail ? props.selectedEmail.description : ''),
		},
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
          swalDeleteSuccess('Khách hàng');
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
                  <Row className='mt-2'>
                    <Col sm={3}>
                      <Form.Label>Email *:</Form.Label>
                    </Col>
                    <Col sm={5}>
                      <Form.Control
                        disabled={readOnly}
                        isInvalid={invalid || !!serverErrors['primary_email']}
                        {...field}
                      />
                      {invalid && <Form.Control.Feedback type="invalid">{error?.message}</Form.Control.Feedback>}
                      {!!serverErrors['primary_email'] && <Form.Control.Feedback type="invalid">{serverErrors['primary_email']}</Form.Control.Feedback>}
                    </Col>
                    <Col sm={4}>
                      <Form.Label>@domain.com</Form.Label>
                    </Col>
                  </Row>
                </Form.Group>
              )}
            />
            
            <Controller
              name="password"
              control={control}
              render={({ field, fieldState: { invalid, error } }) => (
                <Form.Group controlId="password">
                  <Row className='mt-2'>
                    <Col sm={3}>
                      <Form.Label>Password *:</Form.Label>
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
                  <Row className='mt-2'>
                    <Col sm={3}>
                      <Form.Label>Họ *:</Form.Label>
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
                  <Row className='mt-2'>
                    <Col sm={3}>
                      <Form.Label>Tên *:</Form.Label>
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
                  <Row className='mt-2'>
                    <Col sm={3}>
                      <Form.Label>Số điện thoại :</Form.Label>
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