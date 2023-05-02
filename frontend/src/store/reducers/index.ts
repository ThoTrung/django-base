import { combineReducers } from 'redux'
import layoutReducer, { LayoutReducerState } from './layoutReducer'
import menuReducer, { MenuReducerState } from './menuReducer'
import offcanvasReducer, { OffcanvasReducerState } from './offcanvasReducer'
import breadcrumbReducer, { BreadcrumbReducerState } from './breadcrumbReducer'
import pageReducer, { PageReducerState } from './pageReducer'
import loginReducer from "../auth/reducer";
import { ILoginState } from "../auth/types";
import myInfoReducer from 'store/myInfo/reducers';
import { IState as IMyInfoState } from 'store/myInfo/types';
import commonReducer from 'store/common/reducers';
import { IState as ICommonState } from 'store/myInfo/types'

export interface State {
	layout: LayoutReducerState,
	breadcrumb: BreadcrumbReducerState,
	offcanvas: OffcanvasReducerState,
	menu: MenuReducerState,
	page: PageReducerState,
  login: ILoginState,
	myInfo: IMyInfoState,
	common: ICommonState,
}

const reducers = combineReducers({
	layout: layoutReducer,
	breadcrumb: breadcrumbReducer,
	offcanvas: offcanvasReducer,
	menu: menuReducer,
	page: pageReducer,
  login: loginReducer,
	myInfo: myInfoReducer,
	common: commonReducer,
})

export type AppState = ReturnType<typeof reducers>;
export default reducers
