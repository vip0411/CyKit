# packet_sniffer.py
from scapy.all import sniff
from scapy.layers.inet import IP

# Define the packet processing function
def process_packet(packet):
    """
    Processes a single packet to extract IP layer information.
    
    :param packet: The packet to process.
    :return: A formatted string with source IP, destination IP, and protocol.
    """
    if packet.haslayer(IP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        protocol = packet[IP].proto
        return f"Packet: {src_ip} -> {dst_ip} (Protocol: {protocol})\n"
    return None

# Define the start_sniffer function
def start_sniffer(callback, packet_count=10, interface=None):
    """
    Starts the packet sniffer and processes each packet through the callback function.
    
    :param callback: A function to handle each processed packet's result (e.g., for displaying in the GUI).
    :param packet_count: Number of packets to capture (default is 10).
    :param interface: The network interface to sniff on (e.g., 'eth0'). Defaults to None, which captures on all interfaces.
    """
    try:
        # Capture packets, applying the callback function to each processed packet
        sniff(
            iface=interface,           # Interface to capture on
            count=packet_count,        # Number of packets to capture
            prn=lambda packet: callback(process_packet(packet)),  # Process each packet
            store=0                    # Do not store packets in memory
        )
    except Exception as e:
        # Handle any exceptions, such as missing permissions or invalid interface
        callback(f"Error starting packet sniffer: {str(e)}\n")
