import { takeEvery, all, fork } from 'redux-saga/effects'
import { separatingActiveLink, helloSaga, watchIncrementAsync } from './menuSaga'
import loginSaga from "../auth/sagas";
import myInfoSaga from 'store/myInfo/sagas';


// function* rootSaga() {
  // 	yield all([helloSaga(), watchIncrementAsync()])
  // }
  
function* rootSaga() {
  yield takeEvery('MENU_ACTIVE_LINK_CHANGE', separatingActiveLink)
  yield all([loginSaga(), myInfoSaga()]);
}

export default rootSaga
