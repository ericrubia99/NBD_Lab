"""Functions for reading parallell files."""

def read_parallel(file_name: str):
    """Reads a pcap file in parallel and creates a dataframe of its contents."""

    # create directory where to put temporary pcap files
    sub_dir = "SplitRead/"

    # Remove directory already created
    shutil.rmtree(sub_dir)

    try:
        os.mkdir("./" + sub_dir)

    # If you have already created it Error
    except OSError:
        print("Creation of the directory %s failed" % sub_dir)
    else:
        print("Successfully created the directory %s" % sub_dir)

    cmd('editcap -c 1 ' + pcap_analyzed + " ./" + sub_dir + "__mini.pcap")

    # split pcap file into different files, into the previous subdirectory

    # create subprocesses for reading files
