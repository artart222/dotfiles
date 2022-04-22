install_yay() {
  sudo pacman -S base-devel git --noconfirm
  cd /tmp
  git clone https://aur.archlinux.org/yay.git
  cd yay
  makepkg -si
}

install_pkg() {
  LIST_OF_APPS=($(ls "/bin")+$(ls "/usr/bin"))
  IFS="|"
  if [[ "${IFS}"${LIST_OF_APPS[*]}"${IFS}" =~ "${IFS}$1${IFS}" ]]; then
    echo "$1, is installed. Checking next dependency.."
  else
    echo $1 "is not installed."
    echo "Installing" $1
    yay -S --noconfirm $1
  fi
}

config_linker() {
  ln -s "~/dotfiles/$1" "$XDG_CONFIG_HOME/$1"
}

install_yay

install_pkg "nvidia"
install_pkg "nvidia-utils"
install_pkg "lib32-nvidia-utils"

install_pkg "python"
install_pkg "python-black"
install_pkg "python-psutil"
install_pkg "python-pylint"
install_pkg "python-setuptools"
install_pkg "cargo"
install_pkg "npm"
install_pkg "make"
install_pkg "colormake"
install_pkg "g++"
install_pkg "clang"
install_pkg "cmake"
install_pkg "shfmt"
install_pkg "stylua"

install_pkg "man-db"
install_pkg "tldr"
install_pkg "xclip"
install_pkg "dunst"
install_pkg "xorg-xinit"
install_pkg "unzip"
install_pkg "wget"
install_pkg "curl"
install_pkg "lsd"
install_pkg "fd"
install_pkg "ripgrep"
install_pkg "bat"
install_pkg "checkupdates+aur"
install_pkg "ranger"
install_pkg "htop"
install_pkg "onefetch"
install_pkg "neofetch"

install_pkg "xorg-server"

install_pkg "rofi"
install_pkg "qtile"
install_pkg "qtile-extras-git"
install_pkg "picom-ibhagwan-git"

install_pkg "pulseaudio"
install_pkg "pulsemixer"
install_pkg "brightnessctl"

install_pkg "ttf-dejavu"
install_pkg "ttf-liberation"
install_pkg "nerd-fonts-jetbrains-mono"
install_pkg "noto-fonts-emoji"
install_pkg "noto-color-emoji-fontconfig"

install_pkg "firefox"
install_pkg "kitty"
install_pkg "virtualbox-host-modules-arch"
install_pkg "virtualbox-ext-oracle"
install_pkg "virtualbox-guest-iso"
install_pkg "discord"
install_pkg "skypeforlinux-stable-bin"
install_pkg "dropbox"

install_pkg "zsh"
install_pkg "zsh-autosuggestions"
install_pkg "zsh-syntax-highlighting"
install_pkg "zsh-theme-powerlevel10k"
install_pkg "zsh-z-git"

cd "/home/artin/"
ln -s "/home/artin/dotfiles/zsh/zshenv.zsh" "/home/artin/.zshenv"
ln -s "/home/artin/dotfiles/zsh/" "~/.config/zsh"
chsh -s "/usr/bin/zsh"
zsh

config_linker "kitty"
config_linker "git"
config_linker "neofetch"
config_linker "htop"
config_linker "picom"
config_linker "ranger"
config_linker "rofi"
config_linker "python"

ln -s "~/dotfiles/xinitrc" "~/.xinitrc"
sudo rm "/etc/pacman.conf"
sudo ln -s "~/dotfiles/pacman.conf" "/etc/pacman.conf"
sudo rm "/etc/locale-gen"
sudo ln -s "~/dotfiles/locale-gen" "/etc/locale-gen"
