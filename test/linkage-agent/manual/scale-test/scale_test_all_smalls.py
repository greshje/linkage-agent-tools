# ------
#
# This test is not part of the automated test suite.  It is intended to be
# run manually after the folder ./test-data/time-test/time-test-no-households
# has been copied to C:\test.
#
# This module exists primarily to enable debugging of the process called by the cmd line
#
# ------

import time_test as tt

if __name__ == "__main__":
    tt.run_test("C:\\test\\pprl\\linkage-agent-scaling-test-set-2\\test-set-all-smalls")
