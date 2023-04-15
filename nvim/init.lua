-- bootstrap lazy.nvim, LazyVim and your plugins
require("config.lazy")

-- for neovide
if vim.g.neovide then
  -- Put anything you want to happen only in Neovide here
  vim.g.neovide_remember_window_size = true
end
