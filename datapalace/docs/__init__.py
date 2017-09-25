'''
Dominic Smith <domlucasmith@gmail.com>

Data size increase:
    On testing create_master_database.py, as the size of the file read increased, the memory footprint    of the script also increased. Stress testing pointed to potential problems where the size of file     was comparable to the available RAM.
    Solution would be to target memory usage (e.g memory_profile) There exist several alternative 
    methods to improve performance (https://wiki.python.org/moin/PythonSpeed/PerformanceTips)

    If a file becomes too large to load in memory, the file can be broken into mutiple smaller 
    files. Then proces each file separately and aggregate results afterwards (useful for 
    parallel processing / batch submission)

    Apply automate testing of the process, through a continuous integration system that runs the 
    tests against every pull request will monitor the performance.

'''
