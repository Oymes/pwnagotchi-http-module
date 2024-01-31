# HTTP Server Plugin for Pwnagotchi

## Overview

This is a simple HTTP server plugin for [Pwnagotchi](https://pwnagotchi.ai/). This can be used to retrieve captured pcaps from within the web browser. 

## Installation

1. Install script into plugins folder. (/usr/local/share/pwnagotchi/custom-plugins)

2. Edit the config.toml

	`main.plugins.httpserver.enabled = true`

## Usage

Once the Pwnagotchi is running, you can access the captured handshakes by navigating to `http://<your-pwnagotchi-ip>:8000` in your web browser.

## Configuration

The script is configured to serve files from the `/root/handshakes` directory. 
The script is configured to serve files using port 8000.

These options hard coded but will be updated to support config changes at a later date. 


