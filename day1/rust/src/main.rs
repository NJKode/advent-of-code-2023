use regex::Regex;
use std::fs;

fn main() {
    let file_path = String::from("src/input/test1.txt");
    println!("In file {}", file_path);

    let contents = fs::read_to_string(file_path).expect("Could not find file");

    let lines = contents.split("\n");

    let digit_reg = Regex::new(r"\d").unwrap();

    // let mut game_number = 1;

    for line in lines {
        let digit = digit_reg
        println!("{}", line)
    }
}
