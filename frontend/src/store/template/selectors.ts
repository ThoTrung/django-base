import { createSelector } from "reselect";

import reducers, { State } from "../reducers/index";

const getPending = (state: State) => state.todo.pending;

const getTodos = (state: State) => state.todo.todos;

const getError = (state: State) => state.todo.error;

export const getTodosSelector = createSelector(getTodos, (todos) => todos);

export const getPendingSelector = createSelector(
  getPending,
  (pending) => pending
);

export const getErrorSelector = createSelector(getError, (error) => error);


const getLoginToken = (state: State) => state.login.token;
const getLoginPending = (state: State) => state.login.pending;
const getLoginError = (state: State) => state.login.error;

export const getSLoginToken = createSelector(getLoginToken, (token) => token);
export const getSLoginPending = createSelector(getLoginPending, (pending) => pending);
export const getSLoginError = createSelector(getLoginError, (error) => error);
