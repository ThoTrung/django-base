import type { Direction } from '@blueupcode/components/types'
import { LayoutNames } from 'components/layout/getLayout'

/*
 * Page Configuration
 * you can customize general page configuration in the object below
 */

const PAGE: PAGE_INTERFACE = {
	appName: 'Upmin',
	favicon: '/images/favicon.ico',
	enableContainerFluid: true,
	defaultLayoutName: 'custom',
	defaultDirection: 'ltr',
	menuLinkSeparator: '.',
	loginPagePath: '/login',
	homePagePath: '/',
}

export interface PAGE_INTERFACE {
	appName: string
	favicon: string
	enableContainerFluid: boolean
	defaultLayoutName: LayoutNames
	defaultDirection: Direction
	menuLinkSeparator: string
	loginPagePath: string
	homePagePath: string
}

export default PAGE
