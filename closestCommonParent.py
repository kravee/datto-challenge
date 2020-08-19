def closestCommonParent(files, parents, file1, file2):
    '''
    You're on a team at Datto tasked with implementing a backup system aimed at minimizing storage space. While exploring potential solutions, you notice something interesting: while performing backups on enterprise client accounts, the system often outputs clusters of files originating from the same source file, but each with slight differences. You come up with an idea to back up the original file and then use incremental differences to generate all the other files as needed.
    To implement this feature, you start by finding the closest common parent file (CCPF) of two files. More specifically, if you define the distance between a parent (the original) file and a child (modified) file as the number of intermediate files between them, then their CCPF is the file that has the least total distance to both of the given files among all of the files in the cluster. Assume that the distance between a file and a file itself is 0.
    Given a list of files in a cluster, and the files each of them originated from as an array, parents, find the CCPF of file1 and file2.

    Example

    For files = ["F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8"],
    parents = ["-1", "F1", "F1", "F2", "F2", "F4", "F4", "F4"],
    file1 = "F5", and file2 = "F8", the output should be
    closestCommonParent(files, parents, file1, file2) = "F2".

     The CCPF of "F5" and "F8" is "F2", since it's a parent for both "F5" and "F8", and is located below "F1" (which is also a parent to both of the files).
    :param files: list
    :param parents: list
    :param file1: str
    :param file2: str
    :return: str
    '''
    class file_backup:
        def __init__(self, file, parent):
            self._file = file
            self._parent = parent

        def file_name(self):
            return self._file

        def parent_name(self):
            return self._parent

    def return_parent (file):
        return file.parent_name()

    def build_path (file_map, file):
        path = []
        path.append(file)
        p_file = ''
        while p_file != '-1':
            for i in file_map:
                if i.file_name() == file:
                    p_file = return_parent(i)
                    file = p_file
                    path.append(file)
        return path

    def find_smaller(lst1, lst2):
        for i in lst1:
            for j in lst2:
                if i == j:
                    return i


    file_map = []
    for i in range(len(files)):
        file_to_backup = file_backup(files[i], parents[i])
        file_map.append(file_to_backup)


    path1 = build_path(file_map, file1)
    path2 = build_path(file_map, file2)

    if len(path1) >= len(path2):
        result = find_smaller(path1, path2)
    else:
        result = find_smaller(path2, path1)

    return result

# Driver program
if __name__ == "__main__":
    files=["F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8"]
    parents =["-1", "F1", "F1", "F2", "F2", "F4", "F4", "F4"]
    file1 = "F5"
    file2 = "F8"


    print(closestCommonParent(files, parents, file1, file2))