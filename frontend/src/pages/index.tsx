import React from 'react'
import Moment from 'moment';
import { GetStaticProps, GetStaticPaths, GetServerSideProps } from 'next'
import withAuth from 'components/auth/withAuth'
import { Row, Col, Portlet, Form, Button, InputGroup, Table, Spinner } from '@blueupcode/components'
import Widget3 from 'components/widgets/Widget3'
import Widget7 from 'components/widgets/Widget7'
import Widget10 from 'components/widgets/Widget10'
import Widget13 from 'components/widgets/Widget13'
import Widget14 from 'components/widgets/Widget14'
import Widget15 from 'components/widgets/Widget15'
import Widget16 from 'components/widgets/Widget16'
import Widget18 from 'components/widgets/Widget18'
import Widget21 from 'components/widgets/Widget21'
import Widget22 from 'components/widgets/Widget22'
import Widget27 from 'components/widgets/Widget27'
import Widget28 from 'components/widgets/Widget28'
import Widget29 from 'components/widgets/Widget29'
import Widget33 from 'components/widgets/Widget33'
import Widget34 from 'components/widgets/Widget34'
import Widget35 from 'components/widgets/Widget35'
import type { ExtendedNextPage } from '@blueupcode/components/types'
import Router from 'next/router'
import PAGE from 'config/page.config'
import DateTimePicker from 'react-datetime'
import { string } from 'prop-types'
import {
	listFolderFromDisk, IListFolderFromDisk, IOneFolder,
	getSearchFolderSetting, ISettingSearchFolder, putSearchFolderSetting
} from 'store/request/job_manager'

// https://upmin-react.blueupcode.com/

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
	const [startTime, setStartTime] = React.useState<string>('');
	const [endTime, setEndTime] = React.useState<string>('');
	const [loading, setLoading] = React.useState<boolean>(false);
	const [data, setData] = React.useState<IOneFolder[]>();

	React.useEffect(() => {
		getSearchFolderSetting()
			.then((res) => res.data)
			.then((data) => {
				setDriverPath(data.data.driver);
				setDropboxPath(data.data.dropbox);
			})
	}, [])

	// const updateSearchFolderSetting = (subkey: string) => {
	// 	if (subkey === 'driver') {
	// 		const value = driverPath;
	// 		setIsEditingDriverPath(!isEditingDriverPath);
	// 		putSearchFolderSetting({subkey, value});
	// 	} else if (subkey === 'dropbox'){
	// 		const value = dropboxPath;
	// 		setIsEditingDropboxPath(!isEditingDropboxPath);
	// 		putSearchFolderSetting({subkey, value});
	// 	}
	// }

	const filter = async () => {
		setLoading(true);
		const res = await listFolderFromDisk({
			driverPath,
			dropboxPath,
			startTime: startTime ? startTime.format('YYYY-MM-DD h:mm') : '',
			endTime: endTime ? endTime.format('YYYY-MM-DD h:mm') : '',
		})
		setLoading(false);
		if (res.status === 200) {
			console.log(res.data, res.status);
			setData(res.data.data);
		}
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
					<Button variant={'primary'} onClick={toggleEditingDropboxPath} className="ms-3 text-nowrap miw-80">
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
					<Button variant={'primary'} onClick={toggleEditingDriverPath} className="ms-3 text-nowrap miw-80">
						{isEditingDriverPath ? 'Lưu' : 'Thay đổi'}
					</Button>{' '}
				</Col>

				<Col sm={12} className='d-flex flex-row mt-3'>
					<Form.Label column className='me-3 maw-140'>
						Thời gian bắt đầu
					</Form.Label>
					<DateTimePicker
						closeOnSelect
						dateFormat="YYYY-MM-DD"
						timeFormat="hh:mm a"
						onChange={e => setStartTime(e)}
					/>
					<Form.Label column className='ms-5 me-3 maw-140'>
						Thời gian kết thúc
					</Form.Label>
					<DateTimePicker
						closeOnSelect
						dateFormat="YYYY-MM-DD"
						timeFormat="hh:mm a"
						onChange={e => setEndTime(e)}
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
								<th scope="col" className=''>Thư mục</th>
								<th scope="col" className='w-130'>Thời gian cập nhật</th>
								<th scope="col" className='w-30'>Số file</th>
							</tr>
						</thead>
						<tbody>
							{data && data?.length > 0 ? (
								data.map((item, idx) => (
									<tr key={idx + 1}>
										<th scope="row">{idx + 1}</th>
										<td>{item.path}</td>
										<td>{item.lastModifiedFolder}</td>
										<td>{item.files ? item.files.length : 0}</td>
									</tr>
								))
							) : (
								<div className='w-130'>Không có data.</div>
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
