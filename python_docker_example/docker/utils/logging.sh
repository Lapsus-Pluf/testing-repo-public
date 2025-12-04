#!/usr/bin/env sh

# ======================================================================================================================
# CONSTANTS
# ======================================================================================================================
# 🎨 Colors
BLUE="\033[94m"
CYAN="\033[0;36m"
GRAY="\033[0;90m"
GREEN="\033[92m"
RED="\033[91m"
YELLOW="\033[93m"

# ✒️ Formatting styles
BOLD="\033[1m"
DIM="\033[2m"
RESET="\033[0m"

# ======================================================================================================================
# FUNCTIONS
# ======================================================================================================================
# 📝 Aligned loggings
log_debug() { local name="$1"; shift; echo "${DIM}[$(date '+%Y-%m-%d %H:%M:%S (UTC%z)')][$name]${RESET}${BLUE}[DEBUG] $*${RESET}"; }
log_done()  { local name="$1"; shift; echo "${DIM}[$(date '+%Y-%m-%d %H:%M:%S (UTC%z)')][$name]${RESET}${GREEN}[ DONE] $*${RESET}"; }
log_error() { local name="$1"; shift; echo "${DIM}[$(date '+%Y-%m-%d %H:%M:%S (UTC%z)')][$name]${RESET}${RED}${BOLD}[ERROR] $*${RESET}"; }
log_info()  { local name="$1"; shift; echo "${DIM}[$(date '+%Y-%m-%d %H:%M:%S (UTC%z)')][$name]${RESET}[ INFO] $*"; }
log_warn()  { local name="$1"; shift; echo "${DIM}[$(date '+%Y-%m-%d %H:%M:%S (UTC%z)')][$name]${RESET}${YELLOW}${BOLD}[ WARN] $*${RESET}"; }
