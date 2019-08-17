use tokio;
use failure::Error;
use futures::future;
use futures::future::{lazy, Future};
use lapin_futures as lapin;
use crate::lapin::{BasicProperties, Client, ConnectionProperties};
use crate::lapin::options::{BasicPublishOptions, QueueDeclareOptions};
use crate::lapin::types::FieldTable;


fn main() {
    // get the AMQP server's address from env var
    // default to localhost if not provided
    let amqp_addr = std::env::var("AMQP_ADDR")
        .unwrap_or_else(|_| "amqp://127.0.0.1:5672/%2f".into());
    // future that pubs greeting to "hello"
    let amqp_pub = Client::connect(&amqp_addr, ConnectionProperties::default())
        // attempt to connect, print an Error if it has a bruh moment
        .map_err(|_| println!("failed to connect to client"))
        // when the connect future resolves without bruh moment, set up a channel
        .and_then(|client| {
            client.create_channel()
                .map_err(|_| println!("failed to create channel"))
        })
        .and_then(|mut channel| {
            let id = channel.id();
            // set up the queue
            // pass ownership of everything to inner closure
            channel.queue_declare("hello", 
                                  QueueDeclareOptions::default(),
                                  FieldTable::default())
            .and_then(move |_| {
                channel.basic_publish("", 
                                      "hello", 
                                      b"hello from the card registry".to_vec(),
                                      BasicPublishOptions::default(),
                                      BasicProperties::default())
            })
            .map_err(|_| println!("failed to declare the queue"))
        });
    tokio::run(amqp_pub);
}
