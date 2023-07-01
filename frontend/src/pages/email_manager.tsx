import React from 'react'

import withAuth from 'components/auth/withAuth'
import { Row, Col, Portlet, Form, Button, InputGroup, Table, Spinner, Badge, Pagination } from '@blueupcode/components'
import { useDispatch, useSelector } from "react-redux";
import { AShowLoading, AHideLoading } from 'store/common/actions'
import type { ExtendedNextPage } from '@blueupcode/components/types'
import { modalType, detailType, newType, updateType } from 'constant/type';
import { isSuccessRequest } from 'store/request/helper'
import SortableHeader, { IHandleSortParam, handleSortData } from 'components/table/sortable-header';
import {
	ICreateEmail,
	IFilterEmail,
	listEmails,
	DEFAULT_FILTER_EMAIL,
	IEmailSetting,
	getEmailSetting,
} from 'store/request/email_manager';
import {
	listCommon
} from 'store/request/common';
import { param } from 'react-dom-factories';
import { useForm, Controller } from 'react-hook-form'
import * as yup from 'yup'
import { yupResolver } from '@hookform/resolvers/yup'
import CommonModal from 'modals/common';
import { getSMyInfo } from 'store/myInfo/selectors';
import PaginationNormal from 'components/common/pagination/pagination_normal';

const PAGE_KEY = 'email_manager';

const configData = {
	filterConfig: {
		defaultValue: {
			email: '',
		},
		fields: {
			primary_email: {
				default: ''
			}
		}
	},
	fieldsInTable: ['primary_email', 'first_name', 'last_name', 'phone_number'],
	fields: {
		primary_email: {
			display_name: 'Email',
			require: true,
			validate: yup.string().required('Bạn cần nhập email'),
			default_value: '',
			disable_on_edit: true,
			extra_data: {
				type: 'LABLE',
				width: 4,
				data: '',
			}
		},
		password: {
			display_name: 'Password',
			require: true,
			validate: yup.string().required('Bạn cần nhập mật khẩu mặc định cho Email này'),
			default_value: '',
		},
		first_name: {
			display_name: 'Họ',
			require: true,
			validate: yup.string().required('Bạn cần nhập Họ'),
			default_value: '',
		},
		last_name: {
			display_name: 'Tên',
			require: true,
			validate: yup.string().required('Bạn cần nhập Tên'),
			default_value: '',
		},
		phone_number: {
			display_name: 'SDT',
			default_value: '',
		},
	}
}


export type IEmailProps = {
	data: {
		items: any[],
	}
};

const validationSchema = yup.object().shape({
	// No validate need for filter
})

export type TStatuses = {
	[key: string]: {
		text: string,
		variant: string,
	}
}

export type TAdditionalData = {
	statuses: TStatuses
}

const EmailManagerPage: ExtendedNextPage<any> = (props) => {
	const [showModal, setShowModal] = React.useState<boolean>(false);
	const [errorMsg, setErrorMsg] = React.useState<string>('');
	const [items, setItems] = React.useState<any[]>(props.data.items);
	const [selectedItem, setSelectedItem] = React.useState<any | null>(null)
	const [sortKey, setSortKey] = React.useState<string>('');
	const [sortType, setSortType] = React.useState<string>('');
	const [emailSetting, setEmailSetting] = React.useState<IEmailSetting | null>(null);
	const [additionalData, setAdditionalData] = React.useState<TAdditionalData | null>(null)
	const [totalPages, setTotalPages] = React.useState<number>(0)
	const [curPage, setCurPage] = React.useState<number>(0)
	const [filterData, setFilterData] = React.useState<any>(configData.filterConfig.defaultValue);

	
	const filterSubmitBtnRef = React.useRef<HTMLButtonElement>(null);
	const myInfo = useSelector(getSMyInfo);

	React.useEffect(() => {
		if (myInfo && myInfo.id && emailSetting === null) {
			const getEmailSettingLocal = async() => {
				const resEmailSetting = await getEmailSetting(myInfo.id);
				if (isSuccessRequest(resEmailSetting)) {
					setEmailSetting(resEmailSetting.data)
				}
			}
			getEmailSettingLocal();
		}

	}, [myInfo])

	React.useEffect(() => {
		filter(filterData);
	}, [])

	const dispatch = useDispatch();

  const {control, handleSubmit} = useForm<IFilterEmail>({
    resolver: yupResolver(validationSchema),
		defaultValues: DEFAULT_FILTER_EMAIL,
  })

	const refreshData = () => {
		if (filterSubmitBtnRef.current) {
			filterSubmitBtnRef.current.click()
		}
	}

	const filter = async(params: any, page: number = 1) => {
		dispatch(AShowLoading());
		const res = await listEmails(params);
		if (isSuccessRequest(res)) {
			setItems(res.data.results);
			if (res.data.additional_data) {
				setAdditionalData(res.data.additional_data)
			}
			if (res.data.total_pages) {
				setTotalPages(res.data.total_pages);
			}
		}
		setCurPage(page);

    dispatch(AHideLoading());
	}

	const onSubmit = async (formData: any) => {
		const params={
			email: formData.email,
		}
		setFilterData(params);
		filter(params);
	}

	const handleChangePage = async (pageNumber: number) => {
		const params = {
			...filterData,
			page: pageNumber,
		}
		filter(params, pageNumber);
	}

	const createNew = async () => {
		setSelectedItem(null);
		setShowModal(true);
	}

	const viewDetail = (idx: number) => {
		setSelectedItem(items[idx]);
		setShowModal(true);
	}

	const handleSortTableColumn = (param: IHandleSortParam) => {
		dispatch(AShowLoading());
		setSortKey(param.orgKey);
		setSortType(param.sortType);
		if (items) {
			const sortedEmails = handleSortData(param, items);
			setItems(sortedEmails);
		}
		dispatch(AHideLoading());
	}

	return (
		<>
			<Form onSubmit={handleSubmit(onSubmit)} className="d-grid gap-3">
				<Row>
					<Col sm={2}>
						<Controller
							name="email"
							control={control}
							render={({ field, fieldState: { invalid, error } }) => (
								<Form.Group controlId="email">
									<Form.Label>Email</Form.Label>
									<Form.Control
										{...field}
									/>
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
			<div>
				<div>
					Domain: {emailSetting?.domain??''}
				</div>
				<div>
					Số mail tối đa: {emailSetting?.max_email??''}
				</div>
			</div>

			<Table bordered striped hover className='mt-4'>
				<thead className='table-primary'>
					<tr>
						<th scope="col" className='w-30'>#</th>
						<th scope="col" className='2-130'>
							<SortableHeader
								title='Email'
								orgKey='primary_email'
								sortKey={sortKey}
								handleSortTableColumn={handleSortTableColumn}
							/>
						</th>
						<th scope="col" className=''>
							<SortableHeader
								title='Họ'
								orgKey='first_name'
								sortKey={sortKey}
								handleSortTableColumn={handleSortTableColumn}
							/>
						</th>
						<th scope="col" className=''>
							<SortableHeader
								title='Tên'
								orgKey='last_name'
								sortKey={sortKey}
								handleSortTableColumn={handleSortTableColumn}
							/>
						</th>
						<th scope="col" className=''>
							<SortableHeader
								title='Trạng thái'
								orgKey='status'
								sortKey={sortKey}
								handleSortTableColumn={handleSortTableColumn}
							/>
						</th>
						<th scope="col" className=''>Số điện thoại</th>
					</tr>
				</thead>
					<tbody>
					{items && items?.length > 0 ? (
							items.map((item, idx) => (
								<tr key={idx + 1} className="cursor-pointer" onDoubleClick={() => viewDetail(idx)}>
									<th scope="row">{idx + 1}</th>
									<td>{item.primary_email}</td>
									<td>{item.first_name}</td>
									<td>{item.last_name}</td>
									<td>
										{(item.status && additionalData?.statuses[item.status]) ? (
												<>
													<Badge variant={additionalData.statuses[item.status].variant ?? ''} className='badge-md'>
														{additionalData.statuses[item.status].text}
													</Badge>{' '}
												</>
											) : (
												item.status
											)
										}
									</td>
									<td>{item.phone_number}</td>
								</tr>
							))
						) : (
							<tr><div className=''>{errorMsg}</div></tr>
					)}
				</tbody>
			</Table>
			
			<PaginationNormal
					totalPages={totalPages}
					curPage={curPage}
					handleChangePage={handleChangePage}
			/>

			{showModal && <CommonModal
					show={showModal}
					handleShow={setShowModal}
					selectedItem={selectedItem}
					refreshData={refreshData}
					emailSetting={emailSetting}
					fields={configData.fields}
					title="Email"
				/>
				}
		</>
	)
}


export async function getServerSideProps() {
	const	resEmail = await listEmails();
	if (isSuccessRequest(resEmail)) {
		const data = {
			items: resEmail.data,
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

EmailManagerPage.pageTitle = 'Quản lý khách hàng'
EmailManagerPage.activeLink = 'email_manager'
EmailManagerPage.breadcrumb = [
	{ text: "Quản lý khách hàng", link: "/email_manager" },
]

export default withAuth(EmailManagerPage)
