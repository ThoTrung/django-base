import { createSelector } from "reselect";

import reducers, { State } from "../reducers/index";

const getMyInfo = (state: State) => state.myInfo.data;

export const getSMyInfo = createSelector(getMyInfo, (data) => data);
