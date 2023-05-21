# Installing some basic packages.
sudo pacman -S --noconfirm base base-devel linux linux-firmware neovim xclip man lsd tldr unzip wget curl fd bat ripgrep onefetch git swaybg acpi

# Installing yay(aur helper).
cd ~
git clone https://aur.archlinux.org/yay.git
cd yay
makepkg -si --noconfirm
cd ..
sudo rm -r yay

# Cloning my dotfiles.
git clone https://github.com/artart222/dotfiles

# Using my git config.
ln -sf ~/dotfiles/git ~/.config/git

# Installing delta.
# A syntax-highlighting pager for git, diff, and grep output
yay -S git-delta

# Using my pacman.conf file.
sudo rm /etc/pacman.conf
sudo ln -sf ~/dotfiles/pacman.conf /etc/pacman.conf

yay -S --noconfirm neofetch
ln -sf ~/dotfiles/neofetch/ ~/.config/neofetch

# Installing networkmanager.
yay -S --noconfirm networkmanager
sudo systemctl start NetworkManager
sudo systemctl enable NetworkManager

# Installing kitty as terminal emulator.
yay -S --noconfirm kitty
ln -sf ~/dotfiles/kitty ~/.config/kitty

# Installing htop as system-monitor.
yay -S --noconfirm htop
ln -sf ~/dotfiles/htop ~/.config/htop

# Installing CodeArt as neovim config.
mkdir programming
cd programming
git clone https://github.com/artart222/CodeArt
ln -sf CodeArt ~/.config/nvim
cd

# Installing web browser.
yay -S firefox --noconfirm

# Installing hyprland as wm.
yay -S hyprland --noconfirm
ln -sf ~/dotfiles/hypr/ ~/.config/hypr/

# Installing widget system(using for top bar and etc...).
yay -S eww-wayland --noconfirm
ln -sf ~/dotfiles/eww ~/.config/eww

# Installing rofi as app launcher.
yay -S --noconfirm rofi
ln -sf ~/dotfiles/rofi ~/.config/rofi

# Installing some fonts!
yay -S --noconfirm ttf-jetbrains-mono-nerd ttf-dejavu ttf-liberation noto-fonts-emoji noto-color-emoji-fontconfig

# Installing jq(it's a json parser and I used it in dotfiles alot).
yay -S jq --noconfirm

# Installing zsh.
yay -S --noconfirm zsh zsh-completions
ln -sf ~/dotfiles/zsh ~/.config/zsh
ln -sf dotfiles/zsh/zshenv.zsh ~/.zshenv
chsh -s /usr/bin/zsh
sudo chsh -s /usr/bin/zsh

# zsh theme.
# TODO: Consider using other themes as well!
yay -S --noconfirm zsh-theme-powerlevel10k

# Some zsh plugins.
yay -S --noconfirm zsh-z
yay -S --noconfirm zsh-syntax-highlighting
yay -S --noconfirm zsh-autosuggestions

# A command-line fuzzy finder.
yay -S --noconfirm fzf

# A colorful make!
yay -S --noconfirm colormake

# Installing nvidia drivers
yay -S --noconfirm nvidia nvidia-utils lib32-nvidia-utils

# Fixing some problems with gpu by using custome mkinitcpio file.
sudo rm /etc/mkinitcpio.conf
sudo ln -sf ~/dotfiles/mkinitcpio.conf /etc/mkinitcpio.conf
sudo mkinitcpio -P

# Installing virtualbox.
yay -S --noconfirm virtualbox-host-modules-arch virtualbox-ext-oracle virtualbox-guest-iso

# Installing some python related packages.
yay -S --noconfirm python-pylint python-black
ln -sf ~/dotfiles/python ~/.config/python

# Installing ranger as file manager.
yay -S --noconfirm ranger
ln -sf ~/dotfiles/ranger/ ~/.config/ranger

# Installing tmux.
yay -S --noconfirm tmux
ln -sf ~/dotfiles/tmux ~/.config/tmux

# Installing some rust related packages.
yay -S --noconfirm rustup
yay -S --noconfirm cargo

# Some other packages
yay -S --noconfirm npm cmake shfmt stylua clang
#https://aur.archlinux.org/packages/dropbox#comment-676597
sudo gpg --recv-keys 1C61A2656FB57B7E4DE0F4C1FC918B335044912E
yay -S --noconfirm discord dropbox
yay -S --noconfirm dunst
yay -S --noconfirm pulseaudio pulsemixer
yay -S --noconfirm brightnessctl

git clone https://github.com/artart222/wallpapers Pictures/wallpapers

# Setting up bluetooth
yay -S --noconfirm bluez bluez-utils
sudo systemctl enable bluetooth
sudo systemctl start bluetooth
