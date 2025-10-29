use pcap::{Device, Capture};

fn main() {
    let device = Device::lookup().unwrap();
    let mut cap = Capture::from_device(device).unwrap()
        .promisc(true)
        .snaplen(5000)
        .open().unwrap();

    while let Ok(packet) = cap.next() {
        println!("received packet! {:?}", packet);
    }
}
