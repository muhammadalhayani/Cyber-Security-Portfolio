import time
from scapy.all import sniff, IP, TCP, UDP, ICMP, Raw, wrpcap

# Initialize a packet index counter
packet_index = 0

# Callback function to process each captured packet
def packet_callback(packet):
    global packet_index
    packet_index += 1

    # Print packet index
    print(f"=== Packet #{packet_index} ===")
    
    # Check if the packet has an IP layer
    if IP in packet:
        ip_layer = packet[IP]
        # Print source and destination IP addresses
        print(f"Source IP: {ip_layer.src}")
        print(f"Destination IP: {ip_layer.dst}")
        
        # Check if the packet has a TCP layer and print details
        if TCP in packet:
            tcp_layer = packet[TCP]
            print(f"Protocol: TCP")
            print(f"Source Port: {tcp_layer.sport}")
            print(f"Destination Port: {tcp_layer.dport}")
        
        # Check if the packet has a UDP layer and print details
        elif UDP in packet:
            udp_layer = packet[UDP]
            print(f"Protocol: UDP")
            print(f"Source Port: {udp_layer.sport}")
            print(f"Destination Port: {udp_layer.dport}")
        
        # Check if the packet has an ICMP layer and print details
        elif ICMP in packet:
            print(f"Protocol: ICMP")
    
    # Check if the packet has a Raw layer and print payload
    if Raw in packet:
        raw_layer = packet[Raw]
        print(f"Payload: {raw_layer.load}")
    
    # Print an empty line to separate this packet's details from the next packet
    print()

    # Save packet to pcap file
    wrpcap(output_file_path, packet, append=True)

    # Add a delay of 0.5 seconds before processing the next packet (optional)
    time.sleep(0.5)

# Function to print a disclaimer about the tool's usage
def disclaimer():
    print("=== Disclaimer ===")
    print("This tool is for educational purposes only. Unauthorized use is prohibited.")
    print()

# Print the disclaimer
disclaimer()

# Prompt user to specify where to save the file
output_file_path = input("Enter the path where you want to save the captured packets (e.g., /path/to/save/captured_packets.pcap): ")

# Specify the network interface
interface = "Wi-Fi"

try:
    # Start capturing packets and call packet_callback for each packet captured
    sniff(prn=packet_callback, iface=interface)
except KeyboardInterrupt:
    print("\n=== Capture stopped by user ===")
