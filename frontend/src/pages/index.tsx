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
import { DATETIME_FORMAT, DATE_FORMAT, TIME_FORMAT, DATE_FORMAT_DISPLAY } from 'constant/const';

import SortableHeader, { IHandleSortParam, handleSortData } from 'components/table/sortable-header';
import { isSuccessRequest } from 'store/request/helper';
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

const DashboardPage: ExtendedNextPage = (props) => {
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
		if (data) {
			const sortedData = handleSortData(param, data);
			setData(sortedData);
		}
		setLoading(false);
	}

	const filter = async () => {
		setLoading(true);
		const orgKey = 'lastModifiedFolder';
		const sortType = 'DESC';
		setSortKey(orgKey);
		try {
			// const res = await listFolderFromDisk({
			const res = await listSpecifyFolderFromDisk({
				driverPath,
				dropboxPath,
				startTime: startTime ? startTime.format(DATETIME_FORMAT) : '',
				endTime: endTime ? endTime.format(DATETIME_FORMAT) : '',
			})
			if (isSuccessRequest(res)) {
				const sortedData = handleSortData({orgKey, sortType}, res.data.data);
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
			<Form.Group as={Row} controlId="colFormLabelLg">
				<Col sm={12} className='d-flex flex-row'>
					<Form.Label column className='miw-60'>
						Dropbox:
					</Form.Label>
					<Form.Label column className='ps-3 miw-90'>
						E:\Dropbox\
					</Form.Label>
					<Form.Control
						placeholder="Your Dropbox path"
						className='ms-1'
						disabled={!isEditingDropboxPath}
						onChange={e => setDropboxPath(e.target.value)}
						defaultValue={dropboxPath}
					/>
					<Button variant={'primary'} disabled={loading} onClick={toggleEditingDropboxPath} className="ms-3 text-nowrap miw-80">
					{isEditingDropboxPath ? 'Lưu' : 'Thay đổi'}
					</Button>{' '}
				</Col>

				<Col sm={12} className='d-flex flex-row mt-3'>
					<Form.Label column className='miw-60'>
						Driver:
					</Form.Label>
					<Form.Label column className='ps-3 miw-90'>
						E:\MyDrive\
					</Form.Label>
					<Form.Control
						placeholder="Your Driver path"
						className='ms-1'
						disabled={!isEditingDriverPath}
						onChange={e => setDriverPath(e.target.value)}
						defaultValue={driverPath}
					/>
					<Button variant={'primary'} disabled={loading} onClick={toggleEditingDriverPath} className="ms-3 text-nowrap miw-80">
						{isEditingDriverPath ? 'Lưu' : 'Thay đổi'}
					</Button>{' '}
				</Col>

				<Col sm={12} className='d-flex flex-row mt-3'>
					<Form.Label column className='me-3 maw-140'>
						Thời gian bắt đầu
					</Form.Label>
					<DateTimePicker
						closeOnSelect
						dateFormat={DATE_FORMAT_DISPLAY}
						timeFormat={TIME_FORMAT}
						onChange={e => setStartTime(e)}
						value={startTime}
					/>
					<Form.Label column className='ms-5 me-3 maw-140'>
						Thời gian kết thúc
					</Form.Label>
					<DateTimePicker
						closeOnSelect
						dateFormat={DATE_FORMAT_DISPLAY}
						timeFormat={TIME_FORMAT}
						onChange={e => setEndTime(e)}
						value={endTime}
					/>
					<Button
						variant={'success'}
						className="ms-3 text-nowrap miw-80"
						onClick={filter}
						disabled={loading}
					>
						{loading && <Spinner animation="border" size="sm" className="me-2" />}
						Tìm kiếm
					</Button>{' '}
				</Col>
			</Form.Group>
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
	// const searchFolderSetting = await getSearchFolderSetting()
  return {
    props: {
			// searchFolderSetting: searchFolderSetting.data
		}, // will be passed to the page component as props
  }
}

DashboardPage.pageTitle = 'Thông tin cloud'
DashboardPage.activeLink = 'cloud_info'
DashboardPage.breadcrumb = [
	{ text: "Thông tin cloud", link: "/" },
]

export default withAuth(DashboardPage)
