import React from 'react'
import withAuth from 'components/auth/withAuth'
import type { ExtendedNextPage } from '@blueupcode/components/types'

const StatisticPage: ExtendedNextPage = (props) => {
	
	return (
		<>
			Developing ...
		</>
	)
}

StatisticPage.pageTitle = 'Thống kê'
StatisticPage.activeLink = 'statistic'
StatisticPage.breadcrumb = [
	{ text: "Thống kê", link: "/statistic" },
]

export default withAuth(StatisticPage)
