import React from 'react'
import Moment from 'moment';
import { GetStaticProps, GetStaticPaths, GetServerSideProps } from 'next'
import withAuth from 'components/auth/withAuth'
import { Row, Col, Portlet, Form, Button, InputGroup, Table, Spinner } from '@blueupcode/components'

import type { ExtendedNextPage } from '@blueupcode/components/types'
import Router from 'next/router'
import PAGE from 'config/page.config'
import DateTimePicker from 'react-datetime'
import { string } from 'prop-types'
import {
	listFolderFromDisk, IListFolderFromDisk, IOneFolder, listSpecifyFolderFromDisk,
	getSearchFolderSetting, ISettingSearchFolder, putSearchFolderSetting
} from 'store/request/job_manager'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
// https://upmin-react.blueupcode.com/
import {
	faAngleDown,
} from '@fortawesome/free-solid-svg-icons'
import { DATETIME_FORMAT, DATE_FORMAT, TIME_FORMAT } from 'constant/const';

import SortableHeader, { IHandleSortParam } from 'components/table/sortable-header';
interface ISearchFolderSetting {
	driver: string;
	dropbox: string;
}


// interface aa {
// 	lastModifiedFolder: string;
// 	files: string[],
// }
type IProps = {
	searchFolderSetting: ISearchFolderSetting
	// [key: string]: aa[]
}

const RoleManager: ExtendedNextPage = (props) => {
	const [driverPath, setDriverPath] = React.useState<string>('');
	const [isEditingDriverPath, setIsEditingDriverPath] = React.useState<boolean>(false);
	const [dropboxPath, setDropboxPath] = React.useState<string>('');
	const [isEditingDropboxPath, setIsEditingDropboxPath] = React.useState<boolean>(false);
	const [startTime, setStartTime] = React.useState<Moment.Moment>(Moment().startOf('day'));
	const [endTime, setEndTime] = React.useState<Moment.Moment>(Moment());
	const [loading, setLoading] = React.useState<boolean>(false);
	const [errorMsg, setErrorMsg] = React.useState<string>('');
	const [data, setData] = React.useState<IOneFolder[]>();
	const [sortkey, setSortKey] = React.useState<string>('');

	React.useEffect(() => {
		getSearchFolderSetting()
			.then((res) => res.data)
			.then((data) => {
				setDriverPath(data.data.driver);
				setDropboxPath(data.data.dropbox);
			})
	}, [])

	const createJob = () => {
		return Router.push('/create_job')
	}

	const handleSortTableColumn = (param: IHandleSortParam) => {
		setLoading(true);
		setSortKey(param.orgKey);
		console.log('param', param);
		if (data) {
			const sortedData = [...data].sort((a, b) => {
				const res = param.sortType === 'DESC' ? 1 : -1;
				return b[param.orgKey] > a[param.orgKey] ? res : -res;
			});
			setData(sortedData);
		}
		// Sort array
		setLoading(false);
	}

	const filter = async () => {
		setLoading(true);
		setSortKey('handleSortTableColumn');
		try {
			// const res = await listFolderFromDisk({
			const res = await listSpecifyFolderFromDisk({
				driverPath,
				dropboxPath,
				startTime: startTime ? startTime.format(DATETIME_FORMAT) : '',
				endTime: endTime ? endTime.format(DATETIME_FORMAT) : '',
			})
			if (res.status === 200) {
				const sortedData = [...res.data.data].sort((a, b) => {
					const res = 1;
					return b['handleSortTableColumn'] > a['handleSortTableColumn'] ? res : -res;
				});
				setData(sortedData);
				if (res.data.data?.length === 0) {
					setErrorMsg('Không có data.');
				}
			}
		} catch (e) {
			console.log(e);
			setData([]);
			setErrorMsg('Có lỗi xảy ra khi thực hiện Tìm kiếm. Bạn hãy chỉ định khoảng Tìm kiếm cụ thể hơn hoặc liên lạc với Admin để được hỗ trợ');
		}
		setLoading(false);
	}

	const toggleEditingDriverPath = () => {
		setIsEditingDriverPath(!isEditingDriverPath);
		putSearchFolderSetting({subkey: 'driver', value: driverPath});
	}
	const toggleEditingDropboxPath = () => {
		setIsEditingDropboxPath(!isEditingDropboxPath);
		putSearchFolderSetting({subkey: 'dropbox', value: dropboxPath})
	}

	console.log('props',props)
	return (
		<>
			<Button
				variant={'success'}
				className="ms-3 text-nowrap miw-80"
				onClick={filter}
				disabled={loading}
			>
				{loading && <Spinner animation="border" size="sm" className="me-2" />}
				Thêm
			</Button>{' '}
			{loading ? (
				<div className='align-middle text-center mt-5'>
					<Spinner animation="border" size="sm" style={{ height: '3rem', width: '3rem' }} className="me-2" />
				</div>
				) : (
					<Table bordered striped hover className='mt-4'>
						<thead className='table-primary'>
							<tr>
								<th scope="col" className='w-30'>#</th>
								<th scope="col" className=''>
									<SortableHeader
										title='Thư mục'
										orgKey='path'
										sortKey={sortkey}
										handleSortTableColumn={handleSortTableColumn}
									/>
								</th>
								<th scope="col" className='w-130'>
									<SortableHeader
										title='Thời gian cập nhật'
										orgKey='lastModifiedFolder'
										sortKey={sortkey}
										handleSortTableColumn={handleSortTableColumn}
									/>
								</th>
								<th scope="col" className='w-30'>Số file</th>
								<th scope="col" className='w-30'>Trạng thái</th>
								<th scope="col" className='w-30'>Thao tác</th>
							</tr>
						</thead>
							<tbody>
							{data && data?.length > 0 ? (
									data.map((item, idx) => (
										<tr key={idx + 1}>
											<th scope="row">{idx + 1}</th>
											<td>{item.path}</td>
											<td>{Moment.unix(parseFloat(item.lastModifiedFolder)).format('YYYY-MM-DD HH:mm')}</td>
											<td>{item.files ? item.files.length : 0}</td>
											<td className='miw-120'>Chưa tạo job</td>
											<td>
												<Button variant={'success'} onClick={createJob} className="ms-3 text-nowrap miw-80">
													Tạo Job
												</Button>{' '}
											</td>
										</tr>
									))
							) : (
								<tr><div className=''>{errorMsg}</div></tr>
							)}
						</tbody>
					</Table>
				)}
		</>
	)
}

export const getStaticProps: GetStaticProps = async (context) => {
  return {
    props: {
		}, // will be passed to the page component as props
  }
}

RoleManager.pageTitle = 'Quản lý role'
RoleManager.activeLink = '/role_manager'
RoleManager.breadcrumb = [
	{ text: "Quản lý role", link: "/role_manager" },
]

export default withAuth(RoleManager)
