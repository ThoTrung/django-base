import React from 'react'
import withAuth from 'components/auth/withAuth'
import { Row, Col, Portlet, Form, Button, InputGroup } from '@blueupcode/components'
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
import DateTimePicker from 'react-datetime'

// https://upmin-react.blueupcode.com/

const DashboardPage: ExtendedNextPage = () => {
	return (
		<>
			<Form.Group as={Row} controlId="colFormLabelLg">
				<Col sm={12} className='d-flex flex-row'>
					<Form.Label column className='miw-60'>
						Dropbox:
					</Form.Label>
					<Form.Label column className='ps-3 miw-90'>
						E:\Dropbox\
					</Form.Label>
					<Form.Control placeholder="Your path" className='ms-1' />
					<Button variant={'primary'} className="ms-3 text-nowrap miw-80">
						Thay đổi
					</Button>{' '}
				</Col>
				<Col sm={12} className='d-flex flex-row mt-3'>
					<Form.Label column className='miw-60'>
						Driver:
					</Form.Label>
					<Form.Label column className='ps-3 miw-90'>
						E:\MyDrive\
					</Form.Label>
					<Form.Control placeholder="Your path" className='ms-1' />
					<Button variant={'primary'} className="ms-3 text-nowrap miw-80">
						Thay đổi
					</Button>{' '}
				</Col>
				<Col sm={12} className='d-flex flex-row mt-3'>
					<Form.Label column className='me-3 maw-140'>
						Thời gian bắt đầu
					</Form.Label>
					<DateTimePicker closeOnSelect />
					<Form.Label column className='ms-5 me-3 maw-140'>
						Thời gian kết thúc
					</Form.Label>
					<DateTimePicker closeOnSelect />
					<Button variant={'success'} className="ms-3 text-nowrap miw-80">
						Tìm kiếm
					</Button>{' '}
				</Col>
			</Form.Group>
		</>
	)
}

DashboardPage.pageTitle = 'Thông tin cloud'
DashboardPage.activeLink = 'cloud_info'
DashboardPage.breadcrumb = [
	{ text: "Thông tin cloud", link: "/" },
]

export default withAuth(DashboardPage)
