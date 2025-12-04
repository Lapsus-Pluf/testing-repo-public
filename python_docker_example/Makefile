# ======================================================================================================================
# INCLUDES
# ======================================================================================================================
# Load logging constants and functions
include logging_utils.mk


# ======================================================================================================================
# CONSTANTS
# ======================================================================================================================
# ⚙️ CONFIGURATIONS ---------------------------------------------------------------------------------------------------
AVAILABLE_MAKEFILE_TARGETS := dev | prod
AVAILABLE_MAKEFILE_IN_DOCKER_TARGETS := coverage | debug | format | lint | run | test
COVERAGE_REPORT_TYPE := html
LOGGER_NAME := ./Makefile
# ⚙️ CONFIGURATIONS ---------------------------------------------------------------------------------------------------

# 🐋 DOCKER -----------------------------------------------------------------------------------------------------------
IN_DOCKER := $(shell test -f /.dockerenv && echo "true" || echo "false")
# 🐋 DOCKER -----------------------------------------------------------------------------------------------------------

# 📂 FILE NAMES & PATHS -------------------------------------------------------------------------------------------------
SCRIPT_PATH := scripts/run_app_name.py
SRC_PATH := src/app_name
# 📂 FILE NAMES & PATHS -------------------------------------------------------------------------------------------------


# ======================================================================================================================
# MAKEFILE TARGETS
# ======================================================================================================================
# GENERAL TARGETS ------------------------------------------------------------------------------------------------------
.PHONY: all
all: no_target  # Set the default target when no target is specified (or 'make all' is executed)

.PHONY: no_target
# Display an error message stating that no target was specified, along with a list of available targets (depending on the context)
no_target:
	$(call log_error,$(LOGGER_NAME),No target specified! Please specify a target to execute.)
ifeq ($(IN_DOCKER),true)
	$(call log_info,$(LOGGER_NAME),Available targets are: $(AVAILABLE_MAKEFILE_IN_DOCKER_TARGETS).)
else
	$(call log_info,$(LOGGER_NAME),Available targets are: $(AVAILABLE_MAKEFILE_TARGETS).)
endif
# GENERAL TARGETS ------------------------------------------------------------------------------------------------------

# OUT-OF-DOCKER TARGETS ------------------------------------------------------------------------------------------------
.PHONY: dev
# Build and start the development environment Docker container
dev:
ifeq ($(IN_DOCKER),true)
	$(call log_error,$(LOGGER_NAME),This Makefile target is meant to be executed only outside a Docker container, but you are already inside one!)
else
	$(call log_info,$(LOGGER_NAME),Building development environment image...)
	@docker compose build dev
	$(call log_done,$(LOGGER_NAME),Development environment image built successfully!)
	$(call log_info,$(LOGGER_NAME),Starting development environment container...)
	@docker compose run --rm dev
	$(call log_warn,$(LOGGER_NAME),Development environment container ended!)
	$(call log_info,$(LOGGER_NAME),Stopping development environment container...)
	@docker compose down dev
	$(call log_done,$(LOGGER_NAME),Development environment container stopped successfully!)
endif

.PHONY: prod
# Build and start the production environment Docker container
prod:
ifeq ($(IN_DOCKER),true)
	$(call log_error,$(LOGGER_NAME),This Makefile target is meant to be executed only outside a Docker container, but you are already inside one!)
else
	$(call log_info,$(LOGGER_NAME),Building production environment image...)
	@docker compose build app_name
	$(call log_done,$(LOGGER_NAME),Production environment image built successfully!)
	$(call log_info,$(LOGGER_NAME),Starting production environment container...)
	@docker compose up app_name; docker compose down app_name
	$(call log_error,$(LOGGER_NAME),Production environment container ended!)
endif
# OUT-OF-DOCKER TARGETS ------------------------------------------------------------------------------------------------

# IN-DOCKER TARGETS ----------------------------------------------------------------------------------------------------
.PHONY: coverage
# Generate the coverage report
# Notice that first it should exist test data (run 'make test' if not)
coverage:
ifeq ($(IN_DOCKER),true)
	$(call log_info,$(LOGGER_NAME),Generating coverage report...)
	@rm -rf coverage_html_report
	@python -m coverage report -m
	@python -m coverage ${COVERAGE_REPORT_TYPE}
	$(call log_done,$(LOGGER_NAME),Coverage report generated successfully!)
else
	$(call log_error,$(LOGGER_NAME),This Makefile target is meant to be executed only inside a Docker container! Make any of '$(AVAILABLE_MAKEFILE_TARGETS)' targets first.)
endif

.PHONY: debug
# Run the app_name Python application through the main script in debug mode (with frozen modules disabled)
debug:
ifeq ($(IN_DOCKER),true)
	$(call log_info,$(LOGGER_NAME),Running the app_name application (in DEBUG mode)...)
	@python -Xfrozen_modules=off ${SCRIPT_PATH} --debug
	$(call log_done,$(LOGGER_NAME),app_name application exited successfully!)
else
	$(call log_error,$(LOGGER_NAME),This Makefile target is meant to be executed only inside a Docker container! Make any of '$(AVAILABLE_MAKEFILE_TARGETS)' targets first.)
endif

.PHONY: format
# Format the source code using 'Black' and 'isort' Python libraries
format:
ifeq ($(IN_DOCKER),true)
	$(call log_info,$(LOGGER_NAME),Formatting the source code with 'Black' and 'isort' libraries...)
	@python -m black ${SRC_PATH}
	@python -m isort ${SRC_PATH}
	$(call log_done,$(LOGGER_NAME),Source code formatted successfully!)
else
	$(call log_error,$(LOGGER_NAME),This Makefile target is meant to be executed only inside a Docker container! Make any of '$(AVAILABLE_MAKEFILE_TARGETS)' targets first.)
endif

.PHONY: lint
# Lint the source code using 'flake8' Python library
lint:
ifeq ($(IN_DOCKER),true)
	$(call log_info,$(LOGGER_NAME),Linting the source code with 'flake8' library...)
	@python -m flake8 ${SRC_PATH}
	$(call log_done,$(LOGGER_NAME),Source code linted successfully!)
else
	$(call log_error,$(LOGGER_NAME),This Makefile target is meant to be executed only inside a Docker container! Make any of '$(AVAILABLE_MAKEFILE_TARGETS)' targets first.)
endif

.PHONY: run
# Run the app_name Python application through the main script
run:
ifeq ($(IN_DOCKER),true)
	$(call log_info,$(LOGGER_NAME),Running the app_name application...)
	@python ${SCRIPT_PATH}
	$(call log_done,$(LOGGER_NAME),app_name application exited successfully!)
else
	$(call log_error,$(LOGGER_NAME),This Makefile target is meant to be executed only inside a Docker container! Make any of '$(AVAILABLE_MAKEFILE_TARGETS)' targets first.)
endif

.PHONY: test
# Execute the app_name Python application integration and unit tests
test:
ifeq ($(IN_DOCKER),true)
	$(call log_info,$(LOGGER_NAME),Running the app_name integration and unit tests...)
	@python -m coverage run -m pytest -v
	@rm -rf .pytest_cache
	$(call log_done,$(LOGGER_NAME),Tests completed successfully!)
else
	$(call log_error,$(LOGGER_NAME),This Makefile target is meant to be executed only inside a Docker container! Make any of '$(AVAILABLE_MAKEFILE_TARGETS)' targets first.)
endif
# IN-DOCKER TARGETS ----------------------------------------------------------------------------------------------------
