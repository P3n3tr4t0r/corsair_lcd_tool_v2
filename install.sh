#!/bin/bash
set -e

echo "📦 Installing udev rule for Corsair device..."

# Copy udev rule
sudo cp udev/99-corsair.rules /etc/udev/rules.d/

# Reload udev rules
sudo udevadm control --reload-rules
sudo udevadm trigger

echo "✅ Done!"