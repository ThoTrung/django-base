import {
  SHOW_LOADING,
  HIDE_LOADING,
} from "./actionTypes";

export interface IShowLoading {
  type: typeof SHOW_LOADING;
}
export interface IHideLoading {
  type: typeof HIDE_LOADING;
}

export type TLoading = 
  | IShowLoading
  | IHideLoading

export interface IState{
  loading: boolean;
}