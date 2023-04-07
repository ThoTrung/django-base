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
  getPendingSelector,
  getTodosSelector,
  getErrorSelector,
	getSLoginPending,
	getSLoginToken,
} from "../store/auth/selectors";

const DashboardPage: ExtendedNextPage = () => {
	// const token = useSelector(getSLoginToken);
	// React.useEffect(() => {
	// 	console.log('redirect to dashboard', token);
	// 	if (!token) {
	// 		const redirectUrl = (Router.query.redirect as string) || PAGE.loginPagePath
	// 		Router.push(redirectUrl)
	// 	}
  // }, [token]);
	return (
		<>
			<Row>
				<Col xs="12">
					<Widget33 />
				</Col>
			</Row>
			<Row>
				<Col xl="4">
					<Row portletFill="md" className="h-100">
						<Col md="7" xl="12">
							<Widget22 />
						</Col>
						<Col md="5" xl="12">
							<Widget10 />
						</Col>
					</Row>
				</Col>
				<Col xl="4">
					<Row portletFill="md" className="h-100">
						<Col md="4" xl="12">
							<Widget28 />
						</Col>
						<Col md="4" xl="12">
							<Widget29 />
						</Col>
						<Col md="4" xl="12">
							<Widget34 />
						</Col>
					</Row>
				</Col>
				<Col xl="4">
					<Row portletFill="md" className="h-100">
						<Col md="6" xl="12">
							<Widget3 />
						</Col>
						<Col md="6" xl="12">
							<Row portletFill="sm">
								<Col sm="6">
									<Widget21 />
									<Widget16 />
								</Col>
								<Col sm="6">
									<Widget35 />
									<Widget18 />
								</Col>
							</Row>
						</Col>
					</Row>
				</Col>
			</Row>
			<Row portletFill="xl">
				<Col xl="4">
					<Widget27 />
				</Col>
				<Col xl="8">
					<Row portletFill="md">
						<Col md="6">
							<Widget13 />
							<Widget14 />
						</Col>
						<Col md="6">
							<Widget7 />
							<Widget15 />
						</Col>
					</Row>
				</Col>
			</Row>
		</>
	)
}

DashboardPage.pageTitle = 'Dashboard'
DashboardPage.activeLink = 'dashboard'
DashboardPage.breadcrumb = [
	{ text: "Dashboard", link: "/" },
]

// export default DashboardPage
export default withAuth(DashboardPage)
// export default withAuth(DashboardPage)
