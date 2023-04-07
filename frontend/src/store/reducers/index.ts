import { combineReducers } from 'redux'
import layoutReducer, { LayoutReducerState } from './layoutReducer'
import menuReducer, { MenuReducerState } from './menuReducer'
import offcanvasReducer, { OffcanvasReducerState } from './offcanvasReducer'
import breadcrumbReducer, { BreadcrumbReducerState } from './breadcrumbReducer'
import pageReducer, { PageReducerState } from './pageReducer'
import todoReducer, { loginReducer } from "../auth/reducer";
import { TodoState, ILoginState } from "../auth/types";

export interface State {
	layout: LayoutReducerState,
	breadcrumb: BreadcrumbReducerState,
	offcanvas: OffcanvasReducerState,
	menu: MenuReducerState,
	page: PageReducerState,
  todo: TodoState,
  login: ILoginState
}

const reducers = combineReducers({
	layout: layoutReducer,
	breadcrumb: breadcrumbReducer,
	offcanvas: offcanvasReducer,
	menu: menuReducer,
	page: pageReducer,
  todo: todoReducer,
  login: loginReducer,
})

export type AppState = ReturnType<typeof reducers>;
export default reducers
