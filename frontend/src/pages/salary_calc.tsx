import React from 'react'
import withAuth from 'components/auth/withAuth'
import type { ExtendedNextPage } from '@blueupcode/components/types'

const SalaryCalcPage: ExtendedNextPage = (props) => {
	
	return (
		<>
			Developing ...
		</>
	)
}

SalaryCalcPage.pageTitle = 'Tính lương'
SalaryCalcPage.activeLink = 'salary_calc'
SalaryCalcPage.breadcrumb = [
	{ text: "Tính lương", link: "/salary_calc" },
]

export default withAuth(SalaryCalcPage)
