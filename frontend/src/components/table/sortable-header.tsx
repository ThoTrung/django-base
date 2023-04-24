import React from 'react'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import {
	faAngleDown,
	faAngleUp,
} from '@fortawesome/free-solid-svg-icons'
export interface IHandleSortParam {
	orgKey: string,
	sortType: string,
}

export interface ISortableHeaderProps {
	title: string,
	orgKey: string,
	sortKey: string,
	handleSortTableColumn: (param: IHandleSortParam) => void
}

const SortableHeader:React.FC<ISortableHeaderProps> = (props) => {
	const [sortType, setSortType] = React.useState<string>('DESC');

	const localHanldeSortTableColumn = () => {
		const newSortType = sortType === 'DESC' ? 'ASC' : 'DESC';
		setSortType(newSortType);
		props.handleSortTableColumn({
			sortType: newSortType,
			orgKey: props.orgKey
		})
	}

	React.useEffect(() => {
		if (props.orgKey !== props.sortKey) {
			setSortType('');
		}
	}, [props.sortKey, props.orgKey])
	return (
		<div className='cursor-pointer d-flex' onClick={localHanldeSortTableColumn}>
			<div>{props.title}</div>
			{props.orgKey === props.sortKey &&
				<div className='ps-3 font-size-14px'>
					<FontAwesomeIcon icon={sortType === 'DESC' ? faAngleDown : faAngleUp} /> 
				</div>
			}
		</div>
	)
}

export default SortableHeader