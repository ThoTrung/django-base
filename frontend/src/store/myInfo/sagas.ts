import { all, call, put, takeLatest } from "redux-saga/effects";
import { IMyInfo } from "./types"
import { GET_MYINFO_REQUEST } from "./actionTypes";
import requestInstance from "../request/base"
import { AMyInfoFailure, AMyInfoSuccess } from "./actions";


const getMyInfo = () => {
  return requestInstance.get<IMyInfo>('api/user/me');
}

function* requestMyInfo() {
  try {
    const res = yield call(getMyInfo);
    console.log('myInfo .... ', res);
    yield put(
      AMyInfoSuccess({...res.data})
    )
  } catch(e:any) {
    console.log(e.message);
    yield put(
      AMyInfoFailure({
        error: e.message
      })
    )
  }
}

function* myInfoSaga() {
  yield all([takeLatest(GET_MYINFO_REQUEST, requestMyInfo)]);
}

export default myInfoSaga;
