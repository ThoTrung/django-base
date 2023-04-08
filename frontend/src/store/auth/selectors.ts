import { createSelector } from "reselect";

import reducers, { State } from "../reducers/index";

const getLoginToken = (state: State) => state.login.token;
const getLoginPending = (state: State) => state.login.pending;
const getLoginError = (state: State) => state.login.error;

export const getSLoginToken = createSelector(getLoginToken, (token) => token);
export const getSLoginPending = createSelector(getLoginPending, (pending) => pending);
export const getSLoginError = createSelector(getLoginError, (error) => error);
