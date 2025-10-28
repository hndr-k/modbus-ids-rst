use pcap::*;
use serde::Deserialize;
use std::{error::Error, fs};

#[derive(Debug, Deserialize)]
struct Config {
    iface: String,
    promisc: bool,
    immediate: bool,
    snaplen: i32,
    timeout: i32,
}

fn main() {
    {
        let cfg_text = fs::read_to_string("config.toml").unwrap();
        let cfg: Config = toml::from_str(&cfg_text).unwrap();
        println!("Config: {:?}", cfg);

        let mut cap = Capture::from_device(cfg.iface.as_str())
            .unwrap()
            .promisc(cfg.promisc)
            .immediate_mode(cfg.immediate)
            .snaplen(cfg.snaplen)
            .timeout(cfg.timeout)
            .open()
            .unwrap();

        let mut savefile = cap.savefile("test.pcap").unwrap();
        let mut count = 0;
        while let Ok(packet) = cap.next_packet() {
            //println!("{:?}", packet.header);
            count += 1;
            savefile.write(&packet);

            if count > 100 {
                println!("Stopping after {count} packets");
                break;
            }
        }

    }



}
