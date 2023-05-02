import React from 'react'
import withAuth from 'components/auth/withAuth'
import type { ExtendedNextPage } from '@blueupcode/components/types'

const ExportInvoicePage: ExtendedNextPage = (props) => {
	
	return (
		<>
			Developing ...
		</>
	)
}

ExportInvoicePage.pageTitle = 'Xuất hóa đơn'
ExportInvoicePage.activeLink = 'export_invoice'
ExportInvoicePage.breadcrumb = [
	{ text: "Xuất hóa đơn", link: "/export_invoice" },
]

export default withAuth(ExportInvoicePage)
