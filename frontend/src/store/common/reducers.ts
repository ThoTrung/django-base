import {
  SHOW_LOADING,
  HIDE_LOADING,
} from './actionTypes'
import { IState, TLoading } from './types'

const InitState = {
  loading: false,
}

const commonReducer = (state: IState = InitState, action: TLoading) => {
  switch (action.type) {
    case SHOW_LOADING:
      return {
        ...state,
        loading: true,
      }   
    case HIDE_LOADING:
      return {
        ...state,
        loading: false,
      }
    default:
      return state;
  }
}

export default commonReducer
