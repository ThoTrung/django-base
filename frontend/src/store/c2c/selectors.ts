import { createSelector } from "reselect";

import reducers, { State } from "../reducers/index";

const getCreateJob = (state: State) => state.c2c.create_job;

export const getSCreateJob = createSelector(getCreateJob, (loading) => loading);
