import React from 'react'
import withAuth from 'components/auth/withAuth'
import type { ExtendedNextPage } from '@blueupcode/components/types'

const CreateJobPage: ExtendedNextPage = (props) => {
	
	return (
		<>
			Trang tạo job
		</>
	)
}

CreateJobPage.pageTitle = 'Tạo job'
CreateJobPage.activeLink = 'create_job'
CreateJobPage.breadcrumb = [
	{ text: "Tạo job", link: "/create_job" },
]

export default withAuth(CreateJobPage)
