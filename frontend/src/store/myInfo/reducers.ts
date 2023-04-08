import {
  GET_MYINFO_REQUEST,
  GET_MYINFO_SUCCESS,
  GET_MYINFO_FAILURE,
} from './actionTypes'
import { AnyAction } from 'redux'
import {
  IState
} from './types'

const InitState = {
  pending: false,
  error: null,
  data: {
    email: 'example@gmail.com',
    name: 'example',
  }
}

const myInfoReducer = (state: IState = InitState, action: AnyAction) => {
  switch (action.type) {
    case GET_MYINFO_REQUEST:
      return {
        ...state,
        pending: true,
      }   
    case GET_MYINFO_SUCCESS:
      return {
        ...state,
        pending: false,
        data: action.payload,
        error: null,
      }
    case GET_MYINFO_FAILURE:
      return {
        ...state,
        pending: false,
        data: null,
        error: action.payload.error,
      }
    default:
      return state;
  }
}

export default myInfoReducer
