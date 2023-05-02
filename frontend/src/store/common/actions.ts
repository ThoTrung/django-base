import {
  SHOW_LOADING,
  HIDE_LOADING,
} from './actionTypes'

import {
  IShowLoading,
  IHideLoading,
} from "./types"

export const AShowLoading = (): IShowLoading => ({
  type: SHOW_LOADING,
})

export const AHideLoading = (): IHideLoading => ({
  type: HIDE_LOADING,
})
