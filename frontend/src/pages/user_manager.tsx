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
import { listCUsers, listUserBanks } from 'store/request/user_manager';
import { param } from 'react-dom-factories';

// export type IRoleManageProps = {
// 	data: {
// 		userGroups: IUserGroups[]
// 		userPermissions: {
// 			[key: number]: IUserPermissions
// 		}
// 	}
// };

const UserManagerPage: ExtendedNextPage = (props) => {
	

	const createNew = async () => {
		const param = {
			name: 'tho',
			group: 33,
			status: 'W',
			fullName: 'trungtho',
		}
		const res = await listCUsers(param);
		console.log('--------------------------', res)
	}

	return (
		<>
			<div>
				<div className='w-100 d-flex justify-content-end'>
					<Button
						variant={'success'}
						className="ms-3 text-nowrap miw-80"
						onClick={createNew}
					>
						Thêm
					</Button>{' '}
				</div>
			</div>
		</>
	)
}


// export async function getServerSideProps() {
// 	const	[resUserGroups, resUserPermission] = await Promise.all([listUserGroups(), listUserPermissions()]);
// 	if (isSuccessRequest(resUserGroups) && isSuccessRequest(resUserPermission)) {
// 		const userPermissions = resUserPermission.data.reduce((acc, item) => {
// 			acc[item.id] = item;
// 			return acc;
// 		}, {});
// 		console.log('userPermissions', userPermissions);
// 		const data = {
// 			userGroups: resUserGroups.data,
// 			userPermissions: userPermissions
// 		}
// 		return {
// 			props: {
// 				data
// 			}
// 		}
// 	}
// }


UserManagerPage.pageTitle = 'Quản lý user'
UserManagerPage.activeLink = 'user_manager'
UserManagerPage.breadcrumb = [
	{ text: "Quản lý user", link: "/user_manager" },
]

export default withAuth(UserManagerPage)
