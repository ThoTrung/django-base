import React from 'react'
import DefaultLayout from './template/DefaultLayout'
import BackgroundLayout from './template/BackgroundLayout'
import BlankLayout from './template/BlankLayout'
import CustomLayout from './template/CustomLayout'
import PAGE from 'config/page.config'

export type LayoutType = React.ElementType

export type LayoutNames = 'default' | 'background' | 'blank' | 'custom'

export type LayoutOptionsInterface = {
	[layoutName in LayoutNames]: LayoutType
}

export const layoutOptions: LayoutOptionsInterface = {
	default: DefaultLayout,
	background: BackgroundLayout,
	blank: BlankLayout,
	custom: CustomLayout,
}

export default function getLayout(layoutName: LayoutNames): LayoutType {
	if (layoutName in layoutOptions) {
		return layoutOptions[layoutName]
	}

	return layoutOptions[PAGE.defaultLayoutName]
}
