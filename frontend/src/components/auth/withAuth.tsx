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

import { AMyInfoRequest } from 'store/myInfo/actions'

const withAuth = (PageComponent: ExtendedNextPage) => {
	// Initialize wrapper component
	const WrapperComponent: ExtendedNextPage = (props) => {
		const token = useSelector(getSLoginToken);
		const dispatch = useDispatch();

		React.useEffect(() => {
		if (!token) {
			return Router.push(PAGE.loginPagePath)
		}
		// Check token and get my info
		dispatch(AMyInfoRequest())
		},[token]);
		return <PageComponent {...props} />
	}
	return Object.assign(WrapperComponent, PageComponent)
}

export default withAuth
