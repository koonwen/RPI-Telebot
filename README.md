# RPI-Telelbot
A telebot for my Raspberry Pi

# Motivation
To address security concerns, the Raspberry Pi is set up with a Firewall that rejects all incoming requests. This creates some complexity in terms of the maintenance of the system as well as managing graceful shutdown of the Pi. Additionally, since we are using the universitys network which dynamically assigns the IP address of the Pi, making that address discoverable is also a challenge when the Pi is headless and remote. Using a telegram bot service can circumvent these problems by establishing a connection with the telegram server upon startup. Simple commands can now be issued to the RPI when it is set up to long poll on the telegram server for updates. Long polling allows us to overcome our networking policy by making the RPI the client.

# Exposed commands
* /ip: Return ip address
* /temp: Get CPU temperature of pi
* /pic: Get sample picture of frame
* /fwup: Setup firewall (Block all incoming and only allow outgoing https)
* /fwdn: Teardown firewall (Allow only incoming ssh connections and allow outgoing https)
* /shutdown: Initiate graceful shutdown sequence
