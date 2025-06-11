flatpak remote-modify --collection-id=org.flathub.Stable flathub
flatpak create-usb ~/SOBER org.vinegarhq.Sober
$$$$$$
flatpak install --user --sideload-repo=./.ostree/repo flathub org.vinegarhq.Sober