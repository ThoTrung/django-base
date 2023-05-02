import React from 'react'
import { Row, Col, ListGroup, Button, Modal, Form } from '@blueupcode/components'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faTimes } from '@fortawesome/free-solid-svg-icons'
import { modalType, newType, updateType, detailType } from 'constant/type'
import { IUserPermissions, IUserGroups, createUserGroups, updateUserGroups, deleteUserGroups } from 'store/request/user_manager'
import { useDispatch } from "react-redux";
import { AShowLoading, AHideLoading } from 'store/common/actions'
import { useForm, Controller } from 'react-hook-form'
import * as yup from 'yup'
import { yupResolver } from '@hookform/resolvers/yup'
import { isSuccessRequest } from 'store/request/helper'
import { swalSuccess, swalDelete, swalDeleteSuccess } from 'components/swals/swals'

type Props = {
  type: modalType;
  show: boolean;
  permissions: {
    [key: number]: IUserPermissions
  }
  selectedGroup: IUserGroups | null;
  handleShow: (show:boolean) => void;
  refreshData: () => void;
}

interface IRoleManager {
	name: string,
  permissions: number[],
}

const validationSchema = yup.object().shape({
	name: yup.string().required('Bạn cần nhập tên Role'),
})

const RoleManagerModal = (props: Props) => {
  const [readOnly, setReadOnly] = React.useState<boolean>(false);
  const [show, setShow] = React.useState<boolean>(props.show);
  const [formTitle, setFormTitle] = React.useState<string>('');
  const [serverErrors, setServerErrors] = React.useState({});
  
  const dispatch = useDispatch();

  const {control, handleSubmit} = useForm<IRoleManager>({
    resolver: yupResolver(validationSchema),
		defaultValues: {
			name: (props.selectedGroup ? props.selectedGroup.name : ''),
      permissions: (props.selectedGroup ? props.selectedGroup.permissions : []),
		},
  })

  const handleDelete = async() => {
    if (props.selectedGroup !== null) {
      const result = await swalDelete();
      if (result.isConfirmed) {
        dispatch(AShowLoading());
        const res = await deleteUserGroups(props.selectedGroup.id)
        if (isSuccessRequest(res)) {
          props.refreshData();
          handleHide();
          swalDeleteSuccess('Role');
        }
        dispatch(AHideLoading());
      }
    }
  }

  const onSubmit = async (formData: IRoleManager) => {
    dispatch(AShowLoading());
    const payload={name: formData.name, permissions: formData.permissions}
    let res = null;
    let swalTitle = '';
    if (props.selectedGroup === null) {
      res = await createUserGroups(payload);
      swalTitle = 'Thêm role thành công.'
    } else {
      res = await updateUserGroups(props.selectedGroup.id, payload);
      swalTitle = 'Cập nhật role thành công.'
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
    let readOnlyTemp = true;
    let formTitleTemp = "Xem chi tiết Role"
    if (props.type === newType) {
      readOnlyTemp = false;
      formTitleTemp = "Thêm Role";
    } else if(props.type === updateType) {
      readOnlyTemp = false;
      formTitleTemp = "Cập nhật Role"
    }
    setReadOnly(readOnlyTemp);
    setFormTitle(formTitleTemp);
  }, [props.type])

	return (
		<>
      <Modal
        show={show}
        onHide={handleHide}
        backdrop="static"
        keyboard={false}
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
                  <Row>
                    <Col sm={5}>
                      <Form.Label>Tên Role</Form.Label>
                    </Col>
                    <Col sm={7}>
                      <Form.Control
                        placeholder="Tên Role"
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
              name="permissions"
              control={control}
              render={({ field: {value, onChange}, fieldState: { invalid, error } }) => (
                <Form.Group>
                  <Row className='mt-3'>
                    <Col sm={5}>
                      <Form.Label>Danh sách màn hình</Form.Label>
                    </Col>
                    <Col sm={7}>
                      <ListGroup>
                        {Object.keys(props.permissions).map((key: string) => (
                          <ListGroup.Item key={key}>
                            <Form.Check.Input
                              type="checkbox"
                              value={key}
                              checked={value.includes(parseInt(key))}
                              className="me-2"
                              onChange={(e) => {
                                const isChecked = e.target.checked;
                                const newValue = parseInt(e.target.value);
                                onChange(
                                  value.includes(newValue)
                                  ? value.filter((val) => val !== newValue)
                                  : [...value, newValue]
                                )
                              }}
                            />
                            {props.permissions[key].name}
                          </ListGroup.Item>
                        ))}
                      </ListGroup>
                    </Col>
                  </Row>
                </Form.Group>
              )}
            />
          </Modal.Body>
          <Modal.Footer>
            <Button type="submit" variant="primary">{props.selectedGroup ? 'Cập nhật' : 'Tạo mới'}</Button>
            <Button variant="outline-secondary" onClick={handleHide}>Cancel</Button>
            {props.selectedGroup && <Button variant="outline-danger" onClick={handleDelete}>Xóa</Button>}
          </Modal.Footer>
        </Form>
      </Modal>
			{/* END Modal */}
		</>
	)
}

export default RoleManagerModal;
