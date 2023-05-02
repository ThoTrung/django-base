import React from 'react'

import withAuth from 'components/auth/withAuth'
import { Row, Col, Portlet, Form, Button, InputGroup, Table, Spinner } from '@blueupcode/components'
import { useDispatch } from "react-redux";
import { AShowLoading, AHideLoading } from 'store/common/actions'

import type { ExtendedNextPage } from '@blueupcode/components/types'
import { IUserGroups, listUserGroups, IUserPermissions, listUserPermissions } from 'store/request/user_manager';
import RoleManagerModal from 'modals/role_manager';
import { modalType, detailType, newType, updateType } from 'constant/type';
import { isSuccessRequest } from 'store/request/helper'
import SortableHeader, { IHandleSortParam, handleSortData } from 'components/table/sortable-header';


export type IRoleManageProps = {
	data: {
		userGroups: IUserGroups[]
		userPermissions: {
			[key: number]: IUserPermissions
		}
	}
};

const RoleManager: ExtendedNextPage<IRoleManageProps> = (props) => {
	const [loading, setLoading] = React.useState<boolean>(false);
	const [errorMsg, setErrorMsg] = React.useState<string>('');
	const [typeModal, setTypeModal] = React.useState<modalType>(updateType);
	const [showModal, setShowModal] = React.useState<boolean>(false);
	const [userGroups, setUserGroups] = React.useState<IUserGroups[]>(props.data.userGroups);
	const [selectedGroup, setSelectedGroup] = React.useState<IUserGroups | null>(null)
	const [sortKey, setSortKey] = React.useState<string>('');
	const [sortType, setSortType] = React.useState<string>('');

	const dispatch = useDispatch();

	const refreshData = async() => {
		const resUserGroups = await listUserGroups();
		console.log('resUserGroups', resUserGroups.data, sortKey, sortType)
		if (isSuccessRequest(resUserGroups)) {
			const sortedUserGroups = handleSortData({orgKey: sortKey, sortType:sortType}, resUserGroups.data);
			console.log('vao vao aofaofasfoasfdo',sortedUserGroups)
			setUserGroups(sortedUserGroups);
		}
	}

	const createNew = () => {
		setSelectedGroup(null);
		setTypeModal(newType);
		setShowModal(true);
	}

	const viewDetail = (idx: number) => {
		setSelectedGroup(userGroups[idx]);
		setTypeModal(updateType);
		setShowModal(true);
	}

	const handleSortTableColumn = (param: IHandleSortParam) => {
		dispatch(AShowLoading());
		setSortKey(param.orgKey);
		setSortType(param.sortType);
		if (userGroups) {
			const sortedUserGroups = handleSortData(param, userGroups);
			setUserGroups(sortedUserGroups);
		}
		dispatch(AHideLoading());
	}

	return (
		<>
			<div className='w-100 d-flex justify-content-end'>
				<Button
					variant={'success'}
					className="ms-3 text-nowrap miw-80"
					onClick={createNew}
					disabled={loading}
				>
					{loading && <Spinner animation="border" size="sm" className="me-2" />}
					Thêm
				</Button>{' '}
			</div>
			{loading ? (
				<div className='align-middle text-center mt-5'>
					<Spinner animation="border" size="sm" style={{ height: '3rem', width: '3rem' }} className="me-2" />
				</div>
				) : (
					<Table bordered striped hover className='mt-4'>
						<thead className='table-primary'>
							<tr>
								<th scope="col" className='w-30'>#</th>
								<th scope="col" className='2-130'>
									<SortableHeader
										title='Tên role'
										orgKey='name'
										sortKey={sortKey}
										handleSortTableColumn={handleSortTableColumn}
									/>
								</th>
								<th scope="col" className=''>Danh sách mành hình</th>
							</tr>
						</thead>
							<tbody>
							{userGroups && userGroups?.length > 0 ? (
									userGroups.map((item, idx) => (
										<tr key={idx + 1} className="cursor-pointer" onDoubleClick={() => viewDetail(idx)}>
											<th scope="row">{idx + 1}</th>
											<td>{item.name}</td>
											<td>
												{item.permissions && item.permissions?.length > 0 && (
													<span>
														{item.permissions.map(function(id) {
															return props.data.userPermissions[id] ? props.data.userPermissions[id].name : '';
														}).join(', ')}
													</span>
												)}
											</td>
										</tr>
									))
							) : (
								<tr><div className=''>{errorMsg}</div></tr>
							)}
						</tbody>
					</Table>
				)}
				{showModal && <RoleManagerModal
					show={showModal}
					type={typeModal}
					handleShow={setShowModal}
					permissions={props.data.userPermissions}
					selectedGroup={selectedGroup}
					refreshData={refreshData}
				/>
				}
		</>
	)
}

export async function getServerSideProps() {
	const	[resUserGroups, resUserPermission] = await Promise.all([listUserGroups(), listUserPermissions()]);
	if (isSuccessRequest(resUserGroups) && isSuccessRequest(resUserPermission)) {
		const userPermissions = resUserPermission.data.reduce((acc, item) => {
			acc[item.id] = item;
			return acc;
		}, {});
		console.log('userPermissions', userPermissions);
		const data = {
			userGroups: resUserGroups.data,
			userPermissions: userPermissions
		}
		return {
			props: {
				data
			}
		}
	}
}

RoleManager.pageTitle = 'Quản lý role'
RoleManager.activeLink = 'role_manager'
RoleManager.breadcrumb = [
	{ text: "Quản lý role", link: "/role_manager" },
]

export default withAuth(RoleManager)
