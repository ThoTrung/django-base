import React from 'react'
import withAuth from 'components/auth/withAuth'
import { Row, Col } from '@blueupcode/components'
import Widget3 from 'components/widgets/Widget3'
import Widget7 from 'components/widgets/Widget7'
import Widget10 from 'components/widgets/Widget10'
import Widget13 from 'components/widgets/Widget13'
import Widget14 from 'components/widgets/Widget14'
import Widget15 from 'components/widgets/Widget15'
import Widget16 from 'components/widgets/Widget16'
import Widget18 from 'components/widgets/Widget18'
import Widget21 from 'components/widgets/Widget21'
import Widget22 from 'components/widgets/Widget22'
import Widget27 from 'components/widgets/Widget27'
import Widget28 from 'components/widgets/Widget28'
import Widget29 from 'components/widgets/Widget29'
import Widget33 from 'components/widgets/Widget33'
import Widget34 from 'components/widgets/Widget34'
import Widget35 from 'components/widgets/Widget35'
import type { ExtendedNextPage } from '@blueupcode/components/types'
import Router from 'next/router'
import PAGE from 'config/page.config'
import { useDispatch, useSelector } from "react-redux";
import {
	getSLoginPending,
	getSLoginToken,
} from "../store/auth/selectors";

const DashboardPage: ExtendedNextPage = () => {
	return (
		<>
		</>
	)
}

DashboardPage.pageTitle = 'Dashboard'
DashboardPage.activeLink = 'dashboard'
DashboardPage.breadcrumb = [
	{ text: "Dashboard", link: "/" },
]

export default withAuth(DashboardPage)
