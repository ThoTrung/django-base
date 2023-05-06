import React from 'react'
import Router from 'next/router'
import authVerifyCookie from './authVerifyCookie'
import PAGE from 'config/page.config'
import type { AdditionalNextPageProps, ExtendedNextPage } from '@blueupcode/components/types'
import type { NextPageContext } from 'next'
import { useDispatch, useSelector } from "react-redux";
import {
	getSLoginToken,
} from '../../store/auth/selectors';

import { getSMyInfo } from 'store/myInfo/selectors'
import { AMyInfoRequest } from 'store/myInfo/actions'


const withAuth = (PageComponent: ExtendedNextPage) => {

	console.log('PageComponent.activeLink', PageComponent.activeLink)

	// Initialize wrapper component
	const WrapperComponent: ExtendedNextPage = (props) => {
		const token = useSelector(getSLoginToken);
		const myInfo = useSelector(getSMyInfo);
		const [permissions, setPermissions] = React.useState<string[]>((myInfo && myInfo.permissions) ? myInfo.permissions : []);
		const dispatch = useDispatch();
		if (permissions.length === 0 && myInfo && myInfo.permissions?.length > 0) {
			setPermissions(myInfo.permissions);
		}
		console.log('----------------------', myInfo ,permissions, PageComponent.activeLink)


		React.useEffect(() => {
			if (!token) {
				return Router.push(PAGE.loginPagePath)
			}
			if (!PageComponent.activeLink || (permissions.length > 0 && !permissions.includes(PageComponent.activeLink))) {
				return Router.push(`/${permissions[0]}`)
			}
			// Check token and get my info
			dispatch(AMyInfoRequest())
		},[token, permissions]);
		return <PageComponent {...props} />
	}
	return Object.assign(WrapperComponent, PageComponent)
}

export default withAuth
