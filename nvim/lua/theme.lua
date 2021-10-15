-- Hide ~ from end of lines.
vim.opt.fillchars = {eob = " "}

vim.g.tokyonight_style = 'night' -- styles: storm, night and day.
-- vim.g.onedark_style = 'deep'     -- styles: dark, darker, cool, deep, warm and warmer.
-- vim.g.onedark_transparent_background = true
--
require('onedark').setup {
  transparent = true,
}

vim.cmd('colorscheme onedark')
