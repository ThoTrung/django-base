import { all } from 'axios'
import { takeEvery } from 'redux-saga/effects'
import { separatingActiveLink, helloSaga, watchIncrementAsync } from './menuSaga'

function* rootSaga() {
	yield takeEvery('MENU_ACTIVE_LINK_CHANGE', separatingActiveLink)
	yield all([helloSaga(), watchIncrementAsync()])
}

export default rootSaga
