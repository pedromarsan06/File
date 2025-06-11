flatpak remote-modify --collection-id=org.flathub.Stable flathub
flatpak create-usb ~/SOBER org.vinegarhq.Sober

$$$$$$
tar -czf - ~/SOBER | curl --upload-file - https://transfer.sh/SOBER.tar.gz
$$$$$$

$$$$$$
flatpak install --user --sideload-repo=./.ostree/repo flathub org.vinegarhq.Sober