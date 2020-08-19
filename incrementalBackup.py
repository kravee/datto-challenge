def incrementalBackups(lastBackupTime, changes):
    '''
    One of the easiest ways to back up files is with an incremental backup. This method only backs up files that have changed since the last backup.
    You are given a list of changes that were made to the files in your database, where for each valid i, changes[i][0] is the timestamp of the time the change was made, and changes[i][1] is the file id.
    Knowing the timestamp of the last backup lastBackupTime, your task is to find the files which should be included in the next backup. Return the ids of the files that should be backed up as an array sorted in ascending order.

    Example

    For lastBackupTime = 461620205 and

    changes = [[461620203, 1],
           [461620204, 2],
           [461620205, 6],
           [461620206, 5],
           [461620207, 3],
           [461620207, 5],
           [461620208, 1]]
    the output should be
    incrementalBackups(lastBackupTime, changes) = [1, 3, 5].

    Here's how the answer is calculated:

    File with id = 1 was changed at 461620203 and 461620208, and since the last backup was at 461620205, it should be included in the next backup.
    File with id = 2 was changed only at 461620204, so there's no need to back it up.
    File with id = 3 was changed at 461620207, so it should be backed up next time.
    File with id = 5 was changed at 461620206 and 461620207, so it should be included in the new backup as well.
    File with id = 6 was changed at 461620205, so it can be ignored.
    :param lastBackupTime: int
    :param changes: matrix 2Xn, each is int
    :return: list of int
    '''
    
    file_to_change = []
    for change in changes:
        time_change, file = change
        if time_change > lastBackupTime:
            file_to_change.append(file)
    file_to_change = list(dict.fromkeys(file_to_change))
    file_to_change.sort()

    return file_to_change

