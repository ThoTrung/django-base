import requestInstance from "./base";

export interface IListFolderFromDisk {
  driverPath: string;
  dropboxPath: string;
  startTime: string;
  endTime: string;
}

export interface IOneFolder {
  path: string;
  lastModifiedFolder: string;
  files: string[];
}

export const listFolderFromDisk = async (params: IListFolderFromDisk) => {
  const res = await requestInstance.get('api/job-managers/list-folder-from-disk', {params});
  return res;
}
