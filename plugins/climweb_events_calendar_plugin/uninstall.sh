#!/bin/bash
# Bash strict mode: http://redsymbol.net/articles/unofficial-bash-strict-mode/
set -euo pipefail

# This file is automatically run by ClimWeb when the plugin is uninstalled.

# ClimWeb will automatically `pip uninstall` the plugin after this script has been
# called for you so no need to do that in here.

# If you plugin has applied any migrations you should run
# `./climweb migrate climweb_events_calendar_plugin zero` here to undo any changes
# made to the database.