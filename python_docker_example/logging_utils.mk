# ======================================================================================================================
# CONSTANTS
# ======================================================================================================================
# 🎨 Colors
BLUE   := \033[94m
CYAN   := \033[0;36m
GRAY   := \033[0;90m
GREEN  := \033[92m
RED    := \033[91m
YELLOW := \033[93m

# ✒️ Formatting styles
BOLD   := \033[1m
DIM    := \033[2m
RESET  := \033[0m


# ======================================================================================================================
# MACROS
# ======================================================================================================================
# 📝 Aligned loggings
define log_debug
	@printf "$$(printf '$(DIM)')[$$(date '+%Y-%m-%d %H:%M:%S (UTC%z)')][$(1)]$(RESET)$(BLUE)[DEBUG] $(2)$(RESET)\n"
endef

define log_done
	@printf "$$(printf '$(DIM)')[$$(date '+%Y-%m-%d %H:%M:%S (UTC%z)')][$(1)]$(RESET)$(GREEN)[ DONE] $(2)$(RESET)\n"
endef

define log_error
	@printf "$$(printf '$(DIM)')[$$(date '+%Y-%m-%d %H:%M:%S (UTC%z)')][$(1)]$(RESET)$(RED)$(BOLD)[ERROR] $(2)$(RESET)\n"
endef

define log_info
	@printf "$$(printf '$(DIM)')[$$(date '+%Y-%m-%d %H:%M:%S (UTC%z)')][$(1)]$(RESET)[ INFO] $(2)\n"
endef

define log_warn
	@printf "$$(printf '$(DIM)')[$$(date '+%Y-%m-%d %H:%M:%S (UTC%z)')][$(1)]$(RESET)$(YELLOW)$(BOLD)[ WARN] $(2)$(RESET)\n"
endef
