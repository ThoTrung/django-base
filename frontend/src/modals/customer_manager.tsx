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
  ICreateCustomer,
  ICustomer,
  createCustomers,
  updateCustomers,
  deleteCustomers
} from 'store/request/customer_manager'
import { DATETIME_FORMAT, DATE_FORMAT, TIME_FORMAT, DATE_FORMAT_DISPLAY } from 'constant/const';
import { string } from 'prop-types'

type Props = {
  show: boolean;
  selectedCustomer: ICustomer | null;
  handleShow: (show:boolean) => void;
  refreshData: () => void;
}

const validationSchema = yup.object().shape({
	code: yup.string().required('Bạn cần nhập mã khách hàng'),
	name: yup.string().required('Bạn cần tên khách hàng'),
  email: yup.string().required('Bạn cần nhập Email'),
  expose: yup.string().required('Bạn cần nhập số Expose'),
  style: yup.string().required('Bạn cần nhập style cố định'),
  pay_name: yup.string().required('Bạn cần nhập tên thanh toán'),
  // phone_number
  // contact_channel
})

const CustomerManagerModal = (props: Props) => {
  const [readOnly, setReadOnly] = React.useState<boolean>(false);
  const [show, setShow] = React.useState<boolean>(props.show);
  const [formTitle, setFormTitle] = React.useState<string>('');
  const [serverErrors, setServerErrors] = React.useState<any>({});
  
  const dispatch = useDispatch();
  const isUpdateMode = props.selectedCustomer !== null;
  const defaultPasswordNotUse = isUpdateMode ? 'defaultPasswordNotUse' : '';

  const {control, handleSubmit} = useForm<ICreateCustomer>({
    resolver: yupResolver(validationSchema),
		defaultValues: {
      code: (props.selectedCustomer ? props.selectedCustomer.code : ''),
			name: (props.selectedCustomer ? props.selectedCustomer.name : ''),
      email: (props.selectedCustomer ? props.selectedCustomer.email : ''),
      expose: (props.selectedCustomer ? props.selectedCustomer.expose : ''),
      style: (props.selectedCustomer ? props.selectedCustomer.style : ''),
      pay_name: (props.selectedCustomer ? props.selectedCustomer.pay_name : ''),
      phone_number: (props.selectedCustomer ? props.selectedCustomer.phone_number : ''),
      contact_channel: (props.selectedCustomer ? props.selectedCustomer.contact_channel : ''),
      state: (props.selectedCustomer ? props.selectedCustomer.state : ''),
      deadline: (props.selectedCustomer && props.selectedCustomer.deadline ? props.selectedCustomer.deadline.substring(0, 5) : '00:00'),
      // description: (props.selectedCustomer ? props.selectedCustomer.description : ''),
      customer_price: (props.selectedCustomer ? props.selectedCustomer.customer_price : 0),
      editor_price: (props.selectedCustomer ? props.selectedCustomer.editor_price : 0),
		},
  })

  const handleDelete = async() => {
    if (props.selectedCustomer !== null) {
      const result = await swalDelete();
      if (result.isConfirmed) {
        dispatch(AShowLoading());
        const res = await deleteCustomers(props.selectedCustomer.id)
        if (isSuccessRequest(res)) {
          props.refreshData();
          handleHide();
          swalDeleteSuccess('Khách hàng');
        }
        dispatch(AHideLoading());
      }
    }
  }

  const onSubmit = async (formData: ICreateCustomer) => {
    dispatch(AShowLoading());
    let deadline = formData.deadline ? formData.deadline : '';
    if (typeof formData.deadline !== 'string') {
      deadline = deadline.format(TIME_FORMAT);
    }
    const payload={
      code: formData.code,
      name: formData.name,
      email: formData.email,
      expose: formData.expose,
      style: formData.style,
      pay_name: formData.pay_name,
      phone_number: formData.phone_number,
      contact_channel: formData.contact_channel,
      state: formData.state,
      deadline: deadline,
      customer_price: formData.customer_price,
      editor_price: formData.editor_price,
      // description: formData.description,
    }
    // if (!isUpdateMode || changePassword) {
    // }
    let res = null;
    let swalTitle = '';
    if (props.selectedCustomer === null) {
      res = await createCustomers(payload);
      swalTitle = 'Thêm khách hàng thành công.'
    } else {
      res = await updateCustomers(props.selectedCustomer.id, payload);
      swalTitle = 'Cập nhật khách hàng thành công.'
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
    let formTitleTemp = "Thêm khách hàng"
    if (props.selectedCustomer !== null) {
      formTitleTemp = "Cập nhật khách hàng"
    }
    setReadOnly(readOnlyTemp);
    setFormTitle(formTitleTemp);
  }, [props.selectedCustomer])

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
              name="code"
              control={control}
              render={({ field, fieldState: { invalid, error } }) => (
                <Form.Group controlId="code">
                  <Row className='mt-2'>
                    <Col sm={5}>
                      <Form.Label>Mã KH *:</Form.Label>
                    </Col>
                    <Col sm={7}>
                      <Form.Control
                        disabled={readOnly}
                        isInvalid={invalid || !!serverErrors['code']}
                        {...field}
                      />
                      {invalid && <Form.Control.Feedback type="invalid">{error?.message}</Form.Control.Feedback>}
                      {!!serverErrors['code'] && <Form.Control.Feedback type="invalid">{serverErrors['code']}</Form.Control.Feedback>}
                    </Col>
                  </Row>
                </Form.Group>
              )}
            />
            <Controller
              name="name"
              control={control}
              render={({ field, fieldState: { invalid, error } }) => (
                <Form.Group controlId="name">
                  <Row className='mt-2'>
                    <Col sm={5}>
                      <Form.Label>Tên KH *:</Form.Label>
                    </Col>
                    <Col sm={7}>
                      <Form.Control
                        disabled={readOnly}
                        isInvalid={invalid || !!serverErrors['name']}
                        {...field}
                      />
                      {invalid && <Form.Control.Feedback type="invalid">{error?.message}</Form.Control.Feedback>}
                      {!!serverErrors['name'] && <Form.Control.Feedback type="invalid">{serverErrors['name']}</Form.Control.Feedback>}
                    </Col>
                  </Row>
                </Form.Group>
              )}
            />
            <Controller
              name="email"
              control={control}
              render={({ field, fieldState: { invalid, error } }) => (
                <Form.Group controlId="email">
                  <Row className='mt-2'>
                    <Col sm={5}>
                      <Form.Label>Email *:</Form.Label>
                    </Col>
                    <Col sm={7}>
                      <Form.Control
                        type='email'
                        disabled={readOnly}
                        isInvalid={invalid || !!serverErrors['email']}
                        {...field}
                      />
                      {invalid && <Form.Control.Feedback type="invalid">{error?.message}</Form.Control.Feedback>}
                      {!!serverErrors['email'] && <Form.Control.Feedback type="invalid">{serverErrors['email']}</Form.Control.Feedback>}
                    </Col>
                  </Row>
                </Form.Group>
              )}
            />
            <Controller
              name="expose"
              control={control}
              render={({ field, fieldState: { invalid, error } }) => (
                <Form.Group controlId="expose">
                  <Row className='mt-2'>
                    <Col sm={5}>
                      <Form.Label>Số expose *:</Form.Label>
                    </Col>
                    <Col sm={7}>
                      <Form.Control
                        disabled={readOnly}
                        isInvalid={invalid || !!serverErrors['expose']}
                        {...field}
                      />
                      {invalid && <Form.Control.Feedback type="invalid">{error?.message}</Form.Control.Feedback>}
                      {!!serverErrors['expose'] && <Form.Control.Feedback type="invalid">{serverErrors['expose']}</Form.Control.Feedback>}
                    </Col>
                  </Row>
                </Form.Group>
              )}
            />
            <Controller
              name="style"
              control={control}
              render={({ field, fieldState: { invalid, error } }) => (
                <Form.Group controlId="style">
                  <Row className='mt-2'>
                    <Col sm={5}>
                      <Form.Label>Style cố định *:</Form.Label>
                    </Col>
                    <Col sm={7}>
                      <Form.Control
                        as="textarea"
                        disabled={readOnly}
                        isInvalid={invalid || !!serverErrors['style']}
                        {...field}
                      />
                      {invalid && <Form.Control.Feedback type="invalid">{error?.message}</Form.Control.Feedback>}
                      {!!serverErrors['style'] && <Form.Control.Feedback type="invalid">{serverErrors['style']}</Form.Control.Feedback>}
                    </Col>
                  </Row>
                </Form.Group>
              )}
            />
            <Controller
              name="pay_name"
              control={control}
              render={({ field, fieldState: { invalid, error } }) => (
                <Form.Group controlId="pay_name">
                  <Row className='mt-2'>
                    <Col sm={5}>
                      <Form.Label>Tên thanh toán *:</Form.Label>
                    </Col>
                    <Col sm={7}>
                      <Form.Control
                        disabled={readOnly}
                        isInvalid={invalid || !!serverErrors['pay_name']}
                        {...field}
                      />
                      {invalid && <Form.Control.Feedback type="invalid">{error?.message}</Form.Control.Feedback>}
                      {!!serverErrors['pay_name'] && <Form.Control.Feedback type="invalid">{serverErrors['pay_name']}</Form.Control.Feedback>}
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
                    <Col sm={5}>
                      <Form.Label>Số ĐT:</Form.Label>
                    </Col>
                    <Col sm={7}>
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
            <Controller
              name="contact_channel"
              control={control}
              render={({ field, fieldState: { invalid, error } }) => (
                <Form.Group controlId="contact_channel">
                  <Row className='mt-2'>
                    <Col sm={5}>
                      <Form.Label>Kênh liên lạc:</Form.Label>
                    </Col>
                    <Col sm={7}>
                      <Form.Control
                        disabled={readOnly}
                        isInvalid={invalid || !!serverErrors['contact_channel']}
                        {...field}
                      />
                      {invalid && <Form.Control.Feedback type="invalid">{error?.message}</Form.Control.Feedback>}
                      {!!serverErrors['contact_channel'] && <Form.Control.Feedback type="invalid">{serverErrors['contact_channel']}</Form.Control.Feedback>}
                    </Col>
                  </Row>
                </Form.Group>
              )}
            />
            <Controller
              name="state"
              control={control}
              render={({ field, fieldState: { invalid, error } }) => (
                <Form.Group controlId="state">
                  <Row className='mt-2'>
                    <Col sm={5}>
                      <Form.Label>Múi giờ/bang:</Form.Label>
                    </Col>
                    <Col sm={7}>
                      <Form.Control
                        disabled={readOnly}
                        isInvalid={invalid || !!serverErrors['state']}
                        {...field}
                      />
                      {invalid && <Form.Control.Feedback type="invalid">{error?.message}</Form.Control.Feedback>}
                      {!!serverErrors['state'] && <Form.Control.Feedback type="invalid">{serverErrors['state']}</Form.Control.Feedback>}
                    </Col>
                  </Row>
                </Form.Group>
              )}
            />

            <Controller
              name="deadline"
              control={control}
              render={({ field, fieldState: { invalid, error } }) => (
                <Form.Group controlId="deadline">
                  <Row className='mt-2'>
                    <Col sm={5}>
                      <Form.Label>Deadline:</Form.Label>
                    </Col>
                    <Col sm={7}>

                      <DateTimePicker
                        closeOnSelect
                        dateFormat={false}
                        timeFormat={TIME_FORMAT}
                        onChange={(date) => field.onChange(date)}
                        value={field.value}
                        initialViewMode={'time'}
                      />
                      {invalid && <Form.Control.Feedback type="invalid">{error?.message}</Form.Control.Feedback>}
                      {!!serverErrors['deadline'] && <Form.Control.Feedback type="invalid">{serverErrors['deadline']}</Form.Control.Feedback>}
                    </Col>
                  </Row>
                </Form.Group>
              )}
            />
            <Controller
              name="customer_price"
              control={control}
              render={({ field, fieldState: { invalid, error } }) => (
                <Form.Group controlId="customer_price">
                  <Row className='mt-2'>
                    <Col sm={5}>
                      <Form.Label>Giá KH:</Form.Label>
                    </Col>
                    <Col sm={7}>
                      <Form.Control
                        type='number'
                        step="any"
                        disabled={readOnly}
                        isInvalid={invalid || !!serverErrors['customer_price']}
                        min={0}
                        {...field}
                      />
                      {invalid && <Form.Control.Feedback type="invalid">{error?.message}</Form.Control.Feedback>}
                      {!!serverErrors['customer_price'] && <Form.Control.Feedback type="invalid">{serverErrors['customer_price']}</Form.Control.Feedback>}
                    </Col>
                  </Row>
                </Form.Group>
              )}
            />

            <Controller
              name="editor_price"
              control={control}
              render={({ field, fieldState: { invalid, error } }) => (
                <Form.Group controlId="editor_price">
                  <Row className='mt-2'>
                    <Col sm={5}>
                      <Form.Label>Giá editor:</Form.Label>
                    </Col>
                    <Col sm={7}>
                      <Form.Control
                        type='number'
                        step="any"
                        disabled={readOnly}
                        isInvalid={invalid || !!serverErrors['editor_price']}
                        min={0}
                        {...field}
                      />
                      {invalid && <Form.Control.Feedback type="invalid">{error?.message}</Form.Control.Feedback>}
                      {!!serverErrors['editor_price'] && <Form.Control.Feedback type="invalid">{serverErrors['editor_price']}</Form.Control.Feedback>}
                    </Col>
                  </Row>
                </Form.Group>
              )}
            />
            
          </Modal.Body>
          <Modal.Footer>
            <Button type="submit" variant="primary">{props.selectedCustomer ? 'Cập nhật' : 'Tạo mới'}</Button>
            <Button variant="outline-secondary" onClick={handleHide}>Cancel</Button>
            {props.selectedCustomer && <Button variant="outline-danger" onClick={handleDelete}>Xóa</Button>}
          </Modal.Footer>
        </Form>
      </Modal>
			{/* END Modal */}
		</>
	)
}

export default CustomerManagerModal;