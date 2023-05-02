import { createSelector } from "reselect";

import reducers, { State } from "../reducers/index";

const getLoading = (state: State) => state.common.loading;

export const getSLoading = createSelector(getLoading, (loading) => loading);
