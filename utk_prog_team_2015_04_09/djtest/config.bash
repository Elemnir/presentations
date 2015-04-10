#!/bin/bash

################################################################################
#                                                                              #
#    The variables exported in this script are used by the project's           #
#    settings module for configuration. Many of these variables are secure     #
#    and should not be shared. Before entering values, this file should be     #
#    copied to 'config.bash' and precautions should be taken to ensure that    #
#    'config.bash' does not get committed to the git repo.                     #
#                                                                              #
################################################################################

# Enable debugging, options are 'True' and 'False'
export DJANGO_DEBUG='True'

# This should be a large, randomly generated string of characters
export DJANGO_SECRET_KEY='-cqtip6&c%vci@+%it6w!9w6k*=4o^iyw4q&e_0x#=fmghvmp&'

# Database settings
export DJANGO_DB_NAME='test.sqlite3'
