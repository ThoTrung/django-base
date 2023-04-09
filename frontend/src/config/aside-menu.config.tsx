import { ReactNode } from 'react'
import { Badge } from '@blueupcode/components'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import {
	faAdjust,
	faChartPie,
	faUsers,
	faDesktop,
	faDice,
	faIcons,
	faPalette,
	faMoneyBill1,
	faFileInvoiceDollar,
	faChartSimple,
	faPlus,
	faList,
	faCloud,
	faUserCheck,
	faPeopleRoof,
} from '@fortawesome/free-solid-svg-icons'
//https://fontawesome.com/search
/*
 * Aside Menu Configuration
 * the object below is representation of the side navigation menu configuration
 * there are some property you can use to customize your menu
 */

const ASIDE_MENU: ASIDE_MENU_INTERFACE = [
	{
		type: 'link',
		name: 'user_manager',
		title: 'Quản lý user',
		link: '/user_manager',
		icon: <FontAwesomeIcon icon={faUsers} />,
	},
	{
		type: 'link',
		name: 'role_manager',
		title: 'Quản lý role',
		link: '/role_manager',
		icon: <FontAwesomeIcon icon={faPeopleRoof} />,
	},
	{
		type: 'link',
		name: 'customer_manager',
		title: 'Quản lý khách hàng',
		link: '/customer_manager',
		icon: <FontAwesomeIcon icon={faUserCheck} />,
	},
	{
		type: 'link',
		name: 'cloud_info',
		title: 'Thông tin cloud',
		link: '/',
		icon: <FontAwesomeIcon icon={faCloud} />,
	},
	{
		type: 'link',
		name: 'create_job',
		title: 'Tạo Job',
		link: '/create_job',
		icon: <FontAwesomeIcon icon={faPlus} />,
	},
	{
		type: 'link',
		name: 'job_list',
		title: 'Danh sách job',
		link: '/job_list',
		icon: <FontAwesomeIcon icon={faList} />,
	},
	{
		type: 'link',
		name: 'statistic',
		title: 'Thống kê',
		link: '/statistic',
		icon: <FontAwesomeIcon icon={faChartSimple} />,
	},
	{
		type: 'link',
		name: 'salary_calc',
		title: 'Tính lương',
		link: '/salary_calc',
		icon: <FontAwesomeIcon icon={faMoneyBill1} />,
	},
	{
		type: 'link',
		name: 'export_invoice',
		title: 'Xuất hóa đơn',
		link: '/export_invoice',
		icon: <FontAwesomeIcon icon={faFileInvoiceDollar} />,
	},
]

export type ASIDE_MENU_INTERFACE = Array<
	ASIDE_MENU_LINK_INTERFACE | ASIDE_MENU_GROUP_INTERFACE | ASIDE_MENU_SECTION_INTERFACE
>

export interface ASIDE_MENU_LINK_INTERFACE {
	type: 'link'
	name: string
	title: string
	link: string
	icon?: ReactNode
	addon?: ReactNode
}

export interface ASIDE_MENU_SECTION_INTERFACE {
	type: 'section'
	name: string
	title: string
	child: Array<ASIDE_MENU_LINK_INTERFACE | ASIDE_MENU_GROUP_INTERFACE>
}

export interface ASIDE_MENU_GROUP_INTERFACE {
	type: 'group'
	name: string
	title: string
	icon?: ReactNode
	child: Array<ASIDE_MENU_LINK_INTERFACE | ASIDE_MENU_GROUP_INTERFACE>
}

export type ASIDE_MENU_ITEM_TYPES = 'link' | 'section' | 'group'

export default ASIDE_MENU
