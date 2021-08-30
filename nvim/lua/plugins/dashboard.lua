local g = vim.g
local fn = vim.fn

local plugins_count = fn.len(fn.globpath("~/.local/share/nvim/site/pack/packer/start", "*", 0, 1))

g.dashboard_disable_statusline = 1
g.dashboard_default_executive = "telescope"

g.dashboard_custom_header = {
 "                                                                             ",
 "                                                                             ",
 "    █████████               █████            █████████              █████    ",
 "   ███░░░░░███             ░░███            ███░░░░░███            ░░███     ",
 "  ███     ░░░   ██████   ███████   ██████  ░███    ░███  ████████  ███████   ",
 " ░███          ███░░███ ███░░███  ███░░███ ░███████████ ░░███░░███░░░███░    ",
 " ░███         ░███ ░███░███ ░███ ░███████  ░███░░░░░███  ░███ ░░░   ░███     ",
 " ░░███     ███░███ ░███░███ ░███ ░███░░░   ░███    ░███  ░███       ░███ ███ ",
 "  ░░█████████ ░░██████ ░░████████░░██████  █████   █████ █████      ░░█████  ",
 "   ░░░░░░░░░   ░░░░░░   ░░░░░░░░  ░░░░░░  ░░░░░   ░░░░░ ░░░░░        ░░░░░   ",
 "                                                                             "
}

g.dashboard_custom_section = {
    a = {description = {"  Find File                 SPC f f"}, command = "Telescope find_files"},
    b = {description = {"  Recents                   SPC f o"}, command = "Telescope oldfiles"},
    c = {description = {"  Find Word                 SPC f w"}, command = "Telescope live_grep"},
    d = {description = {"洛 New File                  SPC f n"}, command = "DashboardNewFile"},
    e = {description = {"  Bookmarks                 SPC b m"}, command = "Telescope marks"},
    f = {description = {"  Load Last Session         SPC s l"}, command = "SessionLoad"}
}

g.dashboard_custom_footer = {
    " ",
    "CodeArt Loaded " .. plugins_count .. " plugins!",
    "CodeArt v0.1"
}

-- Disable bufferline (tabline) and whitespace highlighting on dashboard.
vim.cmd('autocmd FileType dashboard set showtabline=0 | autocmd BufWinLeave <buffer> set showtabline=2')
vim.cmd('autocmd FileType dashboard execute "DisableWhitespace" | autocmd BufWinLeave <buffer> execute "EnableWhitespace"')
