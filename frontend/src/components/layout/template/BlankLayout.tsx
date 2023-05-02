import React from 'react'
import { Container, Structure } from '@blueupcode/components'
import LayoutFloatingButton from '../floating-button/FloatingButton'
import SimpleLoading from 'components/loading/simpleLoading'

const BlankLayout: React.FC = ({ children }) => {
	return (
		<>
			<SimpleLoading />
			<Structure type="holder">
				<Structure type="wrapper">
					<Structure type="content">
						<Container fluid className="g-4">{children}</Container>
					</Structure>
				</Structure>
			</Structure>
			{/* <LayoutFloatingButton /> */}
		</>
	)
}

export default BlankLayout
