import React from 'react'

import withAuth from 'components/auth/withAuth'
import { Row, Col, Portlet, Form, Button, InputGroup, Table, Spinner } from '@blueupcode/components'
import { useDispatch } from "react-redux";
import { AShowLoading, AHideLoading } from 'store/common/actions'

import type { ExtendedNextPage } from '@blueupcode/components/types'
import { modalType, detailType, newType, updateType } from 'constant/type';
import { isSuccessRequest } from 'store/request/helper'
import SortableHeader, { IHandleSortParam, handleSortData } from 'components/table/sortable-header';
import { listCUsers, listUserBanks, listUserGroups, IFilterCuser, ICreateCUser, IUserGroups, IUserBanks,  STATUS_CHOICES } from 'store/request/user_manager';
import { param } from 'react-dom-factories';
import { useForm, Controller } from 'react-hook-form'
import * as yup from 'yup'
import { yupResolver } from '@hookform/resolvers/yup'



const validationSchema = yup.object().shape({
	// No validate need for filter
})

export const defaultParamFilter = {
	name: '',
	group: '',
	status: '',
	full_name: '',
}

interface IUserManageFilterProps {
  userGroups: {
    [key: number]: IUserGroups
  },
  createNew: () => void,
  setCUsers: (data: ICreateCUser[]) => void,
}

const UserManagerFilter = (props: IUserManageFilterProps) => {
	const dispatch = useDispatch();

  const {control, handleSubmit} = useForm<IFilterCuser>({
    resolver: yupResolver(validationSchema),
		defaultValues: defaultParamFilter,
  })

	const onSubmit = async (formData: IFilterCuser) => {
    dispatch(AShowLoading());

		const params={
			name: formData.name,
			group: formData.group,
			status: formData.status,
			full_name: formData.full_name,
		}
		const res = await listCUsers(params);
		if (isSuccessRequest(res)) {
			props.setCUsers(res.data);
		}

    dispatch(AHideLoading());
	}

	return (
		<>
			<Form onSubmit={handleSubmit(onSubmit)} className="d-grid gap-3">
				<Row>
					<Col sm={2}>
						<Controller
							name="name"
							control={control}
							render={({ field, fieldState: { invalid, error } }) => (
								<Form.Group controlId="name">
									<Form.Label>Mã nhân viên</Form.Label>
									<Form.Control
										{...field}
									/>
								</Form.Group>
							)}
						/>
					</Col>
					<Col sm={2}>
						<Controller
							name="full_name"
							control={control}
							render={({ field, fieldState: { invalid, error } }) => (
								<Form.Group controlId="full_name">
									<Form.Label>Họ và tên</Form.Label>
									<Form.Control
										{...field}
									/>
								</Form.Group>
							)}
						/>
					</Col>
					<Col sm={2}>
						<Controller
							name="status"
							control={control}
							render={({ field, fieldState: { invalid, error } }) => (
								<Form.Group controlId="status">
									<Form.Label>Trạng thái</Form.Label>
									<Form.Select
										defaultValue=""
										{...field}
									>
										<option value=""></option>
										{Object.keys(STATUS_CHOICES).map((key: string) => (
											<option key={key} value={key}>{STATUS_CHOICES[key]}</option>
										))}
									</Form.Select>
								</Form.Group>
							)}
						/>
					</Col>
					<Col sm={2}>
						<Controller
							name="group"
							control={control}
							render={({ field, fieldState: { invalid, error } }) => (
								<Form.Group controlId="group">
									<Form.Label>Role</Form.Label>
									<Form.Select
										defaultValue=""
										{...field}
									>
										<option value=""></option>
										{Object.keys(props.userGroups).map((key: string) => (
											<option key={key} value={key}>{props.userGroups[key].name}</option>
										))}
									</Form.Select>
								</Form.Group>
							)}
						/>
					</Col>
				</Row>
				<div className='d-flex justify-content-between'>
					<Button type="submit" variant="primary">Tìm kiếm</Button>
					<Button
						variant={'success'}
						className="ms-3 text-nowrap miw-80"
						onClick={props.createNew}
					>
						Thêm
					</Button>{' '}
				</div>
			</Form>
		</>
	)
}

export default UserManagerFilter;
