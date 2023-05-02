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

const withGuest = (PageComponent: ExtendedNextPage) => {
	const WrapperComponent: ExtendedNextPage = (props) => {
		const token = useSelector(getSLoginToken);
		React.useEffect(() => {
			if (token) {
				return Router.push((Router.query.redirect as string) || PAGE.homePagePath)
			}
		}, [token]);
		return <PageComponent {...props} />
	}
	// Inject page component attributes to wrapper component
	return Object.assign(WrapperComponent, PageComponent)
}

export default withGuest
