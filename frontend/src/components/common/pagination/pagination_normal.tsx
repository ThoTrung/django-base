import React from 'react'

import { Pagination } from '@blueupcode/components'

export type TProps = {
	totalPages: number;
	curPage: number;
	handleChangePage: (pageNumber: number) => void
}


const PaginationNormal = (props: TProps) => {
	const [displayPages, setDisplayPages] = React.useState<number[]>([]);
	
	React.useEffect(() => {
			const haftNumberOfDisplay = 3;
			let start = props.curPage - haftNumberOfDisplay;
			let end = props.curPage + haftNumberOfDisplay;
			if (start < 1) {
				const delta = 1 - start;
				start += delta;
				end += delta;
			}
			end = end <= props.totalPages ? end : props.totalPages;
			const displayPagesTmp = []
			while(start <= end){
				displayPagesTmp.push(start++);
			}
			setDisplayPages(displayPagesTmp)
		}, [props.curPage, props.totalPages])

	const handleChangePage = (pageNumber: number) => {
		props.handleChangePage(pageNumber);
		console.log('--------', pageNumber)
	}

	return (
		<Pagination>
			<Pagination.Item> {'<'} </Pagination.Item>
			{displayPages.map((pageNumber: number) => (
				<Pagination.Item
					key={pageNumber}
					active={pageNumber === props.curPage}
					onClick={() => handleChangePage(pageNumber)}
				>
					{pageNumber}
				</Pagination.Item>
			))}
			<Pagination.Item> {'>'} </Pagination.Item>
		</Pagination>
	)
}

export default PaginationNormal;
