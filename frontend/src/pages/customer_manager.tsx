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
	ICreateCustomer,
	ICustomer,
	IFilterCustomer,
	listCustomers,
	DEFAULT_FILTER_CUSTOMER,
} from 'store/request/customer_manager';
import { param } from 'react-dom-factories';
import { useForm, Controller } from 'react-hook-form'
import * as yup from 'yup'
import { yupResolver } from '@hookform/resolvers/yup'
import CustomerManagerModal from 'modals/customer_manager';

export type ICustomerProps = {
	data: {
		customers: ICustomer[],
	}
};

const validationSchema = yup.object().shape({
	// No validate need for filter
})

const CustomerManagerPage: ExtendedNextPage<ICustomerProps> = (props) => {
	const [showModal, setShowModal] = React.useState<boolean>(false);
	const [errorMsg, setErrorMsg] = React.useState<string>('');
	const [customers, setCustomers] = React.useState<ICustomer[]>(props.data.customers);
	const [selectedCustomer, setSelectedCustomer] = React.useState<ICustomer | null>(null)
	const [sortKey, setSortKey] = React.useState<string>('');
	const [sortType, setSortType] = React.useState<string>('');
	const filterSubmitBtnRef = React.useRef<HTMLButtonElement>(null);

	const dispatch = useDispatch();

  const {control, handleSubmit} = useForm<IFilterCustomer>({
    resolver: yupResolver(validationSchema),
		defaultValues: DEFAULT_FILTER_CUSTOMER,
  })

	const refreshData = () => {
		if (filterSubmitBtnRef.current) {
			filterSubmitBtnRef.current.click()
		}
	}

	const onSubmit = async (formData: IFilterCustomer) => {
    dispatch(AShowLoading());

		const params={
			name: formData.name,
			email: formData.email,
		}
		console.log(params)
		const res = await listCustomers(params);
		if (isSuccessRequest(res)) {
			setCustomers(res.data);
		}

    dispatch(AHideLoading());
	}

	const createNew = async () => {
		setSelectedCustomer(null);
		setShowModal(true);
	}

	const viewDetail = (idx: number) => {
		setSelectedCustomer(customers[idx]);
		setShowModal(true);
	}

	const handleSortTableColumn = (param: IHandleSortParam) => {
		dispatch(AShowLoading());
		setSortKey(param.orgKey);
		setSortType(param.sortType);
		if (customers) {
			const sortedCustomers = handleSortData(param, customers);
			setCustomers(sortedCustomers);
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
									<Form.Label>Tên khách hàng</Form.Label>
									<Form.Control
										{...field}
									/>
								</Form.Group>
							)}
						/>
					</Col>
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

			<Table bordered striped hover className='mt-4'>
				<thead className='table-primary'>
					<tr>
						<th scope="col" className='w-30'>#</th>
						<th scope="col" className='2-130'>
							<SortableHeader
								title='Mã Khách hàng'
								orgKey='code'
								sortKey={sortKey}
								handleSortTableColumn={handleSortTableColumn}
							/>
						</th>
						<th scope="col" className=''>
							<SortableHeader
								title='Tên khách hàng'
								orgKey='name'
								sortKey={sortKey}
								handleSortTableColumn={handleSortTableColumn}
							/>
						</th>
						<th scope="col" className=''>
							<SortableHeader
								title='Email'
								orgKey='email'
								sortKey={sortKey}
								handleSortTableColumn={handleSortTableColumn}
							/>
						</th>
						<th scope="col" className=''>Múi giờ/bang</th>
						<th scope="col" className=''>Số expose</th>
						<th scope="col" className=''>Style cố định</th>
						<th scope="col" className=''>Tên thanh toán</th>
						<th scope="col" className=''>Số ĐT</th>
						<th scope="col" className=''>Kênh liên lạc</th>
						<th scope="col" className=''>Giá KH</th>
						<th scope="col" className=''>Giá editor</th>
					</tr>
				</thead>
					<tbody>
					{customers && customers?.length > 0 ? (
							customers.map((item, idx) => (
								<tr key={idx + 1} className="cursor-pointer" onDoubleClick={() => viewDetail(idx)}>
									<th scope="row">{idx + 1}</th>
									<td>{item.code}</td>
									<td>{item.name}</td>
									<td>{item.email}</td>
									<td>{item.state}</td>
									<td>{item.expose}</td>
									<td>{item.style}</td>
									<td>{item.pay_name}</td>
									<td>{item.phone_number}</td>
									<td>{item.contact_channel}</td>
									<td>{item.customer_price}</td>
									<td>{item.editor_price}</td>
								</tr>
							))
						) : (
							<tr><div className=''>{errorMsg}</div></tr>
					)}
				</tbody>
			</Table>
			{showModal && <CustomerManagerModal
					show={showModal}
					handleShow={setShowModal}
					selectedCustomer={selectedCustomer}
					refreshData={refreshData}
				/>
				}
		</>
	)
}


export async function getServerSideProps() {
	const	resCustomer = await listCustomers();
	if (isSuccessRequest(resCustomer)) {
		const data = {
			customers: resCustomer.data,
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

CustomerManagerPage.pageTitle = 'Quản lý khách hàng'
CustomerManagerPage.activeLink = 'customer_manager'
CustomerManagerPage.breadcrumb = [
	{ text: "Quản lý khách hàng", link: "/customer_manager" },
]

export default withAuth(CustomerManagerPage)
