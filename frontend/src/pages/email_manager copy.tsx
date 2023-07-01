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
	IEmail,
	IFilterEmail,
	listEmails,
	DEFAULT_FILTER_EMAIL,
	IEmailSetting,
	getEmailSetting,
} from 'store/request/email_manager';
import { param } from 'react-dom-factories';
import { useForm, Controller } from 'react-hook-form'
import * as yup from 'yup'
import { yupResolver } from '@hookform/resolvers/yup'
import EmailManagerModal from 'modals/common';
import { getSMyInfo } from 'store/myInfo/selectors';

export type IEmailProps = {
	data: {
		emails: IEmail[],
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

export type TPagingData = {
	total_pages: number;
	cur_page: number;
}

const handleChangePage = (pageNumber: number) => {
	console.log('--------', pageNumber)
}

const PaginationNormal = (props: any) => {
	const {pagingData, ...res} = props;
	const haftNumberOfDisplay = 3;
	let start = pagingData.cur_page - haftNumberOfDisplay;
	let end = pagingData.cur_page + haftNumberOfDisplay;
	if (start < 0) {
		const delta = 1 - start;
		start += delta;
		end += delta;
	}
	end = end <= pagingData.total_pages ? end : pagingData.total_pages;
	const paginationNumber = []
	while(start <= end){
		paginationNumber.push(start++);
	}
	return (
		<Pagination {...res}>
			<Pagination.Item> {'<'} </Pagination.Item>
			{paginationNumber.map((pageNumber: number) => (
				<Pagination.Item
					key={pageNumber}
					active={pageNumber === pagingData.cur_page}
					onClick={() => handleChangePage(pageNumber)}
				>
					{pageNumber}
				</Pagination.Item>
			))}
			<Pagination.Item> {'>'} </Pagination.Item>
		</Pagination>
	)
}


const EmailManagerPage: ExtendedNextPage<IEmailProps> = (props) => {
	const [showModal, setShowModal] = React.useState<boolean>(false);
	const [errorMsg, setErrorMsg] = React.useState<string>('');
	const [emails, setEmails] = React.useState<IEmail[]>(props.data.emails);
	const [selectedEmail, setSelectedEmail] = React.useState<IEmail | null>(null)
	const [sortKey, setSortKey] = React.useState<string>('');
	const [sortType, setSortType] = React.useState<string>('');
	const [emailSetting, setEmailSetting] = React.useState<IEmailSetting | null>(null);
	const [additionalData, setAdditionalData] = React.useState<TAdditionalData | null>(null)
	const [totalPages, setTotalPages] = React.useState<number>(0)

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

	const onSubmit = async (formData: IFilterEmail) => {
    dispatch(AShowLoading());

		const params={
			email: formData.email,
		}
		const res = await listEmails(params);
		if (isSuccessRequest(res)) {
			setEmails(res.data.results);
			if (res.data.additional_data) {
				setAdditionalData(res.data.additional_data)
			}
			if (res.data.total_pages) {
				setTotalPages(res.data.total_pages);
			}
		}

    dispatch(AHideLoading());
	}

	const createNew = async () => {
		setSelectedEmail(null);
		setShowModal(true);
	}

	const viewDetail = (idx: number) => {
		setSelectedEmail(emails[idx]);
		setShowModal(true);
	}

	const handleSortTableColumn = (param: IHandleSortParam) => {
		dispatch(AShowLoading());
		setSortKey(param.orgKey);
		setSortType(param.sortType);
		if (emails) {
			const sortedEmails = handleSortData(param, emails);
			setEmails(sortedEmails);
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
					{emails && emails?.length > 0 ? (
							emails.map((item, idx) => (
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
				pagingData = {{
					'total_pages': totalPages,
					'cur_page': 1
				}}
			/>

			{showModal && <EmailManagerModal
					show={showModal}
					handleShow={setShowModal}
					selectedEmail={selectedEmail}
					refreshData={refreshData}
					emailSetting={emailSetting}
				/>
				}
		</>
	)
}


export async function getServerSideProps() {
	const	resEmail = await listEmails();
	if (isSuccessRequest(resEmail)) {
		const data = {
			emails: resEmail.data,
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
