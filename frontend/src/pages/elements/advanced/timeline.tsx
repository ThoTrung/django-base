import React from 'react'
import withAuth from 'components/auth/withAuth'
import { Row, Col, Portlet, Marker, Timeline, RichList, Avatar, Badge } from '@blueupcode/components'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faCog, faRocket, faStar } from '@fortawesome/free-solid-svg-icons'
import Link from 'next/link'
import type { ExtendedNextPage } from '@blueupcode/components/types'

const TimelinePage: ExtendedNextPage = () => {
	return (
		<Row>
			<Col md={6}>
				{/* BEGIN Portlet */}
				<Portlet>
					<Portlet.Header bordered>
						<Portlet.Title>Basic</Portlet.Title>
					</Portlet.Header>
					<Portlet.Body>
						<p>
							<strong>Timeline</strong> can be used for listing agenda. Use{' '}
							<Link href="/elements/base/marker">marker</Link> as the timeline pin. Put your content into{' '}
							<code>Timeline.Item</code>.
						</p>
						{/* BEGIN Timeline */}
						<Timeline>
							<Timeline.Item pin={<Marker type="dot" variant="primary" />}>
								<p className="mb-0">Lorem ipsum dolor sit amit</p>
							</Timeline.Item>
							<Timeline.Item pin={<Marker type="dot" variant="success" />}>
								<p className="mb-0">
									Lorem ipsum dolor sit amit,consectetur eiusmdd tempor incididunt ut labore et dolore magna
								</p>
							</Timeline.Item>
							<Timeline.Item pin={<Marker type="dot" variant="danger" />}>
								<p className="mb-0">
									Lorem ipsum dolor sit amit,consectetur eiusmdd tempor incididunt ut labore et dolore magna elit enim
									at minim veniam quis nostrud
								</p>
							</Timeline.Item>
						</Timeline>
						{/* END Timeline */}
					</Portlet.Body>
				</Portlet>
				{/* END Portlet */}
				{/* BEGIN Portlet */}
				<Portlet>
					<Portlet.Header bordered>
						<Portlet.Title>More content</Portlet.Title>
					</Portlet.Header>
					<Portlet.Body>
						<p>
							Use your creativity to make a more complex timeline. In the example below, we use{' '}
							<Link href="/elements/advanced/rich-list">rich list</Link> to appear bordered and clickable timeline item.
						</p>
						{/* BEGIN Timeline */}
						<Timeline as={RichList} bordered>
							<Timeline.Item pin={<Marker type="circle" variant="primary" />}>
								{/* BEGIN Rich List */}
								<RichList.Item>
									<RichList.Addon addonType="prepend">
										{/* BEGIN Avatar */}
										<Avatar display>
											<FontAwesomeIcon icon={faStar} />
										</Avatar>
										{/* END Avatar */}
									</RichList.Addon>
									<RichList.Content>
										<RichList.Title>Consectetur</RichList.Title>
										<RichList.Subtitle>Dapibus ac facilisis in</RichList.Subtitle>
									</RichList.Content>
									<RichList.Addon addonType="append">
										<Badge variant="success">9+</Badge>
									</RichList.Addon>
								</RichList.Item>
								{/* END Rich List */}
							</Timeline.Item>
							<Timeline.Item pin={<Marker type="circle" variant="success" />}>
								{/* BEGIN Rich List */}
								<RichList.Item>
									<RichList.Addon addonType="prepend">
										{/* BEGIN Avatar */}
										<Avatar display>
											<FontAwesomeIcon icon={faRocket} />
										</Avatar>
										{/* END Avatar */}
									</RichList.Addon>
									<RichList.Content>
										<RichList.Title>Porta</RichList.Title>
										<RichList.Paragraph>
											Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut
											labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris
											nisi ut aliquip ex ea commodo consequat.
										</RichList.Paragraph>
										<RichList.Subtitle>Cras justo odio</RichList.Subtitle>
									</RichList.Content>
								</RichList.Item>
								{/* END Rich List */}
							</Timeline.Item>
							<Timeline.Item pin={<Marker type="circle" variant="danger" />}>
								{/* BEGIN Rich List */}
								<RichList.Item>
									<RichList.Addon addonType="prepend">
										{/* BEGIN Avatar */}
										<Avatar display>
											<FontAwesomeIcon icon={faCog} />
										</Avatar>
										{/* END Avatar */}
									</RichList.Addon>
									<RichList.Content>
										<RichList.Title>Vestibulum</RichList.Title>
										<RichList.Subtitle>Morbi leo risus</RichList.Subtitle>
									</RichList.Content>
									<RichList.Addon addonType="append">
										<Badge variant="info">new</Badge>
									</RichList.Addon>
								</RichList.Item>
								{/* END Rich List */}
							</Timeline.Item>
						</Timeline>
						{/* BEGIN Timeline */}
					</Portlet.Body>
				</Portlet>
				{/* END Portlet */}
			</Col>
			<Col md={6}>
				{/* BEGIN Portlet */}
				<Portlet>
					<Portlet.Header bordered>
						<Portlet.Title>Time</Portlet.Title>
					</Portlet.Header>
					<Portlet.Body>
						<p>
							Add time information to your timeline by setting <code>time</code> property and you must add{' '}
							<code>timed</code> property to <code>Timeline</code> component.
						</p>
						{/* BEGIN Timeline */}
						<Timeline timed>
							<Timeline.Item time="12.20" pin={<Marker type="dot" variant="primary" />}>
								<p className="mb-0">Lorem ipsum dolor sit amit</p>
							</Timeline.Item>
							<Timeline.Item time="13.00" pin={<Marker type="dot" variant="success" />}>
								<p className="mb-0">
									Lorem ipsum dolor sit amit,consectetur eiusmdd tempor incididunt ut labore et dolore magna
								</p>
							</Timeline.Item>
							<Timeline.Item time="14.05" pin={<Marker type="dot" variant="danger" />}>
								<p className="mb-0">
									Lorem ipsum dolor sit amit,consectetur eiusmdd tempor incididunt ut labore et dolore magna elit enim
									at minim veniam quis nostrud
								</p>
							</Timeline.Item>
						</Timeline>
						{/* END Timeline */}
					</Portlet.Body>
				</Portlet>
				{/* END Portlet */}
				{/* BEGIN Portlet */}
				<Portlet>
					<Portlet.Header bordered>
						<Portlet.Title>Zigzag</Portlet.Title>
					</Portlet.Header>
					<Portlet.Body>
						<p>
							We have one more timeline version, you just need to add <code>zigzag</code> property to default timeline
							elements to appear like below.
						</p>
						{/* BEGIN Timeline */}
						<Timeline zigzag>
							<Timeline.Item pin={<Marker type="circle" variant="primary" />}>
								<p className="mb-0">
									Lorem ipsum dolor sit amit,consectetur eiusmdd tempor incididunt ut labore et dolore magna elit enim
									at minim veniam quis nostrud
								</p>
							</Timeline.Item>
							<Timeline.Item pin={<Marker type="circle" variant="success" />}>
								<p className="mb-0">
									Lorem ipsum dolor sit amit,consectetur eiusmdd tempor incididunt ut labore et dolore magna
								</p>
							</Timeline.Item>
							<Timeline.Item pin={<Marker type="circle" variant="danger" />}>
								<p className="mb-0">
									Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore
									et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut
									aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum
									dolore eu fugiat nulla pariatur.
								</p>
							</Timeline.Item>
							<Timeline.Item pin={<Marker type="circle" variant="info" />}>
								<p className="mb-0">
									Lorem ipsum dolor sit amit,consectetur eiusmdd tempor incididunt ut labore et dolore magna
								</p>
							</Timeline.Item>
						</Timeline>
						{/* END Timeline */}
					</Portlet.Body>
				</Portlet>
				{/* END Portlet */}
			</Col>
		</Row>
	)
}

TimelinePage.pageTitle = 'Timeline'
TimelinePage.activeLink = 'elements.advanced.timeline'
TimelinePage.breadcrumb = [
	{ text: 'Dashboard', link: '/' },
	{ text: 'Elements' },
	{ text: 'Advanced' },
	{ text: 'Timeline', link: '/elements/advanced/timeline' },
]

export default withAuth(TimelinePage)
