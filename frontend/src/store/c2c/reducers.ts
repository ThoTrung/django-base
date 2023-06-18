import { AnyAction } from 'redux'
import {
  SET_CREATE_JOB_DATA,
  DELETE_CREATE_JOB_DATA,
} from './actionTypes'
import { IState, TData } from './types'

const InitState = {
  create_job: null
}

const c2cReducer = (state: IState = InitState, action: AnyAction) => {
  switch (action.type) {
    case SET_CREATE_JOB_DATA:
      return {
        ...state,
        create_job: action.payload,
      }   
    case DELETE_CREATE_JOB_DATA:
      return {
        ...state,
        create_job: null,
      }
    default:
      return state;
  }
}

export default c2cReducer
