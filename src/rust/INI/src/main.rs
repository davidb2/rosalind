use std::env;
use std::fs::OpenOptions;
use std::io::Read;
use std::collections::HashMap;

const BASE_PAIRS: [char; 4] = ['A', 'C', 'G', 'T'];

fn main() {
  let args: Vec<String> = env::args().collect();

  let filepath = match args.get(1) {
    None => panic!("Must provide filepath as an argument."),
    Some(filepath) => filepath,
  };

  let mut file = match OpenOptions::new().read(true).open(filepath) {
    Ok(file) => file,
    Err(error) => panic!("Error trying to open file: {error:?}"),
  };

  let mut contents = String::new();
  match file.read_to_string(&mut contents) {
    Ok(num_bytes) => println!("Read {num_bytes} bytes"),
    Err(error) => println!("Error reading file: {error:?}"),
  }

  println!("{contents}");

  let mut bp_counts: HashMap<char, u32> = HashMap::new();
  for bp in BASE_PAIRS {
    bp_counts.insert(bp, 0);
  }

  for bp in contents.trim().chars() {
    match bp_counts.get(&bp) {
      None => panic!("Character {bp} is not a valid base pair."),
      Some(count) => bp_counts.insert(bp, count+1),
    };
  }

  let counts = BASE_PAIRS.map(|bp| {
    match bp_counts.get(&bp) {
      None => 0u32,
      Some(count) => *count,
    }
  });

  counts.map(|count| print!("{count} "));
  println!("");
}
