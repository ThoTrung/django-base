import { put, PutEffect, select, SelectEffect, takeEvery } from 'redux-saga/effects'
import { menuActiveLinkPartialChange } from 'store/actions'
import { State } from 'store/reducers'
import PAGE from 'config/page.config'

export const delay = (ms:number) => new Promise(res => setTimeout(res, ms))

export function* separatingActiveLink(): Generator<SelectEffect | PutEffect, void, string> {
	const activeLink: string = yield select((state: State) => state.menu.activeLink)
	const activeLinkPartial = activeLink?.split(PAGE.menuLinkSeparator) ?? []

	yield put(menuActiveLinkPartialChange(activeLinkPartial))
}

export function* helloSaga() {
  console.log('Hello Sagas!')
}

export function* incrementAsync() {
  yield delay(1000)
  yield put({ type: 'INCREMENT' })
}

export function* watchIncrementAsync() {
  yield takeEvery('INCREMENT_ASYNC', incrementAsync)
}