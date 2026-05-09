#!/bin/bash

#!/bin/bash

install_flatpak() {
    echo "=== Updating system package list ==="
    sudo apt update
    echo "=== Installing Flatpak ==="
    sudo apt install -y flatpak
    flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
    echo "Flatpak installation complete."
}

install_sober() {
    echo "=== Installing Sober (Flatpak app) ==="
    flatpak install flathub org.vinegarhq.Sober -y
    echo "Sober installation complete."
}

install_kvm() {
    echo "=== Updating system package list ==="
    sudo apt update
    echo "=== Installing KVM and Virtual Machine Manager ==="
    sudo apt install -y qemu-kvm libvirt-daemon-system libvirt-clients bridge-utils virt-manager
    echo "=== Enabling and starting libvirtd service ==="
    sudo systemctl enable --now libvirtd
    echo "=== Adding $USER to libvirt and kvm groups ==="
    sudo usermod -aG libvirt $USER
    sudo usermod -aG kvm $USER
    echo "Installation complete. Please log out and back in for changes to take effect."
}

# Call the function passed as the first argument
"$1"   
