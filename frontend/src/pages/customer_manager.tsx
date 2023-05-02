import React from 'react'
import withAuth from 'components/auth/withAuth'
import type { ExtendedNextPage } from '@blueupcode/components/types'

const CustomerManagerPage: ExtendedNextPage = (props) => {
	
	return (
		<>
			Developing ...
		</>
	)
}

CustomerManagerPage.pageTitle = 'Quản lý khách hàng'
CustomerManagerPage.activeLink = 'customer_manager'
CustomerManagerPage.breadcrumb = [
	{ text: "Quản lý khách hàng", link: "/customer_manager" },
]

export default withAuth(CustomerManagerPage)
