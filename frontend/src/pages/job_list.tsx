import React from 'react'
import withAuth from 'components/auth/withAuth'
import type { ExtendedNextPage } from '@blueupcode/components/types'

const JobListPage: ExtendedNextPage = (props) => {
	
	return (
		<>
			Developing ...
		</>
	)
}

JobListPage.pageTitle = 'Danh sách job'
JobListPage.activeLink = 'job_list'
JobListPage.breadcrumb = [
	{ text: "Danh sách job", link: "/job_list" },
]

export default withAuth(JobListPage)
