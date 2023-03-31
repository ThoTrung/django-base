import { createSelector } from "reselect";

import appReducer, { State } from "../index";

const getPending = (state: State) => state.todo.pending;

const getTodos = (state: State) => state.todo.todos;

const getError = (state: State) => state.todo.error;

export const getTodosSelector = createSelector(getTodos, (todos) => todos);

export const getPendingSelector = createSelector(
  getPending,
  (pending) => pending
);

export const getErrorSelector = createSelector(getError, (error) => error);
