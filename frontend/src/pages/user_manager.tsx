import React from 'react'

import withAuth from 'components/auth/withAuth'
import { Row, Col, Portlet, Form, Button, InputGroup, Table, Spinner } from '@blueupcode/components'
import { useDispatch } from "react-redux";
import { AShowLoading, AHideLoading } from 'store/common/actions'

import type { ExtendedNextPage } from '@blueupcode/components/types'
import { modalType, detailType, newType, updateType } from 'constant/type';
import { isSuccessRequest } from 'store/request/helper'
import SortableHeader, { IHandleSortParam, handleSortData } from 'components/table/sortable-header';
import {
	listCUsers,
	listUserBanks,
	listUserGroups,
	IFilterCuser,
	ICUser,
	ICreateCUser,
	IUserGroups,
	IUserBanks,
	STATUS_CHOICES,
	DEFAULT_FILTER_USER,
} from 'store/request/user_manager';
import { param } from 'react-dom-factories';
import { useForm, Controller } from 'react-hook-form'
import * as yup from 'yup'
import { yupResolver } from '@hookform/resolvers/yup'
import UserManagerModal from 'modals/user_manager';

export type ICuserProps = {
	data: {
		cUsers: ICUser[],
		userBanks: {
			[key: number]: IUserBanks
		},
		userGroups: {
			[key: number]: IUserGroups
		},
	}
};

const validationSchema = yup.object().shape({
	// No validate need for filter
})

const UserManagerPage: ExtendedNextPage<ICuserProps> = (props) => {
	const [showModal, setShowModal] = React.useState<boolean>(false);
	const [errorMsg, setErrorMsg] = React.useState<string>('');
	const [cUsers, setCUsers] = React.useState<ICUser[]>(props.data.cUsers);
	const [selectedCUser, setSelectedCUser] = React.useState<ICUser | null>(null)
	const [sortKey, setSortKey] = React.useState<string>('');
	const [sortType, setSortType] = React.useState<string>('');
	const filterSubmitBtnRef = React.useRef<HTMLButtonElement>(null);

	const dispatch = useDispatch();

  const {control, handleSubmit} = useForm<IFilterCuser>({
    resolver: yupResolver(validationSchema),
		defaultValues: DEFAULT_FILTER_USER,
  })

	const refreshData = () => {
		if (filterSubmitBtnRef.current) {
			filterSubmitBtnRef.current.click()
		}
	}

	const onSubmit = async (formData: IFilterCuser) => {
    dispatch(AShowLoading());

		const params={
			name: formData.name,
			group: formData.group,
			status: formData.status,
			full_name: formData.full_name,
		}
		console.log(params)
		const res = await listCUsers(params);
		if (isSuccessRequest(res)) {
			setCUsers(res.data);
		}

    dispatch(AHideLoading());
	}

	const createNew = async () => {
		setSelectedCUser(null);
		setShowModal(true);
	}

	const viewDetail = (idx: number) => {
		setSelectedCUser(cUsers[idx]);
		setShowModal(true);
	}

	const handleSortTableColumn = (param: IHandleSortParam) => {
		dispatch(AShowLoading());
		setSortKey(param.orgKey);
		setSortType(param.sortType);
		if (cUsers) {
			const sortedCUsers = handleSortData(param, cUsers);
			setCUsers(sortedCUsers);
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
										<option value={0}></option>
										{Object.keys(props.data.userGroups).map((key) => (
											<option key={key} value={key}>{props.data.userGroups[parseInt(key)].name}</option>
										))}
									</Form.Select>
								</Form.Group>
							)}
						/>
					</Col>
				</Row>
				<div className='d-flex justify-content-between'>
					<Button type="submit" ref={filterSubmitBtnRef} variant="primary">Tìm kiếm</Button>
					<Button
						variant={'success'}
						className="ms-3 text-nowrap miw-80"
						onClick={createNew}
					>
						Thêm
					</Button>{' '}
				</div>
			</Form>

			<Table bordered striped hover className='mt-4'>
				<thead className='table-primary'>
					<tr>
						<th scope="col" className='w-30'>#</th>
						<th scope="col" className='2-130'>
							<SortableHeader
								title='Mã NV'
								orgKey='name'
								sortKey={sortKey}
								handleSortTableColumn={handleSortTableColumn}
							/>
						</th>
						<th scope="col" className=''>Họ và tên</th>
						<th scope="col" className=''>Role</th>
						<th scope="col" className=''>Số ĐT</th>
						<th scope="col" className=''>Mail</th>
						<th scope="col" className=''>Địa chỉ</th>
						<th scope="col" className=''>Trạng thái</th>
					</tr>
				</thead>
					<tbody>
					{cUsers && cUsers?.length > 0 ? (
							cUsers.map((item, idx) => (
								<tr key={idx + 1} className="cursor-pointer" onDoubleClick={() => viewDetail(idx)}>
									<th scope="row">{idx + 1}</th>
									<td>{item.name}</td>
									<td>{item.full_name}</td>
									<td>{item.groups[0] ? props.data.userGroups[item.groups[0]].name: ''}</td>
									<td>{item.phone_number}</td>
									<td>{item.email}</td>
									<td>{item.address}</td>
									<td>{STATUS_CHOICES[item.status]}</td>
								</tr>
							))
						) : (
							<tr><div className=''>{errorMsg}</div></tr>
					)}
				</tbody>
			</Table>
			{showModal && <UserManagerModal
					show={showModal}
					handleShow={setShowModal}
					selectedCUser={selectedCUser}
					userGroups={props.data.userGroups}
					userBanks={props.data.userBanks}
					refreshData={refreshData}
				/>
				}
		</>
	)
}


export async function getServerSideProps() {
	const	[resCUsers, resUserGroups, resUserBanks] = await Promise.all([listCUsers(), listUserGroups(), listUserBanks()]);
	if (isSuccessRequest(resCUsers) && isSuccessRequest(resUserGroups) && isSuccessRequest(resUserBanks)) {
		const userGroups = resUserGroups.data.reduce((acc, item) => {
			acc[item.id] = item;
			return acc;
		}, {});
		const userBanks = resUserBanks.data.reduce((acc, item) => {
			acc[item.id] = item;
			return acc;
		}, {});


		const data = {
			cUsers: resCUsers.data,
			userGroups: userGroups,
			userBanks: userBanks
		}
		return {
			props: {
				data
			}
		}
	}
	return {
    props: {
    }
  }
}


UserManagerPage.pageTitle = 'Quản lý user'
UserManagerPage.activeLink = 'user_manager'
UserManagerPage.breadcrumb = [
	{ text: "Quản lý user", link: "/user_manager" },
]

export default withAuth(UserManagerPage)
