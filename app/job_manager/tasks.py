import pathlib #https://realpython.com/get-all-files-in-directory-python/
from job_manager.models import UserSettingJob, JobManager, JobStatus
import datetime

from celery import shared_task

@shared_task
def checkJob():
    DRIVER_FOLDER = '/LocalDrive'
    DROPBOX_FOLDER = '/LocalDropbox'
    INPUT_FOLOER = 'INPUT'

    notAJobStatus = JobStatus.objects.filter(key='not_a_job').first()
    newJobStatus = JobStatus.objects.filter(key='new').first()

    driverFolder = pathlib.Path(DRIVER_FOLDER)
    for customerFolder in driverFolder.iterdir():

        if customerFolder.is_dir():
            print ('customerFolder', customerFolder.resolve())
            for inputFolder in customerFolder.iterdir():
                if inputFolder.is_dir() and inputFolder.name == INPUT_FOLOER:
                    print ('inputFolder', inputFolder.resolve())
                    for jobFolder in inputFolder.iterdir():
                        if jobFolder.is_dir():
                            # files = [str(file.resolve()) for file in jobFolder.rglob("*")]
                            files = [file for file in jobFolder.rglob("*")]
                            if len(files) > 0:
                                jobPath = jobFolder.resolve()
                                existedJobs = JobManager.objects.filter(path=jobPath)
                                if len(existedJobs) > 0:
                                    existedFiles = []
                                    for existedJob in existedJobs:
                                        existedFiles += existedJob.files
                                    newFiles = list(set(files) - set(existedFiles))
                                    if len(newFiles) > 0:
                                        existedNotAJob = existedJobs.filter(status=notAJobStatus).first()
                                        if existedNotAJob:
                                            existedNotAJob.files += newFiles
                                            existedNotAJob.checked_time = datetime.datetime.now()
                                            existedNotAJob.save()
                                        else:
                                            JobManager.objects.create(
                                                path=jobPath,
                                                checked_time = datetime.datetime.now(),
                                                status=notAJobStatus,
                                                files=newFiles,
                                            )
                                else:
                                    JobManager.objects.create(
                                        path=jobPath,
                                        checked_time = datetime.datetime.now(),
                                        status=newJobStatus,
                                        files=files,
                                    )
    return True

