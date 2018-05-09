from knitter import executor
from hobby import conf
from hobby.testcase import module1_inputs, module2_combine

executor.run(conf.windows, module1_inputs, module2_combine)

"""

You can run your specified modules or test cases or their combinations, just append them as the second 
or next parameters.
"""
# executor.run(conf.windows, module1_inputs.TestCase01_UserInformation)
# executor.run(conf.windows, module1_inputs.TestCase02_Gender, module2_combine)

