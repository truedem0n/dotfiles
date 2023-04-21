# Key bindings
bindkey '^[[1;5D' backward-word
bindkey '^[[1;5C' forward-word
bindkey "^[[1;3C" forward-word
bindkey "^[[1;3D" backward-word




source ~/.aliases
source ~/.exported_paths

# starship
eval "$(starship init zsh)"
