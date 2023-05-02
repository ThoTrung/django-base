import React from 'react'
import withAuth from 'components/auth/withAuth'
import type { ExtendedNextPage } from '@blueupcode/components/types'

const UserManagerPage: ExtendedNextPage = (props) => {
	
	return (
		<>
			Developing ...
		</>
	)
}

UserManagerPage.pageTitle = 'Quản lý user'
UserManagerPage.activeLink = 'user_manager'
UserManagerPage.breadcrumb = [
	{ text: "Quản lý user", link: "/user_manager" },
]

export default withAuth(UserManagerPage)
