import React from 'react'
import { Row, Col, ListGroup, Button, Modal, Form } from '@blueupcode/components'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faTimes } from '@fortawesome/free-solid-svg-icons'
import { modalType, newType, updateType, detailType } from 'constant/type'
import { useDispatch } from "react-redux";
import { AShowLoading, AHideLoading } from 'store/common/actions'
import { useForm, Controller } from 'react-hook-form'
import * as yup from 'yup'
import { yupResolver } from '@hookform/resolvers/yup'
import { isSuccessRequest } from 'store/request/helper'
import { swalSuccess, swalDelete, swalDeleteSuccess } from 'components/swals/swals'
import {
  ICreateCUser,
  ICUser,
  IUserGroups,
  IUserBanks,
  STATUS_CHOICES,
  GENDER_CHOICES,
  createCusers,
  updateCusers,
  deleteCusers,
} from 'store/request/user_manager';

type Props = {
  show: boolean;
  selectedCUser: ICUser | null;
  handleShow: (show:boolean) => void;
  userBanks: {
    [key: number]: IUserBanks
  },
  userGroups: {
    [key: number]: IUserGroups
  },
  refreshData: () => void;
}

interface IRegisterCUser extends ICreateCUser {
  password1: string,
  password2: string,
  group: number,
}

const validationSchema = yup.object().shape({
	name: yup.string().required('Bạn cần nhập Mã NV'),
  email: yup.string().required('Bạn cần nhập Email'),
  full_name: yup.string().required('Bạn cần nhập Họ và tên'),
  password1: yup.string().min(6, 'Password cần tối thiểu 6 kí tự').required('Đây là trường bắt buộc'),
	password2: yup
		.string()
		.min(6, 'Password cần tối thiểu 6 kí tự')
		.oneOf([yup.ref('password1')], 'Password không giống nhau')
		.required('Nhập lại password'),
  // gender: yup.string().required('Bạn cần nhập Giới tính'), // Set default
  // phone_number: yup.string().required('Bạn cần nhập Số ĐT'),
  // address: yup.string().required('Bạn cần nhập Địa chỉ'),
  // bank: yup.string().required('Bạn cần nhập tên Ngân Hàng'),
  // bank_number: yup.string().required('Bạn cần nhập Số tk'),
  // status: yup.string().required('Bạn cần nhập Trạng thái'), // set default
  group: yup.number().min(1, 'Bạn cần nhập Role').required('Bạn cần nhập Role'), // set default
})

const UserManagerModal = (props: Props) => {
  const [readOnly, setReadOnly] = React.useState<boolean>(false);
  const [show, setShow] = React.useState<boolean>(props.show);
  const [formTitle, setFormTitle] = React.useState<string>('');
  const [serverErrors, setServerErrors] = React.useState<any>({});
  const [changePassword, setChangePassword] = React.useState<boolean>(false);
  
  const dispatch = useDispatch();
  const isUpdateMode = props.selectedCUser !== null;
  const defaultPasswordNotUse = isUpdateMode ? 'defaultPasswordNotUse' : '';

  const {control, handleSubmit} = useForm<IRegisterCUser>({
    resolver: yupResolver(validationSchema),
		defaultValues: {
			name: (props.selectedCUser ? props.selectedCUser.name : ''),
      email: (props.selectedCUser ? props.selectedCUser.email : ''),
      full_name: (props.selectedCUser ? props.selectedCUser.full_name : ''),
      gender: (props.selectedCUser ? props.selectedCUser.gender : 'M'),
      phone_number: (props.selectedCUser ? props.selectedCUser.phone_number : ''),
      address: (props.selectedCUser ? props.selectedCUser.address : ''),
      bank: (props.selectedCUser ? props.selectedCUser.bank : 0),
      bank_number: (props.selectedCUser ? props.selectedCUser.bank_number : ''),
      status: (props.selectedCUser ? props.selectedCUser.status : 'W'),
      group: (props.selectedCUser  && props.selectedCUser.groups.length > 0 ? props.selectedCUser.groups[0] : 0),
      password1: defaultPasswordNotUse,
      password2: defaultPasswordNotUse,
		},
  })

  const handleDelete = async() => {
    if (props.selectedCUser !== null) {
      const result = await swalDelete();
      if (result.isConfirmed) {
        dispatch(AShowLoading());
        const res = await deleteCusers(props.selectedCUser.id)
        if (isSuccessRequest(res)) {
          props.refreshData();
          handleHide();
          swalDeleteSuccess('User');
        }
        dispatch(AHideLoading());
      }
    }
  }

  const onSubmit = async (formData: IRegisterCUser) => {
    dispatch(AShowLoading());
    const payload={
      name: formData.name,
      email: formData.email,
      full_name: formData.full_name,
      gender: formData.gender,
      phone_number: formData.phone_number,
      address: formData.address,
      bank: (formData.bank && formData.bank > 0) ? formData.bank : null,
      bank_number: formData.bank_number,
      status: formData.status,
      groups: [formData.group],
      password: '',
    }
    // if (!isUpdateMode || changePassword) {
    payload['password'] = formData.password1
    // }
    let res = null;
    let swalTitle = '';
    if (props.selectedCUser === null) {
      res = await createCusers(payload);
      swalTitle = 'Thêm User thành công.'
    } else {
      res = await updateCusers(props.selectedCUser.id, payload);
      swalTitle = 'Cập nhật User thành công.'
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
    let formTitleTemp = "Thêm User"
    if (props.selectedCUser !== null) {
      formTitleTemp = "Cập nhật User"
    }
    setReadOnly(readOnlyTemp);
    setFormTitle(formTitleTemp);
  }, [props.selectedCUser])

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
              name="name"
              control={control}
              render={({ field, fieldState: { invalid, error } }) => (
                <Form.Group controlId="name">
                  <Row className='mt-2'>
                    <Col sm={5}>
                      <Form.Label>Mã nhân viên *:</Form.Label>
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
              name="group"
              control={control}
              render={({ field, fieldState: { invalid, error } }) => (
                <Form.Group>
                  <Row className='mt-2'>
                    <Col sm={5}>
                      <Form.Label>Role *:</Form.Label>
                    </Col>
                    <Col sm={7}>
                      <Form.Select
                        isInvalid={invalid }
                        {...field}
                      >
                        <option value={0}></option>
                        {Object.keys(props.userGroups).map((key) => (
                          <option key={key} value={key}>{props.userGroups[parseInt(key)].name}</option>
                        ))}
                      </Form.Select>
                      {invalid && <Form.Control.Feedback type="invalid">{error?.message}</Form.Control.Feedback>}
                    </Col>
                  </Row>
                </Form.Group>
              )}
            />
            <Controller
              name="full_name"
              control={control}
              render={({ field, fieldState: { invalid, error } }) => (
                <Form.Group controlId="full_name">
                  <Row className='mt-2'>
                    <Col sm={5}>
                      <Form.Label>Họ và tên *:</Form.Label>
                    </Col>
                    <Col sm={7}>
                      <Form.Control
                        disabled={readOnly}
                        isInvalid={invalid || !!serverErrors['full_name']}
                        {...field}
                      />
                      {invalid && <Form.Control.Feedback type="invalid">{error?.message}</Form.Control.Feedback>}
                      {!!serverErrors['full_name'] && <Form.Control.Feedback type="invalid">{serverErrors['full_name']}</Form.Control.Feedback>}
                    </Col>
                  </Row>
                </Form.Group>
              )}
            />
            <Controller
              name="password1"
              control={control}
              render={({ field, fieldState: { invalid, error } }) => (
                <Form.Group controlId="password1">
                  <Row className='mt-2'>
                    <Col sm={5}>
                      <Form.Label>Mật khẩu *:</Form.Label>
                    </Col>
                      {!isUpdateMode ? (
                        <Col sm={5}>
                          <Form.Control
                            type="password"
                            isInvalid={invalid}
                            {...field}
                          />
                          {invalid && <Form.Control.Feedback type="invalid">{error?.message}</Form.Control.Feedback>}
                        </Col>
                      ):(
                        <>
                          {!changePassword ? (
                            <Col sm={5}>
                              <Button variant="primary" onClick={() => setChangePassword(true)}>Đổi Mật khẩu</Button>
                            </Col>
                          ) :(
                            <>
                              <Col sm={5}>
                                <Form.Control
                                  type="password"
                                  isInvalid={invalid}
                                  {...field}
                                />
                                {invalid && <Form.Control.Feedback type="invalid">{error?.message}</Form.Control.Feedback>}
                              </Col>
                              <Col sm={2}>
                                <Button variant="outline-secondary" onClick={() => setChangePassword(false)}>Cancel</Button>
                              </Col>
                            </>
                          )}
                        </>
                      )}
                  </Row>
                </Form.Group>
              )}
            />
            {(!isUpdateMode || changePassword) && <Controller
                name="password2"
                control={control}
                render={({ field, fieldState: { invalid, error } }) => (
                  <Form.Group controlId="password2">
                    <Row className='mt-2'>
                      <Col sm={5}>
                        <Form.Label>Xác nhận mật khẩu *:</Form.Label>
                      </Col>
                      <Col sm={5}>
                        <Form.Control
                          type="password"
                          isInvalid={invalid}
                          {...field}
                        />
                        {invalid && <Form.Control.Feedback type="invalid">{error?.message}</Form.Control.Feedback>}
                      </Col>
                    </Row>
                  </Form.Group>
                )}
              />
            }

            <Form.Group>
              <Row className='mt-2'>
                <Col sm={5}>
                  <Form.Label>Giới tính</Form.Label>
                </Col>
                <Col sm={7} className='d-flex'>
                  {Object.keys(GENDER_CHOICES).map((key) => (
                    <Controller
                    key={key}
                    name="gender"
                    control={control}
                    render={({ field: {value, onChange}, fieldState: { invalid, error } }) => (
                        <Form.Check
                          className='me-4'
                          type='radio'
                          id={`gender-${key}`}
                          value={key}
                          name='gender-radio'
                          checked={value == key ? true : false}
                          label={GENDER_CHOICES[key]}
                          onChange={(e) => onChange(e.target.value)}
                        />
                        )}
                      />
                  ))}
                </Col>
              </Row>
            </Form.Group>

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
              name="address"
              control={control}
              render={({ field, fieldState: { invalid, error } }) => (
                <Form.Group controlId="address">
                  <Row className='mt-2'>
                    <Col sm={5}>
                      <Form.Label>Địa chỉ:</Form.Label>
                    </Col>
                    <Col sm={7}>
                      <Form.Control
                        disabled={readOnly}
                        isInvalid={invalid || !!serverErrors['address']}
                        {...field}
                      />
                      {invalid && <Form.Control.Feedback type="invalid">{error?.message}</Form.Control.Feedback>}
                      {!!serverErrors['address'] && <Form.Control.Feedback type="invalid">{serverErrors['address']}</Form.Control.Feedback>}
                    </Col>
                  </Row>
                </Form.Group>
              )}
            />
            <Controller
              name="bank"
              control={control}
              render={({ field, fieldState: { invalid, error } }) => (
                <Form.Group>
                  <Row className='mt-2'>
                    <Col sm={5}>
                      <Form.Label>Tên ngân hàng</Form.Label>
                    </Col>
                    <Col sm={7}>
                      <Form.Select
                        {...field}
                      >
                        <option value={0}></option>
                        {Object.keys(props.userBanks).map((key) => (
                          <option key={key} value={key}>{props.userBanks[parseInt(key)].name}</option>
                        ))}
                      </Form.Select>
                    </Col>
                  </Row>
                </Form.Group>
              )}
            />
            <Controller
              name="bank_number"
              control={control}
              render={({ field, fieldState: { invalid, error } }) => (
                <Form.Group controlId="bank_number">
                  <Row className='mt-2'>
                    <Col sm={5}>
                      <Form.Label>Số TK:</Form.Label>
                    </Col>
                    <Col sm={7}>
                      <Form.Control
                        disabled={readOnly}
                        isInvalid={invalid || !!serverErrors['bank_number']}
                        {...field}
                      />
                      {invalid && <Form.Control.Feedback type="invalid">{error?.message}</Form.Control.Feedback>}
                      {!!serverErrors['bank_number'] && <Form.Control.Feedback type="invalid">{serverErrors['bank_number']}</Form.Control.Feedback>}
                    </Col>
                  </Row>
                </Form.Group>
              )}
            />


            <Controller
              name="status"
              control={control}
              render={({ field: {value, onChange}, fieldState: { invalid, error } }) => (
                <Form.Group>
                  <Row className='mt-2'>
                    <Col sm={5}>
                      <Form.Label>Trạng Thái *:</Form.Label>
                    </Col>
                    <Col sm={7} className='d-flex'>
                      {Object.keys(STATUS_CHOICES).map((key) => (
                        <Form.Check
                          key={key}
                          className='me-4'
                          type='radio'
                          id={`status-${key}`}
                          value={key}
                          name='status-radio'
                          checked={value == key ? true : false}
                          label={STATUS_CHOICES[key]}
                          onChange={(e) => onChange(e.target.value)}
                        />
                        
                      ))}
                    </Col>
                  </Row>
                </Form.Group>
              )}
            />
            
          </Modal.Body>
          <Modal.Footer>
            <Button type="submit" variant="primary">{props.selectedCUser ? 'Cập nhật' : 'Tạo mới'}</Button>
            <Button variant="outline-secondary" onClick={handleHide}>Cancel</Button>
            {props.selectedCUser && <Button variant="outline-danger" onClick={handleDelete}>Xóa</Button>}
          </Modal.Footer>
        </Form>
      </Modal>
			{/* END Modal */}
		</>
	)
}

export default UserManagerModal;
