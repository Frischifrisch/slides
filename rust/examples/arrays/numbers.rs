fn main() {
    let numbers: [i32; 3] = [10, 11, 12];

    println!("{:?}", numbers);
    println!("{}", numbers.len());

    for num in numbers {
        println!("{}", num);
    }
    println!("");

    for ix in 0..numbers.len() {
        println!("{ix} {}", numbers[ix]);
    }
    println!("");

    numbers[0] = 30; // cannot assign to `numbers[_]`, as `numbers` is not declared as mutable
    println!("{:?}", numbers);
}
