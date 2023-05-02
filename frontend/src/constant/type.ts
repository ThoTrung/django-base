export const detailType = 'detail'
export const newType = 'new'
export const updateType = 'update'
export type modalType =
  typeof detailType |
  typeof newType |
  typeof updateType;
  
